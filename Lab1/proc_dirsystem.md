 El siguiente resumen proporciona  una  rápida  visita  a  la  jerarquía
       /proc.

       [número]
              Hay un subdirectorio numérico para cada proceso en ejecución; el
              nombre del subdirectorio es el ID del proceso. Cada uno de ellos
              contiene los siguientes pseudo ficheros y directorios.

              cmdline
                     Éste  contiene  la  línea  de  órdenes  completa  para el
                     proceso,  a  menos  que  el  proceso   entero   se   haya
                     intercambiado  a  disco  o  a menos que el proceso sea un
                     proceso zombie. En cualquiera de estos dos últimos casos,
                     no  hay  nada  en el fichero, es decir, una lectura sobre
                     este fichero devolverá 0 caracteres. Los argumentos de la
                     línea  de  órdenes  aparecen  en  este  fichero  como  un
                     conjunto de cadenas separadas por nulos, con un byte nulo
                     adicional tras la última cadena.

              cwd    Éste  es  un enlace hacia el directorio de trabajo actual
                     del proceso. Por ejemplo, para encontrar el directorio de
                     trabajo actual del proceso 20, puede hacer esto:

                     cd /proc/20/cwd; /bin/pwd

                     Dese  cuenta que la orden pwd es frecuentemente una orden
                     interna del shell, y podría no  funcionar  adecuadamente.
                     En bash, debe usar pwd -P.

              environ
                     Este   fichero  contiene  el  entorno  del  proceso.  Las
                     entradas están serparadas por caracteres nulos, y  podría
                     haber  un carácter nulo al final. Por tanto, para mostrar
                     el entorno del proceso 1, debería hacer:

                     (cat /proc/1/environ; echo) | tr "\000" "\n"

                     (Una razón por la que  alguien  querría  hacer  esto,  la
                     puede encontrar en lilo(8).)

              exe    En  la  versiones  2.2  y  2.4  de Linux exe es un enlace
                     simbólico que contiene el nombre de la ruta actual de  la
                     orden  ejecutada.   El  enlace  simbólico  exe  se  puede
                     resolver de forma normal - el intentar abrir  exe  abrirá
                     el  ejecutable.  Incluso puede teclear /proc/[number]/exe
                     para ejecutar otra copia del mismo proceso [número].

                     En Linux 2.0 y versiones anteriores exe es un puntero  al
                     fichero  binario  que  fue  ejecutado  y  aparece como un
                     enlace simbólico. Una  llamada  readlink(2)  aplicada  al
                     fichero   especial  "exe"  devuelve  una  cadena  con  el
                     formato:

                     [dispositivo]:nodo-i

                     Por ejemplo, [0301]:1502 sería el nodo-i  1502  sobre  el
                     dispositivo con número mayor 03 (discos IDE, MFM, etc.) y
                     número menor 01 (primera partición del primer disco.

                     find(1) con la opción -inum se puede usar para buscar  el
                     fichero.

              fd     Éste  es  un  subdirectorio  que contiene una entrada por
                     cada fichero que tiene abierto el proceso,  nombrada  con
                     el  descriptor  del  fichero,  y  la  cual  es  un enlace
                     simbólico al fichero real (como lo es  la  entrada  exe).
                     Por  tanto,  0  es  la  entrada  estándar, 1 es la salida
                     estándar, 2 es la salida estándar de error, etc.

                     Los programas que no leen de la  entrada  estándar,  sino
                     que  leen  de  un fichero, y que no escriben en la salida
                     estándar, sino que escriben en  un  fichero,  pueden  ser
                     engañados de la siguiente manera, suponiendo que -i es la
                     opción que designa al fichero de entrada y -o  la  opción
                     que designa al fichero de salida:
                     foobar -i /proc/self/fd/0 -o /proc/self/fd/1
                     y  de  esta  manera  su  programa funcionará como filtro.
                     Note que esto no funcionará  en  programas  que  realizan
                     accesos   aleatorios  sobre  sus  ficheros,  ya  que  los
                     ficheros del directorio  fd  no  permiten  este  tipo  de
                     acceso.

                     /proc/self/fd/N es aproximadamente lo mismo que /dev/fd/N
                     en algunos sistemas UNIX y sistemas al  estilo  UNIX.  De
                     hecho,  la  mayoría de los guiones shell MAKEDEV de Linux
                     enlazan simbólicamente /proc/self/fd con /dev/fd.

              maps   Fichero que contiene las regiones de memoria  actualmente
                     asociadas y sus permisos de acceso.

                     El formato es:

        Dirección         perms desplaz disp  nodo-i    ruta
        08048000-08056000 r-xp 00000000 03:0c 64593      /usr/sbin/gpm
        08056000-08058000 rw-p 0000d000 03:0c 64593      /usr/sbin/gpm
        08058000-0805b000 rwxp 00000000 00:00 0
        40000000-40013000 r-xp 00000000 03:0c 4165       /lib/ld-2.2.4.so
        40013000-40015000 rw-p 00012000 03:0c 4165       /lib/ld-2.2.4.so
        4001f000-40135000 r-xp 00000000 03:0c 45494      /lib/libc-2.2.4.so
        40135000-4013e000 rw-p 00115000 03:0c 45494      /lib/libc-2.2.4.so
        4013e000-40142000 rw-p 00000000 00:00 0
        bffff000-c0000000 rwxp 00000000 00:00 0

                     donde  dirección es el espacio de direcciones del proceso
                     que ocupa, perms es un conjunto de permisos:

                          r = leer
                          w = escribir
                          x = ejecutar
                          s = compartido
                          p = privado (copia en escritura)

                     desplaz es el  desplazamiento  dentro  del  fichero/cosa,
                     disp es el dispositivo (mayor:menor) y nodo-i es el nodo-
                     i en ese dispositivo. 0  indica  que  no  hay  un  nodo-i
                     asociado  a  la  región de memoria, como ocurriría con la
                     región bss del proceso.

                     En Linux 2.0 no existe un campo que dé el  nombre  de  la
                     ruta.

              mem    A  través  del fichreo mem se puede acceder a las páginas
                     de la memoria de un proceso mediante open(2),  read(2)  y
                     fseek(3).

              root   Unix  y Linux soportan la idea de una raíz del sistema de
                     ficheros por proceso, asignada por la llamada al  sistema
                     chroot(2).  Root apunta a la raíz del sistema de ficheros
                     y se comporta como lo hacen exe, fd/*, etc.

              stat   Información de estado del  proceso.  Ésta  es  usada  por
                     ps(1).  Se define en /usr/src/linux/fs/proc/array.c.

                     Los  campos,  en  orden,  junto  con  sus  indicadores de
                     formato apropiados para scanf(3), son:

                     pid %d Identificador del proceso.

                     comm %s
                            Nombre de fichero del ejecutable,  en  paréntesis.
                            Éste es visible dependiendo de si el ejecutable ha
                            sido o no intercambiado.

                     state %c
                            Un  carácter  de  la  cadena  "RSDZTW"   donde   R
                            significa  en  ejecución,  S  bloqueado  de  forma
                            interrumpible, D bloqueado de forma ininterrupible
                            en  una  espera  de  disco, Z zombie, T proceso en
                            ejecución paso a paso o parado (en una señal) y  W
                            transfiriendo páginas.

                     ppid %d
                            El PID del padre.

                     pgrp %d
                            El   identificador   del  grupo  de  procesos  del
                            proceso.

                     session %d
                            El identificador de sesión del proceso.

                     tty_nr %d
                            El terminal que usa el proceso.

                     tpgid %d
                            El identificador del grupo de procesos del proceso
                            al  que pertenece actualmente la terminal a la que
                            está conectado el proceso.

                     flags %u
                            Las banderas del proceso.  El bit "math" es  el  4
                            (en  decimal)  y  el  bit  "paso a paso" el 10 (en
                            decimal).

                     minflt %lu
                            El número de fallos de página  menores  producidos
                            por  el  proceso que no han necesitado la carga de
                            una página de memoria desde disco.

                     cminflt %lu
                            El número de fallos de página  menores  producidos
                            por el proceso y sus hijos.

                     majflt %lu
                            El  número  de fallos de página mayores producidos
                            por el proceso que han necesitado la carga de  una
                            página de memoria desde disco.

                     cmajflt %lu
                            El  número  de fallos de página mayores producidos
                            por el proceso y sus hijos.

                     utime %ld
                            El número  de  jiffies  que  este  proceso  se  ha
                            planificado en modo usario.

                     stime %ld
                            El  número  de  jiffies  que  este  proceso  se ha
                            planificado en modo núcleo.

                     cutime %ld
                            El número de jiffies que este proceso y sus  hijos
                            se han planificado en modo usuario.

                     cstime %ld
                            El  número de jiffies que este proceso y sus hijos
                            se han planificado en modo núcleo.

                     priority %ld
                            El valor ``nice'' estándar, más 15. El valor nunca
                            es negativo dentro del núcleo.

                     nice %ld
                            El  valor  ``nice'',  que  va  desde  19  (el  más
                            generoso) hasta -19 (el más codicioso).

                     0 %ld  Este valor se fija a  0  en  el  propio  código  y
                            representa  el  lugar  que  ocupaba  de  un  campo
                            eliminado.

                     itrealvalue %u
                            El tiempo en jiffies antes  de  que  la  siguiente
                            señal SIGALRM sea enviada al proceso.

                     starttime %lu
                            Tiempo  en  jiffies  desde el arranque del sistema
                            hasta el inicio de la ejecución del proceso.

                     vsize %lu
                            Tamaño de la memoria virtual en bytes.

                     rss %ld
                            Tamaño del conjunto  residente  (RSS):  número  de
                            páginas  que  el  proceso  tiene  en memoria real,
                            menos 3 (para propósitos  administrativos).  Dicho
                            conjunto está formado por las páginas que componen
                            actualmente el espacio de código, datos y pila. No
                            incluye  aquellas  páginas  que  no se han cargado
                            bajo demanda o que se han intercambiado a disco.

                     rlim %lu
                            Límite actual,  en  bytes,  del  RSS  del  proceso
                            (normalmente, 4294967295 en i386).

                     startcode %lu
                            Dirección  por encima de la cual se puede ejecutar
                            el código del programa.

                     endcode %lu
                            Dirección por debajo de la cual se puede  ejecutar
                            el código del programa.

                     startstack %lu
                            Dirección de comienzo de la pila.

                     kstkesp %lu
                            El  valor  actual  del  registro  ESP  (puntero de
                            pila), tal como se encuentra en la página de  pila
                            del proceso.

                     kstkeip %lu
                            Valor actual del EIP (puntero de instrucción).

                     signal %lu
                            Mapa  de  bits  de señales pendientes (normalmente
                            0).

                     blocked %lu
                            Mapa de bits de señales bloqueadas (normalmente 0,
                            2 para los shells).

                     sigignore %lu
                            Mapa de bits de señales ignoradas.

                     sigcatch %lu
                            Mapa de bits de señales capturadas.

                     wchan %lu
                            Este  es  el ``canal'' en el que está esperando el
                            proceso. Es la dirección de una llamada al sistema
                            y  se  puede  mirar  en  una  lista  de nombres si
                            necesita un nombre textual. (Pruebe ps -l para ver
                            WCHAN en acción.)

                     nswap %lu
                            Número de páginas intercambiadas - no guardadas.

                     cnswap %lu
                            nswap acumulativo para los procesos hijos.

                     exit_signal %d
                            Señal a enviar al padre cuando muramos.

                     processor %d
                            Número de CPU en la que se ejecutó por última vez.

              statm  Proporciona  información,  en páginas, sobre la situación
                     de memoria.  Las columnas son:
                      size       tamaño total del programa
                      resident   tamaño del conjunto residente
                      share      páginas compartidas
                      trs        texto (código)
                      drs        datos/pila
                      lrs        biblioteca
                      dt         páginas modificadas

              status Proporciona gran parte de la información de stat y  statm
                     en  un  formato  que  es mucho más fácil de leer para una
                     persona.