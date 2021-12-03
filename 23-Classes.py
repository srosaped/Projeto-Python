# Classes

class Cliente:
    __nome=""
    __morada=""
    __codigopostal=""
    __telefone=""
    __email=""

    def __init__(self,nome,morada,codigopostal,telefone,email):
        self.__nome=nome
        self.__morada=morada
        self.__codigopostal=codigopostal
        self.__telefone=telefone
        self.__email=email

    def showCliente(self):
        print(cliente1.__nome)
        print(cliente1.__morada)
        print(cliente1.__codigopostal)
        print(cliente1.__telefone)
        print(cliente1.__email)

    def getNome(self):
        return self.__nome

    def getMorada(self):
        return self.__morada

    def getCodigoPostal(self):
        return self.__codigopostal

    def getTelefone(self):
        return self.__telefone

    def getEmail(self):
        return self.__email

    def getListCliente(self):
        return [self.__nome,self.__morada,self.__codigopostal,self.__telefone,self.__email]

    def getTupleCliente(self):
        return (self.__nome,self.__morada,self.__codigopostal,self.__telefone,self.__email)

    def getSetCliente(self):
        return {self.__nome,self.__morada,self.__codigopostal,self.__telefone,self.__email}

    def getJSONCliente(self):
        return {"Nome":self.__nome,"Morada":self.__morada,"CodigoPostal":self.__codigopostal,"Telefone":self.__telefone,"EMail":self.__email}

    def getXMLCliente(self):
        return """<cliente>
                    <nome"""+self.__nome+"""</nome>
                    <morada"""+self.__morada+"""</morada>
                    <codigopostal"""+self.__codigopostal+"""</codigopostal>
                    <telefone"""+self.__telefone+"""</telefone>
                    <email"""+self.__email+"""</email>
                  </cliente>"""

cliente1=Cliente("João Santos","Rua dos Santos nº1","1000-100 Lisboa","211234567","joao.santos@sapo.pt")
cliente1.showCliente()
print(cliente1.getNome())
print(cliente1.getListCliente())
print(cliente1.getTupleCliente())
print(cliente1.getSetCliente())
print(cliente1.getJSONCliente())
print(cliente1.getXMLCliente())