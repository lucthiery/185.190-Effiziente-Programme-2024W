#!/bin/bash

#prof BM:   155,414,886,890      cycles
#benchmark_v1: 157,245,632,747      cycles

# Ensure proper usage
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 file1 file2 file3 file4"
    exit 1
fi

# Input files
file1=$1
file2=$2
file3=$3
file4=$4

# Temporary sorted files
sorted_f1=$(mktemp)
sorted_f2=$(mktemp)
sorted_f3=$(mktemp)
sorted_f4=$(mktemp)

# Sort the files by their respective join fields
sort -t, -k1 "$file1" > "$sorted_f1"
sort -t, -k1 "$file2" > "$sorted_f2"
sort -t, -k1 "$file3" > "$sorted_f3"
sort -t, -k1 "$file4" > "$sorted_f4"

# Join the files step by step
join -t, -1 1 -2 1 "$sorted_f1" "$sorted_f2" | \
    join -t, -1 1 -2 1 - "$sorted_f3" | \
    sort -t, -k4 | \
    join -t, -1 4 -2 1 - "$sorted_f4"

# Cleanup
rm "$sorted_f1" "$sorted_f2" "$sorted_f3" "$sorted_f4"
