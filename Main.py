from Main_funciones import *

# Una institución educativa desea procesar los datos de sus estudiantes.  
# Para ello, se tienen los siguientes datos:



#  Una lista de legajos de los estudiantes. Cada legajo debe ser numérico del tipo entero. 
#  Una lista de apellidos y nombres de los estudiantes. Validar que sea alfabético. 
#  Una lista de géneros de los estudiantes. Cada género debe ser alguno de los siguientes: [‘F’ | ‘M’ | ‘X’]. 
#  Una lista de notas del primer parcial. Cada nota debe ser un número entero entre 1 y 10. 
#  Una lista de notas del segundo parcial. Cada nota debe ser un número entero entre 1 y 10.


# Cada una de estas listas debe ser de treinta (30) elementos, las mismas se corresponden entre sí. 
# Es decir, que se debe trabajar como listas paralelas.

# Se deberá programar un menú de opciones operado por consola, que realice lo siguiente: 


# 1 – Realizar la carga de los datos en cada una de las listas. 
# Validar cada dato a ser cargado. 
# Realizar una función para cada dato.

# 2 – Mostrar todos los datos (en forma de informe con su título y los registros), de los estudiantes: 
# legajo, apellido y nombre, género, primer parcial y segundo parcial (5). 
# Realizar una función que recorra todos los elementos 
# y otra para mostrar un elemento. La segunda función será llamada dentro de la primera.

# 3 – Calcular el promedio de cada estudiante y guardarlo en una nueva lista de promedios. 
# Realizar una función que calcule el promedio, el cual debe ser de números reales 
# entre 1.00 y 10.00, con su parte entera y dos (2) decimales.

# 4 – Mostrar todos los datos (en forma de informe con su título y los registros), de 
# los estudiantes ordenados por promedio de manera DESC. 
# Realizar una función que ordene, la cual deberá ordenar de manera ASC o DESC, 
# de acuerdo a un parámetro de ordenamiento

# 5 – Mostrar el/los estudiante/s con mayor promedio. Utilizar las funciones 
# desarrolladas para el ítem 2 
# (Una función que recorra todos los elementos y otra para mostrar un elemento).

# 6 – Buscar y mostrar todos los datos de un estudiante por legajo. 
# Utilizar las funciones desarrolladas para el ítem 2 
# (Una función que recorra todos los elementos y otra para mostrar un elemento).

# 7 – Salir del programa.



# NOTAS:
# Nota 0: Los datos de las listas podrán estar hardcodeadas a los efectos de realizar las pruebas de
# funcionamiento correspondientes.
# Nota 1: No se podrá acceder a ningún ítem del menú, sin antes haber cargado los datos. En tal sentido, realizar
# la validación correspondiente.
# Nota 2: Los puntos deben ser accedidos mediante un menú de opciones.
# Nota 3: Cada ítem del menú deberá ser una función.
# Nota 4: Se deberá desarrollar biblioteca y funciones propias, las mismas deberán estar correctamente
# documentadas.
# Nota 5: Se deberá desarrollar una función para la validación de cada uno de los datos.
# Nota 6: Desarrollar una función que recorra los elementos y otra que muestre un elemento. La segunda será
# llamada dentro de la primera

menu = '''
1) Cargar datos .
2) Mostrar datos.
3) Calcular promedios.
4) Mostrar todos los datos.
5) Mostrar el mayor promedio.
6) Mostrar todos los datos de un estudiante por legajo
7) Salir

Seleccione una opción: '''

Legajos_estudiantes = []
Apellidos_nombres = []
Generos_estudiantes = []
Notas_parcial_1 = [] 
Notas_parcial_2 = [] 
Lista_Promedios = []

while True:
    opcion = input(menu)
    match opcion:
        case '1':
            print ('Eligió Cargar Datos ')
            Legajos_estudiantes = ingresar_numeros_lista (Legajos_estudiantes, 'Ingrese el legajo del alumno: ')
            Apellidos_nombres = ingresar_apellido_nombre (Apellidos_nombres, 'Ingresar el Apellido y nombre del alumno: ' )
            Generos_estudiantes =Ingresar_Generos_estudiantes (Generos_estudiantes, 'Ingresar el género como F , M o X: ')
            Notas_parcial_1 = Ingresar_Notas(Notas_parcial_1, ' Ingresar la nota del parcial 1: ')
            Notas_parcial_2 = Ingresar_Notas (Notas_parcial_2, 'Ingresar la nota del parcial 2: ')
        case '2':
            print('Eligió Mostrar datos ')
            Informe_Estudiante = Mostrar_estudiante (Legajos_estudiantes,Apellidos_nombres, Generos_estudiantes,Notas_parcial_1, Notas_parcial_2 )   
        case '3':
            print('Eligió Calcular promedios ')
            Lista_Promedios= Calcular_promedios (Lista_Promedios, Notas_parcial_1, Notas_parcial_2)
        case '4':
            print('Eligió Mostrar todos los datos ')
            Ordenamiento = Mostrar_promedios (Legajos_estudiantes,Apellidos_nombres, Generos_estudiantes,Notas_parcial_1, Notas_parcial_2, Lista_Promedios )
            
        case '5':
            print('Eligió Mostrar el mayor promedio ')
            mayor_promedio = Mostrar_mayor_promedio (Legajos_estudiantes,Apellidos_nombres, Generos_estudiantes,Notas_parcial_1, Notas_parcial_2, Lista_Promedios  )
        case '6':
            print('Eligió Mostrar todos los datos de un estudiante por legajo ')
            Datos_de_un_estudiante = Buscar_estudiante_por_legajo (Legajos_estudiantes,Apellidos_nombres, Generos_estudiantes,Notas_parcial_1, Notas_parcial_2)
            
        case '7':
            print('Eligió Salir.Buenas suerte ')
            break
            
        case _:
            print ('Opción inválida vuelva a elegir ')




