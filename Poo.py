from multiprocessing.sharedctypes import Value



class Calculadora():
    __valor1 = float
    __valor2 = float

    def verify_values(self):
        if (self.valor1 == 0) or (self.valor2 == 0):
            return False
        else:
            return True
        
    @property
    def valor1(self):
        return self.__valor1
    
    @property
    def valor2(self):
        return self.__valor2

    def multi(self):
        self.verify_values()
        return self.__valor1 * self.__valor2

    def div(self):
        self.verify_values()
        return self.__valor1 / self.__valor2
    
    def __init__(self, valor1, valor2):
        self.__valor1 = valor1
        self.__valor2 = valor2




valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

c = Calculadora(valor1, valor2)

print('Os resultados foram:', c.multi(), c.div())

