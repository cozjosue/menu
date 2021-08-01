class Basico:
    def __init__(self,num=0):
        self.num=num
        
        
    def numerosN(self):
        for i in range(1,self.num+1):
            print (i,end=" ")
        print()
    def sumaN(self):
        acu = 0
        for i in range(1,self.num+1):
            acu = acu + i
        return acu
        
    def multiplo(self):
        for i in range(1,11):
            print("{} x {} =".format(i,self.num), i*self.num)

    def DivisoresNumero(self):
        for i in range(1,self.num+1):
            if not self.num % i :
                print (i)

    def primo(self,numero):
        lista=[]
        for i in range(1,100):
            if not numero % i :
                lista.append(i)
        if not len(lista)>2 or len(lista)<2:
            
            return numero
            # print("{} no es un numero primo".format(numero))
            #print(lista)
            
        # else:
        #     # print("{} es un numero primo".format(numero))
        #     return numero
            
            #print(lista)
            
        
        

    def perfecto(self):
        acu=0
        for contador in range(1,self.num):
            rec=self.num%contador
            if rec == 0 :
                acu=acu+contador
        if acu == self.num:
            print("{} es perfecto".format(self.num))
        else:
            print("{} No es perfecto".format(self.num))
            
class Intermedio(Basico):
    def __init__(self, num=1):
        super().__init__(num=num)
        

    def numerosN(self):
        return super().numerosN()

    def factorial(self,numero):
        acu = 1
        for i in range(1,numero+1):
            acu = acu * i
        return acu
        
    def fibonacci(self,n=1):

        a=0
        b=1
        for i in range(0,n):
            acu = a + b
            a = b
            b = acu
            print(a,end=" ")
                
        
                
    def primosgemelos(self,n1,n2):
        if n1 == (n2 - 2):
            print("Los numeros {} y {} son primos gemelos ".format(n1,n2))
        else :
            print("Los numeros {} y {} no son primos gemelos ".format(n1,n2))

    def numerosamigos(self,n1,n2):
        acu1=0
        acu2=0
        for i in range(1,n1):
            if not n1%i:
                acu1 = acu1 + i

        for j in range(1,n2):
            if not n2%j:
                acu2 = acu2 + j

        if acu1 == n2 and acu2 == n1:
            print("Los numeros {} y {} son amigos".format(n1,n2))
        else:
            print("Los numeros {} y {} no son amigos".format(n1,n2))

# obj=Intermedio()
# obj.numerosamigos(1184,1210)