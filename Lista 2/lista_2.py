from datetime import date
import turtle
import math

#Questão 1
 #Os valores que vão ser escritos na tela do usuário serão
 #os que estão guardados na variável C, pois 
 # A=5, B=10, C=15, D=20 e Maior=20, 
 # logo percebe-se que a única condição que é verdadeira é C ser menor que Maior,
 # pois C equivale a 15 e Maior equivale a 20.

#Questão 2
def task2():
    A = 10
    B = 20
    print('Inicialmente os valores são:', A, 'e', B)
    
    C = A
    A = B
    B = C
    print('Invertendo os valores temos', A, 'e', B)


#Questão 3
def task3():
    aceitavelStart = 0.05
    aceitavelEnd = 0.25
    firstGroupWarn = 0.3
    secondGroupWarn = 0.4
    thirdGroupWarn = 0.5

    firstIndustriesGroup = ['Industria A', 'Industria B']
    secondIndustriesGroup = ['Industria C', 'Industria D']
    thirdIndustriesGroup = ['Industria E', 'Industria F']
    poluicao = float(input('Digite o estado de poluição: '))

    if(poluicao > aceitavelStart) and (poluicao <= aceitavelEnd):
        print('A poluição está em níveis aceitaveis')
    elif (poluicao > aceitavelEnd) and (poluicao <= firstGroupWarn) and (poluicao < secondGroupWarn):
        industriesWarn = firstIndustriesGroup
        print(industriesWarn, 'Intimadas')
    elif(poluicao > firstGroupWarn) and (poluicao <= secondGroupWarn):
        industriesWarn = firstIndustriesGroup + secondIndustriesGroup
        print(industriesWarn, 'Intimadas')
    elif(poluicao >= thirdGroupWarn):
        industriesWarn = firstIndustriesGroup + secondIndustriesGroup + thirdIndustriesGroup
        print(industriesWarn, 'Intimadas')

#Questão 4
def task4():
    num = int(input('Digite um número: '))


    if (num < 0):
        print(num, 'é negativo')
    elif (num > 0):
        print(num, 'é maior que zero')
    elif (num == 0):
        print(num, 'é zero')
    
    if (num % 2 == 0):
        print(num, 'é um número par')
    else:
        print(num, 'é um número impar')
    

#Questão 5
def task5():
     dia = int(input('Digite o dia do seu nascimento: '))
     mes = int(input('Digite o mês do seu nascimento: '))
     ano = int(input('Digite o ano do seu nascimento: '))
     hoje = date.today()
     
     nasc = date(year=ano, month=mes, day=dia)

     calc = (hoje - nasc)/365
     idade = calc.days
     print('Você tem', idade, 'anos')
    

#Questão 6
def task6():
    cX = float(input('Digite a posição do centro X do círculo: '))
    cY = float(input('Digite a posição do centro Y do círculo: '))
    raio = float(input('Digite o raio do círculo: '))
    pX = float(input('Digite qualquer ponto X: '))
    pY = float(input('Digite qualquer ponto Y: '))

    distPontos = (cX - pX)**2 + (cY + pY)**2
    if  (distPontos > raio**2) or (distPontos == raio**2):
            print('O ponto está fora do círculo')
    elif (distPontos < raio**2):
            print('O ponto está dentro do círculo')

    while True:
        t = turtle.Turtle()
        t.setpos(0, 500)
        t.setpos(0, -500)
        t.up()
        t.setpos(500, 0)
        t.down()
        t.setpos(-500, 0)
        t.up()
        t.setpos(cX, cY - raio * 2)
        t.down()
        t.circle(raio * 2)
        t.up()
        t.setpos(cX, cY)
        t.down()
        t.setpos(pX, pY)
    
#Questão 7
def task7():
    segundos = float(input('Digite a duração do evento em segundos: '))

    horas = segundos / 3600
    minutos = segundos / 60

    print('Horas:', horas, 'Minutos:', minutos, 'Segundos:', segundos)


#Questão 8
def task8():
    num = 0
    while num < 10:
        num += 1
        print(num)

#Questão 9
def task9():
    num = int(input('Digite um número: '))
    loop = 0

    while loop < num:
        loop += 1
        print(loop)

#Questão 10
def task10():
    num = int(input('Digite um número: '))

    if (num >= 1) and (num <=10):
        loop = 0
        while loop < 10:
            loop += 1
            tabuada = num * loop
            print(num, '*', loop, '=', tabuada)

#Questão 11
def task11():
    continuar = True
    salarios = []
    filhos = []
    while continuar == True:
        salario = float(input('Digite o seu sálario: '))
        if salario > 0:
            salarios.append(salario)
        else:
            print('Entrada de dados parada!')
            continuar = False
            continue

        filho = int(input('Digite quantos filhos você tem: '))
        if filho > 0:
            filhos.append(filho)
    
    mediaSal = sum(salarios)/len(salarios)
    mediaFilhos = sum(filhos)/len(filhos)
    
    salarios_100_qnt = 0

    for salario in salarios:
        if salario <= 100:
            salarios_100_qnt += 1

    mediaSalarios100 = salarios_100_qnt * 100/len(salarios)

    mediaFilhosFormat = math.floor(mediaFilhos)
    salariosFormat = max(salarios)
    
    print('--------------------------------------------------------------------')
    print('A media de filhos dos usuarios é de:', "{:.2f}".format(round(mediaFilhosFormat)), 'filhos')
    print('O salário médio dos usuários é de:', 'R$' + "{:.2f}".format(mediaSal))
    print('O maior salário é de:', 'R$' + '{:.2f}'.format(salariosFormat))
    print('Percentual de pessoas que vivem com até R$100.00:', "{:.2f}".format(mediaSalarios100) + '%')
    print('--------------------------------------------------------------------')