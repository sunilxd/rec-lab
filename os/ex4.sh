#!/bin/bash

echo "enter a"
read a
echo "enter b"
read b
echo "enter c"
read c

if [[ $b -ge $a ]]
then
	a=$b
fi
if [[ $c -ge $a ]]
then
	a=$c
fi

echo "greatest number $a"
