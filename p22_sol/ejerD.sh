#!/bin/bash
if test -f $1
then 
   cat $1 
elif test -d $1
then
   cd $1;ls
else 
   echo "$1 no es un fichero ni un directorio"
fi
