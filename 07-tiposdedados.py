# Tipos de dados

#string (texto)
x="Maria"
x='Maria'
y="M"
y='M'
print(type(x))
print(type(y))

#int
x=5
x=12345567890
print(type(x))

#float
x=20.5
print(type(x))

# complex
# a + bj
# a
# bj
# a + bj

x=1
print(type(x))
x=1+1j
print(type(x))
x=2j
print(type(x))
x=1.5+3.2j
print(type(x))

x=2+3j
y=4+5j
print(x+y)

x=2+3j
y=4-5j
print(x+y)

#lista
x=["Lisboa", "Porto", "Faro"]
print(x)
x[0]="Funchal"
print(x)

#tuplo
x=("Lisboa", "Porto", "Faro")
print(x)
print(x[0])
#x[0]="Funchal" Não é possível alterar valores de um tuplo
print(x)

#range
x=range(6)

#dicionário
x={"Cidade":"Lisboa","Freguesia":"Belém"}
y={"Cidade":"Porto","Freguesia":"Bonfim"}
z={"Cidade":"Coimbra","Freguesia":"Santo António dos Olivais"}
a=[x,y,z]

#Lista de dicionarios <=> JSON
a=[
    {"Cidade":"Lisboa","Freguesia":"Belém"},
    {"Cidade":"Porto","Freguesia":"Bonfim"},
    {"Cidade":"Coimbra","Freguesia":"Santo António dos Olivais"}
]

print(a)

#set
x={"Lisboa", "Porto", "Coimbra"}

paises={"Nome":"Portugal", "Cidades":x}
pais1={"Nome":"Portugal", "Cidades":{"Lisboa", "Porto", "Coimbra"}}
pais2={"Nome":"Espanha", "Cidades":{"Madrid", "Barcelona","Sevilha"}}

paises=[pais1,pais2]
paises=[{"Nome":"Portugal", "Cidades":{"Lisboa", "Porto", "Coimbra"}},{"Nome":"Espanha", "Cidades":{"Madrid", "Barcelona","Sevilha"}}]

#frozenset
x=frozenset({"Madrid", "Barcelona","Sevilha"})

#Booleano
x=True
y=False

#bytes
x=b"Ola" #Só aceita caracteres da Tabela de Código ASCII entre o código 0 e o 127

x=bytearray(5)
y=memoryview(bytes(5))
print(y)





