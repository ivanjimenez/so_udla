#!/bin/bash
# kill_proc.sh

echo -e "Dime el pid del proceso que quieres eliminar:"
read PID
`kill -9 $PID`
