#!/usr/bin/env python3

"""Simple fizzbuzz generator.

This script prints out a sequence of numbers from a provided range
with the following restrictions:

 - if the number is divisible by 3, then print out "fizz",
 - if the number is divisible by 5, then print out "buzz",
 - if the number is divisible by 3 and 5, then print out "fizzbuzz".
"""

def fizzbuzz(num_start, num_end):
    """return status number 1 do 100"""
    if num_start%3==0 and num_start%5!=0:
        print(f'Fizz - {num_start}')
    elif num_start%3!=0 and num_start%5==0:
        print(f'Buzz - {num_start}')
    elif num_start%3==0 and num_start%5==0:
        print(f'FizzBuzz - {num_start}')
    else:
        print(num_start)
    
    if num_start != num_end:
        num_start+=1
        return fizzbuzz(num_start, num_end)


if __name__=='__main__':
    fizzbuzz(1, 100)
