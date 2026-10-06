'''
s = '123456789'
given string s,
write a python program to calculate the sum of digits in the string s
use for loop

'''
s = '123456789'
sum_of_digits = 0
for char in s:
    sum_of_digits += int(char)
print(f"Sum of digits in the string s is: {sum_of_digits}")
