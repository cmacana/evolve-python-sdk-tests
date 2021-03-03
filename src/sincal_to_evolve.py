from zepben.evolve import *

import pyodbc

path = "G:\My Drive\ZeppelinBend\SD - Software Dev\EWB\Sample Data\sincal_master_db\Local line types Version 16.mdb"
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + ';')
cursor = conn.cursor()
cursor.execute('select * from StdTwoWindingTransformer')

for row in cursor.fetchall():
    print(row)
