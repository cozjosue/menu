from calculadora import *
from operacionnumeros import *
from clasecadena import *
from listas import *
import os
class Menu:
    def __init__(self, titulo='', opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input('Elija opcion [1...{}]: '.format(len(self.opciones)))
        return opc

opc = ''
while opc != '5':
    os.system("cls")
    menu = Menu('MENU PRINCIPAL', ['1) Calculadora', '2) Operacion numeros', '3) Tratamiento de listas', '4) Operacion de cadenas', '5) Salir'])
    opc = menu.menu()

    if opc == '1':
        opc1 = ''
        while opc1 != '10':
            os.system("cls")
            menu1 = Menu('//--MENU CALCULADORA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                os.system("cls")
                try:
                    print('Suma')
                    n1=float(input("Ingrese el primer numero: "))
                    n2=float(input("Ingrese el segundo numero: "))
                    obj1=calCientifica(n1,n2)
                    print(("{} + {} = {}").format(n1,n2,obj1.suma()))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue
            if opc1 == '2':
                os.system("cls")
                try:
                    print('Resta')
                    n1=float(input("Ingrese el primer numero: "))
                    n2=float(input("Ingrese el segundo numero: "))
                    obj1=calCientifica(n1,n2)
                    print(("{} - {} = {}").format(n1,n2,obj1.resta()))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue
            if opc1 == '3':
                os.system("cls")
                try:
                    print('Multiplicacion')
                    n1=float(input("Ingrese el primer numero: "))
                    n2=float(input("Ingrese el segundo numero: "))
                    obj1=calCientifica(n1,n2)
                    print(("{} * {} = {}").format(n1,n2,obj1.multiplicacion()))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '4':
                os.system("cls")
                try:
                    print('Division')
                    n1=float(input("Ingrese el primer numero: "))
                    n2=float(input("Ingrese el segundo numero: "))
                    if n2 != 0:
                        obj1=calCientifica(n1,n2)
                        print(("{} / {} = {}").format(n1,n2,obj1.division()))
                        input("Presione una tecla para continuar...")
                    else:
                        print("Error division para 0")
                        input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue
            
            if opc1 == '5':
                os.system("cls")
                try:
                    print('Exponente')
                    n1=float(input("Ingrese el primer numero: "))
                    n2=float(input("Ingrese el segundo numero: "))
                    obj1=calEstandar(n1,n2)
                    print(("{} ** {} = {}").format(n1,n2,obj1.exponente()))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '6':
                os.system("cls")
                try:
                    print('Valor Absoluto')
                    n=float(input("Ingrese un numero: "))
                    obj1=calEstandar()
                    print(("el numero es :{} , en valor absoluto: {}").format(n,obj1.valorAbsoluto(n)))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '7':
                os.system("cls")
                try:
                    print('Circunferencia')
                    rad = float(input("Ingrese el radio: "))
                    obj1=calCientifica(radio=rad)
                    print(("la cinfunferencia es : {}").format(round(obj1.circunferencia(),2)))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '8':
                os.system("cls")
                try:
                    print('Area del circulo')
                    rad = float(input("Ingrese el radio: "))
                    obj1=calCientifica(radio=rad)
                    print(("el area del circulo es : {}").format(round(obj1.areaCirculo(),2)))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue
            
            if opc1 == '9':
                os.system("cls")
                try:
                    print('Area Cuadrado')
                    lado = float(input("Ingrese un lado del cuadrado: "))
                    obj1=calCientifica()
                    print(("el area del cuadrado es : {}").format(obj1.areaCuadrado(lado)))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

    elif opc == '2':
        opc1 = ''
        while opc1 != '11':
            os.system("cls")
            menu1 = Menu('//--OPERACION NUMEROS--//', ['1) Presentar los números de 1 a n', '2) Sumar los números de 1 a n', '3) Múltiplo de cualquier numero', '4) Presentar los divisores de un numero', '5) Numero Primo', '6) Factorial de cualquier numero', '7) Fibonacci de una serie de n números', '8) Numero Perfecto','9) Primos gemelos', '10) Números amigos','11) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                os.system("cls")
                try:
                    print('PRESENTAR NUMEROS DE 1 HASTA N')
                    n=int(input("Ingrese hasta que numero desea presentar en pantalla :"))
                    obj = Basico(n)
                    obj.numerosN()
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '2':
                os.system("cls")
                try:
                    print('SUMA DE NUMEROS DE 1 HASTA N')
                    n=int(input("Ingrese el numero hasta el que desea sumar :"))
                    obj = Basico(n)
                    print('La suma de 1 hasta {} es : {} '.format(n,obj.sumaN()))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '3':
                os.system("cls")
                try:
                    print('MULTIPLOS')
                    n=int(input("Ingrese el numero que desea saber sus multiplos :"))
                    obj = Basico(n)
                    print('Los primeros 10 multiplos de {} son:'.format(n))
                    obj.multiplo()
                    input("Presione una tecla para continuar...")   
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '4':
                os.system("cls")
                try:
                    print('DIVISORES DE UN NUMERO')
                    n=int(input("Ingrese un numero :"))
                    obj = Basico(n)
                    print('Los divisores de {} son:'.format(n))
                    obj.DivisoresNumero()
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '5':
                os.system("cls")
                try:
                    print('NUMERO PRIMO')
                    n=int(input("Ingrese un numero para comprobar si es primo (hasta 100):"))
                    obj = Basico()
                    
                    if obj.primo(n) != None:
                        print("{} es un numero primo".format(n))
                    else:
                        print("{} no es un numero primo".format(n))

                    input("Presione una tecla para continuar...")
                except ValueError :
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue
            
            if opc1 == '6':
                os.system("cls")
                try:
                    print('FACTORIAL')
                    n=int(input("Ingrese el numero para calcular su factorial :"))
                    obj= Intermedio()
                    print("El factorial de {} es : {}".format(n,obj.factorial(n)))
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '7':
                os.system("cls")
                try:
                    print("FIBONACCI")
                    sel = True
                    preg ="y"
                    while sel:
                        if preg.lower() == "y":
                            n = int(input("Ingrese un numero : "))
                            obj=Intermedio()
                            obj.fibonacci(n) 
                            print()
                            print()
                            preg = input ("Desea continuar ? digite (y) para seguir: ")
                        else:
                            sel = False
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '8':
                os.system("cls")
                try:
                    print('NUMERO PERFECTO')
                    n=int(input("Ingrese un numero para comprobar si es perfecto :"))
                    obj= Basico(n)
                    obj.perfecto()
                    input("Presione una tecla para continuar...")   
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '9':
                os.system("cls")
                try:
                    print('PRIMOS GEMELOS')
                    n1=int(input("Ingrese el primer numero :"))
                    n2=int(input("Ingrese el segundo numero :"))
                    obj= Intermedio()
                    obj.primosgemelos(n1,n2)
                    input("Presione una tecla para continuar...")  
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue

            if opc1 == '10':
                os.system("cls")
                try:
                    print('NUMEROS AMIGOS')
                    n1=int(input("Ingrese el primer numero :"))
                    n2=int(input("Ingrese el segundo numero :"))
                    obj= Intermedio()
                    obj.numerosamigos(n1,n2)
                    input("Presione una tecla para continuar...")
                except ValueError:
                    print("Ingrese un dato valido !")
                    input("Presione una tecla para continuar...")
                    continue
    elif opc == '3':
        opc1 = ''
        while opc1 != '11':
            os.system("cls")
            menu1 = Menu('//--TRATAMIENTO LISTAS--//', ['1) Recorrer y presentar los datos de una lista', '2) Buscar un valor en una lista', '3) Retornar una lista con los factoriales', '4) Retornar una lista de números primos', '5) Recorrer una lista de diccionario con notas de alumnos', '6) Insertar un dato en una Lista dada lo Posición', '7) Eliminar todas las ocurrencias en una Lista', '8) Retornar cualquier valor de una lista eliminándolo ','9) Copiar cada elemento de una tupla en una lista', '10) Dar el vuelto a varios clientes','11) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                os.system("cls")  
                print('RECORRER Y PRESENTAR DATOS')
                lista=[]
                y=True
                while y:
                    lista.append(input("Ingrese datos en la lista : "))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls")
                print('RECORRER Y PRESENTAR DATOS')
                obj = Listas(lista)
                obj.presentarLista()
                input("Presione una tecla para continuar...")
                 
                      
            if opc1 == '2':
                os.system("cls") 
                print('BUSCAR VALOR')
                lista=[]
                y=True
                while y:
                    lista.append(input("Ingrese datos en la lista : "))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls")
                print('BUSCAR VALOR')
                obj = Listas(lista)
                val = input("Ingrese el valor que desea buscar : ")
                obj.buscarLista(val)
                input("Presione una tecla para continuar...") 

            if opc1 == '3':
                os.system("cls") 
                print('RETORNAR LISTA FACTORIALES')
                lista=[]
                y=True
                while y:
                    lista.append(int(input("Ingrese datos en la lista : ")))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls")
                print('RETORNAR LISTA FACTORIALES')
                obj=Listas(lista)
                obj.listaFactorial()
                input("Presione una tecla para continuar...")  
                
            if opc1 == '4':
                os.system("cls") 
                print('RETORNAR LISTA NUMEROS PRIMOS')
                lista=[]
                y=True
                while y:
                    lista.append(int(input("Ingrese datos en la lista : ")))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls")
                print('RETORNAR LISTA NUMEROS PRIMOS')
                print('Los numeros primos ingresados son :')
                obj=Listas(lista)
                print(obj.listaPrimo())
                input("Presione una tecla para continuar...") 

            if opc1 == '5':
                os.system("cls") 
                print('RETORNAR DICCIONARIO ALUMNOS - NOTAS')
                dic = {}
                y = True
                while y:
                    clave = input("Ingrese el nombre del alunmo : ")
                    valor = input("Ingrese su nota : ")
                    dic[clave]=valor
                    y = input("Desea agregar otro alumno? (ingrese y para continuar) ")
                    if y != "y":
                         y = False
                    else:
                        continue
                    list =[]
                    list.append(dic)

                os.system("cls")
                print('RETORNAR DICCIONARIO ALUMNOS - NOTAS')
                obj=Listas()
                obj.listaNotas(list)
                input("Presione una tecla para continuar...")  

            if opc1 == '6':
                os.system("cls") 
                print('INSERTAR UN DATO')
                lista=[]
                y=True
                while y:
                    lista.append((input("Ingrese datos en la lista : ")))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls") 
                print('INSERTAR UN DATO')
                obj = Listas(lista)
                pos = int(input("Ingrese la posicion en la que desea insertar el dato : "))
                valor = input("Que dato desea ingresar a la lista :")
                print(obj.insertarLista(pos,valor))
                input("Presione una tecla para continuar...")  

            if opc1 == '7':
                os.system("cls") 
                print('ELIMINAR OCURRENCIAS')
                lista=[]
                y=True
                while y:
                    lista.append(input("Ingrese datos en la lista : "))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls") 
                print('ELIMINAR OCURRENCIAS')       
                obj = Listas(lista)
                valor = input("Que dato desea eliminar de la lista :")
                print(obj.eliminarLista(valor))
                input("Presione una tecla para continuar...")  

            if opc1 == '8':
                os.system("cls") 
                print('RETORNAR UN VALOR ELIMINANDOLO DE LA LISTA')
                lista=[]
                y=True
                while y:
                    lista.append(input("Ingrese datos en la lista : "))
                    y = input("Desea ingresar otro dato ? (ingrese y para continuar): ")
                    if y != "y":
                        y = False
                    else:
                        continue
                os.system("cls") 
                print('RETORNAR UN VALOR ELIMINANDOLO DE LA LISTA')
                obj = Listas(lista)
                valor = int(input("Ingrese la posicion del dato que desea retornar :"))
                obj.retornar(valor)
                input("Presione una tecla para continuar...")  
                
            if opc1 == '9':
                os.system("cls") 
                print('COPIAR ELEMENTOS DE TUPLA EN UNA LISTA')
                tupla=("josue","luis","erick",10,8,9)
                print("TUPLA :")
                print(tupla)
                obj=Listas()
                print("LISTA : ")
                print(obj.tuplalista(tupla))
                input("Presione una tecla para continuar...")  

                
            if opc1 == '10':
                os.system("cls") 
                print('DAR VUELTO')
                dic = {}
                y = True
                while y:
                    clave = input("Ingrese el nombre del cliente : ")
                    valor = input("Ingrese el cupo para dicho cliente : ")
                    dic[clave]=valor
                    y = input("Desea agregar otro producto? (ingrese y para continuar) ")
                    if y != "y":
                         y = False
                    else:
                        continue
                    list =[]
                    list.append(dic)
                os.system("cls") 
                print('DAR VUELTO')
                obj = Listas()
                obj.vueltoLista(list)
                
                input("Presione una tecla para continuar...")    

    elif opc=="4":
        opc1 = ''
        while opc1 != '10':
            os.system("cls")
            menu1 = Menu('//--MENU OPERACIONES DE CADENAS--//', ['1) Recorrer y presentar los datos de una cadena', '2) Buscar un carácter en una cadena', '3) Retornar una lista con las posiciones dado un carácter de la cadena', '4) Retornar una lista con todas las palabras de una cadena', '5) Retornar una cadena a partir de una lista', '6) Insertar un dato en una cadena dada lo Posición', '7) Eliminar todas las ocurrencias en una cadena', '8) Retornar cualquier valor de una cadena eliminándolo ','9) Concatenar cadenas', '10) Salir'])
            opc1 = menu1.menu()
            if opc1 == '1':
                os.system("cls")
                print('Recorrer y presentar los datos de una cadena')
                cadena=input("Ingresar cadena:\n-> ").lower()
                llamar=Cadena(cadena)
                print("Cadena recorrida: ")
                llamar.recorrerCadena()
                input("Presione una tecla para continuar...")

            if opc1 == '2':
                os.system("cls")
                print('Buscar un carácter en una cadena')
                cadena=input("Ingresar cadena:\n-> ").lower()
                llamar=Cadena(cadena)
                buscado=input("Ingrese caracter a buscar dentro de la cadena:\n-> ").lower()
                while buscado not in cadena:
                    os.system("cls")
                    print("¡Caracter no hallado en cadena!")
                    buscado=input("Ingrese caracter a buscar dentro de la cadena:\n-> ").lower()           
                llamar.buscarCaracter(buscado)
                input("Presione una tecla para continuar...")

            if opc1 == '3':
                os.system("cls")
                print('Retornar una lista con las posiciones dado un carácter de la cadena')
                cadena=input("Ingresar cadena:\n-> ").lower()
                llamar=Cadena(cadena)
                caracter=input("Ingrese caracter a buscaar dentro de la cadena:\n-> ").lower()
                while caracter not in cadena:
                    os.system("cls")
                    print("¡Caracter no hallado en cadena!")
                    caracter=input("Ingrese caracter a buscar dentro de la cadena:\n-> ").lower()  
                print("Lista de las posiciones del caracter: '{}'".format(caracter))
                print("-> ",llamar.listaPosiciones(caracter))
                input("Presione una tecla para continuar...")

            if opc1 == '4':
                os.system("cls")
                print('Retornar una lista con todas las palabras de una cadena')
                cadena=input("Ingresar cadena\n-> ")
                llamar=Cadena(cadena)
                print("Lista con las palabras de la cadena:\n->",llamar.listaPalabras())
                input("Presione una tecla para continuar...")
            
            if opc1 == '5':
                os.system("cls")
                print('Retornar una cadena a partir de una lista')
                llamar=Cadena()
                lista=[]
                print("Cadena retornada a partir de la lista:\n->",llamar.cadenaLista())
                input("Presione una tecla para continuar...")

            if opc1 == '6':
                os.system("cls")
                print('Insertar un dato en una cadena dada lo Posición')
                cadena=input("Ingresar cadena:\n-> ").lower()
                llamar=Cadena(cadena)
                buscado=input("Ingrese el dato que desea insertar\n-> ").lower()
                while True:
                    try:
                        posicion = int(input("Ingrese la posición en la que desea ingresar el dato:\n-> "))
                    except ValueError:
                        os.system("cls")
                        print("¡Posición no válida!")
                        continue
                    if posicion>len(cadena):
                        os.system("cls")
                        print("¡Posición no válida!")
                        continue
                    else:
                        break
                llamar.insertarDato(buscado,posicion)
                input("Presione una tecla para continuar...")

            if opc1 == '7':
                os.system("cls")
                print('Eliminar todas las ocurrencias en una cadena')
                cadena=input("Ingresar cadena:\n-> ").lower()
                llamar=Cadena(cadena)
                buscado=input("Ingrese elemento a eliminar\n-> ").lower()
                while buscado not in cadena:
                    os.system("cls")
                    print("¡Caracter a eliminar no se encuentra en la cadena!")
                    buscado=input("Ingrese elemento a eliminar\n-> ")
                llamar.eliminarOcurrencias(buscado)
                input("Presione una tecla para continuar...")

            if opc1 == '8':
                os.system("cls")
                print('Retornar cualquier valor de una cadena eliminándolo ')
                cadena=input("Ingresar cadena:\n-> ").lower()
                llamar=Cadena(cadena)
                # posicion=int(input("Ingrese posicion:\n-> "))
                while True:
                    try:
                        posicion = int(input("Ingrese la posición del valor que desea retornar\n-> "))
                    except ValueError:
                        os.system("cls")
                        print("¡Posición incorrecta!")
                        continue
                    if posicion > len(cadena):
                        os.system("cls")
                        print("¡Posición fuera del rango!:\n-> ")
                        continue
                    else:
                        break
                print("El valor retornado de la posicion '{}'es:\n-> '{}'".format(posicion,llamar.retornaValor(posicion)))
                input("Presione una tecla para continuar...")
            
            if opc1 == '9':
                os.system("cls")
                print('Concatenar cadenas')
                llamar=Cadena()
                # dato=int(input("Ingrese el número de de cadenas que desea concatenar-> "))
                while True:
                    try:
                        dato = int(input("Ingrese el número de de cadenas que desea concatenar:\n-> "))
                    except ValueError:
                        os.system("cls")
                        print("¡Número no válido!")
                        continue
                    if dato <=1 or dato >10:
                        os.system("cls")
                        print("No puede concatenar menos de 1 y más de 10 cadenas:\n-> ")
                        continue
                    else:
                        break
                llamar.concatenarCadena(dato)
                input("Presione una tecla para continuar...")   
os.system("cls")