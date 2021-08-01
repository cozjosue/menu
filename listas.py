
from operacionnumeros import *

class Listas(Intermedio):
    def __init__(self, lista=[]):
        self.lista=lista
    def presentarLista(self):
        for i in self.lista:
            print (i)

    def buscarLista(self,valor):           
        if valor in self.lista:
            print("Se ha encontrado el valor de {} en la lista".format(valor))
        else:
            print("Valor no encontrado el valor de {} en la lista".format(valor))

    def listaFactorial(self):
        list = []
        for i in self.lista:
            if type(i) == int:
                print("El factorial del numero {} es {}".format(i,obj.factorial(i)))
                list.append(obj.factorial(i))
        print(list)

    def listaPrimo(self):
        listan=[]
        for i in self.lista:
            if type(i)==int:
                if obj.primo(i) != None:
                    listan.append(obj.primo(i))
        return listan
                
          
        
        

    def listaNotas(self,listaNotasDiccionario):
        print("Notas")
        for i in listaNotasDiccionario:
            for clave , valor in i.items():
                print("El estudiante {} obtuvo una nota de {}".format(clave,valor))

    def insertarLista(self,posicion,valor):
        auxlist=[]
        for i in range(len(self.lista)):
            if i < posicion:
                auxlist.append(self.lista[i])
        auxlist.append(valor)
        auxlist = auxlist+self.lista[posicion:]   
        return auxlist

    def eliminarLista(self,valor):
        for i in self.lista:
            if i == valor:
                self.lista.remove(valor) 
        return self.lista

    def retornar(self,pos):
        for posicion,valor in enumerate (self.lista):
            if pos == posicion:
                print(("El dato retornado es : {}").format(valor)) 
        self.lista.pop(pos)
        print(("La lista sin el valor retornado:  {}") .format(self.lista))


    def tuplalista(self,tupla):
        list = []
        for i in tupla:
            list.append(i)
        return list

    def vueltoLista(self, listaClientesDiccionario):
        print("Clientes")
        for i in listaClientesDiccionario:
            for clave , valor in i.items():
                print("El cliente :{} , tiene un cupo de:{}".format(clave,valor))
