#The proc File System

Podemos decir que Linux tiene dos funciones: controla el acceso a los dispositivos de la computadora y planificar cuándo y como un proceso interactúa con esos dispositivos.

El directorio /proc/ y también llamado proc file system, contiene la jerarquía de los ficheros los cuales representan el actual estado del kernel. Permitiendo a las aplicaciones y usuarios interactuar con la visión del kernel del sistema.

Dentro del /proc/, se puede encontrar una gran cantidad de información bien detallada del HW de sistema y otros procesos que están ejecutándose en el momento. Algunos de estos ficheros dentro del /proc/ pueden ser manipulados por usuarios y aplicaciones para comunicar cambios de configuración al kernel.

##Un Sistema de Ficheros Virtual (VFS)

En Linux TODOS LOS DATOS SE GUARDAN EN FICHEROS (TODO ES UN FICHERO). De los cuales hay dos tipos: texto y binario.
Pero /proc/ tiene otro tipo de fichero, llamado "fichero virtual". Por eso se llama VFS.

- Hay mucho que tienen muchas cualidades, por ejemplo, cero bytes de tamaño
- Otros tienen una gran cantidad de información.
- Hay que tener en cuenta que están constantemente actualizados.

Ficheros virtuales como /proc/interrupts, /proc/meminfo/, /proc/mounts, /proc/partitions proveen una información del HW del sistema al momento.

Otros como el /proc/filesystems y /proc/sys/ proveen información sobre la configuración e interfaces.

El /proc/ tiene una jerarquí de directorios y subdirectorios especial.

## Visualización

Utilizaremos cat, more o less.

$ cat /proc/cpuinfo

Esta información se puede ver, pero hay mucha información que no puede ser entendida por un ser humano, así que, existen otros comandos que estandarizan la salida: 
$ lspci # dispositivos PCI
$ apm # no está implementado (sudo apt-get install apmd)
$ free
$ top
$ htop

##Cambiando ficheros virtuales

$ echo www.example.com > /proc/sys/kernel/hostname 

El directorio /proc/sys sirve para cambiar parámetros.

Algunos ficheros están en binario y dan un 0 o un 1. El siguiente devuelve un 1 si esta ip_foward = on	

$ cat /proc/sys/net/ipv4/ip_forward 

###Nota: 

Utilizar sysctl para ver todas las configuraciones

##Top-level Files dentro del /proc

### buddyinfo

Este archivo se utiliza principalmente para diagnosticar problemas de fragmentaci�n de memoria. Utilizando el algoritmo buddy, cada columna representa el número de páginas de un cierto orden (de un cierto tamaño) que están disponibles en un momento dado. Por ejemplo, para la zona DMA (acceso directo a memoria), hay 90 de 2^(0*PAGE_SIZE) pedazos de memoria. De forma similar, hay 6 de 2^(1*PAGE_SIZE) pedazos, y 2 de 2^(2*PAGE_SIZE) pedazos de memoria disponibles.

La fila DMA hace referencia a los primeros 16 MB en un sistema, la fila HighMem referencia toda la memoria mayor que 4 GB en un sistema, y la fila Normal se refiere a toda la memoria en medio de las anteriores.

Lo siguiente es un ejemplo de la salida t�pica de /proc/buddyinfo:

Node 0, zone      DMA     90      6      2      1      1      ...
Node 0, zone   Normal   1650    310      5      0      0      ...
Node 0, zone  HighMem      2      0      0      1      1      ...


### cgroups
Puede ser utilizado para mejorar la forma en que Linux gestiona el tiempo a los procesos.

cpuset	0	1	1
cpu	0	1	1
cpuacct	0	1	1
memory	0	1	1
devices	0	1	1
freezer	0	1	1
blkio	0	1	1
perf_event	0	1	1

### cmdline

Este archivo muestra los parámetros pasados al kernel en el momento en que este inicia. Un ejemplo del archivo /proc/cmdline se ve como sigue?

ro root=/dev/VolGroup00/LogVol00 rhgb quiet 3

- Esto nos dice que el kernel está montado como de sólo lectura (representado por (ro)), ubicado en el primer volumen lógico (LogVol00) del primer grupo de vol�menes (/dev/VolGroup00). LogVol00 es el equivalente a una partici�n de disco en un sistema no-LVM (Logical Volume Management), de la misma forma que /dev/VolGroup00 es un concepto similar a /dev/hda1,

- Argumentos pasados al núcleo de Linux al  arrancar.  Normalmente
              se hace a través de un gestor de arranque como lilo(1).

+info: http://www.tldp.org/HOWTO/LVM-HOWTO/index.html.


### consoles

Información de los terminales conectados

### cpuinfo

