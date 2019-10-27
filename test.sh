#!/bin/bash

num1=23
num2=33
:<<!
if test $[num1] -lt $[num2]
then
	echo "greater than"
else
	echo "less than"
fi
!

if [ $num1 -eq $num2 ]
then 
	echo "equal"
elif [ $num1 -gt $num2 ]
then
	echo "greater than"
elif [ $num1 -lt $num2 ]
then
	echo "less than"
else
	echo "erro"
fi
