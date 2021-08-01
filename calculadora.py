class Calculadora:
    def __init__(self,num1=0,num2=0) :
        self.num1=num1
        self.num2=num2
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def multiplicacion(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2


class calEstandar(Calculadora):
    def __init__(self,num1=0,num2=0):
        super().__init__(num1,num2)
    def multiplicacion(self):
        multi = self.num1 * self.num2
        print("La multiplicacion es : {}".format(multi))
    def exponente(self):
        return self.num1 ** self.num2 
    def valorAbsoluto(self,numero):
        if numero < 0:
            abso = numero * -1
            return abso
 
class calCientifica(Calculadora):
    PI = 3.1416 
    def __init__(self, numero1=0, numero2=0, radio=0):
        super().__init__(numero1,numero2)
        self.radio=radio
        
    def circunferencia(self):
        return 2*self.PI*self.radio
    def areaCirculo(self):
        return self.PI*(self.radio**2)

    def areaCuadrado(self,lado):
        return lado**2
        
# obj=calEstandar(4,2)
# obj.multiplicacion()
#obj= calCientifica(2,3,5)
#print(obj.areaCirculo())
ob= calEstandar()
print(ob.valorAbsoluto(1))