Este archivo virtual identifica el tipo de procesador usado por su sistema. A continuaci�n se muestra un ejemplo de la salida t�pica de /proc/cpuinfo:

processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 15
model name	: Intel(R) Core(TM)2 CPU         T7200  @ 2.00GHz
stepping	: 6
cpu MHz		: 1998.629
cache size	: 6144 KB
fdiv_bug	: no
hlt_bug		: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 5
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 nx constant_tsc up pni monitor ssse3
bogomips	: 3997.25
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

- processor — Proporciona un n�mero de identificaci�n para cada procesador. En sistemas con un �nico procesador, tan s�lo ver� un 0.

- cpu family — Le da de forma autorizada el tipo de procesador que tiene en el sistema. Para un sistema basado en Intel, ponga el n�mero delante del "86" para calcular el valor. Esto le servir� de ayuda si se est� preguntando sobre el tipo de arquitectura de un sistema antiguo tal como 586, 486 o 386. Ya que los paquetes RPM est�n compilados para cada una de estas arquitecturas particulares, este valor le ayuda a identificar qu� paquetes instalar en el sistema.

- model name — Le indica el nombre conocido del procesador, incluyendo el nombre de proyecto.

- cpu MHz — Le muestra la velocidad precisa en megahertz de ese procesador en particular en mil�simas.

- cache size — Le indica la cantidad de memoria de nivel 2 de la cach� disponible en el procesador.

- siblings — Lista el n�mero de CPUs hermanos dentro del mismo CPU f�sico para las arquitecturas que utilizan m�ltiples hilos (hyper-threading).

flags — Define un n�mero de cualidades diferentes del procesador, como la presencia de una unidad de coma flotante (FPU) y la habilidad para procesar instrucciones MMX.


### crypto

Este archivo lista todos los c�digos de cifrado utilizados por el kernel de Linux, incluyendo detalles adicionales para cada uno. Un ejemplo del archivo /proc/crypto se ver�a como sigue:

name         : sha1
module       : kernel
type         : digest
blocksize    : 64
digestsize   : 20
 
name         : md5
module       : md5
type         : digest
blocksize    : 64
digestsize   : 16

### devices


Character devices:
  1 mem
  4 /dev/vc/0
  4 tty
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
  7 vcs
 10 misc
 13 input
 29 fb
 36 netlink
128 ptm
136 pts
180 usb
 
Block devices:
  1 ramdisk
  3 ide0
  9 md
 22 ide1
253 device-mapper
254 mdp
La salida de datos desde /proc/devices incluye el n�mero mayor y el nombre del dispositivo y se divide en dos secciones: Dispositivos de car�cteres y Dispositivos de bloque.

Los Dispositivos de car�cteres son similares a los Dispositivos de bloque, excepto por dos diferencias b�sicas:

Los dispositivos de car�cteres no requieren buffering. Los dispositivos de bloque disponen de una memoria intermedia o buffer que les permite ordenar las peticiones antes de tratar con ellas. Esto es muy importante para los dispositivos dise�ados para guardar informaci�n — tales como discos duros — porque la habilidad de ordenar la informaci�n antes de escribirla en el dispositivo permite que �sta se almacene de forma m�s eficiente.

Los dispositivos de car�cteres env�an datos sin un tama�o preconfigurado. Los dispositivos de bloque pueden enviar y recibir informaci�n en bloques de un tama�o particular, configurable por dispositivo.

Para m�s informaci�n sobre los dispositivos refi�rase a la siguiente documentaci�n instalada:

/usr/share/doc/kernel-doc-<version>/Documentation/devices.txt


### diskstats

The /proc/diskstats file displays the I/O statistics
		of block devices. Each line contains the following 14
		fields:
		 1 - major number
		 2 - minor mumber
		 3 - device name
		 4 - reads completed successfully
		 5 - reads merged
		 6 - sectors read
		 7 - time spent reading (ms)
		 8 - writes completed
		 9 - writes merged
		10 - sectors written
		11 - time spent writing (ms)
		12 - I/Os currently in progress
		13 - time spent doing I/Os (ms)
		14 - weighted time spent doing I/Os (ms)
		For more details refer to Documentation/iostats.txt


+ info:  https://www.kernel.org/doc/Documentation/iostats.txt


### dma

Este archivo contiene una lista de los canales registrados DMA ISA en uso. Un ejemplo de los archivos /proc/dma se ver�a similar a:

 4: cascade

### execdomains

Este archivo lista los dominios de ejecución soportados en la actualidad por el kernel de Linux junto con la gama de personalidades que soportan.

0-0   Linux           [kernel]

