import os

# DICCIONARIO: colores de los mensajes
COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

# TUPLAS: respuestas afirmativas y negativas
RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")
RESPUESTAS_NO = ("no", "n")


def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")


def imprimir_color(texto, color):
    codigo = COLORES.get(color, COLORES["BLANCO"])
    print(f"{codigo}{texto}{COLORES['RESET']}")


def imprimir_titulo(texto):
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()


def imprimir_exito(mensaje):
    imprimir_color(f"✓ {mensaje}", "VERDE")


def imprimir_error(mensaje):
    imprimir_color(f"✗ {mensaje}", "ROJO")


def imprimir_info(mensaje):
    imprimir_color(f"ℹ {mensaje}", "CYAN")


def imprimir_advertencia(mensaje):
    imprimir_color(f"⚠ {mensaje}", "AMARILLO")


# VALIDAR QUE UN DATO SEA ENTERO
def validar_entero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


# SOLICITAR UN NUMERO ENTERO
def leer_entero(mensaje, minimo=None):
    while True:
        numero = input(mensaje)

        if validar_entero(numero):
            numero = int(numero)

            if minimo is not None and numero < minimo:
                imprimir_error("El numero debe ser mayor o igual a " + str(minimo))
            else:
                return numero
        else:
            imprimir_error("Debe ingresar un numero entero.")


# VALIDAR CEDULA ECUATORIANA
def validar_cedula(cedula):
    if len(cedula) != 10 or not cedula.isdigit():
        return False

    provincia = int(cedula[0:2])
    tercer_digito = int(cedula[2])

    if provincia < 1 or provincia > 24:
        return False

    if tercer_digito > 5:
        return False

    suma = 0

    for i in range(9):
        numero = int(cedula[i])

        if i % 2 == 0:
            numero = numero * 2

            if numero > 9:
                numero = numero - 9

        suma = suma + numero

    verificador = 10 - (suma % 10)

    if verificador == 10:
        verificador = 0

    return verificador == int(cedula[9])


# SOLICITAR UNA CEDULA VALIDA
def leer_cedula():
    while True:
        cedula = input("Ingrese la cedula: ").strip()

        if validar_cedula(cedula):
            return cedula

        imprimir_error("La cedula ingresada no es valida.")


# VALIDAR QUE UN TEXTO NO ESTE VACIO
def leer_texto(mensaje):
    while True:
        texto = input(mensaje)

        if texto.strip() != "":
            return texto.strip()

        imprimir_error("Este campo no puede estar vacio.")


# CONFIRMAR UNA ACCION
def confirmar(mensaje):
    while True:
        respuesta = input(mensaje + " (si/no): ").strip().lower()

        if respuesta in RESPUESTAS_SI:
            return True

        if respuesta in RESPUESTAS_NO:
            return False

        imprimir_error("Responda si o no.")