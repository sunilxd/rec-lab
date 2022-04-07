echo "enter a number"
read a
prod=1
for (( i=1;i<=a; i++))
do
    prod=$((prod*i))
done
echo $prod
