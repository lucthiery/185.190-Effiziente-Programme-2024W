join -t, --check-order <(sort -t, -k1 $1) <(sort -t, -k1 $2)|
    join -t, --check-order - <(sort -t, -k1 $3)|
    sort -t, -k4 |
    join -t, --check-order -1 4 -2 1 - <(sort $4)