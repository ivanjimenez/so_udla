#!/bin/bash

select opcion in "Estadísticas de memoria" \
            "Estadísticas de Sistema" \
            "Salir"
          do
            case $REPLY in
	    1) echo "Introduzca el tiempo de intervalo para estadísticas de memoria: "
	       read x
               echo "Recogiendo estadísticas..." 
	       if vmstat $x 7 > mem_stat.txt
	           then echo "Estadística de MV creada"
               else echo "Error al recolectar estadística de MV"
	       fi
               ;;
	    2) echo "Recogiendo estadísticas..."
	       if sar > system_stat.txt 
	           then echo "Estadísticas de sistema recogidas"
	       else echo "Error"
	       fi
	       ;;
	    3) break;;
	    esac
          done
