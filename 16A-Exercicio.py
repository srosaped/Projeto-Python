#Considerem o seguinte dicionário

clientes={
    "cliente1": {
        "nome":"João Silva",
        "morada":"Rua das Silvas",
        "Telefone":"211234567"
    },
    "cliente2": {
        "nome":"Ana Rosa",
        "morada":"Rua das Rosas",
        "Telefone":"217654321"
    },
    "cliente3": {
        "nome":"Luis Cravo",
        "morada":"Rua das Cravos",
        "Telefone":"219993334"
    }
}

#EXERCÍCIO 1: Obter todos os telefones de todos os clientes

for cliente in clientes:
    print(clientes[cliente].get("Telefone"))
    
#EXERCICIO 2: Remover a morada do cliente2

cliente2 = clientes["cliente2"]
del cliente2["morada"]
print(cliente2)

#EXERCICIO 3: Adicionar uma Key email vazia a todos os clientes
for cliente in clientes:
    addemail = clientes[cliente]
    addemail["email"] = ""
    print(addemail)

#EXERCICIO 4: Adicionar um valor ao email de cada cliente
    #joao.silva@gmail.com
    #ana.rosa@gmail.com
    #luis.cravo@gmail.com
    clientes["cliente1"].update({"email":"joao.silva@gmail.com"})
    clientes["cliente2"].update({"email":"ana.rosa@gmail.com"})
    clientes["cliente3"].update({"email":"luis.cravo@gmail.com"})
    print(clientes)

#EXERCICIO 5: Trocar a morada do cliente1 com o cliente2

moradacliente1 = clientes["cliente1"]
moradacliente2 = clientes["cliente2"]

moradacliente1


