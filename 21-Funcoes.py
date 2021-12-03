# Funcoes

#def somar(a,b,c):
#    return a+b+c

#print(somar(2,3,7))
#2
#3
#7

#print(somar(somar(2,3),7))

def somar(*valores):
    resultado=0
    for valor in valores:
        if type(valor)==int or type(valor)==float or type(valor)==complex:
            resultado+=valor
    return resultado

print(somar(2,3,7))
print(somar(2))
print(somar(2,3,78,2345654,345345345,123123131,324,-34535345))
print(somar(2.4,3.5))
print(somar(1+1j,4+5j))


print(somar(1,2.4,'a',2))