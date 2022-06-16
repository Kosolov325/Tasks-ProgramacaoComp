import time
from math import prod

def task4():
    n = 0
    values = []
    while n < 10:
        n += 1
        value = int(input('Digite um valor: '))
        values.append(value)
    
    valM = sum(values)/10
    print('A média aritmética é', valM)

def task5():
    n = 0
    values = []
    valuesRange = []
    while n < 10:
        n += 1
        val = int(input('Digite um valor: '))
        values.append(val)
    
    for value in values:
        if value > 10 and value < 20:
            valuesRange.append(value)
    
    print('Há cerca de', len(valuesRange), 'números entre 10 e 20.')

def task7():
    values = []
    continuar = True
    while continuar == True:
        val = int(input("Digite um valor: "))

        if val != 0:
            if val % 2 == 0:
                values.append(val)
        else:
            continuar = False
            break

    valuesM = sum(values)/len(values)

    print('A média de números é', valuesM)

def task8():
    n = 0
    values = []
    while n < 50:
        n += 1
        val = int(input('Digite um número: '))
        values.append(val)
    print('O maior número é ', max(values))
    print('O menor número é', min(values))


def task9():
    values = []
    divisores = []
    continuar = True
    while continuar == True:
        val = int(input('Digite um valor: '))
        
        if val > 0 and val % 2 == 0:
            for i in range(1,9):
                if val % i == 0:
                    divisores.append(i)
                print('Os divisores de ', val, 'são esses:', divisores)

        elif val % 2 != 0 and val < 10:
            fact = 1
            for i in range(1, val+1):
                fact *= i
                
            print('O fatorial é', fact)

        elif val % 2 != 0 and val >= 10:
            for i in range(1, val):
                i += i
            print('A soma de valores é', i)
        cont = input('Continuar? (S/N): ')
        if cont.upper() == 'N':
            continuar = False
            break

def task10():
    continuar = True
    values = []
    valuesPares = []

    while continuar == True:
        val = int(input('Digite um valor: '))
        if val == 0:
            continuar = False
            continue
        elif val > 0:
            values.append(val)
    

    for value in values:
        if value % 2 == 0:
            valuesPares.append(value)
    

    print('A soma dos valores pares é', prod(valuesPares))

def task11():
    start_time = time.time()
    qnt = 0
    i = 0
    cont = 1
    while i < cont:
        divisores = []
        for n in range(1, i):
            if i % n == 0:
                divisores.append(n)
                

        if sum(divisores) == i:
            print(i)
            qnt += 1
            if qnt > 5:
                break
        
        cont += 1
        i += 1
       
    
    end_time = time.time() - start_time
    end_time_minutes = end_time/60
    print(end_time, 'segundos')
    print(end_time_minutes, 'minutos')

def task12():
    n = 100
    while n < 200:
        n += 1

        if n % 2:
            print(n)