class MiCola:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    # AGREGAR UN PASAJERO AL FINAL
    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La cola está llena.")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("El número de pasajero ya existe.")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1

        return True

    # MOSTRAR LOS PASAJEROS DESDE EL FRENTE
    def listar(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return

        for i in range(self.cantidad):
            if i == 0:
                print(f"[{i}] {self.datos[i]} <- FRENTE")
            elif i == self.cantidad - 1:
                print(f"[{i}] {self.datos[i]} <- FINAL")
            else:
                print(f"[{i}] {self.datos[i]}")

    # RETIRAR EL PASAJERO DEL FRENTE
    def desencolar(self):
        if self.esta_vacia():
            return None

        pasajero = self.datos[0]

        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return pasajero

    # CONSULTAR EL FRENTE SIN ELIMINARLO
    def ver_frente(self):
        if self.esta_vacia():
            return None

        return self.datos[0]

    # BUSCAR UN PASAJERO DESDE EL FRENTE
    def buscar(self, numero):
        for i in range(self.cantidad):
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

    # ELIMINAR UN PASAJERO UTILIZANDO LA ROTACIÓN DE LA COLA
    def eliminar_por_numero(self, numero):
        eliminado = None
        cantidad_original = self.cantidad

        for i in range(cantidad_original):
            pasajero = self.desencolar()

            if pasajero.numero == numero:
                eliminado = pasajero
            else:
                self.encolar(pasajero)

        return eliminado

    # COPIAR LA COLA CONSERVANDO SU ORDEN
    def copiar(self):
        nueva_cola = MiCola(self.capacidad)

        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])

        return nueva_cola

    # DEVOLVER LA CANTIDAD DE PASAJEROS
    def longitud(self):
        return self.cantidad

    # COMPROBAR SI LA COLA ESTÁ VACÍA
    def esta_vacia(self):
        return self.cantidad == 0