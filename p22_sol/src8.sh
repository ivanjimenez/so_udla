#!/bin/bash
for archivo in `ls`
do 
  test -d $archivo && ls $archivo
done
