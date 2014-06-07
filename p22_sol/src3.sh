#!/bin/bash 
#if [ $# -ne 2 ]
if [ $# -ne 2 ]
then 
  echo -e "Introduzca sólo dos parámetros\n./scr3.sh nom_fich_fuente nom_fich_destino\n"
  exit 1
fi 
fuente=$1
destino=$2
if [ -f $fuente ] && [ -f $destino ]
then
  echo Son fichoros ambos
  cp $fuente $destino
fi  
