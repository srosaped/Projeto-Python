# AND, OR e NOT

a=220
b=50
c=300

# OPERAÇÃO LÓGICA AND
#    a>b    c>a     a>b AND c>a
#     F      F           F
#     F      V           F
#     V      F           F
#     V      V           V

if a>b and c>a:
    print("Ambas as condições são verdadeiras")


# OPERAÇÃO LÓGICA OR
#    a>b    c>a     a>b OR c>a
#     F      F          F
#     F      V          V
#     V      F          V
#     V      V          V

if a>b or c>a:
    print("Pelo menos uma das condições é verdadeira")


# OPERAÇÃO LÓGICA NOT
#    a>b     NOT a>b
#     F         V

if not a>b:
    print('a não é maior que b')
else:
    print('a é maior que b')


if a>b:
    print('a é maior que b')
else:
    print('a não é maior que b')