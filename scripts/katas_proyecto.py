### 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


frase1='Federer'
frase2='Buenas tardes'


# La manera más básica:


def frec_letras(cadena):
    """Cuenta cuántas veces aparece un carácter (sin contar espacios) en una cadena de caracteres.

    Args:
        cadena (str): Cadena de caracteres en la que se contará la frecuencia de cada caracter.

    Returns:
        dict: Devuelve un diccionario con cada uno de los caracteres y la frecuencia con la que aparecen en la cadena.
    """
    cadena=cadena.replace(' ','')
    lista=list(cadena.upper())

    diccio={}
    for pos in range(len(lista)):
        diccio.update({lista[pos]:lista.count(lista[pos])})
    return diccio


# La anterior un poco mejorada:


def frec_letras(cadena):
    """Cuenta cuántas veces aparece un carácter (sin contar espacios) en una cadena de caracteres.

    Args:
        cadena (str): Cadena de caracteres en la que se contará la frecuencia de cada caracter.

    Returns:
        dict: Devuelve un diccionario con cada uno de los caracteres y la frecuencia con la que aparecen en la cadena.
    """
    cadena=cadena.replace(' ','')

    diccio={}
    for letra in cadena.upper():
        diccio[letra] = diccio.get(letra, 0) + 1
    return diccio


print(frec_letras(frase1))
print(frec_letras(frase2))


### 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().


lista1=[1,2,3,4,5]
lista2=[1,-1,2,-2,3,-3]


def doble(numero):
    """Duplica el valor de un número.

    Args:
        numero (float or int): Número a duplicar.

    Returns:
        float or int: Valor duplicado.
    """
    return 2*numero


resultado1=list(map(doble,lista1))
resultado2=list(map(doble,lista2))

print(f"El doble de cada número de la cadena {lista1} es {resultado1}.\n Y de la cadena {lista2} es {resultado2}.")


### 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


palabra_objetivo='er'
verbos=['comer', 'hablar','saltar','freir','beber']


def encontrar_palabras(palabras, palabra_objetivo):
    """Filtra en una lista de palabras una palabra objetivo.

    Args:
        palabras (list[str]): Lista de cadenas donde se realiza la búsqueda.
        palabra_objetivo (str): Cadena de caracteres a buscar en la lista de cadenas.

    Returns:
        list[str]: Lista de palabras que contienen la 'palabra_objetivo'.
    """
    lista=[]
    for palabra in palabras:
        if palabra_objetivo in palabra:
            lista.append(palabra)
    return lista


encontrar_palabras(verbos,palabra_objetivo)


def enc_pal_list_comp(palabras, palabra_objetivo):
    """Filtra en una lista de palabras una palabra objetivo.

    Args:
        palabras (list[str]): Lista de cadenas donde se realiza la búsqueda.
        palabra_objetivo (str): Cadena de caracteres a buscar en la lista de cadenas.

    Returns:
        list[str]: Lista de palabras que contienen la 'palabra_objetivo'.
    """
    return [palabra for palabra in palabras if palabra_objetivo in palabra]


enc_pal_list_comp(verbos,palabra_objetivo)


### 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().


def diferencia(numero1,numero2):
    """Calcula de diferencia entre dos números.

    Args:
        numero1 (float or int): Un número al que se le restará otro.
        numero2 (float or int): Un número que será restado a otro.

    Returns:
        float or int: Devuelve un número que es la diferencia entre 'numero1' y 'numero2'.
    """
    return numero1-numero2


lista_numeros1=[1,2,3,4,6]
lista_numeros2=[-1,-2,5,4,1,2]

print(list(map(diferencia,lista_numeros1,lista_numeros2)))


# Comprobamos que aunque las longitudes de las listas sean distintas map calcula bien las diferencias, luego no será necesario comprobar que ambas listas tienen la misma longitud.


### 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.


notas = [2.5,3,5,8,9.5,10,5.5,6,6.5]


def media_aprobado(notas, nota_aprobado):
    """Calcula la media de una lista de notas y comprueba si nota media supera un umbral para devolver 'Aprobado' si supera el umbral y 'Suspenso' si no.

    Args:
        notas (list[float or int]): lista de notas a las que se les calcula la media.
        nota_aprobado (float or int): valor umbral apartir del cual se considera el estado de 'Aprobado'.

    Returns:
        tuple: Devuelve la nota media y el estado de 'Aprobado' o 'Suspenso'.
    """
    media=sum(notas)/len(notas)
    if media >= nota_aprobado:
        estado = 'Aprobado'
    else:
        estado = 'Suspendo'
    return (media,estado)


