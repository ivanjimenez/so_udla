#!/bin/bash
veces=`who | grep $1 | wc -l`
echo "$1 está conectado $veces veces"
