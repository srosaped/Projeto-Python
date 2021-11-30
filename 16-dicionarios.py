cliente={
    "Nome":"Luís Silva",
    "Morada":"Rua dos Silvas nº1",
    "CPostal":"1000-100 Lisboa",
    "Telefone":"211234567",
    "EMail":"luis.silva@gmail.com",
    "Hobbies":{"Canoagem", "Corrida", "Paraquedismo"}
}

telefone=cliente.get("Telefone")
print(telefone)
email=cliente["EMail"]
print(email)

print(cliente.keys())
print(cliente.values())

for key in cliente.keys():
    print(cliente[key])

for value in cliente.values():
    print(value)

print(cliente.items())
[('Nome', 'Luís Silva'), ('Morada', 'Rua dos Silvas nº1'), ('CPostal', '1000-100 Lisboa'), ('Telefone', '211234567'), ('EMail', 'luis.silva@gmail.com'), ('Hobbies', {'Paraquedismo', 'Corrida', 'Canoagem'})]



for item in cliente.items():
    print(item[0],":", item[1])

if "EMail" in cliente:
    print(cliente["EMail"])

cliente["CPostal"]="4000-400 Porto"
print(cliente)

cliente.update({"CPostal":"3000-3000 Coimbra","EMail":"lsilva@outlook.com"})
print(cliente)

cliente.popitem()
print(cliente)

del cliente["CPostal"]
print(cliente)

#del cliente
#print(cliente)

cliente.clear()
print(cliente)
print(bool(cliente))




cliente={
    "Nome":"Luís Silva",
    "Morada":"Rua dos Silvas nº1",
    "CPostal":"1000-100 Lisboa",
    "Telefone":"211234567",
    "EMail":"luis.silva@gmail.com",
    "Hobbies":{"Canoagem", "Corrida", "Paraquedismo"}
}

novocliente=cliente
novocliente=cliente.copy()
