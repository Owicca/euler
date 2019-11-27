#!/usr/bin/env python3

#get sum of even fibonacci numbers up to 4 000 000
upper_limit = 4000000

def fib(limit = 10, arr = []):
    a = b = 1

    while(True):
        if b >= limit:
            break
        temp = a + b
        a = b
        b = temp

        arr.append(b)

fib_numbers = []
fib(upper_limit, fib_numbers)

even_fib_total = 0
for number in fib_numbers:
    if number % 2 == 0:
        even_fib_total += number

print(even_fib_total)
