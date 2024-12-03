# PREGUNTAS Y PROGRAMAS
### Alumno: Jesús Rodrigo Juárez Martienez
### Profesor: Jesús Eduardo Alcaraz Chavez
### Sistemas Operativos

## Administrador de Entrada/Salida

### 4.1 Dispositivos y manejadores de dispositivos

#### Diferencia entre Dispositivos de Bloque y Dispositivos de Carácter

En los sistemas operativos, los dispositivos se clasifican en **dispositivos de bloque** y **dispositivos de carácter**, dependiendo de cómo manejan los datos y cómo interactúan con el sistema.

##### Dispositivos de Bloque
##### Descripción:
Los dispositivos de bloque transfieren datos en bloques de tamaño fijo. Estos bloques suelen ser de varios cientos o miles de bytes y permiten el acceso aleatorio a los datos. Esto significa que se puede leer o escribir en cualquier posición del dispositivo sin necesidad de procesar secuencialmente los datos.

##### Ejemplo:
- **Disco duro (HDD), unidad de estado sólido (SSD)**: Los discos duros y SSD son ejemplos típicos de dispositivos de bloque. Los datos se dividen en sectores y se accede a ellos mediante direcciones específicas.

##### Características:
- Ofrecen acceso aleatorio.
- Ideales para almacenar sistemas de archivos.
- Suelen ser más rápidos al manejar grandes volúmenes de datos.

---

##### Dispositivos de Carácter
##### Descripción:
Los dispositivos de carácter transfieren datos byte a byte (o carácter a carácter). No permiten acceso aleatorio; los datos deben procesarse de forma secuencial.

##### Ejemplo:
- **Teclado**: Un teclado envía caracteres uno por uno a medida que se teclean, siendo un dispositivo de carácter típico.
- **Mouse**: Los datos de movimiento y clics se envían de forma secuencial.

##### Características:
- No permiten acceso aleatorio; los datos se procesan en flujo continuo.
- Usados para dispositivos que generan datos secuenciales, como entradas de usuario o sensores.

---

##### Diferencias Clave:
| **Aspecto**               | **Dispositivo de Bloque**            | **Dispositivo de Carácter**        |
|---------------------------|------------------------------------|-----------------------------------|
| **Acceso a datos**         | Acceso aleatorio                   | Acceso secuencial                 |
| **Tamaño de transferencia**| Bloques de tamaño fijo             | Byte a byte (carácter a carácter) |
| **Velocidad**              | Más rápidos en grandes volúmenes   | Más lentos                        |
| **Ejemplos**               | HDD, SSD, unidades USB             | Teclado, mouse, impresora         |

---

#### Programa en Python: Manejador de Dispositivos Sencillo para un Dispositivo Virtual de Entrada

Este programa implementa un manejador básico para un dispositivo virtual de entrada. Simula la recepción de datos del dispositivo y su procesamiento en el sistema.

##### Código en Python

```python
import time
import threading

class DispositivoEntrada:
    """
    Clase que simula un dispositivo de entrada.
    """

    def __init__(self):
        self.buffer = []  # Buffer para almacenar datos del dispositivo.
        self.lectura_activa = True  # Bandera para controlar la lectura de datos.

    def enviar_datos(self, datos):
        """
        Simula el envío de datos desde el dispositivo al buffer.
        """
        self.buffer.append(datos)
        print(f"Datos recibidos: {datos}")

    def detener(self):
        """
        Detiene la simulación de la entrada de datos.
        """
        self.lectura_activa = False


class ManejadorDispositivo:
    """
    Clase que actúa como manejador del dispositivo de entrada.
    """

    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def procesar_datos(self):
        """
        Procesa los datos recibidos del dispositivo.
        """
        while self.dispositivo.lectura_activa or self.dispositivo.buffer:
            if self.dispositivo.buffer:
                datos = self.dispositivo.buffer.pop(0)
                print(f"Procesando datos: {datos}")
            time.sleep(1)  # Simula el tiempo de procesamiento.


# Simulación
if __name__ == "__main__":
    # Crear el dispositivo de entrada virtual
    dispositivo = DispositivoEntrada()

    # Crear el manejador para el dispositivo
    manejador = ManejadorDispositivo(dispositivo)

    # Hilo para simular el envío de datos
    def simular_entrada():
        for i in range(5):
            dispositivo.enviar_datos(f"Input-{i}")
            time.sleep(2)  # Simula la entrada intermitente de datos
        dispositivo.detener()

    hilo_entrada = threading.Thread(target=simular_entrada)

    # Hilo para procesar datos
    hilo_procesamiento = threading.Thread(target=manejador.procesar_datos)

    # Iniciar hilos
    hilo_entrada.start()
    hilo_procesamiento.start()

    # Esperar a que ambos hilos terminen
    hilo_entrada.join()
    hilo_procesamiento.join()

    print("Simulación finalizada.")
```

