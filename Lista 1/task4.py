val1 = float(input("Escreva um valor: "))
val2 = float(input("Escreva outro valor: "))
val3 = float(input("Escreva mais um valor: "))


if (val1 > val2 and val1 > val3):
    firstVal = val1
    if (val2 > val3):
        secondVal = val2
    else:
        secondVal = val3

elif (val2 > val1 and val2 > val3):
    firstVal = val2
    if (val1 > val3):
        secondVal = val1
    else:
        secondVal = val3

elif (val3 > val1 and val3 > val2):
    firstVal = val3
    if (val2 > val1):
        secondVal = val2
    else:
        secondVal = val1


print("A soma dos maiores números é: ", firstVal + secondVal)