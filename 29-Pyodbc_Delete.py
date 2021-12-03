import pyodbc

#for driver in pyodbc.drivers():
#    print(driver)

#ODBC Driver 17 for SQL Server

clienteid="1"

servername="DESKTOP-UURFP02"
port="1433"
database="L4Gestao"
username="L4GestaoUser"
password="Pa$$w0rd"

server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};".format(servername,port,database,username,password)

conn=pyodbc.connect(server)

cursor=conn.cursor()

sqlquery="EXEC dbo.SP_ApagarCliente ?"

cursor.execute(sqlquery,clienteid)

conn.commit()

conn.close()



