from re import A


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

Media_exercicio = (n1 + n2 + n3)/3
Media_de_aproveitamento = (n1 + n2*2 + n3*3 + Media_exercicio)/7

if (Media_de_aproveitamento >= 9):
    conceito = "A"

elif (Media_de_aproveitamento >= 7,5) and (Media_de_aproveitamento < 9):
    conceito = "B"

elif (Media_de_aproveitamento >= 6) and (Media_de_aproveitamento < 7,5):
    conceito = "C"

elif (Media_de_aproveitamento < 6):
    conceito = "D"

print ("A faixa do seu aproveitamento foi " + conceito)