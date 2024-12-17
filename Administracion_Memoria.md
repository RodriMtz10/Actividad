# PREGUNTAS Y PROGRAMAS
### Alumno: Jesús Rodrigo Juárez Martinez
### Profesor: Jesús Eduardo Alcaraz Chavez
### Sistemas Operativos

## Administración de Memoria

### 3.1 Política y filosofía

### ¿Cuál es la diferencia entre fragmentación interna y externa?

#### Fragmentación Interna
Ocurre cuando se asigna un bloque de memoria mayor al requerido por el proceso, dejando espacio desperdiciado dentro del bloque asignado.
Este espacio no utilizado reduce la eficiencia de uso de la memoria, ya que aunque está reservado, no puede ser utilizado por otros procesos.

#### Fragmentación Externa
Sucede cuando hay suficientes bloques libres de memoria para satisfacer una solicitud, pero no son contiguos, impidiendo su uso.
La memoria disponible se fragmenta en pedazos no utilizables, lo que limita la capacidad para alojar procesos grandes, incluso si la memoria total libre sería suficiente.

#### Comparación
| Característica          | Fragmentación Interna                      | Fragmentación Externa                      |
|-------------------------|--------------------------------------------|--------------------------------------------|
| **Ubicación del problema** | Dentro de los bloques asignados            | Entre los bloques asignados                |
| **Efecto principal**    | Espacio desperdiciado dentro de los bloques | Espacio libre no utilizable                |
| **Causa**               | Bloques asignados mayores al tamaño necesario | Bloques libres no contiguos                |

#### Soluciones
- **Para fragmentación interna**: Usar técnicas de asignación dinámica como bloques de tamaño variable o ajustar los tamaños de los bloques.
- **Para fragmentación externa**: Implementar estrategias como *compaction* (compactación) o el uso de esquemas de asignación como *paginación* o *segmentación*.

###     Políticas de Reemplazo de Páginas en Sistemas Operativos

Las políticas de reemplazo de páginas son estrategias empleadas por los sistemas operativos para decidir qué página de memoria se debe sustituir cuando ocurre una falla de página y la memoria está llena. Aquí se describen las principales políticas:

#### 1. FIFO (First-In, First-Out)
- **Descripción**: Reemplaza la página más antigua en la memoria.
- **Ventajas**: Es fácil de implementar.
- **Desventajas**: No considera el uso reciente de las páginas, lo que puede provocar la *anomalía de Bélády*, donde aumentar la memoria disponible incrementa las fallas de página.
- **Aplicación**: Adecuada para sistemas simples con patrones de acceso predecibles.
  
#### 2. LRU (Least Recently Used)
- **Descripción**: Sustituye la página que no ha sido utilizada durante más tiempo.
- **Ventajas**: Mejora el rendimiento al asumir que las páginas accedidas recientemente tienen más probabilidades de volver a usarse.
- **Desventajas**: Requiere recursos adicionales para rastrear el acceso reciente de las páginas.
- **Aplicación**: Utilizada en sistemas donde el costo computacional es aceptable.

#### 3. LFU (Least Frequently Used)
- **Descripción**: Reemplaza la página que ha sido utilizada con menor frecuencia en un periodo dado.
- **Ventajas**: Beneficia a las páginas frecuentemente accedidas.
- **Desventajas**: Puede retener páginas que no se volverán a usar, si tuvieron accesos intensivos en el pasado.
- **Aplicación**: Útil en sistemas con datos cuya frecuencia de uso es estable.

#### 4. OPT (Optimal)
- **Descripción**: Sustituye la página que no será utilizada por el periodo más largo en el futuro.
- **Ventajas**: Es teóricamente el más eficiente.
- **Desventajas**: Impracticable en la realidad, ya que requiere conocimiento del acceso futuro a las páginas.
- **Aplicación**: Usado como referencia para comparar otras políticas.

#### 5. CLOCK
- **Descripción**: Aproximación de LRU que utiliza un "puntero" circular y bits de referencia para determinar la página a reemplazar.
- **Ventajas**: Es simple y eficiente, con bajo costo computacional.
- **Desventajas**: Menor precisión que LRU puro.
- **Aplicación**: Común en sistemas con recursos limitados.

#### Comparación y Eficiencia

