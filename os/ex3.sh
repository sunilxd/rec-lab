#!/bin/bash

echo "Enter a number"
read a

if [[ $((a%2)) == 0 ]]
then
	echo "Even"
else
	echo "Odd"
fi
