#!/bin/bash

echo "enter two values"
read a b

echo "Which operation do you want to perform(+ - * /)"

read c

case "$c" in
	+)
		x=$((a+b)) ;;
	-)
		x=$((a-b)) ;;
	\*)
		x=$((a*b)) ;;
	/)
		x=$((a/b)) ;;
	*)
		x="unexptected operation" ;;
esac

echo "output is $x"
