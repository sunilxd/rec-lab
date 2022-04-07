echo "enter a number"
read a
a1=0
a2=1
temp=0
echo $a1
echo $a2
((a-=2))
while [ $a -gt 0 ]
do
    temp=$((a1+a2))
    echo $temp
    a1=$a2
    a2=$temp
    ((a--))
done
echo done
