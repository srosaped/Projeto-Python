# Sets

set1={"Bisonte", "Zebra", "Avestruz", "Leão", "Ornitorrinco", "Vaca"}
set2=set(("Bisonte", "Zebra", "Avestruz", "Leão", "Ornitorrinco", "Vaca"))

set1.update(set2)
print(set1)
print(set1)

frutas=["Banana", "Maçã", "Ananás", "Banana"]
animais=("Vaca", "Porco", "Cavalo", "Galinha")
plantas={"Hortense", "Orquídea", "Alface"}
plantas.update(frutas)
print(plantas)
plantas.update(animais)
print(plantas)