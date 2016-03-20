"""
Problem definition: https://www.hackerrank.com/challenges/sherlock-and-the-beast
"""
import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n== 1:
        print -1
        continue
    else:
        # start with the hindsight that such numbers will always start with either 3 or 5
        # take the greedy approach of starting at the best case of starting with all 5s
        # then reduce the 5's by number of 3s which are divisible by 5
        number = '5'*n
        number_threes = 0
        while True:
            if number.count('5') % 3 == 0 and number.count('3') % 5 == 0:
                print number
                break
            else:
                number_threes += 5
                number = '5' * (n-number_threes) + '3' * (number_threes)
                if number_threes > n:
                    print -1
                    break