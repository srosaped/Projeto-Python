# Listas

frutas=["Banana","Maçã","Ananás","Banana"]
print(frutas)
print(len(frutas))

frutas=["Banana","Maçã","Ananás","Banana"]
classificacoes=[2,5,4,2,3]
permissoes=[True,False,True,True,False]
pack=[1,True,"Banana",23]

print(type(frutas))

frutas=["Banana","Maçã","Ananás","Banana"]
frutas=list(("Banana","Maçã","Ananás","Banana"))

print(frutas[1])
print(frutas[-2])
print(frutas[2:])


animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais[1]="Lobo"
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais[1:3]=["Lobo","Crocodilo"]
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais[1:3]=["Lobo"]
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais.insert(1,"Crocodilo")
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais.insert(len(animais),"Crocodilo")
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais.append("Crocodilo")
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
novosanimais=["Coelho","Peru","Raposa", "Jacaré", "Avestruz", "Rato"]
animais.extend(novosanimais)
print(animais)
animais.remove("Jacaré")
print(animais)

animais=['Vaca', 'Porco', 'Cavalo', 'Galinha', 'Coelho', 'Peru', 'Raposa', 'Jacaré', 'Avestruz', 'Rato']
animais[1:2]=[]
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais.pop(1)
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais.clear()
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]

for animal in animais:
    print(animal)

# range(6)    [0,1,2,3,4,5]

for i in range(len(animais)):
    print(animais[i])

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
print(animais)
animais.sort()
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
print(animais)
animais.sort(reverse=True)
print(animais)

animais=["Vaca", "Porco", "Cavalo", "Galinha"]
print(animais)
animais.reverse()
print(animais)


animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais2=animais
print("animais:",animais)
print("animais2:",animais2)
animais[1]="Canário"
print("animais:",animais)
print("animais2:",animais2)


animais=["Vaca", "Porco", "Cavalo", "Galinha"]
animais2=list(animais)
print("animais:",animais)
print("animais2:",animais2)
animais[1]="Canário"
print("animais:",animais)
print("animais2:",animais2)