##### Descripción del Programa
1. Clase DispositivoEntrada:

- Simula un dispositivo de entrada que envía datos de forma intermitente al sistema.
- Usa un buffer para almacenar temporalmente los datos recibidos.
- Permite detener la entrada de datos mediante una bandera.
2. Clase ManejadorDispositivo:

- Procesa los datos almacenados en el buffer.
- Simula un proceso continuo que verifica el  buffer y procesa los datos uno por uno.
3. Simulación con Hilos:

- Un hilo simula la entrada de datos al dispositivo.
- Otro hilo procesa los datos recibidos.
- Los hilos trabajan de manera concurrente para simular un flujo continuo de datos y procesamiento.

### 4.2 Mecanismos y funciones de los manejadores de los dispositivos 

#### Interrupción por E/S: Concepto y Ejemplo en Pseudocódigo

##### ¿Qué es una interrupción por E/S?

Una interrupción por E/S (Entrada/Salida) ocurre cuando un dispositivo de hardware (como un teclado, disco duro o impresora) requiere la atención del procesador para completar una operación. En lugar de que la CPU espere activamente a que el dispositivo termine, el sistema operativo utiliza interrupciones para ser notificado cuando el dispositivo está listo.

##### Proceso General
1. **Solicitud de E/S:** Una aplicación solicita realizar una operación de entrada/salida.
2. **Inicio de E/S:** El sistema operativo envía la solicitud al controlador del dispositivo.
3. **Interrupción:** Cuando el dispositivo termina la operación, genera una interrupción para notificar al procesador.
4. **Manejador de Interrupciones:** El sistema operativo ejecuta un programa especializado para gestionar la interrupción, procesa los datos y reanuda el proceso interrumpido.

##### Ventajas
- Reduce el tiempo de inactividad de la CPU.
- Mejora el rendimiento del sistema al permitir que la CPU trabaje en otras tareas mientras espera la E/S.

##### Ejemplo de Simulación en Pseudocódigo

```plaintext
# Inicialización de variables
ProcesoEnEjecucion = True
BufferDatos = []

# Simulación de un dispositivo de entrada
function GenerarInterrupcion():
    print("Interrupción de E/S generada.")
    BufferDatos.append("Dato recibido")
    ManejarInterrupcion()

# Manejador de la interrupción
function ManejarInterrupcion():
    print("Manejador de interrupción ejecutado.")
    if BufferDatos no está vacío:
        dato = BufferDatos.pop(0)
        print("Procesando:", dato)
    else:
        print("No hay datos que procesar.")

# Proceso principal
while ProcesoEnEjecucion:
    print("Proceso principal en ejecución.")
    Esperar(2) # Simula tiempo de procesamiento
    if EventoAleatorio():
        GenerarInterrupcion()

    if CondiciónDeParada():
        ProcesoEnEjecucion = False

print("Simulación terminada.")
```

##### Descripción del Ejemplo
Proceso principal: Representa el flujo principal del sistema.
Interrupción generada: Se simula un evento aleatorio que activa una interrupción.
Manejador de interrupciones: Gestiona el dato recibido, simulando el manejo de una operación de E/S.
Evento de parada: Finaliza la simulación cuando se cumple una condición.

#### Simulación de manejo de interrupciones en un sistema básico

Este programa en Python simula un sistema básico que utiliza el manejo de interrupciones. La simulación incluye procesos que ejecutan tareas y generan interrupciones de forma aleatoria para demostrar cómo el sistema responde a ellas.

##### Código en Python

```python
import time
import random

# Definir una lista de posibles interrupciones
INTERRUPCIONES = [
    "Teclado: Entrada de usuario",
    "Impresora: Trabajo completado",
    "Disco duro: Lectura completada",
    "Red: Paquete recibido"
]

def manejar_interrupcion(interrupcion):
    """
    Simula el manejo de una interrupción.
    """
    print(f"[INTERRUPCIÓN] Manejo de {interrupcion}")
    time.sleep(1)  # Simula el tiempo de manejo de la interrupción

def proceso_principal():
    """
    Simula el proceso principal que realiza tareas mientras atiende interrupciones.
    """
    print("Inicio del proceso principal...")
    for i in range(10):  # Simula 10 ciclos de ejecución
        print(f"Ejecutando tarea {i + 1}...")
        time.sleep(0.5)  # Simula tiempo de ejecución de una tarea

        # Simular aleatoriamente si ocurre una interrupción
        if random.random() < 0.3:  # 30% de probabilidad de interrupción
            interrupcion = random.choice(INTERRUPCIONES)
            manejar_interrupcion(interrupcion)

    print("El proceso principal ha terminado.")

if __name__ == "__main__":
    proceso_principal()
```

