import pyodbc

#for driver in pyodbc.drivers():
#    print(driver)

# ODBC Driver 17 for SQL Server

clienteid="1"
nome="João Fonseca"
nif="987654321"
morada="Rua dos Fonsecas nº1"
cpostal="3000-300 Coimbra"
telefone="921231231"
email="joao.fonseca@gmail.com"

servername="DESKTOP-UURFP02"
port="1433"
database="L4Gestao"
username="L4GestaoUser"
password="Pa$$w0rd"

server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};".format(servername,port,database,username,password)

print(server)

conn=pyodbc.connect(server)

cursor=conn.cursor()

sqlquery="EXEC dbo.SP_ConsultarCliente ?"

cursor.execute(sqlquery,clienteid)

result=cursor.fetchall()

clientes=[]

for cliente in result:
    dic={"ClienteID":cliente[0],"Nome":cliente[1],"NIF":cliente[2],"Morada":cliente[3],"CPostal":cliente[4],"Telefone":cliente[5],"EMail":cliente[6]}
    clientes.append(dic)

conn.close()

print(clientes)

