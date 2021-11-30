#Tuplos (READ ONLY)

lista=["Vaca", "Porco", "Cavalo", "Galinha"]
print(lista)

tuplo=("Vaca", "Porco", "Cavalo", "Galinha")
print(tuplo)

lista2=list(tuplo)
print(lista2)

print(tuplo[1])
print(tuplo[-1])
print(tuplo[2:4])
print(tuplo[2:])
print(tuplo[:3])

lista[1]="Doninha"
print(lista)

# Erro - Não se pode alterar um tuplo
# tuplo[1]="Doninha"
# print(tuplo)

# Então como é que eu altero um tuplo?
tuplo=("Vaca", "Porco", "Cavalo", "Galinha")
lista=list(tuplo)
lista[1]="Doninha"
tuplo=tuple(lista)
print(tuplo)