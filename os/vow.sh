#!/bin/bash

echo "enter a char"
read c

case $c in
	[aeiou]|[AEIOU])
		echo "voewl";;
	*)
		echo "consonent";;
esac
