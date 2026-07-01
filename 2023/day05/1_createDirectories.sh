#!/bin/bash

#chmod +x createDirectories.sh
#./createDirectories.sh day 1 10

dirName=$1
start=$2
end=$3

for (( i=$start; i<=$end; i++ ))
do
    mkdir "${dirName}${i}"
done

echo "Directories created successfully"