##### Explicación
1. Proceso principal: Simula un programa en ejecución que realiza tareas periódicas.
2. Interrupciones: Se generan de manera aleatoria con un 30% de probabilidad en cada ciclo.
3. Manejo de interrupciones: Cuando ocurre una interrupción, el sistema pausa su tarea principal, maneja la interrupción, y luego reanuda el trabajo.

### 4.3 Estructuras de datos para manejo de dispositivos

#### Cola de E/S y Simulación de Cola con Prioridad

##### ¿Qué es una cola de E/S?

Una **cola de E/S (Entrada/Salida)** es una estructura de datos utilizada por los sistemas operativos para gestionar las solicitudes de entrada/salida de manera eficiente. Cuando múltiples procesos requieren acceso a un dispositivo de E/S (como un disco duro o impresora), las solicitudes se organizan en una cola para procesarlas en orden. 

##### Características principales:
1. **Orden de llegada**: Las solicitudes suelen atenderse en el orden en que llegaron.
2. **Priorización**: Algunas colas permiten asignar prioridad a ciertas solicitudes, como procesos críticos que necesitan acceso inmediato.
3. **Eficiencia**: Ayuda a minimizar el tiempo de espera global y optimiza el uso del dispositivo.

##### Ejemplo real:
- **Sistema de discos duros**: Los discos modernos utilizan algoritmos como SCAN o SSTF que optimizan el acceso a sectores basándose en la posición actual del cabezal.

---

##### Simulación de una Cola de E/S con Prioridad

El siguiente programa simula una cola de E/S con prioridad en Python. En esta simulación:
- Las solicitudes de E/S tienen diferentes niveles de prioridad.
- Las solicitudes con mayor prioridad se atienden primero.

##### Código en Python

```python
import heapq

class SolicitudES:
    def __init__(self, prioridad, descripcion):
        self.prioridad = prioridad
        self.descripcion = descripcion

    def __lt__(self, other):
        return self.prioridad < other.prioridad

def agregar_solicitud(cola, prioridad, descripcion):
    """
    Agrega una solicitud de E/S a la cola con su prioridad.
    """
    solicitud = SolicitudES(prioridad, descripcion)
    heapq.heappush(cola, solicitud)
    print(f"Solicitud agregada: {descripcion} con prioridad {prioridad}")

def procesar_solicitudes(cola):
    """
    Procesa las solicitudes de E/S en orden de prioridad.
    """
    while cola:
        solicitud = heapq.heappop(cola)
        print(f"Procesando solicitud: {solicitud.descripcion} con prioridad {solicitud.prioridad}")

if __name__ == "__main__":
    # Cola de E/S (min-heap para manejar prioridades)
    cola_es = []

    # Agregar solicitudes a la cola
    agregar_solicitud(cola_es, 2, "Lectura de archivo")
    agregar_solicitud(cola_es, 1, "Escritura en disco")
    agregar_solicitud(cola_es, 3, "Impresión de documento")
    agregar_solicitud(cola_es, 0, "Atender señal de red")

    print("\nProcesando solicitudes de E/S:\n")
    # Procesar las solicitudes en orden de prioridad
    procesar_solicitudes(cola_es)
```
####

#### Explicación del código
1. **Estructura de la cola:**

- Se utiliza un heap (montículo) como estructura subyacente para garantizar que siempre se procese primero la solicitud con la prioridad más alta.
- La clase **SolicitudES** incluye un operador __lt__ para comparar prioridades.
2. **Agregar solicitudes:**

- Las solicitudes se añaden a la cola con heapq.heappush, manteniendo el orden por prioridad.
3. **Procesar solicitudes:**

- Se extraen en orden de prioridad con **heapq.heappop.**

#### Simulación de un manejador de dispositivos con tabla de estructuras

Este programa simula las operaciones de un manejador de dispositivos utilizando una tabla de estructuras para registrar información sobre cada dispositivo, incluyendo su estado y tipo. Se implementan funciones para registrar dispositivos, listar dispositivos activos e interactuar con ellos.

##### Código en Python

