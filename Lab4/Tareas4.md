###Lab 4.1:

 Crear un programa en Python (o en tu lenguaje preferido) la implementación del algoritmo FCFS de Administración de Discos. Como ejemplo, se tiene la siguiente lista de peticiones. (La cabeza está inicialmente en el cilindro 1000):
 
 requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
 

###Lab 4.2

Escribe una función dir_info(directorio) la cual devuelve dos valores:

1) El número de archivos dentro del directorio.
2) El número de directorio dentreo del directorio


def dir_info(dircetory):
    # nfiles = how many files inside directory?
    # ndirs  = how many sub directories inside directory?
    return nfiles, ndirs
 
Indicaciones: 


 * Visualiza el módulo: http://docs.python.org/2/library/os.html
 * Utiliza las siguientes funciones: os.walk

 