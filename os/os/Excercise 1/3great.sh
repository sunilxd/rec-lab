echo "Enter three number: "
read a b c
if [ $a -ge $b -a $a -ge $b ]
then
	echo "$a is greater"
else
	if [ $b -ge $c ]
	then
		echo "$b is greater"
	else
		echo "$c is greater"
	fi
fi
