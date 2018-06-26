import os
os.chdir("C:\\oraclexe\\instantclient_12_2")

import cx_Oracle

class connection():

    def hello():
        print("Hello world")

    def connect():
        # opening connection
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"

        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

    def checkLogin(user, pwd):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"

        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

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

            orcl.close()
            print("Logado com sucesso!")
            return True
        except:
            print("Login nao efetuado...")
            orcl.close()
            return False
    
    # top 15 produtos
    def top15products():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        query = "SELECT NOME, PRECO, PESO, CATEGORIA, QUANTIDADE FROM (SELECT P.NOME, P.PRECO, P.PESO, C.NOME CATEGORIA, SUM(QUANTIDADE) QUANTIDADE FROM VENDA V JOIN ITEMVENDA I ON V.ID_VENDA=I.ID_VENDA JOIN PRODUTO P ON P.ID_PRODUTO=I.ID_PRODUTO JOIN SUBCATEGORIA S ON P.ID_SUBCATEGORIA=S.ID_SUBCATEGORIA JOIN CATEGORIA C ON C.ID_CATEGORIA=S.ID_CATEGORIA WHERE V.DATA_VENDA<=sysdate AND V.DATA_VENDA>=add_months(sysdate,  -6) GROUP BY P.NOME, P.PRECO, P.PESO, C.NOME ORDER BY 5 DESC) WHERE ROWNUM<=15"

        try:
            curs = orcl.cursor()
            curs.execute(query)
            rows = curs.fetchall()
            print(rows)
            orcl.close()
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            print("Deu erro nos top 15")


    def disconnect():
        # closing connection
        orcl.close()
        print("Disconnected to Oracle")