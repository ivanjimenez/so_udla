#!/bin/bash

echo -e "Escribe fichero o directorio\n"
read var
if [ -f $var ]
then 
  cat $var | less
elif [ -d $var ]
then
  cd $var; ls .
else "$var no es ni fichero ni directorio\n"
fi

