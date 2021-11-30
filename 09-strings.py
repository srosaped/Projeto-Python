print("Olá")

a="Olá"
print(a)

a="""Olá bom dia
Hoje está um excelente dia
se não chover"""
print(a)

#Erro
#a="Olá bom dia"+
#  "Hoje está um excelente dia"+
#  "se não chover"

texto="piupiu"

for letra in texto:
    print(letra)

a="A Maria foi à fonte"
print(len(a))

print("Maria" in a)
print("João" in a)

if "Manuel" not in a:
    print("O Manuel não está no texto")

a="A Maria foi à fonte"
print(a[2])
print(a[2:5])
print(a[2:])
print(a[:5])
print(a[-5:-2])
print(a.lower())
print(a.upper())


a="              A Maria foi        à fonte             "
a=a.replace("  "," ")
print("|"+a.strip()+"|")

b="O Manuel foi à Bica"
b=b.replace("Manuel","João")

print(b)

texto="Bom dia hoje está um lindo dia"
print(type(a))
texto=texto.split(" ")
print(texto)
print(texto[2])

for palavra in texto:
    print(palavra)

texto2="Bom dia hoje está um lindo dia"
for letra in texto2:
    print(letra)
