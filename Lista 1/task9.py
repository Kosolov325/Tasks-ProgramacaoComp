typeComb = input("Digite o tipo de combustível: ")
qntComb = float(input("Digite a quantidade de combustível: "))
alcool = "Álcool"
gas = "Gasolina"
if (typeComb == alcool):
    preco = 0.90
    if(qntComb <= 20):
        desconto = 1 - 3/100
    elif(qntComb > 20):
        desconto = 1 - 4/100
elif (typeComb == gas):
    preco = 1.20
    if(qntComb <= 20):
        desconto = 1 - 4/100
    elif(qntComb > 20):
        desconto = 1 - 6/100   
valorF = qntComb * preco * desconto
print("Você irá pagar: R$ " + str(valorF))