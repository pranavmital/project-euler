# Project Euler Problem 2
# Pranav Mital

fibo_series = [1,2] # ATQ series has to start from 1 and 2
n = len(fibo_series)-1
print(fibo_series)
fibo_term = 0
fibo_even_sum = 2 #includes 2 in the sum

while fibo_term < 4000000:
    fibo_term = fibo_series[n] + fibo_series[n-1]
    if fibo_term % 2 == 0:
        fibo_even_sum += fibo_term
    fibo_series.append(fibo_term)
    n = len(fibo_series)-1 # can also write n += 1

print("The sum is:",fibo_even_sum)



