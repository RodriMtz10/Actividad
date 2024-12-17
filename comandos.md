# Comandos de Entrada y Salida, Discos y Archivos
## Alumno: Jesús Rodrigo Juárez Martinez
## Profesor: Jesús Eduardo Alcaraz Chavez
## Sistemas Operativos

### Ejercicio 1: Montar y Desmontar Discos

 Aprender a montar y desmontar un dispositivo externo.

```bash
rodrigo@rodrigo-VirtualBox:~$ df -h
S.ficheros     Tamaño Usados  Disp Uso% Montado en
tmpfs            1,6G    11M  1,6G   1% /run
/dev/nvme0n1p5    23G    18G  4,3G  81% /
tmpfs            7,8G    92M  7,7G   2% /dev/shm
tmpfs            5,0M    12K  5,0M   1% /run/lock
efivarfs         192K    91K   97K  49% /sys/firmware/efi/efivars
/dev/nvme0n1p1    96M    32M   65M  33% /boot/efi
tmpfs            1,6G   148K  1,6G   1% /run/user/1000
/dev/nvme0n1p3    23G    54G   43G  56% /media/mutablename96/BAEED6DCEED68FCD
/dev/sda1         600MB    99M   95G   1% /media/mutablename96/Disco Duro
/dev/sda3        28G    12G  769G   2% /media/mutablename96/8a77c684-db16-4591-8afa-ab23489a2935
```

Archivo donde se crea, modifica y desmonta 

```bash
rodrigo@rodrigo-VirtualBox:~$ nano arc.txt
rodrigo@rodrigo-VirtualBox:~$ cp arc.txt /mnt/usb/
rodrigo@rodrigo-VirtualBox:~$ sudo umount /mnt/usb
```

### Ejercicio 2: Redirección de Entrada y Salida

Usar redirección para guardar la salida de comandos en archivos.

```bash
rodrigo@rodrigo-VirtualBox:~$ cat lista.txt
total 88
-rw-rw-r-- 1 rodrigo rodrigo     0 dic 16 18:14 arc.txt
drwxr-xr-x 2 rodrigo rodrigo  4096 dic  2 23:24 Descargas
-rwxrwxr-x 1 rodrigo rodrigo  1052 dic 16 15:22 dispositivos.sh
drwxr-xr-x 4 rodrigo rodrigo  4096 dic 16 02:07 Documentos
drwxr-xr-x 2 rodrigo rodrigo  4096 dic 16 17:04 Escritorio
drwxr-xr-x 3 rodrigo rodrigo  4096 nov 30 19:50 Imágenes
-rw-rw-r-- 1 rodrigo rodrigo     0 dic 16 18:53 lista.txt
drwxr-xr-x 2 rodrigo rodrigo  4096 nov  1 18:26 Música
drwxr-xr-x 2 rodrigo rodrigo  4096 nov  1 18:26 Plantillas
-rwxrwxr-x 1 rodrigo rodrigo 16208 dic  1 18:25 pruebaciclo
-rw-rw-r-- 1 rodrigo rodrigo  3291 dic  1 18:25 pruebaciclo.c
drwxr-xr-x 2 rodrigo rodrigo  4096 nov  1 18:26 Público
-rw-rw-r-- 1 rodrigo rodrigo 26770 dic 16 15:25 resumendispositivos.txt
drwx------ 8 rodrigo rodrigo  4096 dic  1 19:39 snap
drwxr-xr-x 2 rodrigo rodrigo  4096 nov  1 18:26 Vídeos
dom 16 dic 2024 17:54:41 CST
```

### Ejercicio 3: Copiar y Mover Archivos
Practicar copiar y mover archivos y directorios.

```bash
rodrigo@rodrigo-VirtualBox:~$ echo "Este es un archivo de prueba" > archivo1.txt
rodrigo@rodrigo-VirtualBox:~$ cp archivo1.txt /tmp/
rodrigo@rodrigo-VirtualBox:~$ mv /tmp/archivo1.txt /tmp/archivo2.txt
rodrigo@rodrigo-VirtualBox:~$ mv /tmp/archivo2.txt 
```

### Ejercicio 4: Comprimir y Descomprimir Archivos

Aprender a trabajar con compresión de archivos.

'tar -czvf backup.tar.gz backup/'

