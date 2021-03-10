import pandas as pd
import pyodbc

from map_sincal_vec_grp import *

path = "G:\\My Drive\\ZeppelinBend\\SD - Software Dev\\EWB\\Sample Data\\sincal_master_db" \
       "\\Local line types Version 16.mdb "
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + ';')
query = 'select * from StdTwoWindingTransformer'
std_two_winding_transformer_df = pd.read_sql(query, conn)
conn.close()

net = NetworkService()

for index, row in std_two_winding_transformer_df.iterrows():
    # Mapping of the Asset Info
    pt_info = PowerTransformerInfo(mrid=2)  # Could be also mapped to the pt_info name
    ptt_info = PowerTransformerTankInfo(power_transformer_info='pt_info')
    net.add(ptt_info)

    # Adding PowerTranformerEndInfos
    ptei1 = TransformerEndInfo()
    ptei1.name = str(int(row['Element_ID'])) + "-ptei-1"
    ptei1.endNumber = 1
    ptei1.emergencyS = int(row['Smax'] * 1000000)
    ptei1.ratedU = int(row['Un1'] * 1000)
    ptei1.ratedS = int(row['Sn'] * 1000000)
    ptei1.emergencyS = int(row['Smax'] * 1000000)
    ptei1.power_transformer_tank_info = ptt_info

    ptei2 = TransformerEndInfo()
    ptei2.name = str(int(row['Element_ID'])) + "-ptei-2"
    ptei2.ratedU = int(row['Un2'] * 1000)
    ptei2.ratedS = int(row['Sn'] * 1000000)
    ptei2.emergencyS = int(row['Smax'] * 1000000)
    ptei2.power_transformer_tank_info = ptt_info
    ptei2.endNumber = 2
    # Setting connection kinds and phase_clock
    [ptei1, ptei2] = VectorGroupMap(vec_grp=int(row['VecGrp']), ptei1=ptei1, ptei2=ptei2).get_ends_info()
    # Mapping: ShortCircuitTest
    # Assuming a model referred to the powerTransformerEnd with endNumber= 1.
    sc_test = ShortCircuitTest()
    sc_test.base_power = int(row['Smax'] * 1000000)
    sc_test.voltage = int(row['uk'])
    sc_test.current = float(sc_test.base_power / ptei1.ratedU)
    sc_test.power = int(row['ur'] * ptei1.ratedU * sc_test.current / 100)
    net.add(sc_test)

    # Mapping: NoLoadTest
    nl_test = NoLoadTest()
    nl_test.loss = float(row['Vfe'])  # SINCAL.TwoWindingTransformer.Vfe : Iron Losses [kW]
    nl_test.excitingCurrent = float(row['i0'])  # SINCAL.TwoWindingTransformer.i0 : No Load Current [%]
    net.add(nl_test)

    # Association to Tests
    ptei1.short_circuit_test = sc_test
    ptei1.no_load_test = nl_test
    net.add(ptei1)
    net.add(ptei2)

    # TransformerStarImpedance



# Printing and persisting TransformerEndInfos values
ptei_list = list(net.objects(TransformerEndInfo))
d = {}
for pti in ptei_list:
    for x in pti.__slots__:
        a = getattr(pti, x)
        m = d.get(x, [])
        m.append(a)
        d[x] = m

df = pd.DataFrame(d)
df.to_csv('TransformerEndInfo.csv')

# Printing and persisting ShorCircuitTest values
sc_list = list(net.objects(ShortCircuitTest))
d = {}
for sc in sc_list:
    for x in sc.__slots__:
        a = getattr(sc, x)
        m = d.get(x, [])
        m.append(a)
        d[x] = m

df = pd.DataFrame(d)
df.to_csv('ShortCircuitTest.csv')

# Printing and persisting NoLoadTest values
nl_list = list(net.objects(NoLoadTest))
d = {}
for nl in nl_list:
    for x in nl.__slots__:
        a = getattr(nl, x)
        m = d.get(x, [])
        m.append(a)
        d[x] = m
df = pd.DataFrame(d)
df.to_csv('NoLoadTest.csv')
