#!/bin/bash
printf "Introducza un número\n"
read numero1
printf "Introduzca otro número\n"
read numero2
let respuesta=$numero1+$numero2
printf "$numero1 + $numero2 = $respuesta \n"
