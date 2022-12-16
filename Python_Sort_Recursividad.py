from IPython.display import clear_output
from colorama import Fore
import random
import sys


def base():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t SELECTION SORT & RECURSION \t\t\t')
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Ordenamiento por Selección.')
    print('\t 2. Ingrese "2" para Recursividad.')
    print('\t 3. Ingrese "0" para Salir.')
    opcion_ingresada_sort_recursion = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_ingresada_sort_recursion.isdigit():
        clear_output(wait=True)
        tipo_seleccion(int(opcion_ingresada_sort_recursion))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        base()

def sort():
    print("                                                   ")
    print(Fore.BLUE + "\t\t\t     SELECTION SORT      \t\t\t")
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Ordenamiento Ascendente de Números.')
    print('\t 2. Ingrese "2" para Ordenamiento Descendente de Números.')
    print('\t 1. Ingrese "3" para Ordenamiento Ascendente de Palabras.')
    print('\t 2. Ingrese "4" para Ordenamiento Descendente de Palabras.')
    print('\t 3. Ingrese "9" para Volver.')
    print('\t 4. Ingrese "0" para Salir.')
    opcion_ingresada_sort = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_ingresada_sort.isdigit():
        clear_output(wait=True)
        seleccion_sort(int(opcion_ingresada_sort))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        sort()

def ascendente_numeros():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t ORDENAMIENTO POR SELECCIÓN ASCENDENTE DE NÚMEROS \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se ingresara el tamaño de la lista. Ejemplo 20.')
    print('\t B. El número ingresado debe ser un entero porsitivo.')
    print('\t C. La lista generada sera en el rango de -100 a 100.')
    print('\t D. Se observara la Lista de Desordenada de Elementos.')
    print('\t E. Se observara la Lista de Ordenada de Elementos.')
    tamano_arreglo = input("\t    " + "Ingrese el número de elementos de la lista: ")
    if tamano_arreglo.isdigit():
        print("                                   ")
        print("Lista de Desordenada de Elementos: ")
        conjunto_inicial = set()
        while len(conjunto_inicial) < int(tamano_arreglo):
            conjunto_inicial.add(random.randint(-100, 100))
        conjunto_inicial = list(conjunto_inicial)
        print(conjunto_inicial)
        for elemento in range(int(tamano_arreglo)):
            menor = elemento
            for i in range(elemento + 1, int(tamano_arreglo)):
                if conjunto_inicial[i] < conjunto_inicial[menor]:
                    menor = i
            (conjunto_inicial[elemento], conjunto_inicial[menor]) = (conjunto_inicial[menor], conjunto_inicial[elemento])
        print("                                                       ")
        print(Fore.GREEN + "Lista Ordenada de Elementos: " + Fore.BLACK)
        print(Fore.GREEN + str(conjunto_inicial) + Fore.BLACK)
        print(Fore.GREEN + "                                     ")
        print(Fore.GREEN + "Complejidad del Tiempo: " + Fore.BLACK)
        print(Fore.GREEN + "                        Mejor:    O(n^2)." + Fore.BLACK)
        print(Fore.GREEN + "                        Peor:     O(n^2)." + Fore.BLACK)
        print(Fore.GREEN + "                        Promedio: O(n^2)." + Fore.BLACK)
        print("                                                       ")
        print(Fore.GREEN + "Complejidad Espacial:   O(1)." + Fore.BLACK)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        ascendente_numeros()

