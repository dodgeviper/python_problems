"""
https://www.hackerrank.com/challenges/sherlock-and-squares
Good example of Intermedidate Value theorem: https://en.wikipedia.org/wiki/Intermediate_value_theorem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

t = int(raw_input().strip())
for a0 in xrange(t):
    a,b = map(int, raw_input().strip().split(' '))
    print int(math.floor(b**(0.5))) - int(math.ceil(a**(0.5))) + 1