Piense en los dominios de ejecuci�n como en una especie de "personalidad" de un sistema operativo. Debido a que se pueden usar otros formatos binarios, como Solaris, UnixWare y FreeBSD con Linux, los programadores pueden cambiar el modo en el que el sistema operativo trata las llamadas del sistema desde estos binarios mediante el cambio de la personalidad de la tarea. A excepci�n del dominio de ejecuci�n PER_LINUX, se puede implementar diferentes personalidades como m�dulos cargables de forma din�mica.

### fb

Este archivo contiene una lista de dispositivos frame buffer, con el n�mero del dispositivo frame buffer y su controlador. La salida de datos m�s com�n de /proc/fb para sistemas que contienen dispositivos de frame buffer se ve similar a:

0 VESA VGA

### filesystems

Este archivo muestra una lista de los tipos del sistema de archivos soportados actualmente por el kernel. A continuaci�n tiene un ejemplo de salida de datos gen�rica de un archivo /proc/filesystems:

nodev   sysfs
nodev   rootfs
nodev   bdev
nodev   proc
nodev   sockfs
nodev   binfmt_misc
nodev   usbfs
nodev   usbdevfs
nodev   futexfs
nodev   tmpfs
nodev   pipefs
nodev   eventpollfs
nodev   devpts
        ext2
nodev   ramfs
nodev   hugetlbfs
        iso9660
nodev   mqueue
        ext3
nodev   rpc_pipefs
nodev   autofs

La primera columna significa si el sistema de archivos est� montado en un dispositivo de bloque. 
Aquellos que comiencen con nodev no est�n montados en un dispositivo. 
La segunda columna lista el nombre de los sistemas de archivos soportados.

El comando mount circula por estos sistemas de archivos listados aquí cuando uno no está especificado como un argumento


### interrupts

Este archivo graba el n�mero de interrupciones por IRQ en la arquitectura x86. Un archivo est�ndar /proc/interrupts es similar a lo siguiente:

           CPU0       
  0:   80448940          XT-PIC  timer
  1:     174412          XT-PIC  keyboard
  2:          0          XT-PIC  cascade
  8:          1          XT-PIC  rtc
 10:     410964          XT-PIC  eth0
 12:      60330          XT-PIC  PS/2 Mouse
 14:    1314121          XT-PIC  ide0
 15:    5195422          XT-PIC  ide1
NMI:          0 
ERR:          0
Para una máquina con múltiples procesadores, el archivo aparecere de forma diferente:

           CPU0       CPU1       
  0: 1366814704          0          XT-PIC  timer
  1:        128        340    IO-APIC-edge  keyboard
  2:          0          0          XT-PIC  cascade
  8:          0          1    IO-APIC-edge  rtc
 12:       5323       5793    IO-APIC-edge  PS/2 Mouse
 13:          1          0          XT-PIC  fpu
 16:   11184294   15940594   IO-APIC-level  Intel EtherExpress Pro 10/100 Ethernet
 20:    8450043   11120093   IO-APIC-level  megaraid
 30:      10432      10722   IO-APIC-level  aic7xxx
 31:         23         22   IO-APIC-level  aic7xxx
NMI:          0
ERR:          0
La primera columna se refiere al n�mero de IRQ. Cada CPU del sistema tiene su propia columna y su propio n�mero de interrupciones por IRQ. La columna siguiente le indica el tipo de interrupci�n y la �ltima contiene el nombre del dispositivo que est� localizado en ese IRQ.

Cada uno de los tipos de interrupciones vistos en este archivo, que son espec�ficos para la arquitectura, significan algo diferente. Los siguientes valores son comunes para las m�quinas x86:

XT-PIC — Interrupciones del ordenador AT antiguo que se han producido por un largo periodo de tiempo.

IO-APIC-edge — Se�al de voltaje de las transacciones interrumpidas desde abajo hasta arriba, creando una edge, en la que la interrupci�n IO-APIC-level, tan s�lo se dan a partir de procesadores 586 y superiores.

IO-APIC-level — Genera interrupciones cuando su se�al de voltaje se alza hasta que la se�al desciende nuevamente.

### iomem

Este archivo muestra el mapa actual de la memoria del sistema para los diversos dispositivos:

00000000-0009fbff : System RAM
0009fc00-0009ffff : reserved
000a0000-000bffff : Video RAM area
000c0000-000c7fff : Video ROM
000f0000-000fffff : System ROM
00100000-07ffffff : System RAM
  00100000-00291ba8 : Kernel code
  00291ba9-002e09cb : Kernel data
e0000000-e3ffffff : VIA Technologies, Inc. VT82C597 [Apollo VP3]
e4000000-e7ffffff : PCI Bus #01
  e4000000-e4003fff : Matrox Graphics, Inc. MGA G200 AGP
  e5000000-e57fffff : Matrox Graphics, Inc. MGA G200 AGP
