#!/bin/bash
# ./while1.sh  par1 par2 par3 ...

while [ ! -z $1 ]
do 
	echo Parámetro: $1
	shift
done
