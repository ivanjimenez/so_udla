#POST INSTALACIÓN DE UBUNTU

##Tareas


##### Explicación de comando sudo
	
	sudo passwd root # cambiar contraseña a root
	sudo adduser (usuario) # crear usuario
	sudo adduser <usuario> sudo
	sudo deluser <usuario>
	sudo userdel -r juan # borrar también el home
	sudo usermod -l new_user_name old_user_name # cambio de username
	usermod -d /ruta/al/directorio/nuevo/ usuario # cambiar de home
	
	sudo addgroup nombregrupo # crear grupo
	
	sudo adduser nombreusuario nombregrupo # añadir usuario a un grupo
	
	logout # salida de usuario
	su - # cambio a root
	

##### Cambiar nombre del host
sudo hostname _nuevo_host
hostname

#### Actualizaciones

	sudo apt-get update # actualización de repositorios
	sudo apt-get upgrade # actualización de qué programas tienen actualizaciones
	
	do-release-upgrade # para actualizar a la última distribución Ubuntu
	
	sudo apt-get install unattended-upgrades # isntalación de actualizaciones desantendida
	
	sudo aptitude # instalador de paquetes en modo interfaz de texto
	
	dpkg -l #paquetes instalados en el sistema

##### Idioma y teclado español:

  sudo apt-get install language-pack-es
  sudo apt-get install console-data #teclado
  sudo dpkg-reconfigure console-data # configuración de teclado
  sudo dpkg-reconfigure keyboard-configuration # configuración de tipo de teclado - importante
  sudo setupcon
  
  
##### Ayuda
man [comando]
http://manpages.ubuntu.com/manpages/quantal/es/man1/man.1.html

##### Editor Vi: 

. Cursor movement—h, j, k, l (left, down, up, and right) . Delete character—x
. Delete line—dd
. Mode toggle—Esc, Insert (or i)
. Quit—:q
. Quit without saving—:q!
. Run a shell command—:sh (use ’exit’ to return) . Save file—:w
. Text search—/

  sudo vi $HOME/.bashrc # eliminar el comentario de la linea para que se vea el shell coloreado
  . $HOME/.bashrc # para que tengo los efectos

##### Añadir estas líneas
  
  sudo vi /etc/environment
  sudo vi /etd/default/locale
  
  
  LANG=”es_ES.UTF-8″
  LC_ALL=”es_ES.UTF-8″
  LANGUAGE=”es_ES”
  
  sudo nano /var/lib/locales/supported.d/local # establecer prioridad del idioma
  sudo reboot # para los cambios
  locale # comprobar el idioma configurado
  loale -a # comprobar todos los lenguajes
  
##### Hora

sudo date --set "1 APR 2014 13:40 PM"
sudo hwclock --set --date “09/04/10 10:33:00”
sudo hwclock --show


sudo dpkg-reconfigure tzdata


##### Comandos de apt-get

sudo apt-get install [paquete] # instala paquete
sudo apt-get remove [paquete] # elimina paquete
apt-cache search [expr] | grep [expr]
apt-cache –n search ^mysql # busca los paquetes que comienzan por mysql
apt-cache showpkg mysql-server-5.0  # para ver información del paquete a instalar

##### Servicios (/etc/init.d)

sudo services --status-all
sudo services ssh status
sudo services ssh --status-all # para ver todos los estados

##### Redes Básico

######Configurar Bridge la MV 

sudo apt-get install ethtool 
ifconfig -a
ifconfig eth0
sudo ifdown eth0
sudo ifup eth0
sudo ifconfig eth0 192.168.1.5 netmask 255.255.255.0 up

sudo route add default gw 10.0.0.1 eth0

sudo /etc/init.d/networking start | stop   # para reiniciar servicios de red

##### Instalación de manpages en español

sudo apt-get install manpages-es manpages-es-extra
sudo dpkg-reconfigure locales

##### Uso del disco

$ df --total -h

#### Espacio ocupado por un archivo

$ du -ah



