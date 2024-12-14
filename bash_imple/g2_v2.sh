#!/bin/bash

#prof BM:      155,414,886,890      cycles
#benchmark_v1: 157,245,632,747      cycles
#benchmark_v2: 166,587,475,365      cycles


# Input files
file1=$1
file2=$2
file3=$3
file4=$4

# Sort the files by their respective join fields and join in one pipeline
join -t, -1 1 -2 1 <(sort -t, -k1 "$file1") <(sort -t, -k1 "$file2") | \
    join -t, -1 1 -2 1 - <(sort -t, -k1 "$file3") | \
    sort -t, -k4 | \
    join -t, -1 4 -2 1 - <(sort -t, -k1 "$file4")