e8000000-e8ffffff : PCI Bus #01
  e8000000-e8ffffff : Matrox Graphics, Inc. MGA G200 AGP
ea000000-ea00007f : Digital Equipment Corporation DECchip 21140 [FasterNet]
  ea000000-ea00007f : tulip
ffff0000-ffffffff : reserved
La primera columna muestra los registros de memoria utilizados por cada uno de los diferentes tipos de memoria. La segunda columna indica el tipo de memoria de dichos registros y muestra qu� registros de memoria son usados por el kernel dentro de la RAM del sistema o, si la tarjeta NIC tiene m�ltiples puertos Ethernet, los registros de memoria asignados para cada puerto.

### ioports
- La salida de /proc/ioports proporciona una lista de las regiones de puertos registrados actualmente utilizados para la comunicaci�n de entrada y salida con un dispositivo. Este archivo puede ser muy largo. A continuaci�n se muestra un listado parcial:

- La primera columna le indica el rango de direcciones de los puertos de entrada y salida reservado para el dispositivo listado en la segunda columna.

0000-001f : dma1
0020-003f : pic1
0040-005f : timer
0060-006f : keyboard
0070-007f : rtc
0080-008f : dma page reg
00a0-00bf : pic2
00c0-00df : dma2
00f0-00ff : fpu
0170-0177 : ide1
01f0-01f7 : ide0
02f8-02ff : serial(auto)
0376-0376 : ide1
03c0-03df : vga+
03f6-03f6 : ide0
03f8-03ff : serial(auto)
0cf8-0cff : PCI conf1
d000-dfff : PCI Bus #01
e000-e00f : VIA Technologies, Inc. Bus Master IDE
  e000-e007 : ide0
  e008-e00f : ide1
e800-e87f : Digital Equipment Corporation DECchip 21140 [FasterNet]
  e800-e87f : tulip


### kallsyms
### kcore

Este archivo representa la memoria física del sistema y se almacena en el formato de archivos base. A diferencia de la mayor�a de archivos /proc/, kcore muestra un tama�o. Este valor se da en bytes y es igual al tama�o de la memoria f�sica (RAM) utilizada m�s 4KB.

Sus contenidos est�n dise�ados para que los examine un depurador, como por ejemplo gdb, y no es legible para humanos.

ATENCIÓN!!

Evite visualizar el archivo virtual /proc/kcore. Los contenidos de este archivo se saldr�n del terminal. Si accidentalmente lo visualiza, pulse la combinaci�n de teclas [Ctrl]-[C] para detener el proceso y luego escriba reset para llamar la l�nea de comandos del prompt en que se encontraba.

### key-users

This service allows cryptographic keys, authentication tokens, cross-domain
user mappings, and similar to be cached in the kernel for the use of
filesystems and other kernel services.

Keyrings are permitted; these are a special type of key that can hold links to
other keys. Processes each have three standard keyring subscriptions that a
kernel service can search for relevant keys.

+info: https://www.kernel.org/doc/Documentation/security/keys.txt

0:     4 3/3 0/200 0/20000

### kmsg

Este archivo se utiliza para mantener mensajes generados por el kernel. Luego, estos mensajes son recogidos por otros programas, como por ejemplo /sbin/klogd o /bin/dmesg.


### kpagecount

Conteo de páginas del Kernel. No legible

### kpageflags

Ídem
### latency_stats
### loadvg

Este archivo ofrece una vista de la carga promedio del procesador con respecto al sobretiempo de CPU y de E/S, as� como tambi�n datos adicionales utilizados por uptime y otros comandos. Una muestra del archivo /proc/loadavg ser�a similar a lo siguiente:

0.20 0.18 0.12 1/80 11206
Las primeras tres columnas muestran la utilizaci�n de CPU y de E/S en los �ltimos periodos de 1, 5 y 10 minutos. La cuarta columna le muestra el n�mero de procesos actualmente en ejecuci�n y el n�mero total de los mismos. La �ltima columna visualiza el �ltimo ID de proceso usado.

### locks

Este archivo muestra los archivos bloqueados en la actualidad por el kernel. El contenido de este archivo contiene datos internos de depuraci�n y puede variar enormemente, dependiendo del uso del sistema. Este es un ejemplo de archivo /proc/locks de un sistema ligeramente cargado:

