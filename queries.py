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

# login
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

# relatorio 1 - cartoes vencidos
def rel_cartaoVencido():
    try:
        query = "SELECT P.nome, P.email, V.data_venda, C.cartao_tipo, C.cartao_numero, C.cartao_validade_mes, C.cartao_validade_ano FROM Cliente C JOIN Pessoa P ON P.id_pessoa=C.id_pessoa JOIN Venda V ON C.id_cliente=V.id_cliente WHERE TO_DATE(C.CARTAO_VALIDADE_MES||'/'||C.CARTAO_VALIDADE_ANO, 'MM/YYYY')<SYSDATE"
        curs = orcl.cursor()
        curs.execute(query)
        
        rows = curs.fetchmany(numRows=15)

        commit = "COMMIT"
        curs = orcl.cursor()
        curs.execute(commit)
        return rows
    except:
        print("Erro na query...")
        return None

# relatorio 1 - cartoes vencidos filtro por nome
def rel_cartaoVencidoNome(nome):
    try:
        query = "SELECT P.nome, D.nome, H.turno, H.data_entrada, empregado_ativo(H.data_saida) FROM Pessoa P JOIN HistoricoDepartamento H ON P.id_pessoa=H.id_pessoa JOIN Departamento D ON D.id_departamento=H.id_departamento WHERE P.nome='"+nome+"'"
        curs = orcl.cursor()
        curs.execute(query)

        rows = curs.fetchall()

        commit = "COMMIT"
        curs = orcl.cursor()
        curs.execute(commit)

        return rows
    except:
        return None

# relatorio 2 - historico depart filtro por nome
def rel_historicoDepartEmpregado(nome):
    try:
        query = "SELECT P.nome, D.nome, H.turno, H.data_entrada, empregado_ativo(H.data_saida) FROM Pessoa P JOIN HistoricoDepartamento H ON P.id_pessoa=H.id_pessoa JOIN Departamento D ON D.id_departamento=H.id_departamento WHERE P.nome='"+nome+"'"
        curs = orcl.cursor()
        curs.execute(query)
        
        rows = curs.fetchall()

        return rows
    except:
        print("Erro na query...")
        return None

# relatorio 2 - historico depart filtro por departamento
def rel_historicoDepartNomeD(nome):
    try:
        query = "SELECT P.nome, D.nome, H.turno, H.data_entrada, empregado_ativo(H.data_saida) FROM Pessoa P JOIN HistoricoDepartamento H ON P.id_pessoa=H.id_pessoa JOIN Departamento D ON D.id_departamento=H.id_departamento WHERE D.nome='"+nome+"'"
        curs = orcl.cursor()
        curs.execute(query)
        
        rows = curs.fetchall()

        return rows
    except:
        print("Erro na query...")
        return None

# relatorio 3 - soma dos valores de fretes




# test login successful
#checkLogin("adventure-works\jianshuo0", "OHTnyBvL8Z29tVGOT1/XKjVzsJCf9XezJf5TScu1fa0")

# test login failure
#checkLogin("uasdiusa", "zzzwe")

# test rel 1
#rows = rel_cartaoVencido()
#for row in rows:
#    print(row)

# test rel 1 - filtro (FAIL)
#r = rel_cartaoVencidoNome("Alfredo C Gomez")
#for row in r:
#    print(row)

# test rel 2
#r = rel_historicoDepart()
#for row in r:
#    print(row)

# test rel 2 - filtro nome
#r = rel_historicoDepartEmpregado("Jae B Pak")
#for row in r:
#    print(row)

# test rel 2 - filtro depart
#r = rel_historicoDepartNomeD("Sales")
#for row in r:
#    print(row)





# closing connection
orcl.close()