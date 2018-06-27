import os
os.chdir("C:\\oraclexe\\instantclient_12_2")

import cx_Oracle

class focus():

    def s1_valor(id_produto, valor):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "CALL produto_altera_preco("+str(id_produto)+", "+str(valor)+")"
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False

    def s1_quantidade(id_produto, quantidade):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "CALL produto_altera_quantidade("+str(id_produto)+", "+str(quantidade)+")"
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()   
            return False

    def s2(subcategoria, categoria):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "UPDATE SUBCATEGORIA SET ID_CATEGORIA = "+str(categoria)+" WHERE ID_SUBCATEGORIA = "+str(subcategoria)
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False

    def s3_1(frete):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "UPDATE venda set valor_frete = "+str(frete)+", total=subtotal+"+str(frete)+" where valor_frete<"+str(frete)
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False

    def s3_2(data_inicio, data_fim, desconto):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "UPDATE (SELECT TOTAL, DATA_VENDA FROM VENDA WHERE DATA_VENDA>=TO_DATE('"+data_inicio+"', 'DD/MM/YYYY') AND DATA_VENDA<=TO_DATE('"+data_fim+"', 'DD/MM/YYYY')) SET TOTAL = TOTAL*(1-"+desconto+")"
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False

    def s3_3(data_inicio, data_fim, desconto, valor_minimo):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "UPDATE (SELECT TOTAL, DATA_VENDA FROM VENDA WHERE TOTAL>="+valor_minimo+" AND DATA_VENDA>=TO_DATE('"+data_inicio+"', 'DD/MM/YYYY') AND DATA_VENDA<=TO_DATE('"+data_fim+"', 'DD/MM/YYYY')) SET TOTAL = TOTAL*(1-"+desconto+")"
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False

    def s3_4(pais, desconto):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "UPDATE (SELECT V.SUBTOTAL FROM VENDA V JOIN CLIENTE C ON C.ID_CLIENTE=V.ID_CLIENTE JOIN PESSOA P ON P.ID_PESSOA=C.ID_PESSOA JOIN ENDERECO E ON P.ID_ENDERECO=E.ID_ENDERECO WHERE PAIS='"+pais+"') SET SUBTOTAL = SUBTOTAL*(1-"+str(desconto)+")"
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False

    def s3_5(desconto):
        ORACLE_CONNECT = "a9762942/a9762942@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=grad.icmc.usp.br)(PORT=15215)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"
        orcl = cx_Oracle.connect(ORACLE_CONNECT)

        try:
            query = "UPDATE (SELECT SUBTOTAL FROM VENDA V JOIN ITEMVENDA I ON I.ID_VENDA=V.ID_VENDA WHERE QUANTIDADE_ESTOQUE>1) SET SUBTOTAL = SUBTOTAL*(1-"+str(desconto)+")"
            print(query)
            curs = orcl.cursor()
            curs.execute(query)
            orcl.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            orcl.close()
            return False 
