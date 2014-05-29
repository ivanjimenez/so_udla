#!/bin/bash
        echo El nombre del programa es $0
        echo El número total de parámetros es $#
        echo Todos los parámetros recibidos son $*
        echo Todos los parámetros recibidos son $@
	echo El primer parámetro recibido es $1
        shift
        echo El segundo parámetro recibido es $1
        shift
        echo El tercer parámetro recibido es $1
        echo El cuarto parámetro recibido es $2
