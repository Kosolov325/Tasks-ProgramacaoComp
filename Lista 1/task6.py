numM = int(input("Quantas maças foram compradas: "))
preço1 = 1.30
preço2 = 1
if (numM < 12):
    preçoF = numM * preço1

elif (numM >= 12):
    preçoF = numM * preço2

print("Preço final:", preçoF)