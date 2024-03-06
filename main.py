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

#    * * * * *
#    * * * * *
#    * * * * *
#    * * * * *
#    * * * * *

# n = int(input("enter number: "))
#
# for i in range(n):
#     print("")
#     for j in range(n):
#         print("*", end=" ")

# hollow square

#    *  *  *  *  *
#    *           *
#    *           *
#    *           *
#    *  *  *  *  *

# print("Hollow Square Star Pattern")
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end='  ')
#         else:
#             print(' ', end='  ')
#     print()

# X pattern
# *   *
#   *
# *   *

# print("X pattern")
# for i in range(n):
#     for j in range(n):
#         if i == j or j == n-1-i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# *
# *   *
# *       *
# *   *   *   *
#
# *   *   *   *
# *       *
# *   *
# *

#
# print("Hollow triangle Star Pattern")
# for i in range(n):
#     for j in range(n):
#         if i == j or i == n - 1 or j == 0:
#             print("*", end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
# print()
#
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i + j == n - 1 or j == 0:
#             print("*", end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
#
# for i in range(n):
#     for j in range(n):
#         if i + j == n - 1 or j == n - 1 or i == n - 1:
#             print("*", end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
# print()
#
# for i in range(n):
#     for j in range(n):
#         if i == j or i == 0 or j == n - 1:
#             print("*", end='  ')
#         else:
#             print(' ', end='  ')
#     print()

# Solid star triangle
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end='  ')
#     print()
#
# print()
#
# for i in range(n):
#     for j in range(n):
#         if i + j >= n - 1:
#             print("*", end='  ')
#         else:
#             print(" ", end="  ")
#     print()
#
# print()
#
# for i in range(n):
#     for j in range(n):
#         if i + j <= n - 1:
#             print("*", end='  ')
#         else:
#             print(" ", end="  ")
#     print()
#
# print()
#
# for i in range(n):
#     for j in range(n):
#         if i <= j:
#             print("*", end='  ')
#         else:
#             print(" ", end="  ")
#     print()
#
# print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i + j >= n - 1:
#             print("*", end='  ')
#         else:
#             print(" ", end="  ")
#
#     for k in range(n):
#         if i >= k + 1:
#             print("*", end='  ')
#         else:
#             print(" ", end="  ")
#     print()


# def is_leap(year):
#     leap = False
#     if (year % 4 == 0) and (year % 100 == 0):
#         if year % 400 == 0:
#             leap = True
#         elif (year % 4 == 0) and (year % 100 != 0):
#             leap = True
#         else:
#             leap = False
#
#
# year = int(input())


# def solveMeFirst(a, b):
#     return a + b
#
#
# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1, num2)
# print(res)

# WAPP to sum the elements in the list
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# summation = 0
#
# for i in arr:
#    summation += i
#
# print(summation)

n = 5

for i in range(n):
    for j in range(n):
        if i == j or j == n-1-i:
            print(n-i, end=" ")
        else:
            print(" ", end=" ")
    print()