| Política | Eficiencia Teórica | Complejidad de Implementación | Uso Común |
|----------|---------------------|------------------------------|-----------|
| FIFO     | Baja                | Baja                         | Sistemas simples |
| LRU      | Alta                | Alta                         | Sistemas modernos |
| LFU      | Media               | Media                        | Datos estables |
| OPT      | Máxima              | Impracticable                | Referencia |
| CLOCK    | Media               | Baja                         | Sistemas limitados |

#### Conclusión
- **Más eficiente en teoría**: **OPT**, pero es inalcanzable en la práctica.
- **Mejor equilibrio en sistemas reales**: **LRU**, ya que predice mejor el uso de páginas futuras, aunque con un costo computacional mayor.
- **Alternativa eficiente y simple**: **CLOCK**, ideal para sistemas con restricciones de recursos.

### 3.2 Memoria Real

### Simulación de Administración de Memoria con Particiones Fijas en Python



#### Código en Python

```python
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
```

#### Explicación del Código
##### Clases

**Particion:** Representa una partición fija con un tamaño y un estado (libre u ocupado).
**Proceso:** Representa un proceso con un identificador y un tamaño.
##### Métodos principales:

**asignar_proceso:** Asigna un proceso a la partición si el tamaño del proceso es menor o igual al tamaño de la partición.
**liberar:** Libera la partición, dejándola disponible.
##### Simulación

Se crean particiones y procesos.
Se intenta asignar cada proceso a la primera partición disponible que cumpla con el requisito de tamaño.
Se muestra el estado inicial y final de las particiones.

### Algoritmo de Primera Cabida para Asignación de Memoria

El algoritmo de **Primera Cabida** asigna procesos a la primera partición de memoria que sea lo suficientemente grande para alojarlos. A continuación, se presenta un algoritmo diseñado en Python para calcular qué procesos pueden ser asignados en un sistema con memoria real limitada:

#### Descripción del Algoritmo

1. **Entrada**: 
   - Una lista de particiones de memoria, cada una con un tamaño fijo.
   - Una lista de procesos con sus respectivos tamaños.

2. **Proceso**:
   - Recorre los procesos en orden.
   - Para cada proceso, busca la primera partición que esté libre y cuyo tamaño sea mayor o igual al tamaño del proceso.
   - Si se encuentra una partición adecuada, asigna el proceso a esa partición.
   - Si no se encuentra una partición, marca el proceso como "no asignado".

3. **Salida**:
   - El estado final de las particiones, indicando qué procesos han sido asignados.
   - Una lista de procesos no asignados.

#### Implementación en Python

```python
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

```

### 3.3 Organización de memoria virtual

### Paginación y Segmentación en Sistemas Operativos

#### Concepto de Paginación
La **paginación** es una técnica de administración de memoria que divide tanto la memoria física como la memoria lógica en bloques de tamaño fijo llamados *marcos* y *páginas*, respectivamente. Cada proceso tiene su propio espacio de direcciones dividido en páginas, que se mapean a marcos de memoria física mediante una tabla de páginas.

#### Ventajas de la Paginación
1. **Elimina fragmentación externa**: Dado que los marcos son de tamaño fijo, no hay problemas de fragmentación externa.
2. **Acceso rápido**: Permite acceso rápido a los datos mediante tablas de páginas.
3. **Flexibilidad**: Permite cargar diferentes partes de un proceso en ubicaciones no contiguas en memoria física.
4. **Facilidad de swapping**: Es más sencillo intercambiar páginas en memoria secundaria (disco) gracias a su tamaño fijo.

#### Desventajas de la Paginación
1. **Fragmentación interna**: Si un proceso no utiliza completamente un marco, el espacio restante se desperdicia.
2. **Sobrecarga**: Se necesita memoria adicional para las tablas de páginas.
3. **Latencia**: La búsqueda de direcciones físicas puede ser más lenta debido al mapeo entre páginas y marcos.

---

#### Concepto de Segmentación
La **segmentación** divide la memoria en segmentos lógicos de diferentes tamaños, como *código*, *datos* y *pilas*. Cada segmento tiene un tamaño variable y se administra de forma independiente, con un inicio y un límite definido en la memoria física.

#### Ventajas de la Segmentación
1. **Organización lógica**: Facilita la representación lógica de programas y datos.
2. **Compartición de memoria**: Permite que segmentos específicos sean compartidos entre procesos, como bibliotecas.
3. **Crecimiento dinámico**: Los segmentos pueden crecer según sea necesario, si hay espacio disponible.

