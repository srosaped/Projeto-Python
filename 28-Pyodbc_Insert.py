import pyodbc

#for driver in pyodbc.drivers():
#    print(driver)

#ODBC Driver 17 for SQL Server

nome="Catarina Tavares"
nif="222333444"
morada="Rua dos Tavares nº1"
cpostal="6000-600 Guimarães"
telefone="941231239"
email="ctavares@outlook.com"


servername="DESKTOP-UURFP02"
port="1433"
database="L4Gestao"
username="L4GestaoUser"
password="Pa$$w0rd"

server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};".format(servername,port,database,username,password)

conn=pyodbc.connect(server)

cursor=conn.cursor()

sqlquery="EXEC dbo.SP_InserirCliente ?,?,?,?,?,?"

cursor.execute(sqlquery,nome,nif,morada,cpostal,telefone,email)

conn.commit()

conn.close()



