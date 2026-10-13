from Main_funciones import *

# Funciones de ingreso

def ingresar_numeros_lista(lista: list, mensaje: str) -> list:
    valido = False

    while valido == False:
        num = input(mensaje)

        if len(num) == 0:
            print('No ingresó un número. Vuelva a intentar.')
        else:
            valido = True

            for i in range(len(num)):
                if ord(num[i]) < 48 or ord(num[i]) > 57:
                    print('El dato ingresado no es un número. Ingrese los datos correctamente.')
                    valido = False
                    break

    lista = lista + [num]
    return lista



def ingresar_apellido_nombre(lista: list, mensaje: str) -> list:
    valido = False

    while valido == False:
        apellido_nombre = input(mensaje)

        if len(apellido_nombre) == 0:
            print('No ingresó un apellido y nombre. Vuelva a intentar.')
        else:
            valido = True

            for i in range(len(apellido_nombre)):
                if ((ord(apellido_nombre[i]) >= 65 and ord(apellido_nombre[i]) <= 90) or
                    (ord(apellido_nombre[i]) >= 97 and ord(apellido_nombre[i]) <= 122) or
                    ord(apellido_nombre[i]) == 32):
                    valido = True
                else:
                    print('Solo se permiten letras y espacios. Ingrese los datos de forma correcta.')
                    valido = False
                    break

    lista = lista + [apellido_nombre]
    return lista


def Ingresar_Generos_estudiantes(lista: list, mensaje: str) -> list:
    valido = False

    while valido == False:
        genero = input(mensaje)

        if len(genero) == 0:
            print('No ingresó un género. Vuelva a intentar.')

        elif genero != 'F' and genero != 'M' and genero != 'X':
            print('Género inválido. Ingrese F, M o X. Vuelva a intentar.')

        else:
            valido = True

    lista = lista + [genero]
    return lista



def Ingresar_Notas(lista: list, mensaje: str) -> list:
    valido = False

    while valido == False:
        nota = input(mensaje)

        if len(nota) == 0:
            print('No ingresó una nota. Vuelva a intentar.')
        else:
            puntos = 0
            valido = True

            for i in range(len(nota)):
                if nota[i] == '.':
                    puntos += 1
                elif ord(nota[i]) < 48 or ord(nota[i]) > 57:
                    print('La nota debe ser un número. Ingrese los datos correctamente.')
                    valido = False
                    break

            if valido == True:
                if puntos > 1:
                    print('La nota ingresada es inválida. Vuelva a intentar.')
                    valido = False

            if valido == True:
                nota = float(nota)

                if nota < 1 or nota > 10:
                    print('La nota debe estar entre 1 y 10. Vuelva a intentar.')
                    valido = False

    lista = lista + [nota]
    return lista






# Mostrar los datos

def Mostrar_estudiante(Legajos_estudiantes: list,
                       Apellidos_nombres: list,
                       Generos_estudiantes: list,
                       Notas_parcial_1: list,
                       Notas_parcial_2: list):

    print('INFORME DE TODOS LOS ESTUDIANTES')
    print('Legajo | Apellido y nombre | Género | Parcial 1 | Parcial 2')

    for i in range(len(Legajos_estudiantes)):
        print(f'{Legajos_estudiantes[i]} | '
              f'{Apellidos_nombres[i]} | '
              f'{Generos_estudiantes[i]} | '
              f'{Notas_parcial_1[i]:.2f} | '
              f'{Notas_parcial_2[i]:.2f}')

    Mostrar_un_estudiante(
        Legajos_estudiantes,
        Apellidos_nombres,
        Generos_estudiantes,
        Notas_parcial_1,
        Notas_parcial_2
    )


def Mostrar_un_estudiante(Legajos_estudiantes: list,
                          Apellidos_nombres: list,
                          Generos_estudiantes: list,
                          Notas_parcial_1: list,
                          Notas_parcial_2: list):

    numero_estudiante = int(input(
        '¿Qué número de estudiante ingresado querés ver? '
    ))

    indice = numero_estudiante - 1

    if 0 <= indice < len(Legajos_estudiantes):
        print('INFORME DEL ESTUDIANTE')
        print('Legajo | Apellido y nombre | Género | Parcial 1 | Parcial 2')

        print(f'{Legajos_estudiantes[indice]} | '
              f'{Apellidos_nombres[indice]} | '
              f'{Generos_estudiantes[indice]} | '
              f'{Notas_parcial_1[indice]:.2f} | '
              f'{Notas_parcial_2[indice]:.2f}')
    else:
        print('Número de estudiante inválido.')






# Promedios  

def Calcular_promedios(Lista_Promedios: list, Notas_parcial_1: list, Notas_parcial_2: list) -> list:

    for i in range(len(Notas_parcial_1)):
        promedio = (Notas_parcial_1[i] + Notas_parcial_2[i]) / 2
        promedio = int(promedio * 100) / 100
        Lista_Promedios += [promedio]

    return Lista_Promedios



# Ordenamiento 

