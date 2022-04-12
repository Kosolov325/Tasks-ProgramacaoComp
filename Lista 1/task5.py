A = float(input("Escreva um valor: "))
B = float(input("Escreva outro valor: "))
C = float(input("Escreva mais um valor: "))


if (A < B + C) and (B < A + C) and (C < A + B):
    print("Os valores formam um triângulo.")
else:
    print("Os valores não formam um triângulo.")