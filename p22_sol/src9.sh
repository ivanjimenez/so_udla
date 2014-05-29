#!/bin/bash
echo -e "Dime el pid\n"
read pid
if kill -9 $pid
then 
 echo  Proceso terminado
else 
 echo No existe pid
fi
