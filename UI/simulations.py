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


    def s2(arg1, arg2):
        pass

    def s3_1(arg1):
        pass

    def s3_2(arg1, arg2, arg3):
        pass

    def s3_3(arg1, arg2, arg3, arg4):
        pass

    def s3_4(arg1, arg2):
        pass

    def s3_5(arg1):
        pass

