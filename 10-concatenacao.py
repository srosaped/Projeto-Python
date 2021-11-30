a="Lisboa"
print("Hoje fui a "+a)




idade=23
peso=50
altura=1.73

a="O meu nome é Joana e tenho "+str(idade)
print(a)


a="O meu nome é Joana e tenho {}"
a=a.format(idade)
print(a)

a="O meu nome é Joana, tenho {} anos, peso {}kg e meço {}m de altura"
a=a.format(idade, peso, altura)
print(a)

a="O meu nome é Joana, tenho {2} anos, peso {0}kg e meço {1}m de altura"

a=a.format(peso,altura,idade)
print(a)