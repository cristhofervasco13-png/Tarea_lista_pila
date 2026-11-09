from pasajeros import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

from utils import (
    limpiar_pantalla,
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    imprimir_advertencia,
    leer_entero,
    leer_cedula,
    leer_texto,
    confirmar
)


# CREAR LAS ESTRUCTURAS
pila = MiPila(10)
cola = MiCola(10)


# LEER LOS DATOS DE UN PASAJERO
def leer_pasajero():
    print("\nINGRESAR DATOS DEL PASAJERO")

    numero = leer_entero("Numero de pasajero: ", 1)
    nombre = leer_texto("Nombre: ")
    cedula = leer_cedula()
    edad = leer_entero("Edad: ", 0)
    fecha_vuelo = leer_texto("Fecha de vuelo (AAAA-MM-DD): ")
    destino = leer_texto("Destino: ")
    asiento = leer_texto("Asiento: ").upper()

    return Pasajero(
        numero,
        nombre,
        cedula,
        edad,
        fecha_vuelo,
        destino,
        asiento
    )


# DATOS DE PRUEBA EN ORDEN DE LLEGADA
def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A")
    ]


# CARGAR DATOS DE PRUEBA EN LA PILA
def cargar_pila():
    for pasajero in datos_prueba():
        pila.apilar(pasajero)

    imprimir_exito("Datos de prueba cargados en la pila.")


# CARGAR DATOS DE PRUEBA EN LA COLA
def cargar_cola():
    for pasajero in datos_prueba():
        cola.encolar(pasajero)

    imprimir_exito("Datos de prueba cargados en la cola.")


# MOSTRAR LAS OPCIONES DE LOS MENUS
def mostrar_opciones(titulo, entrar, salir, ver):
    print("\n========== " + titulo + " ==========")
    print("1. " + entrar)
    print("2. Listar")
    print("3. " + salir)
    print("4. " + ver)
    print("5. Buscar")
    print("6. Modificar")
    print("7. Eliminar por numero")
    print("8. Copiar")
    print("9. Longitud / ¿Esta vacia?")
    print("C. Cargar datos de prueba")
    print("0. Volver")


# MENU DE LA PILA
def menu_pila():
    while True:
        mostrar_opciones("MENU 1 - PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")

        opcion = input("Seleccione una opcion: ").strip().upper()

        if opcion == "1":
            pasajero = leer_pasajero()

            if pila.apilar(pasajero):
                imprimir_exito("Pasajero apilado correctamente.")
            else:
                imprimir_error("No se pudo apilar el pasajero.")

        elif opcion == "2":
            pila.listar()

        elif opcion == "3":
            pasajero = pila.desapilar()

            if pasajero is None:
                imprimir_advertencia("La pila esta vacia.")
            else:
                imprimir_exito("Salio: " + str(pasajero))

                tope = pila.ver_tope()

                if tope is not None:
                    imprimir_info("Nuevo tope: " + str(tope))

        elif opcion == "4":
            pasajero = pila.ver_tope()

            if pasajero is None:
                imprimir_advertencia("La pila esta vacia.")
            else:
                imprimir_info("Tope: " + str(pasajero))

        elif opcion == "5":
            numero = leer_entero("Numero de pasajero a buscar: ", 1)
            posicion = pila.buscar(numero)

            if posicion == -1:
                imprimir_error("El pasajero no existe.")
            else:
                imprimir_exito("Pasajero encontrado en la posicion " + str(posicion))
                print(pila.datos[posicion])

        elif opcion == "6":
            numero = leer_entero("Numero de pasajero a modificar: ", 1)
            destino = leer_texto("Nuevo destino: ")
            asiento = leer_texto("Nuevo asiento: ").upper()

            if pila.modificar(numero, destino, asiento):
                imprimir_exito("Pasajero modificado correctamente.")
            else:
                imprimir_error("El pasajero no existe.")

        elif opcion == "7":
            numero = leer_entero("Numero de pasajero a eliminar: ", 1)
            pasajero = pila.eliminar_por_numero(numero)

            if pasajero is None:
                imprimir_error("El pasajero no existe.")
            else:
                imprimir_exito("Pasajero eliminado: " + str(pasajero))

        elif opcion == "8":
            copia = pila.copiar()

            imprimir_info("COPIA DE LA PILA")
            copia.listar()

        elif opcion == "9":
            print("Longitud:", pila.longitud())

            if pila.esta_vacia():
                imprimir_advertencia("La pila esta vacia.")
            else:
                imprimir_exito("La pila no esta vacia.")

        elif opcion == "C":
            cargar_pila()

        elif opcion == "0":
            break

        else:
            imprimir_error("Opcion no valida.")


