# ler 3 números e determinar o maior, o médio e o menor

a = float(input("Digite A: "))
b = float(input("Digite B: "))
c = float(input("Digite C: "))

maior = 0.0
medio = 0.0
menor = 0.0

if (a > b) and (a > c):
    maior = a
    if (b > c):
        medio = b
        menor = c
    else:
        medio = c
        menor = b
elif (b > a) and (b > c):
    maior = b
    if (a > c):
        medio = a
        menor = c
    else:
        medio = c
        menor = a
elif (c > a) and (c > b):
    maior = c
    if (a > b):
        medio = a
        menor = b
    else:
        medio = b
        menor = a

print(maior, medio, menor)