1: POSIX  ADVISORY  WRITE 3568 fd:00:2531452 0 EOF
2: FLOCK  ADVISORY  WRITE 3517 fd:00:2531448 0 EOF
3: POSIX  ADVISORY  WRITE 3452 fd:00:2531442 0 EOF
4: POSIX  ADVISORY  WRITE 3443 fd:00:2531440 0 EOF
5: POSIX  ADVISORY  WRITE 3326 fd:00:2531430 0 EOF
6: POSIX  ADVISORY  WRITE 3175 fd:00:2531425 0 EOF
7: POSIX  ADVISORY  WRITE 3056 fd:00:2548663 0 EOF
A cada bloqueo se le asigna un �nico n�mero al inicio de cada l�nea. La segunda columna se refiere a la clase de bloqueo utilizado; FLOCK, haciendo referencia al estilo antiguo de bloqueos de archivos desde una llamada de sistema flock y POSIX que representa los bloqueos nuevos POSIX desde la llamada de sistema lockf.

La tercera columna puede tener dos valores. ADVISORY o MANDATORY. ADVISORY significa que el bloqueo no impide que otras personas puedan acceder a los datos; tan s�lo previene de que otros intenten establecer un bloqueo. MANDATORY significa que mientras que dura el bloqueo no se permite ning�n otro acceso a los datos. La cuarta columna muestra si el bloqueo permite al responsable del mismo acceso de READ o WRITE (lectura y escritura) al archivo. La quinta muestra el ID del proceso que tiene el bloqueo. La sexta columna muestra el ID del archivo bloqueado, en el formato de MAJOR-DEVICE:MINOR-DEVICE:INODE-NUMBER. La s�ptima y octava columnas muestra el inicio y el final de la regi�n bloqueada del archivo.

### mdstat

Este archivo contiene la informaci�n actual sobre las configuraci�n de discos m�ltiples de RAID. Si su sistema no contiene dicha configuraci�n, el archivo /proc/mdstat ser� parecido a:

Personalities : 
read_ahead not set
unused devices: <none>
Este archivo se mantiene en el mismo estado que el mostrado arriba a menos que un software RAID o dispositivo md est� presente. En ese caso, visualice /proc/mdstat para ver el estado actual de los dispositivos RAID mdX.

El archivo /proc/mdstat a continuaci�n, muestra un sistema con su md0 configurado como un dispositivo RAID 1, mientras est� resincronizando los discos:

Personalities : [linear] [raid1]
read_ahead 1024 sectors
md0: active raid1 sda2[1] sdb2[0] 9940 blocks [2/2] [UU] resync=1% finish=12.3min
algorithm 2 [3/3] [UUU]
unused devices: <none>

### meminfo

Este es uno de los archivos m�s utilizados en el directorio /proc/, ya que proporciona mucha informaci�n importante sobre el uso actual de RAM en el sistema.

La muestra siguiente del archivo virtual /proc/meminfo es de un sistema con 256 MB de RAM y 512 MB de espacio de intercambio (swap):

MemTotal:       255908 kB
MemFree:         69936 kB
Buffers:         15812 kB
Cached:         115124 kB
SwapCached:          0 kB
Active:          92700 kB
Inactive:        63792 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:       255908 kB
LowFree:         69936 kB
SwapTotal:      524280 kB
SwapFree:       524280 kB
Dirty:               4 kB
Writeback:           0 kB
Mapped:          42236 kB
Slab:            25912 kB
Committed_AS:   118680 kB
PageTables:       1236 kB
VmallocTotal:  3874808 kB
VmallocUsed:      1416 kB
VmallocChunk:  3872908 kB
HugePages_Total:     0
HugePages_Free:      0
Hugepagesize:     4096 kB
La mayor�a de la informaci�n que est� aqu� es usada por los comandos free, top y ps. De hecho, la salida de datos del comando free es parecida en apariencia al contenido y estructura de /proc/meminfo. Pero si lee directamente /proc/meminfo, ver� m�s detalles:

MemTotal — Cantidad total de RAM f�sica en kilo bytes.

MemFree — Cantidad de RAM f�sica, en kilobytes, sin utilizar por el sistema.

Buffers — Cantidad de RAM f�sica, en kilobytes, usada para los archivos de memoria intermedia.

Cached — Cantidad de RAM f�sica en kilobytes usada como memoria cach�.

SwapCached — Cantidad de swap en kilobytes usada como memoria cach�.

Active — Cantidad total de memoria intermedia o cach� de p�gina, en kilobytes, que est� en uso activo. Esta es memoria que recientemente ha sido utilizada y que usualmente no se reclama para otros prop�sitos.

Inactive — La cantidad total de memoria intermedia o cach� de p�gina, en kilobytes, que est� libre y disponible. Esta es memoria que no se ha utilizado recientemente y que se puede reclamar para otros prop�sitos.

HighTotal y HighFree — Cantidad total de memoria libre, que no est� mapeada en el espacio del kernel. El valor HighTotal puede variar dependiendo del tipo de kernel utilizado.

