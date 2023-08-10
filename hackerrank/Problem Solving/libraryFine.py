
import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def library_fine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        return 10000
    elif y1==y2:
        if m1>m2:
            res = (m1-m2) * 500
            return res
            
        elif m1==m2:
            if d1>d2:
                res = (d1-d2) * 15
                return res
            else:
                return 0
        else :
            return 0
    else:
        return 0
    