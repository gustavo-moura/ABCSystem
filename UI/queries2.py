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
            #print(rows)
            orcl.close()
            return rows
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            print("Deu erro nos top 15")
            return None

    def rel_1():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT P.nome, P.email, V.data_venda, C.cartao_tipo, C.cartao_numero, C.cartao_validade_mes, C.cartao_validade_ano FROM Cliente C JOIN Pessoa P ON P.id_pessoa=C.id_pessoa JOIN Venda V ON C.id_cliente=V.id_cliente WHERE TO_DATE(C.CARTAO_VALIDADE_MES||'/'||C.CARTAO_VALIDADE_ANO, 'MM/YYYY')<SYSDATE"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows = curs.fetchall()

            commit = "COMMIT"
            curs = orcl.cursor()
            curs.execute(commit)
            orcl.close()
            return rows
        except:
            print("Erro na query...")
            orcl.close()
            return None

    def rel_2():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT P.nome, D.nome, H.turno, H.data_entrada, empregado_ativo(H.data_saida) FROM Pessoa P JOIN HistoricoDepartamento H ON P.id_pessoa=H.id_pessoa JOIN Departamento D ON D.id_departamento=H.id_departamento"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows = curs.fetchall()

            orcl.close()
            return rows
        except:
            print("Erro na query...")
            orcl.close()
            return None
    
    def rel_3_1():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT SUM(valor_frete), EXTRACT(YEAR FROM data_venda) FROM VENDA GROUP BY EXTRACT(YEAR FROM data_venda) ORDER BY 2"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows1 = curs.fetchall()

            orcl.close()
            return rows1
        except:
            print("Erro na query...")
            orcl.close()
            return None

    def rel_3_2():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT SUM(VALOR_FRETE), EXTRACT(YEAR FROM DATA_VENDA) FROM VENDA WHERE TOTAL>2000 GROUP BY EXTRACT(YEAR FROM DATA_VENDA) ORDER BY 2"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows2 = curs.fetchall()

            orcl.close()
            return rows2
        except:
            print("Erro na query...")
            orcl.close()
            return None

    def rel_3_3():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT SUM(VALOR_FRETE), EXTRACT(YEAR FROM DATA_VENDA) FROM VENDA WHERE TOTAL<=2000 GROUP BY EXTRACT(YEAR FROM DATA_VENDA) ORDER BY 2"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows3 = curs.fetchall()

            orcl.close()
            return rows3
        except:
            print("Erro na query...")
            orcl.close()
            return None

    def rel_4(ano):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        if(ano==None):
            ano = 2010

        try:
            query = "SELECT SUM(subtotal), EXTRACT(MONTH FROM data_venda) FROM Venda WHERE EXTRACT(YEAR FROM data_venda)="+ano+"GROUP BY EXTRACT(MONTH FROM data_venda)ORDER BY 2"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows = curs.fetchall()

            orcl.close()
            return rows
        except:
            print("Erro na query...")
            orcl.close()
            return None
    
    def rel_5():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        query = "SELECT NOME, PRECO, PESO, CATEGORIA, QUANTIDADE FROM (SELECT P.NOME, P.PRECO, P.PESO, C.NOME CATEGORIA, SUM(QUANTIDADE) QUANTIDADE FROM VENDA V JOIN ITEMVENDA I ON V.ID_VENDA=I.ID_VENDA JOIN PRODUTO P ON P.ID_PRODUTO=I.ID_PRODUTO JOIN SUBCATEGORIA S ON P.ID_SUBCATEGORIA=S.ID_SUBCATEGORIA JOIN CATEGORIA C ON C.ID_CATEGORIA=S.ID_CATEGORIA WHERE V.DATA_VENDA<=sysdate AND V.DATA_VENDA>=add_months(sysdate,  -6) GROUP BY P.NOME, P.PRECO, P.PESO, C.NOME ORDER BY 5 DESC) WHERE ROWNUM<=15"

        try:
            curs = orcl.cursor()
            curs.execute(query)
            rows = curs.fetchall()

            orcl.close()
            return rows
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            print("Deu erro nos top 15")
            return None

    def rel_6():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT J.CATEGORIA CATEGORIA_1, J.SUBCATEGORIA SUBCATEGORIA_1, J.PRODUTO PRODUTO_1, SUM(J.QTD) QUANTIDADE_1, K.CATEGORIA CATEGORIA_2, K.SUBCATEGORIA SUBCATEGORIA_2, K.PRODUTO PRODUTO_2, SUM(K.QTD) QUANTIDADE_2, COUNT(K.VENDA) QTD_VENDA FROM (SELECT P.NOME PRODUTO, C.NOME CATEGORIA, S.NOME SUBCATEGORIA, I.ID_VENDA VENDA, I.QUANTIDADE_ESTOQUE QTD FROM PRODUTO P JOIN SUBCATEGORIA S ON S.ID_SUBCATEGORIA=P.ID_SUBCATEGORIA JOIN CATEGORIA C ON C.ID_CATEGORIA=S.ID_CATEGORIA JOIN ITEMVENDA I ON I.ID_PRODUTO=P.ID_PRODUTO) J JOIN (SELECT P.NOME PRODUTO, C.NOME CATEGORIA, S.NOME SUBCATEGORIA, I.ID_VENDA VENDA, I.QUANTIDADE_ESTOQUE QTD FROM PRODUTO P JOIN SUBCATEGORIA S ON S.ID_SUBCATEGORIA=P.ID_SUBCATEGORIA JOIN CATEGORIA C ON C.ID_CATEGORIA=S.ID_CATEGORIA JOIN ITEMVENDA I ON I.ID_PRODUTO=P.ID_PRODUTO) K ON J.VENDA=K.VENDA WHERE J.PRODUTO||J.CATEGORIA||J.SUBCATEGORIA!=K.PRODUTO||K.CATEGORIA||K.SUBCATEGORIA GROUP BY J.PRODUTO, J.CATEGORIA, J.SUBCATEGORIA, K.PRODUTO, K.CATEGORIA, K.SUBCATEGORIA ORDER BY 7 DESC"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows = curs.fetchall()

            orcl.close()
            return rows
        except:
            print("Erro na query...")
            orcl.close()
            return None

    def rel_7():
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)
        print("Connected to Oracle: " + orcl.version)

        try:
            query = "SELECT E.PAIS, SUM(SUBTOTAL) FROM VENDA V JOIN CLIENTE C ON C.ID_CLIENTE=V.ID_CLIENTE JOIN PESSOA P ON P.ID_PESSOA=C.ID_PESSOA JOIN ENDERECO E ON E.ID_ENDERECO=P.ID_ENDERECO WHERE PAIS=pais GROUP BY E.PAIS"
"
            curs = orcl.cursor()
            curs.execute(query)
            
            rows = curs.fetchall()

            orcl.close()
            return rows
        except:
            print("Erro na query...")
            orcl.close()
            return None


    def disconnect():
        # closing connection
        orcl.close()
        print("Disconnected to Oracle")