```python
class Dispositivo:
    def __init__(self, id_dispositivo, tipo, estado):
        self.id_dispositivo = id_dispositivo  # Identificador único
        self.tipo = tipo                      # Tipo de dispositivo (ej. entrada/salida)
        self.estado = estado                  # Estado (activo/inactivo)

    def activar(self):
        self.estado = "activo"

    def desactivar(self):
        self.estado = "inactivo"

    def __str__(self):
        return f"Dispositivo {self.id_dispositivo} ({self.tipo}) - Estado: {self.estado}"


class ManejadorDispositivos:
    def __init__(self):
        self.tabla_dispositivos = []  # Lista para almacenar dispositivos

    def registrar_dispositivo(self, id_dispositivo, tipo):
        nuevo_dispositivo = Dispositivo(id_dispositivo, tipo, "inactivo")
        self.tabla_dispositivos.append(nuevo_dispositivo)
        print(f"Dispositivo {id_dispositivo} registrado.")

    def listar_dispositivos(self):
        print("Tabla de dispositivos:")
        for dispositivo in self.tabla_dispositivos:
            print(dispositivo)

    def activar_dispositivo(self, id_dispositivo):
        for dispositivo in self.tabla_dispositivos:
            if dispositivo.id_dispositivo == id_dispositivo:
                dispositivo.activar()
                print(f"Dispositivo {id_dispositivo} activado.")
                return
        print(f"Dispositivo {id_dispositivo} no encontrado.")

    def desactivar_dispositivo(self, id_dispositivo):
        for dispositivo in self.tabla_dispositivos:
            if dispositivo.id_dispositivo == id_dispositivo:
                dispositivo.desactivar()
                print(f"Dispositivo {id_dispositivo} desactivado.")
                return
        print(f"Dispositivo {id_dispositivo} no encontrado.")


# Simulación
if __name__ == "__main__":
    manejador = ManejadorDispositivos()

    # Registrar dispositivos
    manejador.registrar_dispositivo(1, "entrada")
    manejador.registrar_dispositivo(2, "salida")
    manejador.registrar_dispositivo(3, "almacenamiento")

    # Listar dispositivos
    manejador.listar_dispositivos()

    # Activar y desactivar dispositivos
    manejador.activar_dispositivo(1)
    manejador.activar_dispositivo(3)
    manejador.listar_dispositivos()

    manejador.desactivar_dispositivo(1)
    manejador.listar_dispositivos()
```

##### Explicación del Programa

1. Clase Dispositivo:

- Define los atributos básicos del dispositivo (id_dispositivo, tipo, estado).
- Incluye métodos para activar y desactivar dispositivos.

2. Clase ManejadorDispositivos:

- Gestiona una tabla de dispositivos almacenada como una lista.
- Ofrece métodos para registrar, listar, activar y desactivar dispositivos.

3. Simulación:

- Se registran dispositivos de ejemplo con identificadores únicos.
- Se activan y desactivan dispositivos según las operaciones solicitadas.
- Se lista el estado actual de la tabla tras cada operación.

### 4.4 Operaciones Entrada/Salida

#### Proceso de Lectura de un Archivo desde un Disco Magnético

El flujo para la lectura de un archivo desde un disco magnético incluye las siguientes etapas principales:

1. **Solicitud de Archivo**: El sistema recibe una solicitud para acceder a un archivo específico.
2. **Traducción de la Dirección**: El sistema operativo convierte el nombre del archivo en una ubicación física en el disco.
3. **Acceso a la Tabla de Archivos**: Se consulta la tabla de asignación de archivos para identificar los bloques de disco que contienen el archivo.
4. **Movimiento del Brazo de Lectura**: El controlador del disco posiciona el cabezal de lectura en el cilindro correcto.
5. **Lectura de Bloques**: Se leen los sectores correspondientes y se transfieren al búfer de memoria principal.
6. **Entrega de Datos**: El sistema operativo pasa los datos al proceso que los solicitó.

---

##### Código en Python para Simular el Proceso

Este programa simula el proceso básico de lectura de un archivo utilizando estructuras como tablas de asignación y un disco virtual.

```python
class DiscoMagnetico:
    def __init__(self, bloques):
        self.bloques = bloques  # Lista que simula los bloques del disco
        self.tabla_asignacion = {}  # Tabla de asignación de archivos

    def crear_archivo(self, nombre, datos):
        if nombre in self.tabla_asignacion:
            print(f"El archivo {nombre} ya existe.")
            return

        if len(datos) > len(self.bloques):
            print("Espacio insuficiente en el disco.")
            return

        bloques_asignados = []
        for i, bloque in enumerate(self.bloques):
            if bloque is None and len(bloques_asignados) < len(datos):
                self.bloques[i] = datos[len(bloques_asignados)]
                bloques_asignados.append(i)

        self.tabla_asignacion[nombre] = bloques_asignados
        print(f"Archivo {nombre} creado con bloques: {bloques_asignados}")

    def leer_archivo(self, nombre):
        if nombre not in self.tabla_asignacion:
            print(f"El archivo {nombre} no existe.")
            return

        bloques_asignados = self.tabla_asignacion[nombre]
        datos = [self.bloques[bloque] for bloque in bloques_asignados]
        print(f"Archivo {nombre} leído: {''.join(datos)}")

    def mostrar_estado(self):
        print(f"Estado del disco: {self.bloques}")
        print(f"Tabla de asignación: {self.tabla_asignacion}")


# Simulación
if __name__ == "__main__":
    # Crear un disco magnético virtual con 10 bloques
    disco = DiscoMagnetico([None] * 10)

    # Crear archivos en el disco
    disco.crear_archivo("archivo1.txt", "HolaMundo")
    disco.crear_archivo("archivo2.txt", "Python")

    # Leer archivos del disco
    disco.leer_archivo("archivo1.txt")
    disco.leer_archivo("archivo2.txt")

    # Mostrar el estado actual del disco
    disco.mostrar_estado()
```

