from zepben.evolve import *
from typing import List, Optional, Generator
import pyodbc
import pandas as pd

path = "G:\\My Drive\\ZeppelinBend\\SD - Software Dev\\EWB\\Sample Data\\sincal_master_db" \
       "\\Local line types Version 16.mdb "
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + ';')
query = 'select * from StdTwoWindingTransformer'
std_two_winding_transformer_df = pd.read_sql(query, conn)
conn.close()


class PowerTransformerTankInfo(AssetInfo):
    # TODO: Add this class to the SDKs
    power_transformer_info: Optional[PowerTransformerInfo] = None
    """"The power transformer info of this power transformer tank info."""


class TransformerEndInfo(AssetInfo):
    # TODO: Add this class to the SDKs
    ratedS: int = -9999
    ratedU: int = -9999
    endNumber: int = -9999
    emergencyS: int = -9999
    power_transformer_tank_info: Optional[PowerTransformerTankInfo] = None


class TransformerTest(IdentifiedObject):
    base_power: int = -9999
    temperature: int = -9999


class ShortCircuitTest(TransformerTest):
    voltage: int = -9999
    power: int = -9999
    current: int = -9999


net = NetworkService()
for index, row in std_two_winding_transformer_df.iterrows():
    # Mapping of the Asset Info
    pt_info = PowerTransformerInfo()
    pt_info.mrid = int(row['Element_ID'])  # Could be also mapped to the pt_info name
    ptt_info = PowerTransformerTankInfo()
    ptt_info.power_transformer_info = pt_info
    ptei1 = TransformerEndInfo()
    ptei1.ratedU = int(row['Un1'] * 1000)
    ptei1.ratedS = int(row['Sn'] * 1000000)
    ptei1.ratedS = int(row['Sn'] * 1000000)
    ptei1.emergencyS = int(row['Smax'] * 1000000)
    ptei1.power_transformer_tank_info = ptt_info
    ptei2 = TransformerEndInfo()
    ptei2.ratedU = int(row['Un2'] * 1000)
    ptei2.ratedS = int(row['Sn'] * 1000000)
    ptei2.emergencyS = int(row['Smax'] * 1000000)
    ptei2.power_transformer_tank_info = ptt_info

    # Mapping of the ShortCircuitTest
    # Assuming a model referred to the powerTransformerEnd with endNumber= 1.
    sc_test = ShortCircuitTest(test=1)
    sc_test.base_power = int(row['Smax'] * 1000000)
    sc_test.power = int(row['ur'] * ptei1.ratedU * sc_test.current / 100)
    sc_test.current = float(sc_test.base_power / ptei1.ratedU)
    sc_test.voltage = int(row['ur'] * ptei1.ratedU / 100)
    net.add(sc_test)

sc_list = list(net.objects(ShortCircuitTest))
for sc in sc_list:
    sc.__dict__
