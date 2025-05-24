## 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
from functools import reduce


cadena = "Estudiando Python"

def contar_frecuencias(cadena):
    # Creamos un diccionario vacío para almacenar las frecuencias
    frecuencias = {}
    
    # Recorreremos cada carácter en la cadena
    for letra in cadena:
        # Ignoraramos los espacios
        if letra != " ":
            # Incrementamos el contador en el diccionario
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
                
    return frecuencias
resultado = contar_frecuencias(cadena)
print(resultado)

## 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# Lista de números inicial
numeros_iniciales = [2, 4, 6, 8,10]

# Usamos fucnión map par obtener el valor doble.

numeros_dobles = list(map(lambda x: x * 2, numeros_iniciales))

print(numeros_dobles)

## 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

lista = ["manzana", "mandarina", "platano", "datil", "manices"]
objetivo = "man"

def filtrar_palabras(lista, objetivo):
    # Filtrar las palabras que contienen la palabra objetivo
    Palabra_objetivo = list(filter(lambda palabra: objetivo in palabra, lista))
    return Palabra_objetivo
Result = filtrar_palabras (lista, objetivo)
print(Result)

## 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

Lista_1 = [10, 20, 30 , 40]
Lista_2 = [5, 15, 25, 35]

def calcular_diferencia(lista_1, lista_2):
    # Usamos map() para calcular la diferencia elemento por elemento
    diferencia = list(map(lambda x, y: x - y, lista_1, lista_2))
    return diferencia
dif = calcular_diferencia(Lista_1, Lista_2)

print(dif)

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

lista_numeros = [3, 7, 8, 5, 4, 9, 6]

def evaluar_media(lista_numeros, nota_aprobado=5):
    # Calcular la media de los números en la lista
    if len(lista_numeros) == 0:
        raise ValueError("La lista no puede estar vacía.")
    
    media = sum(lista_numeros) / len(lista_numeros)
    
    # Determinar el estado: "aprobado" o "suspenso"
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    
    # Devolver la tupla con la media y el estado
    return (media, estado)
R_media = evaluar_media(lista_numeros)
print(R_media)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

numero = 8

def factorial(n):
    # el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)
R_factorial = factorial(numero)
print(f"el resultado factorial de {numero} es {R_factorial}")

 # 7. Genera una función que convierta una lista de tuplas a una lista de strings. 
 # Usa la función map()

Lista_tuplas = [(1,3), (2,5,6), (5, 6, 3, 1)]

def tuplas_a_strings(lista_tuplas):
    # Usamos map() para convertir cada tupla a un string
    lista_strings = list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))
    return lista_strings
R_string = tuplas_a_strings(Lista_tuplas)
print(R_string)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        # Pedir al usuario dos números
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        # Intentar realizar la división
        resultado = num1 / num2

    except ValueError:
        # Manejar el caso en que se ingrese un valor no numérico
        print("Error: Por favor, introduce valores numéricos.")
    except ZeroDivisionError:
        # Manejar la división por cero
        print("Error: No es posible dividir entre cero.")
    else:
        # Si no hay errores, mostrar el resultado de la división
        print(f"La división fue exitosa. El resultado es: {resultado}")
    finally:
        # Mensaje final opcional
        print("Operación finalizada.")

# Llamar a la función
dividir_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

Mascotas= ["Perro", "Gato", "Hamster", "Tigre", "Mapache", "Conejo", "Oso", "Elefante"]

def filtro_mascotas(lista_mascotas):
    # Lista de mascotas prohibidas en España
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Filtrar las mascotas prohibidas
    mascotas_permitidas = list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))
    
    return mascotas_permitidas
R_mascotas = filtro_mascotas(Mascotas)
print(R_mascotas)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

