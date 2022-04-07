#!/bin/bash

echo "enter a b"
read a b

echo "1.addition"
echo "2.addition"
echo "3.multiplication"
echo "4.divison"
echo ""
echo "enter your choice"
read ch

case "$ch" in
	1)
		c=$((a+b))
		;;
	2)
		c=$((a-b))
		;;
	3)
		c=$((a*b))
		;;
	4)
		c=$((a/b))
		;;
esac
echo ""
echo $c
