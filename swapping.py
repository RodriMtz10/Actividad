class Proceso:
    def __init__(self, id_proceso, tamanio):
        self.id_proceso = id_proceso
        self.tamanio = tamanio

    def __str__(self):
        return f"Proceso {self.id_proceso} de tamaño {self.tamanio} MB"

class Memoria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.memoria = []
        self.ocupada = 0

    def agregar_proceso(self, proceso):
        if self.ocupada + proceso.tamanio <= self.capacidad:
            self.memoria.append(proceso)
            self.ocupada += proceso.tamanio
            print(f"{proceso} agregado a memoria.")
            return True
        else:
            print("Memoria llena, realizando swapping...")
            return self.realizar_swapping(proceso)

    def realizar_swapping(self, nuevo_proceso):
        if self.memoria:
            proceso_removido = self.memoria.pop(0)  # Elimina el primer proceso de la memoria
            self.ocupada -= proceso_removido.tamanio
            print(f"{proceso_removido} intercambiado a disco.")
            # Ahora intentamos agregar el nuevo proceso
            return self.agregar_proceso(nuevo_proceso)
        else:
            print("No hay espacio suficiente incluso después del intercambio.")
            return False

    def estado_memoria(self):
        if not self.memoria:
            print("Memoria vacía.")
        for proceso in self.memoria:
            print(proceso)

# Simulación
memoria_virtual = Memoria(500)  # Memoria total de 500MB

# Agregar procesos
memoria_virtual.agregar_proceso(Proceso(1, 100))  # Proceso 1 de 100MB
memoria_virtual.agregar_proceso(Proceso(2, 150))  # Proceso 2 de 150MB
memoria_virtual.agregar_proceso(Proceso(3, 200))  # Proceso 3 de 200MB

# Intentar agregar el Proceso 4 de 250MB
if not memoria_virtual.agregar_proceso(Proceso(4, 150)):
    print("No se pudo agregar el Proceso 4 por falta de espacio.")

# Mostrar el estado final de la memoria
print("\nEstado final de la memoria:")
memoria_virtual.estado_memoria()
