#!/bin/bash
select respuesta in "Ver contenido directorio actual" \
            "Salir"
        do
            echo Ha seleccionado la opción: $respuesta
            case $REPLY in
            1) ls .
            ;;
            2) break
            ;;
            esac
done