#### Desventajas de la Segmentación
1. **Fragmentación externa**: La asignación de segmentos de tamaño variable puede dejar espacios libres pequeños e inutilizables en memoria.
2. **Complejidad**: Es más compleja de implementar debido a la necesidad de manejar segmentos de diferentes tamaños.
3. **Sobrecarga de administración**: Se requiere información adicional para gestionar la tabla de segmentos.

---

#### Comparación

| Característica            | Paginación                  | Segmentación                |
|---------------------------|-----------------------------|-----------------------------|
| **Tamaño de bloques**     | Fijo (páginas y marcos)     | Variable (segmentos)        |
| **Fragmentación**         | Interna                    | Externa                     |
| **Organización**          | Física                     | Lógica                      |
| **Facilidad de uso**      | Más simple                 | Más intuitiva para el programador |
| **Sobrecarga**            | Tablas de páginas          | Tablas de segmentos         |

---

#### Conclusión
- La **paginación** es eficiente para sistemas que requieren un manejo rápido y uniforme de la memoria, aunque con desperdicio potencial por fragmentación interna.
- La **segmentación** es ideal para sistemas que necesitan organización lógica y flexibilidad, pero sufre de fragmentación externa y mayor complejidad.

La elección entre estas técnicas depende del contexto del sistema operativo y los requisitos de los programas que se ejecutan.

### Simulación de una Tabla de Páginas

El siguiente programa simula una tabla de páginas para procesos en un sistema con memoria virtual. La tabla de páginas mapea direcciones virtuales a marcos de memoria física, y se permite un acceso aleatorio a las páginas.

#### Código

```python
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
```

### 3.4 Administración de memoria virtual

#### Implementación del Algoritmo de Reemplazo de Página "Least Recently Used" (LRU)

El algoritmo LRU se utiliza en sistemas operativos para administrar la memoria caché o la memoria virtual. Este algoritmo reemplaza la página que no se ha utilizado durante el mayor tiempo en un conjunto de páginas cargadas.

#### Código

```python
def lru_replacement(paginas, marcos):
    """
    Simula el algoritmo de reemplazo de páginas LRU.
    
    :param paginas: Lista de referencias a páginas.
    :param marcos: Número de marcos disponibles en memoria.
    """
    memoria = []  # Lista para simular los marcos de páginas
    fallos = 0  # Contador de fallos de página

    for pagina in paginas:
        if pagina not in memoria:
            # Si la página no está en memoria, ocurre un fallo de página
            if len(memoria) < marcos:
                # Si hay espacio disponible, simplemente añadimos la página
                memoria.append(pagina)
            else:
                # Reemplazamos la página menos recientemente usada
                memoria.pop(0)
                memoria.append(pagina)
            fallos += 1
            print(f"Fallo de página: {pagina} cargada -> {memoria}")
        else:
            # Si la página está en memoria, la actualizamos como más recientemente usada
            memoria.remove(pagina)
            memoria.append(pagina)
            print(f"Acceso exitoso: {pagina} -> {memoria}")

    print(f"\nNúmero total de fallos de página: {fallos}")


# Simulación
if __name__ == "__main__":
    # Lista de referencias a páginas
    paginas = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    # Número de marcos disponibles
    marcos = 3

    print("Simulación del algoritmo LRU:\n")
    lru_replacement(paginas, marcos)
```
### Diagrama: Proceso de Traducción de Direcciones Virtuales a Físicas

El proceso de traducción de direcciones virtuales a físicas en un sistema con memoria virtual incluye las siguientes etapas principales:

1. **Solicitud del Procesador**: El procesador genera una dirección virtual (VA) que necesita ser traducida a una dirección física (PA).
2. **Búsqueda en la TLB (Translation Lookaside Buffer)**: Se verifica si la dirección virtual está en la TLB.
   - Si hay un *acierto* en la TLB, se devuelve la dirección física correspondiente.
   - Si ocurre un *fallo*, se consulta la tabla de páginas en memoria principal.
3. **Consulta a la Tabla de Páginas**: 
   - La tabla de páginas contiene el mapeo de las direcciones virtuales a las físicas.
   - Si el marco correspondiente no está en memoria (fallo de página), se invoca el manejador de fallos de página.
4. **Carga del Marco en Memoria**: Si ocurrió un fallo de página:
   - Se selecciona un marco libre (o se reemplaza uno según el algoritmo de reemplazo).
   - Se actualiza la tabla de páginas con el marco asignado.
