#codigo para utilizar utf-8
import sys
import math
import random
sys.stdin.encoding
'UTF-8' 
from pip._vendor.appdirs import unicode 
from builtins import str


 #variables del correo y la contraseña del login
 #es obligar
correo = "actividad@gmail.com"
expediente = 21732599

def ejercicioH(arr): 
    #recorrer desde 1 hasta el tamano del array 
    for i in range(1, len(arr)): 
        key = arr[i] 
        #mover los elementos del array que son mas grandes
        #que key a una posicion mas arriba
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
        print(arr)
    menu(expediente)

def ejercicioGiterative(num):#O(n)
    #se recorre desde el valor de 1 a num+1 para que multiplique tambien
    #el valor del numero
    for i in range(1,num+1):
        if(i== 1 or i==0): 
            #si es 1 o 0 el factorial es 1
            factorial = 1
        else:
            #se multiplica por el valor de i
            factorial = factorial*i
    print('El factorial de ' + str(num) + ' es ' + str(factorial) ) 
    menu(expediente)
    
def ejercicioGrecursive(n):
    if n == 0:
        return 1
    else:
        return n *ejercicioGrecursive(n-1) #recursividad
    menu(expediente)

def karatsuba(x, y):
    if x < 10 and y < 10: return x * y
    n = max(len(str(x)), len(str(y)))
    #print("Num. digitos en X =",len(str(x))," ; en  Y =", len(str(y)))
    m = int(math.ceil(int(n) / 2)) #nos quedamos el mayor 
    #print("n es", n, "m es ",m)

    a = int(math.floor(x / 10 ** m))
    b = int(x % (10 ** m))
    c = int(math.floor(y / 10 ** m))
    d = int(y % (10 ** m))
    #print(" a =",a,"b=",b,"c =",c,"d=",d)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_mas_bc = karatsuba(a + b, c + d)-ac-bd
    return int(ac * (10 ** (m*2)) + ad_mas_bc * (10 ** m) + bd) 
    
def ejercicioGKaratsuba(num):
    for i in range(1,num+1):
        if(i== 1): 
            factorial = i
        else:
            factorial = karatsuba(factorial,i) #algoritmo de karatsuba
    print('El factorial de ' + str(num) + ' es ' + str(factorial) )
    menu(expediente) 
    
                
def ejercicioF(arr): #n^3
    n = len(arr)
    
    #bucle en las filas de la matriz
    for i in range(n):
        #bucle en las columnas de la matriz
        for j in range(len(arr[i])):
            #comparar
            for k in range (len(arr[i])-j-1):
                if(arr[i][k] > arr[i][k+1]):
                    #cambiar de lugar
                    t = arr[i][k]
                    arr[i][k] = arr[i][k+1]
                    arr[i][k+1] = t
    #imprimir la matriz 
    print(arr)
    menu(expediente)


def ejercicioE(n):
    filas1=columnas1=filas2=columnas2= n
    
    #generar matrices de manera randomica
    i, j, matriz3, matriz1, matriz2 = generarMatrices(filas1, columnas1, filas2, columnas2) 

    #dos bucles que recorran las posiciones de las matrices
    for i in range(n):
        for j in range(n):
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j] #n^2
    print ('Su matriz resultante es')
    print (matriz3)
    menu(expediente)
    
            
def ejercicioD(): #--> O(n^2)
    num_s=str(expediente)
    num_list=list(num_s)
    cont = 7
    cap = True #variable que mide si es capicua
    alReves = [0,0,0,0,0,0,0,0] #array para guardar el expediente al reves
    #array para rellenar el array con el expediente dado la vuelta
    for i in range(8):
        alReves[cont] = num_list[i]   #n
        cont= cont -1
    
    for i in range(8):
        if(num_list[i] == alReves[i]): #n
            cap = True
        else:
            cap = False
    if cap == True:
       print("El expediente es capicua")
    else:
        print("El expediente no es capicua")
    menu(expediente)
            
#genera matrices de manera random
def generarMatrices(filas1, columnas1, filas2, columnas2): #-->n*n*n x n^2 x n^2 = O(N^7)    
    matriz1 = []
    for i in range(filas1): #n
        matriz1.append([0] * columnas1)
    
    matriz2 = []
    for i in range(filas2): #n
        matriz2.append([0] * columnas2)
    
    for i in range(filas1):
        for j in range(columnas1): #n^2
            matriz1[i][j] = random.randint(0,9)
    print(matriz1)
    
    for i in range(filas2):
        for j in range(columnas2): #n^2
            matriz2[i][j] = random.randint(0,9)
    print(matriz2)
    
    matriz3 = []
    for i in range(filas1):  #n
        matriz3.append([0] * columnas1)
    
    return i, j, matriz3, matriz1, matriz2

def ejercicioC():
    #multiplicar matrices
    filas1=columnas1=filas2=columnas2= 3
    
    print("Matrices generadas de manera randómica que se van a multiplicar: ")
    i, j, matriz3, matriz1, matriz2 = generarMatrices(filas1, columnas1, filas2, columnas2)  #n^7
    
    #necesito 3 for por que la multiplicacion de matrices es
    #fila por columna y se suma lo que de para el resultado, y asi con
    #todas las filas y columnas hasta que de la matriz resultante
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(filas2):
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]  #n^3 
    print ('Su matriz resultante es: ')
    print (matriz3)
    menu(expediente)
    