LowTotal y LowFree — Cantidad total de memoria libre implantada directamente en el espacio del kernel. El valor LowTotal puede cambiar dependiendo del tipo de kernel utilizado.

SwapTotal — Cantidad total de swap disponible, en kilobytes.

SwapFree — Cantidad total de swap libre, en kilobytes.

Dirty — La cantidad total de memoria, en kilobytes, esperando a ser escrita al disco.

Writeback — Cantidad total de memoria, en kilobytes, que est� siendo escrita activamente al disco.

Mapped — La cantidad total de memoria, en kilobytes, que se ha utilizado para asignar dispositivos, archivos o bibliotecas, usando el comando mmap.

Slab — Cantidad total de memoria, en kilobytes, usada por el kernel para hacer cach� de estructuras de datos para su propio uso.

Committed_AS — Cantidad total de memoria, en kilobytes, estimadas para completar la carga de trabajo. Este valor representa un escenario del peor caso, y tambi�n incluye a la memoria de intercambio o swap.

PageTables — Cantidad total de memoria, en kilobytes, dedicada al nivel m�s bajo de la tabla de p�ginas.

VMallocTotal — Cantidad total memoria, en kilobytes, del espacio total de direcciones virtuales asignadas.

VMallocUsed — La cantidad total de memoria en kilobytes, de espacio de direcciones virtuales utilizada.

VMallocChunk — El bloque continuo de memoria m�s grande, en kilobytes, de espacio de direcciones virtuales disponibles.

HugePages_Total — El n�mero total de paginas gigantes para el sistema. El n�mero se deriva dividiendo Hugepagesize por los megabytes puestos a un lado para las p�ginas gigantes especificadas en /proc/sys/vm/hugetlb_pool. Esta estad�stica s�lo aparece en las arquitecturas x86, Itanium y AMD64.

HugePages_Free — El n�mero total de p�ginas gigantes disponibles para el sistema. Esta estad�stica s�lo aparece en las arquitecturas x86, Itanium y AMD64.

Hugepagesize — El tama�o para cada unidad de hugepages en kilobytes. Por defecto, el valor es 4096 KB en los kernels de un s�lo procesador para las arquitecturas de 32 bits. Para los kernels SMP, hugemem y AMD64, el valor por defecto es 2048 KB. Para las arquitecturas Itanium, el valor por defecto es 262144 KB. Esta estad�stica solamente aparece en las arquitecturas x86, Itanium y AMD64.

### misc

Este archivo lista varios controladores registrados en el principal dispositivo de miscel�neos, que es el n�mero 10:

 63 device-mapper
175 agpgart
135 rtc
134 apm_bios
La primera columna es el n�mero menor (minor) de cada dispositivo y la segunda le muestra el controlador en uso.

### modules

Este archivo muestra una lista de todos los m�dulos cargados en el sistema. Su contenido variar� dependiendo de la configuraci�n y uso de su sistema, pero deber�a organizarse de forma similar al siguiente ejemplo de salida del archivo /proc/modules:

Nota	Nota
 	
Se ha vuelto a formatear este ejemplo en un formato legible. La mayor�a de esta informaci�n tambi�n se puede ver a trav�s del comando /sbin/lsmod.

nfs      170109  0 -          Live 0x129b0000
lockd    51593   1 nfs,       Live 0x128b0000
nls_utf8 1729    0 -          Live 0x12830000
vfat     12097   0 -          Live 0x12823000
fat      38881   1 vfat,      Live 0x1287b000
autofs4  20293   2 -          Live 0x1284f000
sunrpc   140453  3 nfs,lockd, Live 0x12954000
3c59x    33257   0 -          Live 0x12871000
uhci_hcd 28377   0 -          Live 0x12869000
md5      3777    1 -          Live 0x1282c000
ipv6     211845 16 -          Live 0x128de000
ext3     92585   2 -          Live 0x12886000
jbd      65625   1 ext3,      Live 0x12857000
dm_mod   46677   3 -          Live 0x12833000
La primera columna contiene el nombre del m�dulo.

La segunda columna se refiere al tama�o de la memoria del m�dulo, en bytes.

La tercera columna lista cu�ntas instancias del m�dulo est�n cargadas actualmente. Un valor de cero representa un m�dulo sin cargar.

La cuarta columna indica si el m�dulo depende de que otro m�dulo est� presente para poder funcionar, y lista esos otros m�dulos.

La quinta columna lista en qu� estado de carga se encuentra el m�dulo: Live, Loading o Unloading son los �nicos valores posibles.

La sexta columna lista el desplazamiento de memoria del kernel actual para el m�dulo cargado. Esta informaci�n puede ser �til para prop�sitos de depuraci�n o para herramientas de perfiles, tales como oprofile.


