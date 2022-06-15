from shapes import *


def user_menu():
    print('¿Qué figura desea imprimir?')
    print('1) Cubo')
    print('2) Esfera')
    print('3) Prisma rectangular')

    opcion = input('Opcion: ')

    if opcion == "1":
        nom = input('Introduzca el nombre: ')
        lad = input('Introduzca el lado: ')

        cubo = Cubo(nom, lad)

        print(f'Imprimiento…{cubo.nombre} por favor espere\n')
        cubo.print_properties()

    elif opcion == "2":
        nom = input('Introduzca el nombre: ')
        rad = input('Introduzca el radio: ')

        esfera = Esfera(nom, rad)

        print(f'Imprimiento…{esfera.nombre} por favor espere')
        esfera.print_properties()

    elif opcion == "3":
        nom = input('Introduzca el nombre: ')
        bas = input('Introduzca la base: ')
        alt = input('Introduzca la altura: ')
        prof = input('Introduzca la profundidad: ')

        prisma_rectangular = Prisma_rectangular(nom, bas, alt, prof)

        print(f'Imprimiento… {prisma_rectangular.nombre}, por favor espere')
        prisma_rectangular.print_properties()


user_menu()
