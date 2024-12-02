class Particion:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.proceso = None  # Proceso asignado a la partición

    def esta_libre(self):
        return self.proceso is None

    def asignar_proceso(self, proceso):
        if proceso.tamanio <= self.tamanio:
            self.proceso = proceso
            return True
        return False

    def liberar(self):
        self.proceso = None


class Proceso:
    def __init__(self, id_proceso, tamanio):
        self.id_proceso = id_proceso
        self.tamanio = tamanio


def administrar_memoria(particiones, procesos):
    print("Estado inicial de las particiones:")
    mostrar_estado(particiones)

    for proceso in procesos:
        asignado = False
        for particion in particiones:
            if particion.esta_libre() and particion.asignar_proceso(proceso):
                print(f"Proceso {proceso.id_proceso} (Tamaño: {proceso.tamanio}) asignado a partición de tamaño {particion.tamanio}")
                asignado = True
                break
        if not asignado:
            print(f"Proceso {proceso.id_proceso} (Tamaño: {proceso.tamanio}) no puede ser asignado. Espera o termina.")

    print("\nEstado final de las particiones:")
    mostrar_estado(particiones)


def mostrar_estado(particiones):
    for i, particion in enumerate(particiones):
        if particion.proceso:
            print(f"Partición {i+1} (Tamaño: {particion.tamanio}): Proceso {particion.proceso.id_proceso} (Tamaño: {particion.proceso.tamanio})")
        else:
            print(f"Partición {i+1} (Tamaño: {particion.tamanio}): Libre")


# Simulación
if __name__ == "__main__":
    # Crear particiones con tamaños fijos
    particiones = [Particion(100), Particion(200), Particion(300), Particion(400)]

    # Crear procesos con tamaños variables
    procesos = [
        Proceso(1, 90),
        Proceso(2, 200),
        Proceso(3, 150),
        Proceso(4, 350),
        Proceso(5, 50),
    ]

    # Administrar memoria
    administrar_memoria(particiones, procesos)