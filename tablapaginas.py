import random

class TablaPaginas:
    def __init__(self, num_paginas, num_marcos):
        self.num_paginas = num_paginas
        self.num_marcos = num_marcos
        self.tabla = [-1] * num_paginas  # Inicialmente, todas las páginas están sin asignar (-1)

    def asignar_marco(self, pagina, marco):
        if 0 <= pagina < self.num_paginas and 0 <= marco < self.num_marcos:
            self.tabla[pagina] = marco
            print(f"Página {pagina} asignada al marco {marco}")
        else:
            print("Error: Página o marco fuera de rango.")

    def acceder_pagina(self, pagina):
        if 0 <= pagina < self.num_paginas:
            marco = self.tabla[pagina]
            if marco != -1:
                print(f"Acceso exitoso: Página {pagina} está en el marco {marco}")
            else:
                print(f"Fallo de página: La página {pagina} no está en memoria.")
        else:
            print("Error: Página fuera de rango.")

    def mostrar_tabla(self):
        print("Tabla de páginas:")
        for i, marco in enumerate(self.tabla):
            estado = f"Marco {marco}" if marco != -1 else "No asignada"
            print(f"Página {i}: {estado}")


# Simulación
if __name__ == "__main__":
    num_paginas = 8
    num_marcos = 4

    # Crear tabla de páginas
    tabla_paginas = TablaPaginas(num_paginas, num_marcos)

    # Asignar algunas páginas a marcos
    tabla_paginas.asignar_marco(0, 0)
    tabla_paginas.asignar_marco(1, 1)
    tabla_paginas.asignar_marco(2, 2)
    tabla_paginas.asignar_marco(3, 3)

    # Mostrar estado inicial de la tabla
    print("\nEstado inicial:")
    tabla_paginas.mostrar_tabla()

    # Acceso aleatorio a páginas
    print("\nAccesos aleatorios:")
    for _ in range(5):
        pagina = random.randint(0, num_paginas - 1)
        tabla_paginas.acceder_pagina(pagina)

    # Mostrar estado final de la tabla
    print("\nEstado final:")
    tabla_paginas.mostrar_tabla()