# Definir una excepción personalizada
class ListaVaciaError(Exception):
    def __init__(self, mensaje="La lista está vacía. No se puede calcular el promedio."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Función para calcular el promedio
def calcular_promedio(lista_numeros):
    try:
        if not lista_numeros:  # Verificar si la lista está vacía
            raise ListaVaciaError()
        
        # Calcular el promedio
        promedio = sum(lista_numeros) / len(lista_numeros)
        return promedio

    except ListaVaciaError as e:
        print(f"Error: {e}")

# Ejemplo de uso
try:
    numeros = [2,5,7]  # Cambiar a una lista con números para probar otro caso
    resultado = calcular_promedio(numeros)
    if resultado is not None:
        print(f"El promedio es: {resultado}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

def pedir_edad():
    try:
        # Solicitar la edad al usuario
        edad = int(input("Introduce tu edad: "))

        # Verificar si la edad está dentro del rango válido
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")

        print(f"Gracias. Tu edad es {edad} años.")

    except ValueError as e:
        # Manejar errores de valor no válido o fuera del rango
        print(f"Error: {e}. Por favor, introduce un valor numérico válido.")
    except Exception as e:
        # Capturar cualquier otra excepción inesperada
        print(f"Ha ocurrido un error inesperado: {e}")
    finally:
        # Mensaje final opcional
        print("Programa finalizado.")

# Llamar a la función
pedir_edad()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. 
# Usa la función map()

frase= "Aprendiendo a usar Python"

def longitud_palabras(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Usar map() para obtener la longitud de cada palabra
    longitud = list(map(len, palabras))
    
    return longitud

R_longitud= longitud_palabras(frase)

print(R_longitud)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

caracteres= "AbDgrpSWQCXZñpo"

def letras_mayusculas_minusculas(conjunto_caracteres):
    # Eliminar duplicados y quedarnos solo con las letras
    letras_unicas = set(filter(str.isalpha, conjunto_caracteres))
    
    # Usar map() para generar tuplas (mayúscula, minúscula)
    Carac = list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))
    
    return Carac

R_caracteres= letras_mayusculas_minusculas (caracteres)

print(R_caracteres)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()

Palabras= ["manzana", "pera", "melocoton", "melon", "mandarina", "mango", "limon"]
letra_especifica = "man"

def palabras_con_letra(lista_palabras, letra):
    # Usar filter() para encontrar palabras que comiencen con la letra específica
    R_especifica = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
    return R_especifica

R_palabras = palabras_con_letra(Palabras, letra_especifica)

print(R_palabras)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# Lista de ejemplo
L_lambda = [1, 2, 3, 4, 5]

# Aplicar la función lambda
R_Lambda = list(map(lambda x: x + 3, L_lambda))

print(R_Lambda)  

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

texto = "Prueba para realizar filtro de las palabras mas largas"
n = 5

def palabras_largas(texto,n):

 # Dividir la cadena en palabras

    P_largas = texto.split()

 # Filtrar las palabras más largas que n

    R_largas = list(filter(lambda texto: len(texto) > n, P_largas))

    return R_largas

print(palabras_largas(texto,n))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

digitos = [8, 9, 3]

def lista_hacia_numeros(digitos):
    
    # Convierte una lista de dígitos en el número correspondiente.
    
    return reduce(lambda x, y: x * 10 + y, digitos)

print(lista_hacia_numeros(digitos))

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

# Crear una lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Juan", "edad": 20, "notas": 85},
    {"nombre": "Ana", "edad": 18, "notas": 92},
    {"nombre": "Veronica", "edad": 19, "notas": 88},
    {"nombre": "Sara", "edad": 28, "notas": 95},
    {"nombre": "Luis", "edad": 25, "notas": 78}
]

# Usamos filter para extraer estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda estudiante: estudiante["notas"] >= 90, estudiantes))

# Mostrar los estudiantes destacados
print(estudiantes_destacados)

# 19. Crea una función lambda que filtre los números impares de una lista dada.

# Lista de ejemplo
List_impar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos filter con una función lambda para filtrar los números impares
numeros_impares = list(filter(lambda x: x % 2 != 0, List_impar))

print(numeros_impares)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

# Lista con valores mixtos (integer y string)
valores_mixtos = [1, "hola", 3, "ejercicio", 5, "python", 7]

# Usamos filter para extraer solo los valores de tipo int
valores_int = list(filter(lambda x: isinstance(x, int), valores_mixtos))

