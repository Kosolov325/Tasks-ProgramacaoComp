qntMor = float(input("Digite quantos Kg morangos você quer comprar: "))
qntM = float(input("Digite quantos Kg de maça você quer comprar: "))

if (qntMor <= 5):
    valorMor = qntMor * 2.0
else:
    valorMor = qntMor * 1.80

if (qntM <= 5):
    valorM = qntM * 1.50
else:
    valorM = qntM * 1.10

valorT = valorM + valorMor

if (qntMor + qntM > 8) or (valorMor + valorM > 25):
    valorT *= 1 - 10/100

print("Valor total para pagar: " + "R$ " + str(valorT))


