echo "Enter a number:"
read n
sum=0
while [ $n != 0 ]
do
sum=`expr $sum + $n`
n=`expr $n - 1`
done
echo "SUM = $sum"