print(valores_int) 

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

Num_ejemplo = 8

# Creamos una función lambda que calcule el cubo
f_cubo = lambda x: x ** 3

R_cubo = f_cubo(Num_ejemplo)

print(f"El cubo de {Num_ejemplo} es {R_cubo}") 

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.
# Usa la función reduce() .

List_prod = [23, 12, 34, 51]

def Product_total (List_prod):

    #Utilizamos función reduce junto a lambda para hacer producto
    return reduce(lambda x, y: x * y, List_prod)

R_product = Product_total(List_prod)

print(f"El producto total de {List_prod} es {R_product}")

# 23. Concatena una lista de palabras.Usa la función reduce().

L_concatena = ["Haciendo", " ", "Ejercicio", " ", "Python" ]

def concatenar_palabras(L_concatena):

    # Usamos función reduce junto a lamba para concatenar valores de la lista
    
    return reduce(lambda x, y: x + y, L_concatena)

R_concatena = concatenar_palabras(L_concatena)

print(R_concatena)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

L_diferencia = [88, 72, 41, 23, 8]

def diferencia_total(L_diferencia):

    # Usamos reduce junto a lambda para calcular la diferencia en los valores

    return reduce(lambda x, y: x - y, L_diferencia)

R_diferencia = diferencia_total(L_diferencia)

print(f"La diferencia total de {L_diferencia} es {R_diferencia}")

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

f_text = "Haciendo ejercicio Python"

def contar_caract (f_text):

    # Usamos función eln para contar los caracteres

    return len (f_text)

N_caract = contar_caract(f_text)

print(f"El número de caracteres en la cadena {f_text} es {N_caract}")

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

modulo = lambda x, y: x % y

R_modulo = modulo(28,4)

print(R_modulo)

# 27. Crea una función que calcule el promedio de una lista de números.

L_promedios = [5, 8, 15, 23, 75, 80]

def cal_promedios(L_promedios):
    # calculamos promedio, y tenemos en cuenta listas vacías, para que nos devuelva 0
    if not L_promedios:
        return 0
    return sum(L_promedios) / len(L_promedios)

Promedio = cal_promedios (L_promedios)

print(Promedio)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

L_duplicados = [8, 5, 2, 4, 5, 6, 2]

def Prim_duplicado(L_duplicados):
 # Buscar y devolver primer elemento duplicado
 # si no encontramos duplicados, retornamos None
    vistos = set()
    for elemento in L_duplicados:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None
dupli = Prim_duplicado (L_duplicados)

print(dupli)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

Datos = 154289235478

def Enmasc_vble(Datos):
    # Cualquier variable que se pueda convertir a cadena.
    # Retornamos valor String.

    texto = str(Datos)
    if len(texto)<= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

Enmascara = Enmasc_vble(Datos)

print(Enmascara)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.


def anagrama (Palabra1, Palabra2):
    # ¿Son anagramas?, es decir, mismas letras pero con diferente orden.
    # Retornamos valor Bool, True si es anagrama y False si no lo es.
    # Quiamos espacios y ponemos en minúscula, apfa dejar ambas palabras iguales.
    P1 = Palabra1.replace(" ", "").lower()
    P2 = Palabra2.replace(" ", "").lower()
    return sorted(P1) == sorted(P2)

print(anagrama("seto", "esto"))
print(anagrama("lacteo","coleta"))
print(anagrama("leon", "elefante"))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.


def buscar_nombre():
    # Solicitamos al usuario una lista de nombres para buscar
    # si lo encontrmos, imprime un mensaje, si no, una excepción ValueError.
    try:
        # solicitamos lista
        inicio = input("Ingrese una lista de nombres separados por comas: ")
        L_nombres = [nombre.strip() for nombre in inicio.split(",") if nombre.strip()]

        # solicitamos nombre a buscar
        N_buscar = input("Ingrese el nombre a buscar: ").strip()
        if N_buscar in L_nombres:
            print (f"El nombre '{N_buscar}' está en la lista.")
        else:
            raise ValueError (f"El nombre '{N_buscar}' no está en la lista.")
    except ValueError as e:
        print(e)    

