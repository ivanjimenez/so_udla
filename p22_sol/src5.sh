#!/bin/bash
select opcion in "Ver directorio actual" \
            "Copiar ficheros" \
            "Editar ficheros" \
            "Imprimir fichero" \
            "Salir del menú"
          do
            case $REPLY in
            1)    ls -l|more
                  ;;
            2)    echo "Introduzca [nom_fuente] [nom_destino]"
                  read x y
                  cp $x $y
                  read x
                  ;;
            3)    echo "¿Nombre de fichero a editar?"
                  read x;
		  vi $x
                  ;;
            4)    echo "¿Nombre de fichero a imprimir?"
                  read x
                  cat $x
     		  ;;
            5)    clear; break
                  ;;
	    esac 
done
