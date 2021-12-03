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
    #Alternativa 1
for cliente in clientes.values():
    print(cliente["Telefone"])

    #Alternativa 2
for cliente in clientes:
    print("Telefone: "+clientes[cliente].get("Telefone"))

    #Alternativa 3
for cliente in clientes.items():
    print(cliente[1]['Telefone'])



#EXERCICIO 2: Remover a morada do cliente2
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
    #Alternativa 1 - Elimina a key e o value
clientes["cliente2"].pop("morada")
    
    #Alternativa 2 - Elimina o valor
clientes["cliente2"]["morada"]=""

#EXERCICIO 3: Adicionar uma Key email vazia a todos os clientes
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
    #Alternativa 1 - Funciona para qualquer nº de registos
for cliente in clientes.values():
    cliente["Email"]=""

    #Alternativa 2 - Limitado aos registos existentes
clientes["cliente1"].update({"Email":""})
clientes["cliente2"].update({"Email":""})
clientes["cliente3"].update({"Email":""})

    #Alternativa 3 - Funciona para qualquer nº de registos
for key in clientes.keys():
    clientes[key]['Email'] = ''

    #Alternativa 4 - Funciona para qualquer nº de registos
for cliente in clientes:
    clientes[cliente]["email"] = ""

#EXERCICIO 4: Adicionar um valor ao email de cada cliente
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
    #joao.silva@gmail.com
    #ana.rosa@gmail.com
    #luis.cravo@gmail.com

    #Alternativa 1
emails=["joao.silva@gmail.com","ana.rosa@gmail.com","luis.cravo@gmail.com"]
for cliente in clientes.values():
    cliente["Email"]=emails[0]
    emails.pop(0)

    #Alternativa 2
clientes["cliente1"]['Email'] = 'joao.silva@gmail.com'
clientes["cliente2"]['Email'] = 'joao.silva@gmail.com'
clientes["cliente3"]['Email'] = 'joao.silva@gmail.com'

    #Alternativa 3
clientes["cliente1"].update({"Email":"joao.silva@gmail.com"})
clientes["cliente2"].update({"Email":"ana.rosa@gmail.com"})
clientes["cliente3"].update({"Email":"luis.cravo@gmail.com"})


#EXERCICIO 5: Trocar a morada do cliente1 com o cliente2
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
    #Alternativa 1
[clientes["cliente1"]["morada"],clientes["cliente2"]["morada"]]=[clientes["cliente2"]["morada"],clientes["cliente1"]["morada"]]

    #Alternativa 2
temp = clientes["cliente1"]["morada"]
clientes["cliente1"]['morada'] = clientes["cliente2"]['morada']
clientes["cliente2"]['morada'] = temp