### mounts

Este archivo proporciona una lista de todos los montajes en uso por el sistema:

rootfs / rootfs rw 0 0
/proc /proc proc rw,nodiratime 0 0
none /dev ramfs rw 0 0
/dev/mapper/VolGroup00-LogVol00 / ext3 rw 0 0
none /dev ramfs rw 0 0
/proc /proc proc rw,nodiratime 0 0
/sys /sys sysfs rw 0 0
none /dev/pts devpts rw 0 0
usbdevfs /proc/bus/usb usbdevfs rw 0 0
/dev/hda1 /boot ext3 rw 0 0
none /dev/shm tmpfs rw 0 0
none /proc/sys/fs/binfmt_misc binfmt_misc rw 0 0
sunrpc /var/lib/nfs/rpc_pipefs rpc_pipefs rw 0 0
La salida de datos que encontramos aqu� se parece a /etc/mtab, excepto que /proc/mount est� m�s actualizada.

La primera columna especifica el dispositivo que est� montado, la segunda revela el punto de montaje, la tercera indica el tipo de sistema de archivos y la cuarta si est� montado en modo s�lo lectura (ro) o s�lo escritura (rw). La quinta y sexta columna son valores no v�lidos dise�ados para hacer coincidir el formato usado en /etc/mtab.

### mtrr

Este archivo se refiere a la actual Memory Type Range Registers (MTRRs), en uso dentro del sistema. Si la arquitectura de su sistema soporta MTRRs, entonces el archivo /proc/mtrr ser� algo parecido a:

reg00: base=0x00000000 (   0MB), size= 256MB: write-back, count=1
reg01: base=0xe8000000 (3712MB), size=  32MB: write-combining, count=1
Los MTRRs se usan con la familia de procesadores Intel P6 (Pentium II y superior), y controlan el acceso del procesador a los rangos de memoria. Cuando utilice una tarjeta de v�deo en un PCI o un bus AGP, un archivo /proc/mtrr adecuadamente configurado puede incrementar el rendimiento en un 150%.

La mayor�a de las veces, por defecto este valor est� configurado adecuadamente. Se puede encontrar m�s informaci�n sobre la configuraci�n manual de este archivo en la siguiente ubicaci�n:

/usr/share/doc/kernel-doc-<version>/Documentation/mtrr.txt


### net

directorio que contiene varios pseudoficheros, los cuales dan el
              estado  de  algunas  partes  de  la  capa de red. Estos ficheros
              contienen estructuras ASCII y, por tanto,  se  pueden  leer  con
              cat. Sin embargo, la aplicación netstat(8) proporciona un acceso
              mucho más claro a estos ficheros.
			  
+info: http://manpages.ubuntu.com/manpages/quantal/es/man5/proc.5.html



### pagetypeinfo

Para evitar la fragmentación, se agrupan los diferentes tipos de tal forma que, aquellos procesos que mueven muchas páginas, se agrupan en estos tipos de grupos de páginas.


### partitions

El archivo contiene informaci�n sobre la asignaci�n de bloques de particiones. Un ejemplo de este archivo en un sistema b�sico se ver�a como:

major minor  #blocks  name
 
   3     0   19531250 hda
   3     1     104391 hda1
   3     2   19422585 hda2
 253     0   22708224 dm-0
 253     1     524288 dm-1
La mayor�a de la informaci�n no es relevante para los usuarios, a excepci�n de las siguientes l�neas:

major — Número principal (major number) del dispositivo con esta partici�n. El n�mero principal en nuestro ejemplo en /proc/partitions (3), corresponde con el dispositivo ide0 en /proc/devices.

minor — Número menor del dispositivo con esta partici�n. Separa las particiones en diferentes dispositivos f�sicos y los relaciona con el número al final del nombre de la partici�n.

blocks — Lista el número de bloques de disco f�sicos contenidos en una partici�n particular.

name — Nombre de la partición.


### sched_debug

the number of running processes (cfs_rq[0].nr_running)
the runnable processes (runnable tasks)
### schedstat
### self

Este  directorio  hace referencia al proceso que está accediendo
              al sistema de ficheros /proc y  es  idéntico  al  directorio  de
              /proc cuyo nombre es el PID del mismo proceso.
### slabinfo

Información  sobre  las memorias cachés del núcleo. Las columnas
              son:
              cache-name
              num-active-objs
              total-objs
              object-size
              num-active-slabs
              total-slabs
              num-pages-per-slab
              Vea slabinfo(5) para más detalles.
### softirqs
Ver stat
### stat

Este archivo mantiene un registro de las diferentes estad�sticas sobre el sistema desde que fue reiniciado por �ltima vez. El contenido de /proc/stat que puede ser muy largo, usualmente empieza de la siguiente manera:

cpu  7520 5 13788 3768321 10663 6 1422 0 0 0
cpu0 7520 5 13788 3768321 10663 6 1422 0 0 0
intr 582647 206 18267 0 0 0 15967 0 0 0 0 59103 130 147 0 0 37310 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 638701
btime 1396400625
processes 9095
procs_running 1
procs_blocked 0
softirq 569251 0 269296 7620 59677 32812 0 16156 0 805 182885

Algunas de las estad�sticas m�s populares incluyen:

cpu — Mide el n�mero de instantes (1/100 de segundos para sistemas x86) en los que el sistema ha estado en modo usuario, modo usuario con prioridad baja (nice), modo de sistema, tareas ociosas, esperas de E/S, IRQ (hardirq) y softirq respectivamente. El IRQ (hardirq) es la respuesta directa a un evento de hardware. El IRQ hace el esfuerzo m�nimo para encolar el trabajo "pesado" para que lo ejecute el softirq. El softirq se ejecuta a una prioridad m�s baja que el IRQ y por lo tanto puede ser interrumpido con m�s frecuencia. El total para todos los CPUs se d� arriba, mientras que cada CPU individual se lista con sus propias estad�sticas. El ejemplo siguiente es de una configuraci�n 4-way Intel Pentium Xeon con el multihilos activado, por lo tanto muestra cuatro procesadores f�sicos y cuatro procesadores virtuales para un total de ocho procesadores.

page — N�mero de p�ginas que el sistema ha cargado o suprimido del disco.

swap — N�mero de p�ginas swap que el sistema ha introducido o sacado.

intr — N�mero de interrupciones que ha experimentado el sistema.

btime — Tiempo de arranque, medido por el n�mero de segundos desde el 1 de enero de 1970, conocido con el nombre de epoch.



### swaps

Este archivo mide el espacio swap y su uso. Para un sistema con tan s�lo una partici�n de espacio swap, la salida de datos de /proc/swap ser� similar a lo siguiente:


Filename				Type		Size	Used	Priority
/dev/sda5                               partition	521212	0	-1

Mientras que alguna de esta informaci�n se puede encontrar en otros archivos en el directorio /proc/, /proc/swap proporciona una instant�nea de cada nombre de archivo swap, el tipo de espacio swap, el tama�o total y la cantidad de espacio en uso (en kilobytes). La columna de prioridad es �til cuando se usan m�ltiples archivos de espacio de intercambio. Cuanto m�s baja es la prioridad, m�s probable es que se use el archivo de intercambio.

### sysrq-trigger

Using the echo command to write to this file, a remote root user can execute most System Request Key commands remotely as if at the local terminal. To echo values to this file, the /proc/sys/kernel/sysrq must be set to a value other than 0. 

### timer_list

Tiene la información sobre los relojes y timers configurados en el sistema. Es útil para depurar el estado actual de depuración, especialmente cuando se desarrolla para eventos de reloj. Sistemas en Tiempo Real.


### timer_stats

Permite ver la información sobre las rutinas que tienen peticiones de tiempo y reloj del kernel de Linux.

count,  pid command   start_func (expire_func)
To activate the collection of stats (and reset the counters), do "echo 1 >/proc/timer_stats"
To stop collecting stats, do "echo 0 >/proc/timer_stats"

+info: http://elinux.org/Kernel_Timer_Systems

### uptime
El archivo contiene informaci�n sobre el tiempo que lleva encendido el sistema desde el �ltimo reinicio. La salida de datos de /proc/uptime es m�nima:

350735.47 234388.90
- El primer n�mero le indica el n�mero total de segundos que el sistema ha estado en funcionamiento. 
- El segundo indica cu�nto de ese tiempo, tambi�n en segundos, la m�quina ha estado inactiva.


### version

Este archivo muestra las versi�n del kernel de Linux y gcc en uso, as� como la versi�n de Red Hat Enterprise Linux instalada en el sistema:

Linux version 3.5.0-17-generic (buildd@roseapple) (gcc version 4.7.2 (Ubuntu/Linaro 4.7.2-2ubuntu1) ) #28-Ubuntu SMP Tue Oct 9 19:32:08 UTC 2012

Esta informaci�n se usa para diversos prop�sitos, incluyendo la aportaci�n de datos de la versi�n en el int�rprete de comandos de registro est�ndar.



### version_signature
Versión de Linux
### vmallocinfo
Reserva de memoria virtual
### vmstat

Estadísticas de memoria virtual utilizada por el kernel.

Explicar comando vmstat

$ vmstat -a # memoria activa
### zoneinfo

Información sobre zonas de memoria
