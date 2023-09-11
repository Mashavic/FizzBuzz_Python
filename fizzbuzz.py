#!/usr/bin/env python3

def fizzbuzz(num_start, num_end):
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
