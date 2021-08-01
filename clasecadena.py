import os
class Cadena:
    def __init__(self,cadena=""):
        self.cadena=cadena
    
    def recorrerCadena(self):
        for i in self.cadena:
            print(i)
            
    def buscarCaracter(self,buscado):                 
        print("Caracter '{}' encontrado en la posición:\n-> {}".format(buscado,self.cadena.index(buscado)))

    def listaPosiciones(self,caracter):  
        if caracter in self.cadena:
            lista=[]
            for i,j in enumerate(self.cadena):
                if caracter==j:
                    lista+=[i]
            return lista  
                     
    def listaPalabras(self):
        lista=self.cadena.split()
        return lista
    
    def cadenaLista(self):
        while True:
            try:
                numero = int(input("Ingrese el número de elementos que tendrá la lista:\n-> "))
            except ValueError:
                os.system("cls")
                print("Ingrese un número válido")               
                continue
            if numero >10:
                os.system("cls")
                print("¡Lista muy larga!, ingrese menos elementos:\n-> ")              
                continue
            else:
                break
        lista = []
        for i in range(numero):
            print("Ingrese el ",str(i + 1) + " elemento: ", end=" ")
            palabra = input()
            lista += [palabra]
            cadena=" ".join(lista)
        return cadena

    def insertarDato(self,buscado,posicion):
        aux1=self.cadena[:posicion]
        aux1+=buscado
        aux2=self.cadena[posicion:]
        self.cadena=aux1+aux2
        print("Dato '{}' insertado en la posicion '{}'\nCadena:\n-> ".format(buscado,posicion),self.cadena)
        
    def eliminarOcurrencias(self,buscado):
        self.cadena = ''.join( x for x in self.cadena if x not in buscado)
        print("Cadena sin elementos ocurrentes:\n-> {}".format(self.cadena))
        
    def retornaValor(self,posicion):
        cadenaPosicion=self.cadena[posicion]
        aux1=self.cadena[:posicion]
        aux2=self.cadena[posicion+1:]
        self.cadena=aux1+aux2
        return cadenaPosicion
    def concatenarCadena(self,dato):
        cadena=""
        for i in range(dato):
            print("Ingrese la cadena", str(i + 1) + ": ", end=" ")
            palabra = input()+" "
            cadena+= palabra
        print("Cadenas concatenadas:\n-> ",cadena)
os.system("cls")
#cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
''' 1)Recorrer y presentar los datos de una cadena '''
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# llamar.recorrerCadena()
''' 2)	Buscar un carácter en una cadena '''
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# buscado=input("Ingrese caracter a buscar-> ")
# llamar.buscarCaracter(buscado)
''' 3)	Retornar una lista con la posiciones dado un carácter de la cadena '''
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# caracter=input("Ingrese caracter-> ")
# print(llamar.listaPosiciones(caracter))
''' 4)	Retornar una lista con todas las palabras de una cadena '''
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# print(llamar.listaPalabras())
''' 5)	Retornar una cadena a partir de una lista '''
# llamar=Cadena()
# print(llamar.cadenaLista())
""" 6)	Insertar un dato en una cadena dada lo Posición """
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# buscado=input("Ingrese dato-> ")
# posicion=int(input("Ingrese posicion-> "))
# llamar.insertarDato(buscado,posicion)
""" 7)	Eliminar todas las ocurrencias en una cadena """
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# buscado=input("Ingrese elemento a eliminar-> ")
# llamar.eliminarOcurrencias(buscado)
""" 8)	Retornar cualquier valor de una cadena  eliminándolo  """
# cadena=input("Ingresar cadena-> ")
# llamar=Cadena(cadena)
# posicion=int(input("Ingrese posicion-> "))
# print("El valor retornado de la posicion '{}'\nY eliminado de la cadena es -> '{}'".format(posicion,llamar.retornaValor(posicion)))
""" 9)	Concatenar cadenas """
# llamar=Cadena()
# dato=int(input("Ingrese el número de de cadenas que desea concatenar-> "))
# llamar.concatenarCadena(dato)