# MENU DE LA COLA
def menu_cola():
    while True:
        mostrar_opciones("MENU 2 - COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")

        opcion = input("Seleccione una opcion: ").strip().upper()

        if opcion == "1":
            pasajero = leer_pasajero()

            if cola.encolar(pasajero):
                imprimir_exito("Pasajero encolado correctamente.")
            else:
                imprimir_error("No se pudo encolar el pasajero.")

        elif opcion == "2":
            cola.listar()

        elif opcion == "3":
            pasajero = cola.desencolar()

            if pasajero is None:
                imprimir_advertencia("La cola esta vacia.")
            else:
                imprimir_exito("Salio: " + str(pasajero))

                frente = cola.ver_frente()

                if frente is not None:
                    imprimir_info("Nuevo frente: " + str(frente))

        elif opcion == "4":
            pasajero = cola.ver_frente()

            if pasajero is None:
                imprimir_advertencia("La cola esta vacia.")
            else:
                imprimir_info("Frente: " + str(pasajero))

        elif opcion == "5":
            numero = leer_entero("Numero de pasajero a buscar: ", 1)
            posicion = cola.buscar(numero)

            if posicion == -1:
                imprimir_error("El pasajero no existe.")
            else:
                imprimir_exito("Pasajero encontrado en la posicion " + str(posicion))
                print(cola.datos[posicion])

        elif opcion == "6":
            numero = leer_entero("Numero de pasajero a modificar: ", 1)
            destino = leer_texto("Nuevo destino: ")
            asiento = leer_texto("Nuevo asiento: ").upper()

            if cola.modificar(numero, destino, asiento):
                imprimir_exito("Pasajero modificado correctamente.")
            else:
                imprimir_error("El pasajero no existe.")

        elif opcion == "7":
            numero = leer_entero("Numero de pasajero a eliminar: ", 1)
            pasajero = cola.eliminar_por_numero(numero)

            if pasajero is None:
                imprimir_error("El pasajero no existe.")
            else:
                imprimir_exito("Pasajero eliminado: " + str(pasajero))

        elif opcion == "8":
            copia = cola.copiar()

            imprimir_info("COPIA DE LA COLA")
            copia.listar()

        elif opcion == "9":
            print("Longitud:", cola.longitud())

            if cola.esta_vacia():
                imprimir_advertencia("La cola esta vacia.")
            else:
                imprimir_exito("La cola no esta vacia.")

        elif opcion == "C":
            cargar_cola()

        elif opcion == "0":
            break

        else:
            imprimir_error("Opcion no valida.")


# MENU PRINCIPAL
def main():
    while True:
        imprimir_titulo("TAREA PILAS Y COLAS - PASAJEROS")

        print("1. Menu 1 - Pila")
        print("2. Menu 2 - Cola")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            menu_pila()

        elif opcion == "2":
            menu_cola()

        elif opcion == "3":
            if confirmar("¿Desea salir del programa?"):
                imprimir_exito("Hasta pronto.")
                break

        else:
            imprimir_error("Opcion no valida.")


if __name__ == "__main__":
    main()