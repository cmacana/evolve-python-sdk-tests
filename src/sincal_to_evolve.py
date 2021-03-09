# from dataclassy import dataclass
from dataclasses import dataclass
from pandas import DataFrame
from zepben.evolve import *
from zepben.evolve.services.network.network_extensions import *
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


class PowerTransformerEndInfo(AssetInfo):
    power_transformer_info: str = None
    """"The power transformer info of this power transformer tank info."""
    # TODO: Add this class to the SDKs


class PowerTransformerTankInfo(AssetInfo):
    power_transformer_info: str = None
    """"The power transformer info of this power transformer tank info."""
    # TODO: Add this class to the SDKs


class TransformerEndInfo(AssetInfo):
    # TODO: Add this class to the SDKs
    ratedS: int = -9999
    ratedU: int = -9999
    endNumber: int = -9999
    emergencyS: int = -9999
    power_transformer_tank_info: Optional[PowerTransformerTankInfo] = None


@dataclass
class TransformerTest(IdentifiedObject):
    base_power: int = -9999
    temperature: int = -9999


@dataclass
class ShortCircuitTest(TransformerTest):
    voltage: int = -9999
    power: int = -9999
    current: int = -9999


@dataclass
class Test:
    mrid: str


net = NetworkService()

for index, row in std_two_winding_transformer_df.iterrows():
    # Mapping of the Asset Info
    pt_info = PowerTransformerInfo(mrid=2)  # Could be also mapped to the pt_info name
    ptt_info = PowerTransformerTankInfo(power_transformer_info='pt_info')
    net.add(ptt_info)
    ptei1 = TransformerEndInfo()
    ptei1.emergencyS = int(row['Smax'] * 1000000)
    ptei1.ratedU = int(row['Un1'] * 1000)
    ptei1.ratedS = int(row['Sn'] * 1000000)
    net.add(ptei1)
    ptei1.emergencyS = int(row['Smax'] * 1000000)
    ptei1.power_transformer_tank_info = ptt_info
    ptei2 = TransformerEndInfo()
    ptei2.ratedU = int(row['Un2'] * 1000)
    ptei2.ratedS = int(row['Sn'] * 1000000)
    ptei2.emergencyS = int(row['Smax'] * 1000000)
    ptei2.power_transformer_tank_info = ptt_info

    # Mapping of the ShortCircuitTest
    # Assuming a model referred to the powerTransformerEnd with endNumber= 1.
    sc_test = ShortCircuitTest(base_power=int(row['Smax'] * 1000000), voltage=int(row['ur'] * ptei1.ratedU / 100))
    sc_test.power = int(row['ur'] * ptei1.ratedU * sc_test.current / 100)
    sc_test.current = float(sc_test.base_power / ptei1.ratedU)
    net.add(sc_test)
#
sc_list = list(net.objects(TransformerEndInfo))
d = {}
for sc in sc_list:
    for x in sc.__dict__:
        a = getattr(sc, x)
        m = d.get(x, [])
        m.append(a)
        d[x] = m

print(d)
df = pd.DataFrame()
df.to_csv('out.csv')
