echo "enter a number"
read a
sum=0
for (( i=1; i <= a; i++ ))
do
    sum=$((sum+i))
done
echo "sum is $sum"