def ejercicioB():
    primo = 1 #variable que guarda si es primo o no
    if expediente < 1: #0 o 1 no son primos
        primo = 0
    elif expediente == 2: #2 es primo
        primo = 1
    else:
        #bucle desde 2 hasta expediente que comprueba si expediente se puede dividir entre algun numero que no sea él mismo 
        for i in range(2, expediente):  #bucle que aumenta de manera homogénea de 1 en 1, por lo tanto O(n)
            if expediente % i == 0:
                primo = 0
        primo = 1
    
    if primo == 1:
        print(unicode("El número de expediente es primo"))
    else:
        print(unicode("El número de expediente es primo"))
    print(unicode("Complejidad de función primo es O(n)"))
    menu(expediente)

#A1 codificado COMPLEJIDAD n^3
def A1(n):
    sum = 0
    for i in range(0,n,1): #n
        for j in range(0,n*n,1): #n^2
          sum= sum+1 
          print(sum) 

#A2 codificado COMPLEJIDAD n^5
def A2(n):
    sum = 0
    for i in range(0,n,1): #n
        for j in range(0,i*i,1): #n^2
            for k in range(0,j,1): #k aumenta hasta j que es n^2, por tanto es n^2
                sum= sum+1
                print(sum)  

#A3 codificado COMPLEJIDAD logn        
def A3(n):
    i = 1
    x = 0
    while (i<= n): 
        x=x+1
        i+=2    #i aumenta de dos en dos O(logn)
        print(x)
        print(i)
        
        
    
#funcion para ejecutar el ejercicio A y elegir
# ejecutar una de las opciones A1, A2, A3
def ejercicioA():
    print(unicode( "A1 = O(n³)\nA2 = O(n^5)\nA3 = O(log n)\nS = Volver al menú"))
    cod = input("Introduca el codigo que quiera ejecutar:")
    if cod == "A1" or cod == "A2" or cod == "A3":
        n = int(input("Introduzca la n: (Por ejemplo 3)"))
        if cod == "A1":
            print("Ejecutando A1 con n = " + str(n) + " ... \n")
            A1(n)
            ejercicioA()
        elif cod == "A2":
            print("Ejecutando A2 con n = " + str(n) + " ... \n")
            A2(n)
            ejercicioA()
        elif cod == "A3":
            print("Ejecutando A3 con n = " + str(n) + " ... \n")
            A3(n)
            ejercicioA()        
    else:
        menu(expediente)
        
        
def login():
   #se pide el correo
    email = input("Ingrese su email de la uem:")
    correo = email
    contrasena = (input(unicode("Ingrese la contraseña (número de expediente):")))
    #la contrasena tiene que ser 21732599 obligatoriamente
    icontrasena = int(contrasena)
    if(icontrasena != expediente):
        print("No autorizado\nSALIENDO DEL PROGRAMA...")
    else: menu(icontrasena)
           
        
#Funcion para imprimir el menu y elegir opcion
def menu(expediente):
    print("\n******************** UNIVERSIDAD EUROPEA DE MADRID *************************\n"
         + unicode( "Escuela de Ingeniería Arquitectura y Diseño\n\n"))

    print("*****************MENU**********************\n"
          "A: Ejercicio A\n"
          "B: Ejercicio B\n"
          "C: Ejercicio C\n"
          "D: Ejercicio D\n"
          "E: Ejercicio E\n"
          "F: Ejercicio F\n"
          "G: Ejercicio G\n"
          "H: Ejercicio H\n"
          "S: Salir\n")
    opcion = input(unicode("Elija una opción:"))
    
    if opcion == "A":
        ejercicioA()
    elif opcion == "B":
        ejercicioB()
    elif opcion == "C":
        ejercicioC()
    elif opcion == "D":
        ejercicioD()
    elif opcion == "E":
        n = int(input("Introduzca el rango de las matrices n: "))
        ejercicioE(n)
    elif opcion == "F":
        arr = [[64, 34, 25, 12, 22],[1,2,5,4,6]]
        print ("El array ordenado es:")
        ejercicioF(arr)
    elif opcion == "G":
        num = 8 #numero para calcular su factorial
        print("1. Forma recursiva\n2. Forma iterativa\n3. Karatsuba")
        n = int(input("Elija la opcion para calcular el factorial: "))
        if n == 1:
            print(ejercicioGrecursive(num))
        elif n ==2:
            ejercicioGiterative(num)
        else:
            ejercicioGKaratsuba(num)
    elif opcion == "H":
        arr = [int(x) for x in str(expediente)]  
        print("El array original es " + str(arr))

        print("La secuencia de ordenado del insertion sort es: ")
        ejercicioH(arr) 
        #imprimir el array final 
        print("El array colocado al final es " + str(arr))
  
    else:
        print("SALIENDO DEL PROGRAMA...")
        exit





#ejecucion
login()