---

#### Explicación del Programa 
1. Clase DiscoMagnetico:
- Simula un disco magnético con bloques disponibles para almacenamiento.
- Administra una tabla de asignación que mapea los nombres de archivos a los bloques asignados.
2. Crear Archivo: 
- Busca bloques disponibles en el disco.
- Asigna los datos del archivo a esos bloques y actualiza la tabla de asignación.
3. Método leer_archivo:
- Accede a los bloques asignados a un archivo específico y reconstruye los datos.
4. Simulación:
- Crea archivos virtuales, simula su almacenamiento en el disco y realiza la lectura para mostrar los datos.

#### Operaciones de Entrada/Salida Asíncronas con Archivos en Python

En este ejemplo, se implementa un programa en Python que realiza operaciones de entrada/salida (E/S) asíncronas utilizando la biblioteca `asyncio` y `aiofiles`. El objetivo es demostrar cómo manejar la lectura y escritura de archivos de manera no bloqueante, lo que permite que otras tareas se ejecuten mientras se espera que las operaciones de E/S finalicen.

##### Requisitos
Asegúrate de tener instalada la biblioteca `aiofiles`, que se puede instalar usando:

```bash
pip install aiofiles
```

```python
import asyncio
import aiofiles

async def escribir_archivo(nombre_archivo, contenido):
    """Función asíncrona para escribir contenido en un archivo."""
    async with aiofiles.open(nombre_archivo, 'w') as archivo:
        await archivo.write(contenido)
        print(f"Escrito en el archivo {nombre_archivo}")

async def leer_archivo(nombre_archivo):
    """Función asíncrona para leer el contenido de un archivo."""
    async with aiofiles.open(nombre_archivo, 'r') as archivo:
        contenido = await archivo.read()
        print(f"Contenido del archivo {nombre_archivo}:")
        print(contenido)

async def main():
    """Función principal que coordina las operaciones asíncronas."""
    archivo = 'ejemplo.txt'
    
    # Realizar operaciones de escritura y lectura de manera asíncrona
    await escribir_archivo(archivo, "Hola, este es un archivo de ejemplo para operaciones asíncronas en Python.\n")
    await leer_archivo(archivo)

# Ejecutar el ciclo de eventos de asyncio
asyncio.run(main())
```
#### Explicación del Código
1. Bibliotecas Utilizadas:

- asyncio: Se utiliza para gestionar la ejecución de funciones asíncronas en Python.
- aiofiles: Proporciona una forma asíncrona de trabajar con archivos, lo que permite realizar operaciones de E/S sin bloquear el hilo principal.
2. Funciones Asíncronas:

- escribir_archivo: Escribe el contenido de forma asíncrona en el archivo especificado. La operación de escritura se realiza sin bloquear el programa principal.
- leer_archivo: Lee el contenido de un archivo de manera asíncrona y muestra el contenido en consola.
3. main:

- Orquesta las funciones escribir_archivo y leer_archivo utilizando await para esperar su finalización sin bloquear otras tareas que puedan ejecutarse.
4. Ciclo de Eventos:

- asyncio.run(main()): Inicia el ciclo de eventos de asyncio y ejecuta las funciones asíncronas.
---

### Integración
#### Algoritmo de Planificación de Discos "Elevator" (SCAN)

El algoritmo "Elevator" (también conocido como SCAN) es utilizado en la planificación de discos para manejar las solicitudes de acceso a los discos de manera eficiente. En este algoritmo, el cabezal del disco se mueve en una dirección, atendiendo las solicitudes en ese camino, y luego cambia de dirección cuando ya no quedan más solicitudes por atender en esa dirección. Su funcionamiento es similar al de un ascensor, de ahí su nombre.

#### Descripción del Algoritmo
1. Posición Inicial del Cabezal: El cabezal comienza en una posición inicial.
2. Dirección del Movimiento: El cabezal se mueve en una dirección (puede ser hacia la izquierda o hacia la derecha).
3. Servir Solicitudes: A medida que el cabezal se mueve, atiende las solicitudes que están en su camino.
4. Cambio de Dirección: Una vez que el cabezal ha llegado al extremo del disco, cambia de dirección y vuelve a atender las solicitudes en el camino opuesto.

