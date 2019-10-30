#!/bin/bash
#:<<EOF	
#function funtest(){
#	a=$1
#	b=$2
#	return $(($a+$b))
#{}
#funtest 45 55
#echo $?
#EOF

demoFun1(){
	return 0
}
demoFun1
echo $?

if demoFun1
then
	echo True
else
	echo Flse
fi
