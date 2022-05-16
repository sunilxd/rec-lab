#!/bin/bash
echo "Enter a number"
read n
sum=0
for (( i=0; i<n; i++ ))
do
	sum=$((sum+i))
done
echo "The sum of given number is: $sum"
