# Instalar GUEST TOOLS y realizar carpeta compartida

- Ir a la opción "Devices > Install Guest Additons", de esta forma se introduce el CD en la máquina.
- La otra manera es hacerlo mediante el menú ” Machine > Settings…” y en “Storage” seleccionamos 
la imagen que deseamos introducir en la unidad de CD virtual, con el icono del CD.

- Montar CD a mano: 
 $ sudo mount /dev/cdrom /media/cdrom
 
 - Instalar los paquetes de las Guest Additions para evitar errores:
 
   $ sudo apt-get install build-essential
   $ sudo apt-get install linux-headers-(versión del kernel)  #utilizar uname -r

 - Luego:
 
    $ cd  /media/cdrom
    $ ./VBoxLinuxAdditions.run
  	$ sudo reboot
  	
# Compartir Carpeta:

  Esto vale para Linux, Windows y Mac:  
  
  - Definir las carpetas compartidas en Windows/Linux desde VirtualBox, para ello utilizamos la opción de menú de Dispositivos -> Carpetas compartidas…
  - En la ventana que aparecerá a continuación utilizamos el botón (+) para que aparezca la siguiente ventana y añadimos la carpeta que queremos compartir entre ambos sistemas operativos.
  - Poner un nombre, p.e., Public (seleccionar automontar y hacer permanente).
  - En Ubuntu:
  
    $ sudo mkdir /media/windows # será la que tengamos en Linux
    $ sudo mount -t vboxsf LINUX /media/windows # montaje
    
  - si quiere montar siempre que iniciemos sistema:
    
    /etc/init.d/rc.local # añadir la última línea a este fichero.  