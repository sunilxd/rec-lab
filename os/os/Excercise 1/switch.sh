echo " enter first number:"
read num1
echo "enter second number:"
read num2
echo "+ ADDITION"
echo "- SUBTRACTION"
echo "* multiplication"
echo "/ division"
echo "enter your choise: "
read ch

case "$ch" in
#case 1:
#add = num1 +num2
#break;
'+') r=`expr $num1 + $num2`
echo "ADDITION = $r";;
'-') r=`expr $num + $num2`
echo "DIFFERENCE = $r";;
esac 
