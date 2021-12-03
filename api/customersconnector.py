import pyodbc

class Customer:

    def getConnectionString(self):
        servername="DESKTOP-UURFP02"
        port="1433"
        database="L4Gestao"
        username="L4GestaoUser"
        password="Pa$$w0rd"
        server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};".format(servername,port,database,username,password)
        return server

    def getCustomer(self,customerid):
        conn=pyodbc.connect(self.getConnectionString())
        cursor=conn.cursor()
        sqlquery="EXEC dbo.SP_ConsultarCliente ?"
        cursor.execute(sqlquery,customerid)
        result=cursor.fetchall()
        clientes=[]
        for cliente in result:
            dic={"ClienteID":cliente[0],"Nome":cliente[1],"NIF":cliente[2],"Morada":cliente[3],"CPostal":cliente[4],"Telefone":cliente[5],"EMail":cliente[6]}
            clientes.append(dic)
        conn.close()
        return clientes

    def getAllCustomers(self):
        conn=pyodbc.connect(self.getConnectionString())
        cursor=conn.cursor()
        sqlquery="EXEC dbo.SP_ConsultarClientes"
        cursor.execute(sqlquery)
        result=cursor.fetchall()
        clientes=[]
        for cliente in result:
            dic={"ClienteID":cliente[0],"Nome":cliente[1],"NIF":cliente[2],"Morada":cliente[3],"CPostal":cliente[4],"Telefone":cliente[5],"EMail":cliente[6]}
            clientes.append(dic)
        conn.close()    
        return clientes

    def insertCustomer(self,name,fiscalnumber,address,postalcode,phonenumber,email):
        conn=pyodbc.connect(self.getConnectionString())
        cursor=conn.cursor()
        sqlquery="EXEC dbo.SP_InserirCliente ?,?,?,?,?,?"
        cursor.execute(sqlquery,name,fiscalnumber,address,postalcode,phonenumber,email)
        conn.commit()
        conn.close()

    def updateCustomer(self,customerid,name,fiscalnumber,address,postalcode,phonenumber,email):
        conn=pyodbc.connect(self.getConnectionString())
        cursor=conn.cursor()
        sqlquery="EXEC dbo.SP_AtualizarCliente ?,?,?,?,?,?,?"
        cursor.execute(sqlquery,customerid,name,fiscalnumber,address,postalcode,phonenumber,email)
        conn.commit()
        conn.close()

    def deleteCustomer(self,customerid):
        conn=pyodbc.connect(self.getConnectionString())
        cursor=conn.cursor()
        sqlquery="EXEC dbo.SP_ApagarCliente ?"
        cursor.execute(sqlquery,customerid)
        conn.commit()
        conn.close()