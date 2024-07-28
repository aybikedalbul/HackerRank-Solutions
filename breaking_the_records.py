#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    
    score_best = scores[0]
    max_count = 0
    
    score_worst = scores[0]
    min_count = 0

    for score in scores[1:]:
        if score > score_best:
            score_best = score
            max_count += 1
        
        elif score < score_worst:
            score_worst = score 
            min_count += 1
    
    return max_count, min_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
