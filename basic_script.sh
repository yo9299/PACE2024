#!/bin/bash

for file in $(find ./test/ -name *.gr)

do
	python3 main.py $file
done

#for file in $(find ./test -name *.gr)
#for output in $(find ./test -name *.gr)
#do pace2024verifier $file $output