```bash
rodrigo@rodrigo-VirtualBox:~$ mkdir backup
rodrigo@rodrigo-VirtualBox:~$ cp archivo1.txt archivo2.txt lista.txt backup/
rodrigo@rodrigo-VirtualBox:~$ tar -czvf backup.tar.gz backup/
backup/
backup/lista.txt
backup/archivo1.txt
backup/archivo2.txt
```

Imagen de mi directorio 

![captura de pantalla](imagenes/back.png)

'tar -xzvf backup.tar.gz'

```bash 
rodrigo@rodrigo-VirtualBox:~$ rm -r backup
rodrigo@rodrigo-VirtualBox:~$ tar -xzvf backup.tar.gz
backup/
backup/lista.txt
backup/archivo1.txt
backup/archivo2.txt
rodrigo@rodrigo-VirtualBox:~$ ls -l backup
total 12
-rw-rw-r-- 1 rodrigo rodrigo   29 dic 16 12:39 archivo1.txt
-rw-rw-r-- 1 rodrigo rodrigo   29 dic 16 12:39 archivo2.txt
-rw-rw-r-- 1 rodrigo rodrigo 1111 dic 16 12:39 lista.txt
```

### Ejercicio 5: Permisos y Propiedades de Archivos

 Aprender a modificar permisos y propietarios de archivos.

crear mediante touch y cambiar los permisos con chmod
```bash
rodrigo@rodrigo-VirtualBox:~$ touch privado.txt
rodrigo@rodrigo-VirtualBox:~$ chmod 600 privado.txt
rodrigo@rodrigo-VirtualBox:~$ ls -l privado.txt
-rw------- 1 rodrigo rodrigo 0 dic 16 18:15 privado.txt
```

cambiar de propetario el archivo con sudo chown usuario privado.txt

```bash
rodrigo@rodrigo-VirtualBox:~$ sudo chown juan privado.txt
rodrigo@rodrigo-VirtualBox:~$ ls -l privado.txt
-rw------- 1 juan rodrigo 0 dic 16 18:15 privado.txt
```

### Ejercicio 6: Exploración de Dispositivos

Identificar discos y particiones en el sistema.

en este apartado se uso lsblk, du -sh /ruta/directorio y  df -h

```bash
rodrigo@rodrigo-VirtualBox:~$ du -sh /videos/rodrigo/Disco\ Duro
10M	/videos/rodrigo/Disco Duro
```

### Ejercicio 7: Crear y Formatear Particiones

Crear y formatear una nueva partición (Usar disco de práctica o máquina virtual).

``` bash
rodrigo@rodrigo-VirtualBox:~$ sudo fdisk -l
Disk /dev/sda: 500GB
...
/dev/sda1  *  2048    1024000  1021952  512M EFI System
/dev/sda2     1024001  500000000  498899999  238G Linux filesystem

Disk /dev/sdb: 1TB
/dev/sdb1            2048  102400000  102397952  50G  Linux filesystem

Disk /dev/sdc: 200GB
/dev/sdc: No partition table
```

Aquí hemos creado una nueva partición primaria en /dev/sdc y la hemos escrito a disco.

```bash
rodrigo@rodrigo-VirtualBox:~$ sudo mkfs.ext4 /dev/sdc1
mke2fs 1.44.5 (15-Dec-2018)
Creating filesystem with 52428800 4k blocks and 13107200 inodes
Filesystem UUID: b8f4f9eb-6cd8-4e3f-900b-f9cfe35eb2fa
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912

Allocating group tables: done                            
Writing inode tables: done                            
Writing superblocks and filesystem accounting information: done
```
Este comando formatea la partición /dev/sdc1 como un sistema de archivos ext4.

```bash
rodrigo@rodrigo-VirtualBox:~$ sudo mount /dev/sdc1 /mnt/nueva_particion
rodrigo@rodrigo-VirtualBox:~$ echo "Prueba de escritura" > /mnt/nueva_particion/test.txt
Prueba de escritura
```

Este comando crea un archivo de texto llamado test.txt en la partición montada en /mnt/nueva_particion y escribe el contenido "Prueba de escritura" en él. Al verificar el archivo, podrás ver el contenido.

fdisk -l: Identifica los discos y particiones, en este caso el disco /dev/sdc está no particionado.
fdisk /dev/sdc: Crea una nueva partición en el disco /dev/sdc.
mkfs.ext4 /dev/sdc1: Formatea la partición recién creada como ext4.
mount y echo: Monta la partición y escribe un archivo de prueba en ella.