# Question 1 : Odd or Even
# Write a Python function that takes an integer as input and returns whether the number is odd or even.

# def check_num(n):
#     n = int(n)
#     if n % 2 == 0:
#         print (f"{n} is even number")
#     else :
#         print (f"{n} is odd number")

# num =  input("Please enter a number\n")
# check_num(num)

# Question 2 : Palindrome check
# Create a Python function that checks whether a given string is a palindrome 

# Question 3: Factorial Calculation 
# Write a Python function to calculate the factorial of a given number using a loop.

# input = int(input("please enter a number:\n"))
# factorial = 1
# for i in range(2,input+1):
#     factorial = factorial * i

# print(f"factorial of {input} is {factorial}")


# Question 4 : Maximum of Three Numbers
# Implement a Python function that takes three integers as input and returns the largest of the three.

# def max_number(n1,n2,n3):
#     if n1 > n2:
#         if n1 > n3:
#             return (f"{n1} is greater")
#     elif n2 > n3:
#         return (f"{n2} is greater")
#     else :
#         return f"{n3} is greater"

# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# n3=int(input("Enter third number:"))

# print(max_number(n1,n2,n3))

# Question 5 :Count Vowels in a String 
# Write a Python function that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string.

user_input = input("Enter the string: ")
count = 0
user_input.lower()
for i in user_input:
    if i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u':
        count += 1
print(f"there is {count} vowels in {user_input}")