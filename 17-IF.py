#IF, IF ELSE, IF ELIF ELSE
# ==
# !=
# <
# >
# >=
# <=

a=2  #Atribuir o valor 2 à variável a
a==2 #Comparar o valor 2 com o valor guardado na variável a ( O resultado será True ou False)


a=220
b=33


#IF
if a>b:
    print("a>b")

if a<b:
    print("a<b")

if a>=b:
    print("a>=b")

if a<=b:
    print("a<=b")

if a!=b:
    print("a!=b")

if a==b:
    print("a==b")


#if else
if a==b:
    print("a e b são iguais")
else:
    print("a e b são diferentes")

#if elif else
if a>b:
    print("a>b")
elif a<b:
    print("a<b")
elif a>=b:
    print("a>=b")
elif a<=b:
    print("a<=b")
elif a==b:
    print("a==b")
elif a!=b:
    print("a!=b")
else:
    print("Não faço a mais pálida ideia")


#Short Hand If
if a>b: print('a>b')

# Short Hand If Else
if a>b:
    print('a>b')
else:
    print('Outra coisa qualquer')

print('a>b') if a>b else print('Outra coisa qualquer')




