# print("Arithmetic Operations")

# print(10+2)
# print(10-2)
# print(10/2)
# print(10*2)
# print(10%2)
# print(10**2)

# a = 10
# b = 20
# b += a
# print(b)

# a,b = 9, 420
# print(type(a))
# print(type(b))

# a = int(6.9)
# b = float(69)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# 1. WAPP to print the given number if it is -ve then print it in +ve format 
# a = -10

# if (a < 0):
#   a *= -1
#   print(a)
# else:
#   print(a)

# 2. WAPP to check if given number is odd or even
# a = 68
#
# if a % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# 3. Armstrong Number
# 4. Palindrome
# 5. Spy Number

# the sum of digits = product of digits
#
# a = int(input("Enter a number: "))
#
# sum = 0
# product = 1
#
# while a != 0:
#     digit = a % 10
#     sum += digit
#     product *= digit
#     a //= 10
#
# if sum == product:
#     print("It's Spy Number")
# else:
#     print("It's not Spy Number")

# Fibonacci Series using while loop

# series = 10
# numOne = 0
# numTwo = 1
#
# while series > 0:
#     print(numOne, end=" ")
#     numThree = numOne + numTwo
#     numOne = numTwo
#     numTwo = numThree
#     series -= 1

# 6. Perfect Number
# 7. neon number
# 8. fibonacci number
# 9. prime number
# 10. happy number

# For loop

# for x in range(1, 11):
#     print(x, end=" ")

# for i in range(4):
#     print("*", end=" ")


# square pattern

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n = int(input("enter number: "))
#
# for i in range(n):
#     print("")
#     for j in range(n):
#         print("*", end=" ")

# hollow square
n = 5

# *  *  *  *  *
# *           *
# *           *
# *           *
# *  *  *  *  *

print("Hollow Square Star Pattern")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end='  ')
        else:
            print(' ', end='  ')
    print()