media, estado = media_aprobado(notas,6)
print(f"La nota media es {round(media,2)} y el estado es {estado}.")


### 6. Escribe una función que calcule el factorial de un número de manera recursiva.


def factorial(num):
    """Función que calcula el factorial de un número entero de manera recursiva.

    El factorial de un número se define como: n! = n * (n-1) * (n-2) * ... * 1  si n >= 1. Si n = 0 entonces n! = 1.  

    Args:
        num (int): Número entero no negativo al que se le aplica el factorial.

    Returns:
        int: Devuelve el factorial de 'num'.
    """
    if num<2:
        return 1
    else:
        return num * factorial(num-1)


factorial(3)


### 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().


lista_tuplas=[("H","o","l","a"),(3,"+",4),('Luis',' ','XIV')]


# La función 'join' une todos los elementos de una tupla en un string usando un elemento entre corchetes ("") como separador.
tupla1=lista_tuplas[0]
union_tuplas_to_str = lambda tupla: "".join(map(str,tupla))
union_tuplas_to_str(tupla1)
# Obtenemos la tupla unida en un string.


# Aplicamos map sobre la función 'union_tuplas_to_str' para aplicarla sobre cada tupla de la lista.
list(map(union_tuplas_to_str,lista_tuplas))


# Hacemos la función pedida:


def convert_tuple_to_str(lista_tuplas):
    """Convierte una lista de tuplas en una lista de strings. 
    
    Los strings son cada uno de los elementos de la tupla convertidos a str y unidos.

    Args:
        lista_tuplas (list[tuple]): Lista de tuplas que convertiremos en lista de strings.

    Returns:
        list[str]: Devuelve las tuplas convertidas en strings como elementos de una lista.
    """
    return list(map(lambda tupla: "".join(map(str,tupla)),lista_tuplas))


convert_tuple_to_str(lista_tuplas)


### 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.


# División con manejo de errores
try:
    numerador = float(input("Introduce el dividendo (número a dividir): ")) # Convierte en tipo flotante lo introducido por el usuario.
    denominador = float(input("Introduce el divisor (entre cuánto dividir): "))

    division = numerador/denominador
except ZeroDivisionError: # Este error se ejecuta si el usuario introduce en el denominador un cero.
    print("Error: No se puede dividir entre cero.")
except ValueError: # Este error se ejecuta si el usuario introduce caracteres distintos a números.
    print("Error: Debes ingresar un número válido.")
except Exception as e: # Cubre el resto de errores que puedan ocurrir y al nombrarlo como 'e' podemos imprimir el tipo de error.
    print(f"Error: Ha ocurrido un error tipo {e}.")
else:
    print(f"La división se ha realizado correctamente y es: {round(division,5)}")


### 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().


x = lambda elem: elem not in [1,2,3,4]
x(5) # Los elementos que no están en la lista devuelven el valor booleano 'True'.


# Utilizando 'filter' obtenemos todos los elementos de la lista que no están en [1,2,3,4].
filtro = filter(lambda elem: elem not in [1,2,3,4], [1,2,3,4,5,6,7,8,9])
print(list(filtro))


# Hacemos la función pedida:


