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
### cgroups
### cmdline
### consoles
### cpuinfo
### crypto
### devices
### diskstats
### dma
### execdomains
### fb
### filesystems
### interrupts
### iomem
### ioports
### kallsyms
### kcore
### key-users
### kmsg
### kpagecount
### kpageflags
### latency_stats
### loadvg
### locks
### mdstat
### meminfo
### misc
### modules
### mounts
### mtrr
### net
### pagetypeinfo
### partitions
### sched_debug
### schedstat
### self
### slabinfo
### softirqs
### stat
### swaps
### sysrq-trigger
### timer_list
### timer_stats
### uptime
### version
### version_signature
### vmallocinfo
### vmstat
### zoneinfo