5. **Traducción Final**: 
   - La dirección virtual se traduce a física usando el marco recuperado.
   - La TLB se actualiza con esta nueva entrada para futuros accesos.

El diagrama a continuación ilustra este flujo:

```plaintext
+-------------------+         +-----------------+
| Dirección Virtual |         | Tabla de Páginas|
+-------------------+         +-----------------+
           |                           |
           v                           v
  +----------------+       +---------------------+
  | Verificar TLB  | ----> | Fallo de Página?    |
  +----------------+       +---------------------+
           |                           |
  +--------+---------+     +-----------+---------+
  | Acierto en TLB   |     | No (Marco en Memoria)|
  +--------+---------+     +-----------+---------+
           |                           |
           v                           |
+-------------------+         +-----------------+
| Dirección Física  |         | Manejador de Fallos|
+-------------------+         +-----------------+
                                      |
                             +--------+--------+
                             | Selección/Reemplazo|
                             | Actualizar Tabla  |
                             +-------------------+
                                      |
                              +-----------------+
                              | Marco en Memoria|
                              +-----------------+
```

## Implementacion
### Administración de Memoria Virtual en Sistemas Operativos Modernos

#### Linux

Linux utiliza una arquitectura avanzada de gestión de memoria virtual basada en diversas técnicas diseñadas para optimizar el uso de recursos:

1. **Segmentación y Paginación**  
   Linux combina paginación jerárquica y segmentación, asignando a cada proceso un espacio de direcciones virtuales dividido en páginas. Las páginas solo se cargan en memoria física cuando son necesarias (*demand paging*).

2. **MMU (Unidad de Gestión de Memoria)**  
   La MMU traduce direcciones virtuales a físicas mediante tablas de páginas gestionadas por el kernel. Estas tablas incluyen:
   - *Page Global Directory*: Mapea bloques grandes de memoria.
   - Tablas de segundo y tercer nivel para mapear páginas más específicas.

3. **Algoritmos de Reemplazo**  
   Linux emplea una versión optimizada del algoritmo *Least Recently Used (LRU)*, conocida como *Clock Algorithm*. Además, introduce mejoras como *Multi-Gen LRU*, diseñado para entornos de alta carga.

4. **Memoria Compartida y Copy-On-Write (COW)**  
   Permite que procesos compartan páginas de memoria. Las copias físicas solo se crean cuando uno de los procesos modifica los datos.

5. **Swapping**  
   Si la memoria física está llena, Linux usa espacio en disco (*swap*) para almacenar páginas menos utilizadas, liberando memoria para procesos activos.

---

#### Windows

Windows también implementa un sistema robusto de memoria virtual con características similares pero con enfoques específicos:

1. **Paginación Basada en Demanda**  
   Asigna páginas de memoria virtual y las carga en memoria física solo cuando se acceden.

2. **Estructuras de Datos**  
   Usa *Page Tables* y *Page Frame Number Database* para gestionar la traducción entre direcciones virtuales y físicas.

3. **Reemplazo de Páginas**  
   Windows aplica políticas adaptativas basadas en variantes de LRU. Selecciona páginas para reemplazo según patrones de acceso y carga de trabajo.

4. **Working Sets**  
   Cada proceso tiene un conjunto de trabajo (*Working Set*), que es la cantidad de memoria activa asignada. Este conjunto puede ajustarse dinámicamente según las necesidades del sistema.

5. **Swapping y Archivos de Paginación**  
   Windows usa archivos de paginación en disco para manejar escenarios de memoria insuficiente, distribuyendo la carga entre múltiples discos si es necesario.

---

#### Conclusión

Ambos sistemas operativos optimizan la memoria virtual para entornos multiusuario y multitarea. Linux sobresale en entornos abiertos y personalizables, mientras que Windows es eficiente en escenarios empresariales y de usuario final con configuraciones predefinidas.

---

### Simulación de Swapping de Procesos en Memoria Virtual en Java

En esta simulación, implementamos un algoritmo básico de swapping de procesos en memoria virtual utilizando Java. El objetivo es emular el intercambio de procesos entre la memoria principal (RAM) y el disco (swapping), un concepto clave en sistemas operativos para gestionar la memoria virtual.

#### Código en Java

