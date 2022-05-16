echo "Enter a single character: "
read c
case $c in
[aeiou] | [AEIOU]) echo "Vowel";;
[a-z] | [A-Z]) echo "Consonent";;
[0-9]) echo "Number";;

*) echo "Entered invalid input or more than one character"
esac