def descendente_numeros():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t ORDENAMIENTO POR SELECCIÓN DESCENDENTE DE NÚMEROS \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se ingresara el tamaño de la lista. Ejemplo 20.')
    print('\t B. El número ingresado debe ser un entero porsitivo.')
    print('\t C. La lista generada sera en el rango de -100 a 100.')
    print('\t D. Se observara la Lista de Desordenada de Elementos.')
    print('\t E. Se observara la Lista de Ordenada de Elementos.')
    tamano_arreglo = input("\t    " + "Ingrese el número de elementos de la lista: ")
    if tamano_arreglo.isdigit():
        print("                                   ")
        print("Lista de Desordenada de Elementos: ")
        conjunto_inicial = set()
        while len(conjunto_inicial) < int(tamano_arreglo):
            conjunto_inicial.add(random.randint(-100, 100))
        conjunto_inicial = list(conjunto_inicial)
        print(conjunto_inicial)
        for elemento in range(int(tamano_arreglo)):
            mayor = elemento
            for i in range(elemento + 1, int(tamano_arreglo)):
                if conjunto_inicial[i] > conjunto_inicial[mayor]:
                    mayor = i
            (conjunto_inicial[elemento], conjunto_inicial[mayor]) = (conjunto_inicial[mayor], conjunto_inicial[elemento])
        print("                                                       ")
        print(Fore.GREEN + "Lista Ordenada de Elementos: " + Fore.BLACK)
        print(Fore.GREEN + str(conjunto_inicial) + Fore.BLACK)
        print(Fore.GREEN + "                                     ")
        print(Fore.GREEN + "Complejidad del Tiempo: " + Fore.BLACK)
        print(Fore.GREEN + "                        Mejor:    O(n^2)." + Fore.BLACK)
        print(Fore.GREEN + "                        Peor:     O(n^2)." + Fore.BLACK)
        print(Fore.GREEN + "                        Promedio: O(n^2)." + Fore.BLACK)
        print("                                                       ")
        print(Fore.GREEN + "Complejidad Espacial:   O(1)." + Fore.BLACK)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        descendente_numeros()
    
def ascendente_palabras():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t ORDENAMIENTO POR SELECCIÓN ASCENDENTE DE PALABRAS \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se observara la Lista de Desordenada de Elementos.')
    print('\t B. Se observara la Lista de Ordenada de Elementos.')
    print("                                   ")
    print("Lista de Desordenada de Elementos: ")
    conjunto_inicial = list(['Abecedario', 'Wilson', 'Dado', 'Queso', 'Bodega', 'Pato', 'Jarron', 'Pata', 'Mamá', 'Casa', 'Estanteria',                                      'Violin', 'Sardina', 'Kilogramo', 'Uva', 'Hijo', 'Papá', 'Lima', 'Rata', 'Nido', 'Tela', 'Gato', 'Xilofono',                                    'Orquesta', 'Zorro', 'Yeso', 'Fogata', 'Hija', 'Incomodo', 'Zorra'])
    print(conjunto_inicial)
    for elemento in range(30):
        menor = elemento
        for i in range(elemento + 1, 30):
            if conjunto_inicial[i] < conjunto_inicial[menor]:
                menor = i
        (conjunto_inicial[elemento], conjunto_inicial[menor]) = (conjunto_inicial[menor], conjunto_inicial[elemento])
    print("                                                       ")
    print(Fore.GREEN + "Lista Ordenada de Elementos: " + Fore.BLACK)
    print(Fore.GREEN + str(conjunto_inicial) + Fore.BLACK)
    print(Fore.GREEN + "                                     ")
    print(Fore.GREEN + "Complejidad del Tiempo: " + Fore.BLACK)
    print(Fore.GREEN + "                        Mejor:    O(n^2)." + Fore.BLACK)
    print(Fore.GREEN + "                        Peor:     O(n^2)." + Fore.BLACK)
    print(Fore.GREEN + "                        Promedio: O(n^2)." + Fore.BLACK)
    print("                                                       ")
    print(Fore.GREEN + "Complejidad Espacial:   O(1)." + Fore.BLACK)
    salir()