```java
import java.util.LinkedList;
import java.util.Queue;

class Proceso {
    int id;
    int tamanio;

    public Proceso(int id, int tamanio) {
        this.id = id;
        this.tamanio = tamanio;
    }
}

class Memoria {
    int capacidad;
    Queue<Proceso> procesos;

    public Memoria(int capacidad) {
        this.capacidad = capacidad;
        this.procesos = new LinkedList<>();
    }

    public boolean agregarProceso(Proceso proceso) {
        int espacioNecesario = proceso.tamanio;
        int espacioUsado = 0;

        for (Proceso p : procesos) {
            espacioUsado += p.tamanio;
        }

        if (espacioUsado + espacioNecesario <= capacidad) {
            procesos.add(proceso);
            System.out.println("Proceso " + proceso.id + " asignado a memoria.");
            return true;
        } else {
            return false;
        }
    }

    public void hacerSwapping(Proceso proceso) {
        if (!agregarProceso(proceso)) {
            System.out.println("Memoria llena, realizando swapping...");

            // Eliminar el primer proceso (simulando el swap)
            Proceso procesoEliminado = procesos.poll();
            System.out.println("Proceso " + procesoEliminado.id + " intercambiado a disco.");
            
            // Luego agregar el nuevo proceso
            agregarProceso(proceso);
        }
    }

    public void mostrarEstado() {
        System.out.println("Estado actual de la memoria:");
        for (Proceso p : procesos) {
            System.out.println("Proceso " + p.id + " de tamaño " + p.tamanio);
        }
    }
}

public class SwappingSimulacion {

    public static void main(String[] args) {
        // Crear memoria con capacidad para 500 unidades
        Memoria memoria = new Memoria(500);

        // Crear procesos
        Proceso p1 = new Proceso(1, 100);
        Proceso p2 = new Proceso(2, 150);
        Proceso p3 = new Proceso(3, 200);
        Proceso p4 = new Proceso(4, 300); // Este no cabe

        // Agregar procesos
        memoria.hacerSwapping(p1);
        memoria.hacerSwapping(p2);
        memoria.hacerSwapping(p3);
        memoria.hacerSwapping(p4);  // Este debería realizar un swapping
        memoria.mostrarEstado();
    }
}
```
### Simulación de Swapping de Procesos en Memoria Virtual en Python

Este programa simula el proceso de swapping de procesos en memoria virtual. En un sistema operativo, el swapping permite mover procesos entre la memoria principal (RAM) y el disco cuando la memoria RAM está llena. Este mecanismo ayuda a optimizar el uso de la memoria, cargando procesos solo cuando hay espacio disponible.

#### Código en Python

```python
from collections import deque

class Proceso:
    def __init__(self, id_proceso, tamanio):
        self.id = id_proceso
        self.tamanio = tamanio

class Memoria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.procesos = deque()
        self.uso_memoria = 0

    def agregar_proceso(self, proceso):
        if self.uso_memoria + proceso.tamanio <= self.capacidad:
            self.procesos.append(proceso)
            self.uso_memoria += proceso.tamanio
            print(f"Proceso {proceso.id} agregado a memoria.")
            return True
        else:
            return False

    def hacer_swapping(self, proceso):
        if not self.agregar_proceso(proceso):
            print("Memoria llena, realizando swapping...")

            # Simulando el swapping, eliminamos el primer proceso
            proceso_eliminado = self.procesos.popleft()
            self.uso_memoria -= proceso_eliminado.tamanio
            print(f"Proceso {proceso_eliminado.id} intercambiado a disco.")

            # Ahora agregamos el nuevo proceso
            self.agregar_proceso(proceso)

    def mostrar_estado(self):
        print("Estado actual de la memoria:")
        for p in self.procesos:
            print(f"Proceso {p.id} de tamaño {p.tamanio} MB")

def main():
    # Crear memoria con capacidad de 500 MB
    memoria = Memoria(500)

    # Crear procesos de diferentes tamaños
    p1 = Proceso(1, 100)
    p2 = Proceso(2, 150)
    p3 = Proceso(3, 200)
    p4 = Proceso(4, 250)  # Este proceso no cabrá

    # Intentar agregar los procesos a la memoria
    memoria.hacer_swapping(p1)
    memoria.hacer_swapping(p2)
    memoria.hacer_swapping(p3)
    memoria.hacer_swapping(p4)  # Este debería realizar un swapping
    memoria.mostrar_estado()

if __name__ == "__main__":
    main()
```

# Bibliografia

### 3.1 Politica y filosofía 
- "Operating System Concepts" de Abraham Silberschatz, Peter B. Galvin, y Greg Gagne.
- "Modern Operating Systems" de Andrew S. Tanenbaum y Herbert Bos.
- Recursos educativos en línea, como tutoriales de sistemas operativos disponibles en sitios como GeeksforGeeks y TutorialsPoint.

