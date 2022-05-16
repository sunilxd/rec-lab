echo "Enter a value:"
read a
echo "Enter b value:"
read b
d=$b

sum=`expr $a + $b`
sum1=$((a+b))
sub=`expr $a - $b`
sub1=$((a-b))
mul=`expr $a \* $b`
mul1=$((a*b))
div=`expr $a / $b`
div1=$((a/b))
mod=`expr $a % $b`
mod1=$((a%b))

echo "Add 1 = $sum"
echo "Add 2 = $sum1"
echo "Sub 1 = $sub"
echo "Sub 2 = $sub1"
echo "Mul 1 = $mul"
echo "Mul 2 = $mul1"
echo "Div 1 = $div"
echo "Div 2 = $div1"
echo "Mod 1 = $mod"
echo "Mod 2 = $mod1"
echo "Value of D = $d"
