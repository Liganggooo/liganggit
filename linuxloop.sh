#!/bin/bash
:<<EOF
list="1 2 3 4 5 6 10"
for i in $list
do
	echo "列表中的元素有：$i"
done
EOF
#while满足条件时返回TRUE
:<<!
int=1
while(( $int<=5 ))
do
	echo $int
	let "int++"
done
!
:<<!
#until满足条件时返回FLASE
a=1
until [ ! $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done

while :
do
	echo "请输入1~4中的一个数字："
	echo "（输入q退出）"
	read num
	case $num in
		1) echo "你选择了1"
		;;
		2) echo "你选择了2"
		;;
		3) echo "你选择了3"
		;;
		4) echo "你选择了4"
		;;
		q) echo "退出"
			break
		;;
		*) echo "您的输入有误，请重新输入！"
	esac
done
!
for((i=1;i<=6;i++));do
	echo $i
done