``` python
def SCAN(arr, n, head, direction):
    # Ordenar las solicitudes de disco
    arr.sort()

    # Dividir las solicitudes en dos partes: antes y después del cabezal
    left = [i for i in arr if i < head]
    right = [i for i in arr if i >= head]

    # Mover el cabezal a la izquierda si la dirección es hacia la izquierda
    if direction == 0:
        # Procesar las solicitudes a la izquierda del cabezal
        for i in reversed(left):
            print(f"Atendiendo la solicitud: {i}")
        # Procesar las solicitudes a la derecha del cabezal
        for i in right:
            print(f"Atendiendo la solicitud: {i}")
    
    # Mover el cabezal a la derecha si la dirección es hacia la derecha
    elif direction == 1:
        # Procesar las solicitudes a la derecha del cabezal
        for i in right:
            print(f"Atendiendo la solicitud: {i}")
        # Procesar las solicitudes a la izquierda del cabezal
        for i in reversed(left):
            print(f"Atendiendo la solicitud: {i}")

def main():
    n = int(input("Ingrese el número de solicitudes de disco: "))
    arr = list(map(int, input("Ingrese las solicitudes de disco (separadas por espacios): ").split()))
    head = int(input("Ingrese la posición inicial del cabezal: "))
    direction = int(input("Ingrese la dirección de movimiento (0 para izquierda, 1 para derecha): "))

    SCAN(arr, n, head, direction)

if __name__ == "__main__":
    main()
```
---
#### Explicación del código:
1. Entrada de datos:

- El número de solicitudes y las posiciones de las solicitudes de disco se ingresan por el usuario.
- La posición inicial del cabezal y la dirección de movimiento (izquierda o derecha) también son ingresadas.
2. Ordenamiento de solicitudes:

- Se ordenan las solicitudes de disco en orden ascendente utilizando el método sort() de Python.
3. División de solicitudes:

- Se separan las solicitudes en dos listas: left para las solicitudes menores que la posición inicial del cabezal y right para las solicitudes mayores o iguales.
4. Procesamiento:

- Dependiendo de la dirección del cabezal (0 para izquierda o 1 para derecha), el algoritmo procesa las solicitudes primero en la dirección en que el cabezal se mueve.
- Después de llegar al final de la dirección, el cabezal invierte la dirección y procesa las solicitudes restantes en la otra dirección.

#### Código en Python para simular un sistema con múltiples dispositivos

En este diseño, utilizamos clases para representar cada dispositivo y un controlador central para gestionar la comunicación entre ellos. Los dispositivos pueden enviar solicitudes al controlador, y este último maneja esas solicitudes y decide qué dispositivo debe procesarlas en función de la disponibilidad.

``` python
import time
import random

class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "Libre"

    def solicitar_recurso(self):
        if self.estado == "Libre":
            self.estado = "En uso"
            print(f"{self.nombre} está en uso.")
        else:
            print(f"{self.nombre} está ocupado, esperando disponibilidad...")

    def liberar_recurso(self):
        self.estado = "Libre"
        print(f"{self.nombre} ha terminado de procesar la solicitud.")

class DiscoDuro(Dispositivo):
    def __init__(self):
        super().__init__("Disco Duro")

    def realizar_operacion(self):
        print("Accediendo al Disco Duro...")
        time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo de acceso al disco
        print("Operación en el Disco Duro completada.")

class Impresora(Dispositivo):
    def __init__(self):
        super().__init__("Impresora")

    def imprimir(self):
        print("Imprimiendo documento...")
        time.sleep(random.uniform(1, 2))  # Simula el tiempo de impresión
        print("Documento impreso.")

class Teclado(Dispositivo):
    def __init__(self):
        super().__init__("Teclado")

    def leer_entrada(self):
        print("Esperando entrada del teclado...")
        time.sleep(random.uniform(0.3, 0.8))  # Simula el tiempo de espera para la entrada
        entrada = random.choice(["Comando1", "Comando2", "Comando3"])
        print(f"Entrada del teclado: {entrada}")
        return entrada

class Controlador:
    def __init__(self):
        self.dispositivos = {
            "Disco Duro": DiscoDuro(),
            "Impresora": Impresora(),
            "Teclado": Teclado()
        }

    def manejar_solicitudes(self):
        while True:
            # Simulando la llegada de solicitudes
            dispositivo_seleccionado = random.choice(list(self.dispositivos.values()))

            if dispositivo_seleccionado.estado == "Libre":
                dispositivo_seleccionado.solicitar_recurso()

                # Realiza operaciones dependiendo del dispositivo seleccionado
                if isinstance(dispositivo_seleccionado, DiscoDuro):
                    dispositivo_seleccionado.realizar_operacion()
                elif isinstance(dispositivo_seleccionado, Impresora):
                    dispositivo_seleccionado.imprimir()
                elif isinstance(dispositivo_seleccionado, Teclado):
                    comando = dispositivo_seleccionado.leer_entrada()
                    if comando == "Comando1":
                        print("Ejecutando Comando1")
                    elif comando == "Comando2":
                        print("Ejecutando Comando2")
                    elif comando == "Comando3":
                        print("Ejecutando Comando3")

                dispositivo_seleccionado.liberar_recurso()

            time.sleep(random.uniform(1, 3))  # Simula el tiempo de espera entre solicitudes

# Crear el controlador y manejar las solicitudes
controlador = Controlador()
controlador.manejar_solicitudes()
```
---
#### Explicacion del codigo
1. Clases de Dispositivos:

