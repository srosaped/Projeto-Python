# Scope de variáveis
# Grau de visibilidade das variáveis ao longo do programa

x="Lisboa"

def meuMetodo():
    global x
    x="Porto"
    print(x)

def meuMetodo2():
    global x
    x="Coimbra"
    print(x)

print(x)
meuMetodo()
meuMetodo2()
print(x)