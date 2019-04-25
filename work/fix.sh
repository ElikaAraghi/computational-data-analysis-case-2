#!/bin/bash
lines=`wc -l $1 | awk '{print $1}'`
counter=1
comma=','
while [  $counter -le $lines ]; do
	line=`sed "${counter}q;d" $1`
	comma_count=`echo "${line}" | awk -F"${comma}" '{print NF-1}'`
	if [ $comma_count -gt 10 ]
	then
		comma_remove_count=$((comma_count-10))
		for i in $(seq 1 $comma_remove_count);
		do
			fixed_line=`echo "${line}" | sed 's/,//3'`
			line=$fixed_line
		done
	fi
	if (($counter % 1000 == 0))
	then
		echo "Processed $counter rows"
	fi
	let counter=counter+1
done