- Dispositivo: Clase base para todos los dispositivos, con métodos para solicitar y liberar recursos.
- DiscoDuro: Subclase de Dispositivo, simula operaciones de un disco duro.
- Impresora: Subclase de Dispositivo, simula el proceso de impresión.
- Teclado: Subclase de Dispositivo, simula la lectura de entradas de un teclado.
2. Controlador:

- La clase Controlador gestiona las solicitudes de los dispositivos. Selecciona un dispositivo aleatorio y simula su uso, realizando la operación correspondiente (como leer desde el disco, imprimir o recibir entrada del teclado).
3. Flujo de Ejecución:

- El controlador maneja solicitudes en un bucle continuo. Selecciona aleatoriamente un dispositivo y ejecuta su operación si está disponible (es decir, si su estado es "Libre"). Después de procesar la solicitud, libera el recurso del dispositivo.
4. Simulación de Tiempos:

- Cada operación (acceso al disco, impresión o lectura de entrada) tiene un tiempo de espera simulado usando time.sleep(), lo que permite que el sistema "trabaje" durante un tiempo determinado antes de pasar al siguiente dispositivo.

---

### Avanzado

#### Explicación de como los sistemas operativos modernos optimizan las operaciones E/S con el uso de memoria caché

1. ¿Qué es la Memoria Caché?

- La memoria caché es una pequeña cantidad de memoria de acceso extremadamente rápido que se utiliza para almacenar datos temporales o información que se espera que se use nuevamente en un futuro cercano.
- En el contexto de E/S, la memoria caché puede ser utilizada para almacenar datos leídos de dispositivos de almacenamiento (como discos duros o SSD) o para guardar los datos que se están escribiendo en el dispositivo.
2.  Optimización de E/S mediante Caché: Los sistemas operativos optimizan las operaciones de E/S utilizando caché de diferentes maneras:

- Lecturas anticipadas: Cuando el sistema operativo predice que un bloque de datos será requerido en el futuro cercano, puede cargar ese bloque en la memoria caché antes de que realmente se haga la solicitud.
- Escrituras retrasadas: En lugar de escribir los datos de inmediato a un dispositivo, el sistema operativo los guarda en la memoria caché y los escribe en el dispositivo en lotes o de manera diferida. Esto reduce la cantidad de accesos a dispositivos lentos.
- Lecturas y escrituras optimizadas: Los sistemas operativos utilizan políticas para decidir cuándo almacenar datos en caché, cuánto tiempo mantener los datos en caché y cuándo liberar espacio para nuevos datos.
- Caché de disco: Los sistemas operativos modernos emplean algoritmos de caché de disco, como el algoritmo de reemplazo de caché LRU (Least Recently Used) para gestionar la memoria caché y mantener los datos más recientes o frecuentemente accedidos.
3. Beneficios del Uso de Memoria Caché en E/S:

- Mejor rendimiento: Al acceder a datos en la caché, el tiempo de respuesta es mucho más rápido en comparación con los accesos a dispositivos de almacenamiento más lentos.
- Reducción de la latencia: Las lecturas y escrituras se pueden realizar en la memoria caché rápidamente, lo que reduce la latencia en comparación con el acceso directo a dispositivos de almacenamiento.
- Mayor eficiencia en la utilización de recursos: La optimización del uso de la memoria y el almacenamiento reduce la cantidad de operaciones de E/S necesarias, lo que mejora la eficiencia general del sistema.

#### Implementación Simplificada de un Sistema de Caché en Python (Simulación)

