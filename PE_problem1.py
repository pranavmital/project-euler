#Project Euler - Problem 1

counter = 0

for i in range(1,1000):
    if (i%3==0 or i%5==0):
        counter+=i

print("The sum is:",counter)
