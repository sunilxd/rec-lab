echo "Enter a no: "
read a
if [ `expr $a % 2` == 0 ]
then
	echo "$a is an even number."
else
	echo "$a is odd number."
fi