def Mostrar_promedios(Legajos_estudiantes: list,
                        Apellidos_nombres: list,
                        Generos_estudiantes: list,
                        Notas_parcial_1: list,
                        Notas_parcial_2: list,
                        Lista_Promedios: list):

    orden = input('Ingrese ASC o DESC: ')

    while (orden != 'ASC' and orden != 'DESC' and
           orden != 'asc' and orden != 'desc'):
        print('Orden inválido.')
        orden = input('Ingrese ASC o DESC: ')

    if orden == 'asc':
        orden = 'ASC'
    elif orden == 'desc':
        orden = 'DESC'

    for i in range(len(Lista_Promedios) - 1):
        for j in range(len(Lista_Promedios) - 1 - i):

            cambiar = False

            if orden == 'ASC':
                if Lista_Promedios[j] > Lista_Promedios[j + 1]:
                    cambiar = True
            else:
                if Lista_Promedios[j] < Lista_Promedios[j + 1]:
                    cambiar = True

            if cambiar:
                Legajos_estudiantes[j], Legajos_estudiantes[j + 1] = Legajos_estudiantes[j + 1], Legajos_estudiantes[j]

                Apellidos_nombres[j], Apellidos_nombres[j + 1] = Apellidos_nombres[j + 1], Apellidos_nombres[j]

                Generos_estudiantes[j], Generos_estudiantes[j + 1] = Generos_estudiantes[j + 1], Generos_estudiantes[j]

                Notas_parcial_1[j], Notas_parcial_1[j + 1] = Notas_parcial_1[j + 1], Notas_parcial_1[j]

                Notas_parcial_2[j], Notas_parcial_2[j + 1] = Notas_parcial_2[j + 1], Notas_parcial_2[j]

                Lista_Promedios[j], Lista_Promedios[j + 1] = Lista_Promedios[j + 1], Lista_Promedios[j]

    Mostrar_todos_los_datos(
        Legajos_estudiantes,
        Apellidos_nombres,
        Generos_estudiantes,
        Notas_parcial_1,
        Notas_parcial_2,
        Lista_Promedios
    )


def Mostrar_todos_los_datos(Legajos_estudiantes: list,
                            Apellidos_nombres: list,
                            Generos_estudiantes: list,
                            Notas_parcial_1: list,
                            Notas_parcial_2: list,
                            Lista_Promedios: list):

    print('\nINFORME DE TODOS LOS ESTUDIANTES')
    print('Legajo | Apellido y nombre | Género | Parcial 1 | Parcial 2 | Promedio')

    for i in range(len(Legajos_estudiantes)):
        print(f'{Legajos_estudiantes[i]} | '
              f'{Apellidos_nombres[i]} | '
              f'{Generos_estudiantes[i]} | '
              f'{Notas_parcial_1[i]:.2f} | '
              f'{Notas_parcial_2[i]:.2f} | '
              f'{Lista_Promedios[i]:.2f}')




# Mayor Promedio




def Mostrar_mayor_promedio(Legajos_estudiantes: list,
                           Apellidos_nombres: list,
                           Generos_estudiantes: list,
                           Notas_parcial_1: list,
                           Notas_parcial_2: list,
                           Lista_Promedios: list):

    mayor_promedio = Lista_Promedios[0]

    for i in range(1, len(Lista_Promedios)):
        if Lista_Promedios[i] > mayor_promedio:
            mayor_promedio = Lista_Promedios[i]

    print('ESTUDIANTE/S CON MAYOR PROMEDIO')

    for i in range(len(Lista_Promedios)):
        if Lista_Promedios[i] == mayor_promedio:
            Mostrar_un_estudiante(
                Legajos_estudiantes,
                Apellidos_nombres,
                Generos_estudiantes,
                Notas_parcial_1,
                Notas_parcial_2,
                i
            )


def Mostrar_un_estudiante(Legajos_estudiantes: list,
                          Apellidos_nombres: list,
                          Generos_estudiantes: list,
                          Notas_parcial_1: list,
                          Notas_parcial_2: list,
                          indice: int):

    print('Legajo | Apellido y nombre | Género | Parcial 1 | Parcial 2')

    print(f'{Legajos_estudiantes[indice]} | '
          f'{Apellidos_nombres[indice]} | '
          f'{Generos_estudiantes[indice]} | '
          f'{Notas_parcial_1[indice]:.2f} | '
          f'{Notas_parcial_2[indice]:.2f}')



# datos de un estudiante por legajo

def Buscar_estudiante_por_legajo(Legajos_estudiantes: list,
                                Apellidos_nombres: list,
                                Generos_estudiantes: list,
                                Notas_parcial_1: list,
                                Notas_parcial_2: list):

    legajo_buscado = int(input('Ingrese el legajo del estudiante: '))
    encontrado = False

    for i in range(len(Legajos_estudiantes)):
        if Legajos_estudiantes[i] == legajo_buscado:
            Mostrar_un_estudiante(
                Legajos_estudiantes,
                Apellidos_nombres,
                Generos_estudiantes,
                Notas_parcial_1,
                Notas_parcial_2,
                i
            )
            encontrado = True

    if encontrado == False:
        print('No se encontró un estudiante con ese legajo.')


def Mostrar_un_estudiante(Legajos_estudiantes: list,
                          Apellidos_nombres: list,
                          Generos_estudiantes: list,
                          Notas_parcial_1: list,
                          Notas_parcial_2: list,
                          indice: int):

    print('INFORME DEL ESTUDIANTE')
    print('Legajo | Apellido y nombre | Género | Parcial 1 | Parcial 2')

    print(f'{Legajos_estudiantes[indice]} | '
          f'{Apellidos_nombres[indice]} | '
          f'{Generos_estudiantes[indice]} | '
          f'{Notas_parcial_1[indice]:.2f} | '
          f'{Notas_parcial_2[indice]:.2f}')