def mascotas_legales(lista):
    """Filtra los animales de una lista quitando los NO permitidos.

    Args:
        lista (list[str]): Lista de animales a filtrar.

    Returns:
        list[str]: Devuelve una lista de aquellos animales no prohibidos.
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    filtro = filter(lambda mascota: mascota not in mascotas_prohibidas, lista)
    return list(filtro)


lista_mascotas = ["Mapache", "Perro", "Gato", "Trabubu", "Cocodrilo"]
mascotas_legales(lista_mascotas)


### 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.


try:
    lista_numeros=[25,12,14,2,39,87,1]
    print(f'{round(sum(lista_numeros)/len(lista_numeros),5)}') # Si la lista de números está vacía muestra el error ZeroDivisionError
except Exception as e:
    print(f"Error de tipo {e}.")


def promedio(lista_numeros):
    """Calcula el promedio de los números de una lista.

    Args:
        lista_numeros (list[float or int]): Lista de números a la que se le calculará el promedio.

    Returns:
        float: Devuelve el promedio de los números de la lista.
    """
    try:
        resultado = sum(lista_numeros)/len(lista_numeros)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        return round(resultado,5)


lista_num=[25,12,14,2,39,87,1]
promedio(lista_num)


### 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.


def introducir_edad():
    """Pide al usuario que ingrese una edad y se asegura que esta esté en un rango esperado.

    Raises:
        ValueError: Devuelve un error si se introduce un caracter distinto de un número o si no pertenece al rango esperado.
    """
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError(f"La edad {edad} está fuera del rango esperado (0-120).")
    except ValueError as e:
        if "invalid literal" in str(e): # Si el error muestra que es por haber introducido otros caracteres...
            print(f"Error {e}: No has introducido un número entero válido.")    
        else: 
            print(f"Error de rango: {e}")
    else:
        print(f"Edad registrada correctamente: {edad} años.")


introducir_edad()


### 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().


# Queremos medir la longitud de una palabra. Esto podemos hacerlo con la función 'len'.
# 
# Necesitamos convertir la frase en una lista donde los elementos son cada palabra de la frase. La función split() realiza esta tarea. Dentro del paréntesis va el separador, aunque por defecto está el espacio en blanco.


def longitud_palabras(frase):
    """Mide la longitud de cada palabra en una frase.

    Args:
        frase (srt): Una cada de caracteres con palabras separadas por espacios cuyo cantidad longitud queremos medir.

    Returns:
        list[int]: Devuelve una lista con las longitudes de cada palabra en la frase.
    """
    cadena = frase.split()
    longitudes = map(len,cadena)
    return list(longitudes)


frase = 'Esto es una frase aleatoria de prueba'
longitud_palabras(frase)


### 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map().


# Una vez construyamos una función que devuelva un caracter en minúscula y mayúscula usaremos map() para aplicar esta función a cada caracter del conjunto de caracteres.


def devolver_mayusc_minisc(cadena):
    """Genera tuplas de un mismo caracter en minúscula y mayúscula.

    Args:
        cadena (str or set): Cadena o conjunto de caracteres los cuales queremos listar sus minúsculas y mayúsculas.

    Returns:
        list[tuple]: Lista de tuplas con las minúsculas y mayúsculas de cada caracter.
    """
    elem_unicos=list(set(cadena)) # Convertimos la cadena en un conjunto ya que los elementos de un set son únicos.
    elem_unicos.remove(' ') # Una vez convertido de vuelta a una lista eliminamos el espacio en blanco.
    lista_tuplas=map(lambda letra: (letra.lower(),letra.upper()), elem_unicos)
    return list(lista_tuplas)


devolver_mayusc_minisc(frase)


### 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter().


lista_flores = ['Amapola', 'Petunia', 'Rosa', 'Clavel', 'Lavanda','Tulipán','Alstroemeria']


# Haremos una función 'lambda' que detecte si la letra dada coincide con la inicial de una palabra. 
# 
# Posteriormente usaremos la función 'filter' para aplicar esta función a todos los elementos de una lista.


letra = 'a'
flor = lista_flores[0] # Primer elemento de la lista
x = lambda t: t.lower() in flor[0].lower() 
x(letra)


# Como extra: La función que se pide se puede hacer simplemente recorriendo con un bucle los elementos de la lista, sin necesidad de utilizar 'filter'.


listado = [flor for flor in lista_flores if letra.lower() in flor[0].lower()]
listado


# Hacemos la función pedida:


def filtrar_por_inicial(lista):
    letra = str(input("Escribe una letra: "))   
    filtro = filter(lambda elem: letra.lower() in elem[0].lower(), lista_flores)
    return list(filtro)


filtrar_por_inicial(lista_flores)


### 15. Crea una función lambda que sume 3 a cada número de una lista dada.


# Utilizando 'lambda' y 'map()'.


vector = [3,0,8]


sumar3 = lambda t: t+3
list(map(sumar3,vector))


# Utilizando solo 'lambda'.


sumar3 = lambda t: t+3
[sumar3(num) for num in vector]


### 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().


# Creamos una función 'lambda' que detecte si una palabra es más larga que un número previamente dado.


longitud = 4


comprob = lambda t: len(t) > longitud
print(f"¿Es 'sol' más larga que {longitud}?: {comprob('sol')}. ¿Y 'coche'?: {comprob('coche')}")


# Aplicamos a toda una cadena la función 'lambda' anterior usando la función 'filter()'.


def comprob_longitud(cadena, longitud):
    """Comprueba que la longitud de cada elemento de una cadena sea mayor que una longitud.

    Args:
        cadena (list[str]): Cadena de caracteres sobre los que se comprobará la longitud.
        longitud (int): Longitud umbral para que se muestre el elemento de la cadena. 

    Returns:
        list[str]: Devuelve los elementos de la cadena que tienen mayor longitud que la longitud umbral.
    """
    filtro = filter(lambda palabra: len(palabra) > longitud, cadena)
    return list(filtro)


cadena = ['sol','coche','jirafa','pato','casa','sal','col','rinoceronte','ordenador','ñu']


comprob_longitud(cadena,4)


### 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce().


# La función 'reduce()' debería proceder de la siguiente manera:
# 
# [5,7] -> 57, esto es, resultado = 5 * 10 + 7 = 57.
# 
# [57,2] -> 572, esto es, resultado 57 * 10 + 2 = 572.


from functools import reduce


def unir_digitos(vector):
    """Une los dígitos de un vector en un único número.

    Args:
        vector (list[int]): Vector de dígitos enteros entre el 0 y el 9.

    Returns:
        int: Devuelve el vector de dígitos unido en un único valor entero.
    """
    return reduce(lambda suma,num: suma * 10 + num, vector)


vector = [5,7,2]


unir_digitos(vector)


### 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter().


# Lista de diccionarios
estudiantes = [
    {"nombre": "Alvaro", "edad": 29, "calificación": 95},
    {"nombre": "Ambrosio", "edad": 30, "calificación": 92},
    {"nombre": "Antonio", "edad": 30, "calificación": 87},
    {"nombre": "Alberto", "edad": 31, "calificación": 80},
    {"nombre": "Marta", "edad": 29, "calificación": 89},
    {"nombre": "Anabel", "edad": 29, "calificación": 10}
]

sobresaliente = list(filter(lambda t: t["calificación"] >= 90, estudiantes))

print("Estudiantes con calificación mayor o igual a 90:\n")
for alumno in sobresaliente:
    print(f"{alumno["nombre"]}: {alumno["calificación"]}")


### 19. Crea una función lambda que filtre los números impares de una lista dada.


# Como quiere filtrar números usaremos la función 'filter'.


numeros = [1,2,3,4,5,6,7]

print(list(filter(lambda x: x % 2 != 0, numeros)))


### 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter().


lista = [1,2,'hola',5,'saludos',13,'juan']

print(list(filter(lambda x: type(x)==int, lista)))


### 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.


def cubo(num):
    """Calcula la potencia cúbica de un número. Un número es multiplicado por sí mismo tres veces.

    Args:
        num (float or int): El número que se elevará al cubo.

    Returns:
        float or int: Devuelve el resultado de elevar el número al cubo.
    """
    result = lambda x: x**3
    return result(num)


cubo(5)


### 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().


producto = reduce(lambda x, y: x * y, numeros)
print(f"El producto de los valores {numeros} es: {producto}")


### 23. Concatena una lista de palabras. Usa la función reduce().


concatenacion = reduce(lambda x, y: x + ' ' + y, lista_flores)
print(f"La lista concatenada es: {concatenacion}")


### 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().


vector = [52,25,75,102,19]


#vector.sort(reverse=True) # .sort ordena y modifica la lista original, y reverse=True ordena la lista de forma descendente.
reduce(lambda x, y: x - y, vector) 


### 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.


def contar(cadena):
    """Cuenta los caracteres en una cadena de texto (En un string).

    Args:
        cadena (str): Cadena cuya longitud queremos conocer.

    Returns:
        int: Devuelve la longitud de la cadena de texto.
    """
    return len(cadena)


frase = 'Esto es una frase aleatoria de prueba'
contar(frase)


### 26. Crea una función lambda que calcule el resto de la división entre dos números dados.


resto = lambda x, y: x % y
resto(5,2)


### 27. Crea una función que calcule el promedio de una lista de números.


def promedio(lista_numeros):
    """Calcula el promedio de los números de una lista.

    Args:
        lista_numeros (list[float or int]): Lista de números a la que se le calculará el promedio.

    Returns:
        float: Devuelve el promedio de los números de la lista.
    """
    try:
        resultado = sum(lista_numeros)/len(lista_numeros)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        return round(resultado,5)


vector = [52,25,75,102,19]
promedio(vector)


### 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


# Podemos hacer una lista vacía ('comprobados') y vamos agregando los elementos que vamos encontrándonos mientras recorremos la lista.
# 
# En el momento que el elemento que estamos comprobando ya esté en la lista 'comprobados' lo devolvemos con 'return'.


def buscar_duplicado(lista):
    """Busca el primer duplicado en una lista.

    Args:
        lista (list[str or float or int]): lista en la que buscaremos el primer elemento repetido.

    Returns:
        str or float or int: Devuelve el primer elemento duplicado en la lista.
    """
    comprobados = []
    for elem in lista:
        if elem in comprobados:
            return elem
        else:
            comprobados.append(elem)
    return print("Ningún elemento se repite.")



vector = [1,2,4,5,6,4]
buscar_duplicado(vector)


### 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.


# La variable tiene que ser lo suficientemente larga como para poder enmascarar con '#' algún caracter.
# 
# No especifica sobre la variable pero sí dice que hay que convertirla en cadena de texto, luego usaremos 'str'.
# 
# Crearemos un string con tantos '#'s como la longitud del string menos 4, y añadiremos los cuatro últimos caracteres.


def enmascarar(variable):
    """Enmascara los caracteres de una variable excepto los cuatro últimos caracteres.
    Para ello convierte la variable a tipo string.

    Args:
        variable (str or float or int): Variable a enmascarar.

    Returns:
        str: Devuelve la variable convertida a texto pero con todos los caracteres cambiados a '#' excepto los últimos 4.
    """
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    else:
        enmascarado = '#' * (len(texto) - 4) + texto[-4:]
        return enmascarado


nombre = 'alvarosibon'
enmascarar(nombre)


### 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


palabra1 = 'vaca'
palabra2 = 'cava'
palabra3 = 'toro'


def anagrama(palabra1,palabra2):
    """Comprueba que dos palabras tengan las mismas letras sin importar el orden.

    Args:
        palabra1 (str): Una de las palabras a comprobar.
        palabra2 (str): La otra palabra a comprobar.

    Returns:
        str: Devuelve un string que indica si las palabras son o no anagramas.
    """
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return print(f"Las palabras {palabra1} y {palabra2} son anagramas.")
    else:
        return print(f"Las palabras {palabra1} y {palabra2} no son anagramas.")


anagrama(palabra1,palabra2)


anagrama(palabra1,palabra3)


### 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.


# Convertir un string en una lista donde los elementos son cada nombre separado por comas lo puede hacer la función split(). Dentro del paréntesis va el separador, aunque por defecto está el espacio en blanco. Pondremos (",").


def buscar_nombre():
    nombres = str(input("Introduce una lista de nombres separados por comas: "))
    lista_nombres = [nombre.strip() for nombre in nombres.split(",")] # strip: elimina todos los espacios en blanco iniciales y finales.

    busqueda = str(input("Indica el nombre que quieres buscar: ").strip())

    if busqueda in lista_nombres:
        return print(f"El nombre {busqueda} fue encontrado en la lista.")
    else:
        return print(f"No se encontró el nombre {busqueda} en la lista.")
    


buscar_nombre()


### 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


# Pasaremos un nombre de empleado a buscar como una cadena de caracteres y una lista de diccionarios donde guardaremos cada uno de los empleados con su puesto.
# 
# Tenemos que tener en cuenta que dentro de la función se llama a las claves del diccionario de una manera concreta. Si sabemos que el diccionario tiene solo las claves 'nombre' y 'puesto' podremos acceder a ellas con 'keys', aunque nosotros accederemos al puesto llamándolo y declarándolo de la manera en que se hace en la función, como "puesto".


def buscar_empleado(nombre_empleado, lista_empleados):
    """ Busca un nombre en una lista de nombres. Si encuentra el nombre te muestra el puesto que ejerce en una empresa.

    Args:
        nombre_empleado (str): Nombre a buscar
        lista_empleados (list[dict]): La lista donde se guardan todos los empleados con sus puestos en formato diccionario.
        En este se buscará el nombre.

    Returns:
        None: Devuelve un print con el puesto que ejerce la persona cuyo nombre coincide con nombre_empleado.
    """
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre_empleado.lower():
            return f"El puesto de {empleado["nombre"]} es: {empleado["puesto"]}"
    return f"La persona {nombre_empleado} no está en la lista de empleados."


empleados = [
    {"nombre": "Alvaro" , "puesto": "Analista de datos"},
    {"nombre": "Ambrosio" , "puesto": "Programador jefe"},
    {"nombre": "Antonio" , "puesto": "Becario"},
    {"nombre": "Alberto" , "puesto": "Jefe de proyectos"},
    {"nombre": "Marta" , "puesto": "Jefa de Recursos Humanos"},
    {"nombre": "Anabel" , "puesto": "Analista de datos junior"}
]


buscar_empleado('Alvaro', empleados)


### 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.


lista_numeros1=[1,2,3,4,6]
lista_numeros2=[-1,-2,5,4,1,2]


suma = lambda x, y: x + y
nueva_lista = list(map(suma, lista_numeros1, lista_numeros2))
print(f"La nueva lista sumada es: {nueva_lista}.")


### 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.


class Arbol: # CONSTRUCCIÓN DE UNA CLASE

    # MÉTODO CONSTRUCTOR
    def __init__(self): # No hace falta meter aquí parámetros para tronco y ramas porque ya los inicializamos en la definión.
        self.tronco = 1 # Longitud inicial del tronco
        self.ramas = [] # Lista vacía de ramas
        
    # PRIMER MÉTODO: Crecer tronco en una unidad.
    def crecer_tronco(self):
        self.tronco += 1 # Incremento del tamaño del tronco.
        return "El tronco ha crecido."
    
    # SEGUNDO MÉTODO: Nueva rama de longitud 1.
    def nueva_rama(self):
        self.ramas.append(1) # Añade un elemento (rama) a la lista de ramas con longitud 1.
        return "Ha crecido una nueva rama."
    
    # TERCER MÉTODO: Crecer longitud de todas las ramas en 1.
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas] # Aumenta la longitud de cada rama que tiene el Arbol.
        return "Todas las ramas han crecido en longitud."
    
    # CUARTO MÉTODO: Eliminar rama en una posición específica.
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            rama_eliminada = self.ramas.pop(posicion) # pop(pos) elimina un elemento en la posición 'pos' y devuelve el elemento eliminado. 
            return f"Se ha eliminado una rama de tamaño {rama_eliminada}."    
        else:
            return f"No existe una rama en esa posición."    
    # QUINTO MÉTODO: Devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
    def info_arbol(self):
        print("------INFORMACIÓN DEL ÁRBOL-------")
        print(f"Longitud del tronco: {self.tronco}")
        print(f"Número de ramas: {len(self.ramas)}")
        print(f"Longitudes de las ramas: {self.ramas}")
        print("----------------------------------\n")


arbol1 = Arbol() # 1. Creamos un árbol a partir de la clase 'Arbol'.

arbol1.crecer_tronco() # 2. Aplicamos el método 'crecer_tronco'.

arbol1.nueva_rama() # 3. Aplicamos el método 'nueva_rama'.

arbol1.crecer_ramas() # 4. Aplicamos el método 'crecer_ramas' y comprobamos.

arbol1.nueva_rama() # 5. Añadimos dos nuevas ramas al árbol.
arbol1.nueva_rama()

arbol1.quitar_rama(2) # Eliminamos una de las ramas con el método 'quitar_ramas'.
arbol1.info_arbol()


### 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.


# El código a seguir nos dice que hagamos:
# 
# 1. Inicialización.
# 
# 2. retirar_dinero.
# 
# 3. transferir_dinero.
# 
# 4. agregar_dinero.
# 
# Pero como para transferir_dinero necesitamos retirar_dinero y agregar_dinero lo haremos el último utilizando los dos métodos anteriores.
# 
# Implementaré un método extra que muestre la información de la cuenta de un determinado cliente para monitorizar la correcta realización de las operaciones monetarias.


class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        try:
            cantidad = round(float(cantidad),2) # No se pueden retirar partes decimales de céntimos.
            if cantidad < 0:
                return "ERROR: No es posible retirar un valor negativo de dinero."
            elif cantidad > self.saldo:
                return f"ERROR: {self.nombre} no tiene saldo suficiente para retirar {cantidad:.2f}€."
        except ValueError as v: # Por si se introduce un tipo de dato distinto a un número.
            return "ERROR: No has introducido un número."
        else:
            self.saldo -= cantidad # Decremento del saldo en una cantidad.
            return f"Se han retirado {cantidad:.2f}€. Saldo actualizado de {self.nombre}: {self.saldo:.2f}€."
    
    def agregar_dinero(self, cantidad):
        try:
            cantidad = round(float(cantidad),2)
            if cantidad < 0:
                return "No es posible agregar un valor negativo de dinero."
        except ValueError as v:
            return "ERROR: No has introducido un número."
        else:
            self.saldo += cantidad
            return f"Se han agregado {cantidad:.2f}€. Saldo actualizado de {self.nombre}: {self.saldo:.2f}€."
    
    def transferir_dinero(self, usuario_remitente, cantidad):
        try:
            cantidad = float(cantidad)
            if cantidad < 0:
                return "ERROR: No es posible retirar un valor negativo de dinero."
            elif cantidad > usuario_remitente.saldo:
                return f"ERROR: {usuario_remitente.nombre} no tiene saldo suficiente para retirar {cantidad:.2f}€."
        except ValueError as v:
            return "ERROR: No has introducido un número."
        else:
            resultado1 = usuario_remitente.retirar_dinero(cantidad)
            resultado2 = self.agregar_dinero(cantidad)
            return f"Transferencia realizada:\n De {usuario_remitente.nombre} a {self.nombre}.\n Cantidad = {cantidad:.2f}€."
    
    def info_usuario(self):
        print("------INFORMACIÓN DE SALDO-------")
        print(f"Nombre de usuario: {self.nombre}")
        print(f"Saldo: {self.saldo:.2f}€.")
        if self.cuenta_corriente == True: 
            print("Posesión de cuenta corriente: SÍ.")
        else:
            print("Posesión de cuenta corriente: NO.")
        print("----------------------------------\n")


usuario_1 = UsuarioBanco("Alicia", 100, True)
usuario_2 = UsuarioBanco("Bob", 50, True)

usuario_1.info_usuario()
usuario_2.info_usuario()


print(f"1. {usuario_2.agregar_dinero(20)}")
usuario_2.info_usuario()
print(f"2. {usuario_1.transferir_dinero(usuario_2, 40)}")
usuario_1.info_usuario()
usuario_2.info_usuario()
print(f"3. {usuario_1.retirar_dinero(50)}")
usuario_1.info_usuario()


### 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras y eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .


# Necesitamos convertir el texto en una lista donde los elementos son cada palabra de la frase. La función split() realiza esta tarea. Dentro del paréntesis va el separador, aunque por defecto está el espacio en blanco.


def contar_palabras(texto):
    caract_para_eliminar = ".,:;¡!¿?" # Quitamos cada uno de los caracteres que no necesitamos contar.
    for caracter in caract_para_eliminar:
        texto = texto.replace(caracter, '')
    lista = list(texto.lower().split()) # Una lista de cada palabra del texto en minúsculas.
    diccio={}
    for pos in range(len(lista)): # Recorremos todos los elementos de la lista y vemos cuántas veces aparece.
        diccio.update({lista[pos]:lista.count(lista[pos])})
    return diccio

def reemplazar_palabras(texto, palabra_original, palabra_reemplazo):
    texto = ' '+texto # Por si acaso se quiero reemplazar la primera palabra.
    caract_para_eliminar = " .,:;¡!¿?()" # Caracteres más comunes que pueden separar palabras.
    
    # Comprobaremos todas las combinaciones de separadores de palabras para reemplazar por la palabra nueva y los mismos separadores.
    # Evitamos que palabras que incluyan otra palabra sean modificadas.
    for caracter1 in caract_para_eliminar:
        for caracter2 in caract_para_eliminar:
            texto = texto.replace(caracter1+palabra_original+caracter2, caracter1+palabra_reemplazo+caracter2)
    return texto

def eliminar_palabra(texto, palabra):
    texto = ' '+texto # Por si acaso se quiero eliminar la primera palabra.
    caract_para_eliminar = " .,:;¡!¿?()" # Todos los caracteres que pueden separar palabras
    for caracter1 in caract_para_eliminar:
        for caracter2 in caract_para_eliminar:
            texto = texto.replace(caracter1+palabra+caracter2, caracter1+caracter2)
    return texto



texto ='Las autoridades continuarán con las labores de búsqueda de Fernando Martín y tres de sus hijos, que han desaparecido en el mar tras hundirse el barco turístico en el que viajaban.'


# *args se pasa a la función como una tupla, luego habrá que acceder a estos con índices.

def procesar_texto(texto, opcion, *args):
    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar':
        if len(args)<2:
            return "No se han introducido los argumentos necesarios para reemplazar palabras."
        else:
            return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == 'eliminar':
        if len(args)<1:
            return "No se han introducido los argumentos necesarios para eliminar palabras."
        else:
            return eliminar_palabra(texto, args[0])
    else:
        return f"La opción {opcion} no es válida."


texto = procesar_texto(texto, 'reemplazar','mar', 'océano')
texto = procesar_texto(texto, 'eliminar', 'hijos')
procesar_texto(texto, 'contar')



### 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.


def momento_dia():
    """Comprueba en qué momento del día estamos según la hora pasada por el usuario

    Raises:
        ValueError: Devuelve un error si se introduce un caracter distinto de un número o si no pertenece al rango esperado.

    Returns:
        None: No devuelve ningún valor. Imprime por pantalla el momento del día. 
    """
    try:
        hora = int(input("Introduce la hora actual (0-23): "))
        if hora < 0 or hora > 23:
            raise ValueError("Error: La hora introducida no pertenece al intervalo (0-23).")
    except ValueError as v:
        if "invalid literal" in str(v):
            print(f"Error '{v}': No has introducido un número entero válido.")
        else: 
            print(f"{v}")
    except Exception as e:
        print(f"Error: Ha ocurrido un error tipo {e}.")
    else:
        if 6 <= hora < 12:
            return f"La hora {hora} corresponde a la mañana."
        elif 12 <= hora < 20:
            return f"La hora {hora} corresponde a la tarde."
        else:
            return f"La hora {hora} corresponde a la noche"


momento_dia()


### 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente


def calificacion_texto(nota):
    """Convierte una calificación numérica a texto según unos intervalos específicos.

    Args:
        nota (float or int): La calificación numérica que queremos pasar a texto.

    Returns:
        None: Imprime por pantalla la calificación en texto.
    """
    if nota < 0 or nota > 100:
        return "Error: La calificación debe estar entre 0 y 100."
    else:
        if nota < 70:
            return "insuficiente"
        elif nota < 80:
            return "bien"
        elif nota < 90:
            return "muy bien"
        else:
            return "excelente"
    


### 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).


import math

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area(figura, *args):

    if figura == "rectangulo":
        if len(args) < 2:
            return "No se han introducido los argumentos necesarios para calcular el área del rectángulo."
        else:
            return area_rectangulo(args[0],args[1])

    elif figura == "circulo":
        if len(args) < 1:
            return "No se han introducido los argumentos necesarios para calcular el área del círculo."
        else:
            return math.pi * (args[0] ** 2)

    elif figura == "triangulo":
        if len(args) < 2:
            return "No se han introducido los argumentos necesarios para calcular el área del triángulo."
        else:
            return (args[0] * args[1]) / 2
    else:
        return "Error: La figura {figura} no es válida."


rectangulo = calcular_area("rectangulo", 5, 2)
circulo = calcular_area("circulo", 3)
triangulo = calcular_area("triangulo", 6, 4)

print(f"Área Rectángulo: {rectangulo} uds. cuadradas.")
print(f"Área Círculo: {circulo:.2f} uds. cuadradas.") # Redondeado a 2 decimales
print(f"Área Triángulo: {triangulo} uds. cuadradas.")


### 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar elmonto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.


def calcular_compra():
    try:
        precio_original = float(input("Ingresa el precio original del artículo (en €): "))
        
        cupon = input("¿Tienes un cupón de descuento? (Introduce 'sí' o 'no'): ").strip().lower()

        precio_final = precio_original

        if cupon == "sí" or cupon == "si":
            descuento = float(input("Ingresa el valor del cupón de descuento (en €): "))
            
            if descuento > 0:
                if descuento > precio_original:
                    precio_final = 0 
                    print(f"Descuento aplicado: El descuento ({descuento:.2f}€) cubre por completo el precio original ({precio_original:.2f}€).")
                else:
                    precio_final = precio_original - descuento
                    print(f"Descuento de {descuento:.2f}€ aplicado correctamente.")
            else:
                print("Descuento no válido.")
        
        elif cupon == "no":
            print("No se aplica descuento sobre el artículo.")
        else:
            print("Respuesta no válida. Cupón no aplicado.")

        return f"Precio final de la compra: {precio_final:.2f}€."
    except ValueError:
        return "Error: Por favor, ingresa valores numéricos válidos para los precios."


calcular_compra()