- [Aprendiendo Algoritmos de Reemplazo de Páginas – Alegsa](https://www.alegsa.com.ar/Dic/Algoritmo_de_reemplazo_de_paginas.php)&#8203;
- [Explicación de Políticas de Reemplazo – TutorialsPoint](https://www.tutorialspoint.com/operating_system/os_virtual_memory.htm)&#8203;
- Documentación general sobre sistemas operativos y gestión de memoria.

### 3.3 segmentación y paginación

- **"Segmentación en Sistema Operativo"** - Barcelona Geeks.  
   Explica cómo la segmentación divide los programas en bloques lógicos, sus ventajas y desventajas, y su uso en sistemas modernos.  
   [Consulta aquí](https://barcelonageeks.com/segmentacion-sistema-operativo)  

- **"Paginación y Segmentación de un Sistema Operativo"** - paoguaman.blogspot.com.  
   Detalla los conceptos de paginación y segmentación, sus beneficios, desventajas, y el uso combinado en sistemas operativos.  
   [Consulta aquí](http://paoguaman.blogspot.com/paginacion-y-segmentacion)

### 3.4 Administracion de memoria virtual 
1. Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th Edition). Pearson.  
   - Este libro clásico en sistemas operativos detalla conceptos fundamentales como la traducción de direcciones y el manejo de memoria virtual.

2. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th Edition). Wiley.  
   - Aborda de manera clara y profunda temas como la traducción de direcciones, tablas de páginas, TLB, y algoritmos de reemplazo.

3. Stallings, W. (2017). *Operating Systems: Internals and Design Principles* (9th Edition). Pearson.  
   - Proporciona diagramas explicativos y ejemplos prácticos sobre la gestión de memoria virtual.

4. Conceptos básicos de memoria virtual y tablas de páginas. Obtenido de [GeeksforGeeks](https://www.geeksforgeeks.org/).  
   - Una referencia útil para algoritmos como LRU y el flujo general del manejo de memoria.

5. Ejemplos de diagramas de traducción de direcciones virtuales. Tomado de [TutorialsPoint](https://www.tutorialspoint.com/).  
   - Explica gráficamente el flujo de procesos en memoria virtual. 

### Implementacion 

1. **Silberschatz, A., Galvin, P. B., & Gagne, G. (2014).** *Operating System Concepts* (9th ed.). Wiley.  
   Este libro es una de las principales fuentes académicas sobre sistemas operativos, cubriendo conceptos fundamentales de administración de memoria, paginación, segmentación, y algoritmos de reemplazo de páginas. Es utilizado ampliamente en cursos de sistemas operativos y ofrece una comprensión detallada de las técnicas de gestión de memoria en sistemas como Linux y Windows.

2. **Tanenbaum, A. S., & Bos, H. (2014).** *Modern Operating Systems* (4th ed.). Pearson.  
   Tanenbaum y Bos proporcionan una explicación clara sobre los principios detrás de la memoria virtual, la paginación, la segmentación y el manejo de la memoria en sistemas operativos modernos, haciendo hincapié en cómo Linux y Windows gestionan estos recursos.

3. **Love, R. (2010).** *Linux Kernel Development* (3rd ed.). Addison-Wesley Professional.  
   Este libro se centra en los aspectos técnicos del kernel de Linux, detallando cómo maneja la memoria virtual, el proceso de paginación, y la implementación de swap en Linux. Es una referencia esencial para entender la arquitectura interna de este sistema operativo.

4. **Microsoft Docs. (2023).** *Memory Management in Windows*.  
   La documentación oficial de Microsoft proporciona una descripción exhaustiva de cómo Windows maneja la memoria virtual. Incluye detalles sobre las tablas de páginas, el uso de archivos de paginación, y las técnicas de reemplazo de páginas que optimizan el rendimiento del sistema. [Enlace](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/memory-management)

5. **Linux Documentation Project. (2023).** *Memory Management in the Linux Kernel*.  
   Este es un recurso clave que ofrece una comprensión profunda sobre cómo Linux maneja la memoria virtual, la paginación, y la técnica de swapping. La documentación oficial del kernel proporciona los detalles técnicos y las mejores prácticas para administrar recursos de memoria en sistemas Linux. [Enlace](https://www.kernel.org/doc/Documentation/vm/)
