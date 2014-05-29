#!/bin/bash 
#if [ $# -ne 2 ]
if $# != 2
then 
  echo -e "Introduzca sólo dos parámetros\n./ejerC.sh nom_fich_fuente nom_fich_destino\n"
  exit 1
else 
  cp $1 $2
  echo "Copia realizada"
fi
