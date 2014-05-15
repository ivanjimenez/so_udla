#!/bin/bash
read var
case $var in
[Ss]) echo opción sí
;;
[N]|[n]) echo opción no
;;
1) echo opción 1
;;
DOS) echo opción DOS
;;
*) echo Ninguna opción # por defecto
;;
esac
