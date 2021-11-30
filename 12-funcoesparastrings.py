a="hoje está um lindo dia de sol. Eu sou um grande mentiroso."
print(a.upper())
print(a.lower())
print(a.capitalize())



b="A MARIA ESTÁ FELIZ!"
print(b.casefold())
print(b.lower())

b="a maria está feliz!"
print(b.casefold())

c="titulo"
print(b)
print((c.capitalize()).center(len(b),"*"))

print(b)
print("".center(len(b),"*"))


#Imagem que a variável a contem o texto Nome preenchido no formulário da página
#É preciso saber se o cliente preencheu o nome

nome=""

#bool("") dá false
#bool("Luís") dá true

if bool(nome):
    print("O cliente preencheu o nome")
else:
    print("O cliente não preencheu o nome")

print(bool(nome))

z=-10000345345
print(bool(z))

y=0.0
print(bool(y))


x=0+0j
print(bool(x))

cidades=["Lisboa", "Porto", "Coimbra"]
print(bool(cidades))

cidades=[]
print(bool(cidades))

texto=" "
print(bool(texto))


