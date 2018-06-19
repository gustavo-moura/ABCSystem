import os
os.chdir("C:\\oraclexe\\instantclient_12_2")

import cx_Oracle

ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"

orcl = cx_Oracle.connect(ORACLE_CONNECT)
print("Connected to Oracle: " + orcl.version)

"""
    HOW TO EXECUTE A QUERY:

someQuery = "select * from TABLE"
curs = orcl.cursor()
curs.execute(someQuery)

for row in curs:
    print(row)

"""

def checkLogin(user, pwd):
    try:
        query = "SELECT E.login, P.senha, E.funcao, E.documento FROM Pessoa P JOIN Empregado E ON P.id_pessoa=E.id_pessoa where E.login='"+user+"' AND P.senha='"+pwd+"'"
        curs = orcl.cursor()
        curs.execute(query)

        row = curs.fetchone()
        documento = row[3]

        insert = "INSERT INTO LogAcesso VALUES ("+documento+", to_char(sysdate,'DD/MM/YYYY hh24:mm:ss'))"
        curs = orcl.cursor()
        curs.execute(insert)

        commit = "COMMIT"
        curs = orcl.cursor()
        curs.execute(commit)

        print("Logado com sucesso!")
        return True
    except:
        print("Login nao efetuado...")
        return False

# test login
# checkLogin("adventure-works\jianshuo0", "OHTnyBvL8Z29tVGOT1/XKjVzsJCf9XezJf5TScu1fa0")

# closing connection
orcl.close()