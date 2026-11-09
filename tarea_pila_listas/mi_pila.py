class MiPila:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    # AGREGAR UN PASAJERO
    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La pila está llena.")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("El número de pasajero ya existe.")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # MOSTRAR LOS PASAJEROS DESDE EL TOPE
    def listar(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return

        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"[{i}] {self.datos[i]} <- TOPE")
            elif i == 0:
                print(f"[{i}] {self.datos[i]} <- FONDO")
            else:
                print(f"[{i}] {self.datos[i]}")

    # RETIRAR EL PASAJERO DEL TOPE
    def desapilar(self):
        if self.esta_vacia():
            return None

        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1

        return pasajero

    # CONSULTAR EL TOPE SIN ELIMINARLO
    def ver_tope(self):
        if self.esta_vacia():
            return None

        return self.datos[self.cantidad - 1]

    # BUSCAR UN PASAJERO DESDE EL TOPE
    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i

        return -1

    # MODIFICAR EL DESTINO Y EL ASIENTO
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento

        return True

    # ELIMINAR UN PASAJERO UTILIZANDO UNA PILA AUXILIAR
    def eliminar_por_numero(self, numero):
        auxiliar = MiPila(self.capacidad)
        eliminado = None

        while not self.esta_vacia():
            pasajero = self.desapilar()

            if pasajero.numero == numero:
                eliminado = pasajero
            else:
                auxiliar.apilar(pasajero)

        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())

        return eliminado

    # COPIAR LA PILA CONSERVANDO EL MISMO TOPE
    def copiar(self):
        nueva_pila = MiPila(self.capacidad)

        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])

        return nueva_pila

    # DEVOLVER LA CANTIDAD DE PASAJEROS
    def longitud(self):
        return self.cantidad

    # COMPROBAR SI LA PILA ESTÁ VACÍA
    def esta_vacia(self):
        return self.cantidad == 0