#WHILE

# i=1
# while i<6:
#     print(i)
#    i+=1

#Resultado:
# 1
# 2
# 3
# 4
# 5

# i=1
# while i<6:
#     i+=1
#     if i==3:
#         break
#     print(i)
# print("Estou fora")

# Resultado:
# 2

# i=1
# while i<6:
#     i+=1
#     if i==3:
#         continue
#     print(i)

# Resultado:
# 2
# 4
# 5
# 6

i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
else:
    print("O i já não é menor que 6")

# Resultado:
# 2