``` python
import time
from collections import OrderedDict

class Cache:
    def __init__(self, size):
        self.cache = OrderedDict()
        self.size = size

    def get(self, key):
        """Obtiene un valor de la caché, si existe."""
        if key in self.cache:
            # Mueve el item a la última posición (más reciente)
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        """Añade un valor a la caché y maneja la política de reemplazo."""
        if key in self.cache:
            # Si ya existe, solo actualizamos el valor y lo movemos a la última posición
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.size:
            # Si la caché está llena, eliminamos el primer elemento (el menos recientemente usado)
            self.cache.popitem(last=False)
        self.cache[key] = value

    def display_cache(self):
        """Muestra el contenido actual de la caché."""
        print(self.cache)


class SistemaEntradaSalida:
    def __init__(self, cache_size=3):
        self.cache = Cache(cache_size)
        self.datos = {  # Simulando los datos del disco duro
            'file1': 'Contenido de file1',
            'file2': 'Contenido de file2',
            'file3': 'Contenido de file3',
            'file4': 'Contenido de file4',
            'file5': 'Contenido de file5'
        }

    def leer_archivo(self, nombre_archivo):
        """Simula la lectura de un archivo, con optimización de caché."""
        # Intentamos obtener el archivo de la caché
        cached_data = self.cache.get(nombre_archivo)
        if cached_data:
            print(f"Lectura desde la caché: {nombre_archivo}")
            return cached_data
        else:
            # Si no está en caché, lo leemos del "disco"
            print(f"Lectura desde el disco: {nombre_archivo}")
            time.sleep(1)  # Simulando el tiempo de acceso al disco
            data = self.datos[nombre_archivo]
            self.cache.put(nombre_archivo, data)  # Guardamos en la caché
            return data

    def escribir_archivo(self, nombre_archivo, contenido):
        """Simula la escritura de un archivo, con optimización de caché."""
        # Escribimos el archivo en la "caché"
        print(f"Escribiendo en la caché: {nombre_archivo}")
        self.cache.put(nombre_archivo, contenido)
        # Simulamos que la escritura al disco es más lenta
        time.sleep(1)
        print(f"Escritura en el disco: {nombre_archivo}")


# Crear un sistema con caché de tamaño 3
sistema = SistemaEntradaSalida()

# Realizando operaciones de E/S
sistema.leer_archivo('file1')  # Leer desde el disco
sistema.leer_archivo('file2')  # Leer desde el disco
sistema.leer_archivo('file1')  # Leer desde la caché

# Escribir en el sistema
sistema.escribir_archivo('file4', 'Nuevo contenido de file4')
sistema.leer_archivo('file4')  # Leer desde la caché
sistema.leer_archivo('file5')  # Leer desde el disco

# Ver el estado de la caché
sistema.cache.display_cache()
```

#### Explicación de la Implementación:
1. Cache (Clase Caché):

- La clase Cache simula una caché utilizando un OrderedDict para mantener el orden de los elementos. Los elementos más recientes se colocan al final del diccionario.
- Tiene los métodos get y put para acceder a los elementos de la caché y agregar nuevos elementos. Si la caché está llena, se elimina el elemento menos recientemente usado (LRU, Least Recently Used).
2. Sistema de Entrada/Salida:

- La clase SistemaEntradaSalida simula un sistema con una caché que maneja archivos. Tiene dos operaciones principales:
- Leer archivos: Primero verifica si el archivo está en la caché. Si no está, lo lee del "disco" y lo guarda en la caché.
- Escribir archivos: Guarda los archivos en la caché y luego simula la escritura en el disco.
3. Flujo de E/S:

- Al ejecutar el programa, se simula la lectura y escritura de archivos, mostrando si los datos provienen de la caché o del disco. También se visualiza el estado de la caché después de realizar operaciones.

## Bibliografia
### 4.1 Dispositivos y manejadores de dispositivos
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts*. Wiley.
- Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems*. Pearson.
- [Linux Documentation on Device Files](https://www.kernel.org/doc/html/latest/admin-guide/devices.html)

### 4.2 Macanismos y funciones de los manejadores de dispositivos 
1. **Documentación de Linux Kernel**  
   Sitio oficial del kernel de Linux con explicaciones sobre el manejo de interrupciones y drivers:  
   [https://www.kernel.org/doc/html/latest/](https://www.kernel.org/doc/html/latest/)

2. **Tutoriales en línea**  
   - [GeeksforGeeks: Interrupts in OS](https://www.geeksforgeeks.org/interrupts-in-operating-system/)  
   - [Tutorialspoint: Operating System - I/O System](https://www.tutorialspoint.com/operating_system/os_input_output.htm)

### 4.3 Estructuras de datos para manejo de dispositivos
1. **Heap Queue Algorithm (Heapq) Documentation**  
   Explica el funcionamiento y uso del módulo `heapq` en Python para manejar estructuras de datos basadas en montículos.  
   Fuente: [Python Documentation](https://docs.python.org/3/library/heapq.html)

2. **Priority Queue Data Structure**  
   Discusión detallada sobre colas de prioridad, sus implementaciones y aplicaciones.  
   Fuente: [GeeksforGeeks](https://www.geeksforgeeks.org/priority-queue-introduction/)

### Otras referencias utilizadas dentro del archivo

1. **Memoria Caché y Optimización de E/S**:
   - Patterson, D. A., & Hennessy, J. L. (2017). *Computer Organization and Design: The Hardware/Software Interface* (5th ed.). Elsevier.
   - Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.

2. **Sistemas Operativos y Caché**:
   - Tanenbaum, A. S. (2014). *Modern Operating Systems* (4th ed.). Prentice Hall.
   - Tanenbaum, A. S., & Woodhull, A. S. (2006). *Operating Systems: Design and Implementation* (3rd ed.). Prentice Hall.

3. **Algoritmos de Reemplazo de Caché**:
   - Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). *Data Structures and Algorithms in Python*. Wiley.