print(buscar_nombre())

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

trabajadores = [ 
    {"nombre": "Agustin Hernández", "puesto": "Auxiliar"},
    {"nombre": "Juan Delgado", "puesto": "Gerente"},
    {"nombre": "Sebastian Pérez", "puesto": "contable"}
]
    
def puesto_trabajo (N_completo, L_trabajadores):
    # Buscamos nombre de una lista, si no lo encontramos, indicamos que no trabaja aquí.

    for empleado in L_trabajadores:
        if empleado.get('nombre', '').lower() == N_completo.lower():
            return f"Puesto: {empleado.get('puesto', 'Sin especificar')}"
    return f"La persona '{N_completo}' no trabaja aquí"

print(puesto_trabajo("Juan Delgado", trabajadores))    
print(puesto_trabajo("Andrés Lopez", trabajadores))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

L_A = [1, 8, 9]
L_B = [5, 4, 2]

# Hacemos función Lambda para sumar los elementos de las dos listas dadas.

sumar_listas = lambda L_A, L_B: list(map(lambda x, y: x + y, L_A, L_B))

R_suma_lista = sumar_listas (L_A, L_B)

print(R_suma_lista)

# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para
# manipular la estructura del árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        #Aumenta la longitud del tronco en una unidad.
        self.tronco += 1

    def nueva_rama(self):
        # Agrega una nueva rama de longitud 1.
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumenta en una unidad la longitud de todas las ramas.
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        
        # Elimina la rama en la posición especificada (comenzando en 0).
        # Si la posición no existe, no hace nada.
        
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]

    def info_arbol(self):
        # Devuelve información sobre el árbol.
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy()
        }


# Caso de uso
if __name__ == "__main__":
    arbol = Arbol()                # 1. Crear un árbol
    arbol.crecer_tronco()          # 2. Hacer crecer el tronco una unidad
    arbol.nueva_rama()             # 3. Añadir una nueva rama
    arbol.crecer_ramas()           # 4. Hacer crecer todas las ramas una unidad
    arbol.nueva_rama()             # 5. Añadir una nueva rama
    arbol.nueva_rama()             # 5. Añadir otra nueva rama
    arbol.quitar_rama(2)           # 6. Retirar la rama en la posición 2
    info = arbol.info_arbol()      # 7. Obtener información

    print(info)
   

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad} unidades.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad} unidades. Saldo actual: {self.saldo}")

    def agregar_dinero(self, cantidad):
        if cantidad < 0:
            raise ValueError("No se puede agregar una cantidad negativa de dinero.")
        self.saldo += cantidad
        print(f"{self.nombre} ha recibido {cantidad} unidades. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(
                f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad} unidades.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} unidades a {self.nombre}.")
        print(f"Saldo de {otro_usuario.nombre}: {otro_usuario.saldo}")
        print(f"Saldo de {self.nombre}: {self.saldo}")

# Caso de uso:
if __name__ == "__main__":
    # 1. Crear dos usuarios: "Alicia" y "Bob"
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    # 2. Agregar 20 unidades de saldo a "Bob"
    bob.agregar_dinero(40)

    # 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"
    alicia.transferir_dinero(bob, 80)

    # 4. Retirar 50 unidades de saldo a "Alicia"
    alicia.retirar_dinero(50)


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto.

def contar_palabras(texto):
    
    # Contar el número de veces que aparece cada palabra en el texto y
    # devuelver un diccionario: {palabra: cantidad}
    
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra_limpia = palabra.strip(",.?!¡¿:;\"'").lower()
        conteo[palabra_limpia] = conteo.get(palabra_limpia, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    
    # Reemplazar todas las apariciones de palabra_original por palabra_nueva en el texto.
    
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_eliminar):
    
    # Eliminar todas las apariciones de palabra_eliminar del texto.

    palabras = texto.split()
    resultado = [palabra for palabra in palabras if palabra != palabra_eliminar]
    return " ".join(resultado)