def descendente_palabras():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t ORDENAMIENTO POR SELECCIÓN DESCENDENTE DE PALABRAS \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se observara la Lista de Desordenada de Elementos.')
    print('\t B. Se observara la Lista de Ordenada de Elementos.')
    print("                                   ")
    print("Lista de Desordenada de Elementos: ")
    conjunto_inicial = list(['Abecedario', 'Wilson', 'Dado', 'Queso', 'Bodega', 'Pato', 'Jarron', 'Pata', 'Mamá', 'Casa', 'Estanteria',                                      'Violin', 'Sardina', 'Kilogramo', 'Uva', 'Hijo', 'Papá', 'Lima', 'Rata', 'Nido', 'Tela', 'Gato', 'Xilofono',                                    'Orquesta', 'Zorro', 'Yeso', 'Fogata', 'Hija', 'Incomodo', 'Zorra'])
    print(conjunto_inicial)
    for elemento in range(30):
        mayor = elemento
        for i in range(elemento + 1, 30):
            if conjunto_inicial[i] > conjunto_inicial[mayor]:
                mayor = i
        (conjunto_inicial[elemento], conjunto_inicial[mayor]) = (conjunto_inicial[mayor], conjunto_inicial[elemento])
    print("                                                       ")
    print(Fore.GREEN + "Lista Ordenada de Elementos: " + Fore.BLACK)
    print(Fore.GREEN + str(conjunto_inicial) + Fore.BLACK)
    print(Fore.GREEN + "                                     ")
    print(Fore.GREEN + "Complejidad del Tiempo: " + Fore.BLACK)
    print(Fore.GREEN + "                        Mejor:    O(n^2)." + Fore.BLACK)
    print(Fore.GREEN + "                        Peor:     O(n^2)." + Fore.BLACK)
    print(Fore.GREEN + "                        Promedio: O(n^2)." + Fore.BLACK)
    print("                                                       ")
    print(Fore.GREEN + "Complejidad Espacial:   O(1)." + Fore.BLACK)
    salir()

def recursion():
    print("                                                   ")
    print(Fore.BLUE + "\t\t\t     RECURSION     \t\t\t")
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Suma Recursiva.')
    print('\t 2. Ingrese "9" para Volver.')
    print('\t 3. Ingrese "0" para Salir.')
    opcion_ingresada_recursion = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_ingresada_recursion.isdigit():
        clear_output(wait=True)
        seleccion_recursion(int(opcion_ingresada_recursion))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        recursion()    

def suma():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t SUMA RECURSIVA \t\t\t' + Fore.BLACK)
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se ingresara el tamaño de la lista. Ejemplo 20.')
    print('\t B. El número ingresado debe ser un entero porsitivo.')
    print('\t C. La lista generada sera en el rango de -100 a 100.')
    print('\t D. Se observara los Elementos a Sumar.')
    print('\t E. Se observara la Suma de los Elementos.')
    tamano_arreglo = input("\t    " + "Ingrese el número de elementos de la lista: ")
    if tamano_arreglo.isdigit():
        print("                                   ")
        print("Lista de Números a Sumar: ")
        conjunto_inicial = set()
        while len(conjunto_inicial) < int(tamano_arreglo):
            conjunto_inicial.add(random.randint(-100, 100))
        conjunto_inicial = list(conjunto_inicial)
        print(conjunto_inicial)
        def sumatorio(lista):
            if len(lista) == 1:
                return lista[0]
            else:
                return lista[0] + sumatorio(lista[1:])
        print("                                                                                         ")
        print(Fore. GREEN + "La suma de los números es: " + str(sumatorio(conjunto_inicial)) + Fore.BLACK)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        suma()

def default_1():
    clear_output(wait=True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    base()

def default_2():
    clear_output(wait=True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    sort()
    
def default_3():
    clear_output(wait=True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    recursion()

def tipo_seleccion(numero_0):
    return opciones_sort_o_recursion.get(numero_0, default_1)()

def seleccion_sort(numero_1):
    return ordenamiento_sort.get(numero_1, default_2)()

def seleccion_recursion(numero_2):
    return suma_recursion.get(numero_2, default_3)()

def salir():
    # clear_output(wait=True)
    print("                                                     ")
    print(Fore.BLUE + '\t\t\t ADIÓS HASTA LA PRÓXIMA \t\t\t' + Fore.BLACK)
    sys.exit()

def volver():
    clear_output(wait=True)
    base()

opciones_sort_o_recursion = {
    1: sort,
    2: recursion,
    0: salir
    }

ordenamiento_sort = {
    1: ascendente_numeros,
    2: descendente_numeros,
    3: ascendente_palabras,
    4: descendente_palabras,
    9: volver,
    0: salir
    }

suma_recursion = {
    1: suma,
    9: volver,
    0: salir
    }

base()