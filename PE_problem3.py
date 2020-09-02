# Project Euler Problem 3
# Pranav Mital

import math

# function to check if a number is prime

def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

# main script

largest_prime_factor = 0 # initialised

for i in range(2,int(math.sqrt(600851475143))):
    print("Evaluating factor",i)
    if isPrime(i) and 600851475143 % i == 0:
        largest_prime_factor = i

print("\nLargest Prime Factor of 600851475143 is:",largest_prime_factor)