def procesar_texto(texto, opcion, *args):
    
    # Procesa el texto de acuerdo a la opción especificada:
    # "contar": devuelve diccionario de conteo de palabras.
    # "reemplazar": necesita palabra_original y palabra_nueva.
    # "eliminar": necesita palabra_eliminar.

    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar', debes proporcionar palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar', debes proporcionar palabra_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

# Caso de uso
if __name__ == "__main__":
    texto = "Hola mundo, hola universo. Hola a todos en el mundo."
    print("Contar palabras:")
    print(procesar_texto(texto, "contar"))
    print("\nReemplazar 'Hola' por 'Adiós':")
    print(procesar_texto(texto, "reemplazar", "Hola", "Adiós"))
    print("\nEliminar 'mundo':")
    print(procesar_texto(texto, "eliminar", "mundo"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora):
    
    # Tenemos en cuenta los siguientes horarios:
    # Día: 6 a 12 horas
    # Tarde: 13 a 19 horas
    # Noche: 20 a 23 y 0 a 5 horas 

    if not (0 <= hora <= 23):
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora <= 12:
        return "Es de día."
    elif 13 <= hora <= 19:
        return "Es tarde."
    else:
        return "Es de noche."

if __name__ == "__main__":
    try:
        h = int(input("Introduce la hora (0-23): "))
        print(momento_del_dia(h))
    except ValueError as e:
        print("Error:", e)

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion_texto(calificacion):
   
   # Definimos para las reglas de calificación dadas:

    if not (0 <= calificacion <= 100):
        return "Calificación fuera de rango (0-100)."
    if calificacion < 70:
        return "insuficiente"
    elif calificacion < 80:
        return "bien"
    elif calificacion < 90:
        return "muy bien"
    else:
        return "excelente"

if __name__ == "__main__":
    try:
        nota = int(input("Introduce la calificación numérica del alumno (0-100): "))
        print(f"Calificación en texto: {calificacion_texto(nota)}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    
    #Calcula el área de una figura geométrica.
    # Tenemos en cuenta los datos necesarios para calcular el área:
    # rectangulo: (base, altura)
    # circulo: (radio,)
    # triangulo: (base, altura)
   
    figura = figura.lower()
    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Para un rectángulo se requieren 2 datos: base y altura.")
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("Para un círculo se requiere 1 dato: radio.")
        radio, = datos
        from math import pi
        return pi * radio ** 2
    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("Para un triángulo se requieren 2 datos: base y altura.")
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no soportada. Usa 'rectangulo', 'circulo' o 'triangulo'.")

# Ejemplo de uso
if __name__ == "__main__":
    print("Área rectángulo:", calcular_area("rectangulo", (4, 5)))    
    print("Área círculo:", calcular_area("circulo", (3,)))            
    print("Área triángulo:", calcular_area("triangulo", (6, 2)))      


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento.

    # A realizar:
    # Solicitar ingreso de precio original del artículo
    # Preguntar usuario por cupón descuento
    # Si la respuesta anterior es "si", solicitar ingreso del valor del cupón.
    # Aplicar descuento al precio original del artículo, siempre que el cupón sea válido.
    # Mostrar precio final de la compra.

def calcular_precio_final():
    try:
        precio_original = float(input("Ingrese el precio original del artículo (€): "))
        if precio_original < 0:
            print("El precio no puede ser negativo.")
            return

        tiene_cupon = input("¿Tiene un cupón de descuento? (sí/no): ").strip().lower()

        descuento = 0
        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Ingrese el valor del cupón de descuento (€): "))
            if valor_cupon > 0:
                descuento = valor_cupon
            else:
                print("El valor del cupón no es válido. No se aplicará descuento.")
        elif tiene_cupon == "no":
            pass  # No se aplica descuento
        else:
            print("Respuesta no reconocida. No se aplicará descuento.")

        precio_final = precio_original - descuento
        if precio_final < 0:
            precio_final = 0  # El precio final no puede ser negativo

        print(f"El precio final de la compra es: {precio_final:.2f} €")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese valores numéricos donde corresponda.")

if __name__ == "__main__":
    calcular_precio_final()