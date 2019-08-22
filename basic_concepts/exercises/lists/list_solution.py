# Write a program that accepts 3 integers and separate these into odd and even numbers.
# Duplicates are permited in the input but not in the output.

# Example

# >>> Enter first number: 3567
# >>> Enter second number: 789
# >>> Enter third number: 1234
# odd: {789, 3567}
# even: {1234}


odd = []
even = []

num1 = int(input("Enter first number: "))

if num1 % 2 == 1:
    odd.append(num1)
else: even.append(num1) 

num2 = int(input("Enter second number: "))

if num2 % 2 == 1:
    odd.append(num2)
else: even.append(num2) 


num3 = int(input("Enter third number: "))

if num3 % 2 == 1:
    odd.append(num3)
else: even.append(num3) 



print(f"odd: {set(odd)}")
print(f"even: {set(even)}")