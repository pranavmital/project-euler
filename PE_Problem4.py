# Project Euler Problem 4
# Pranav Mital

# function to check if a number is a palindrome

def isPalindrome(n):
    flag = 0
    str_n = str(n)
    for i in range((len(str_n)//2)):
        if str_n[i] != str_n[len(str_n)-1-i]:
            flag += 1
    if flag != 0:
        return False
    else:
        return True

# main script

largest_palindrome = 0

for i in range(100,1000): #nested for loop to try all combinations of 3-digit numbers
    for j in range(100,1000):
        num_p = i*j
        if isPalindrome(num_p):
            if num_p>largest_palindrome:
                largest_palindrome = num_p

print("The largest palindrome made from the product of two 3-digit numbers is:",largest_palindrome)

