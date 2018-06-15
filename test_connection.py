import os
os.chdir("C:\\oraclexe\\instantclient_12_2")

import cx_Oracle

ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"

orcl = cx_Oracle.connect(ORACLE_CONNECT)
print("Connected to Oracle: " + orcl.version)

sql = "select * from CLIENTE"
curs = orcl.cursor()
curs.execute(sql)

for row in curs:
    print(row)

orcl.close()