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
# #
# n = 6
# for i in range(n):
#     for j in range(n):
#         if i + j >= n - 1:
#             print("*", end='  ')
#         else:
#             print(" ", end="  ")
#     print()

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
#
# n = 5
#
# for i in range(n):
#     for j in range(n):
#         if i == j or j == n-1-i:
#             print(n-i, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# def round_up_to_multiple_of_5(n):
#     remainder = n % 5
#
#     # If the remainder is 0, the number is already a multiple of 5, so return it.
#     if remainder == 0:
#         return n
#
#     # Otherwise, add 5 to the remainder and return the result.
#     return n + (5 - remainder)
#
#
# print(round_up_to_multiple_of_5(71))

# WAPP to print even num in the list

# list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for i in list:
#     if i % 2 == 0:
#         print(i, end=" ")

# WAPP to print even index element in the list

# list = [12, 21, 36, 8, 7, 9, 23]

# 12, 36, 7, 23
#
# for i in range(len(list)):
#     if i % 2 == 0:
#         print(list[i], end=" ")

# WAP to print the sum of the element in the list
# list = [12, 21, 36, 8, 7, 9, 23]
#
# sum = 0
# for i in list:
#     sum += i
#
# print(sum)

# WAPP to print the max num in the list

# list = [12, 21, 36, 8, 7, 9, 23]
#
# max = 0
#
# for i in range(len(list)):
#     if max < list[i]:
#         max = list[i]
#
# print(max)

# wapp to print the second maximum in the list
#
# list = [12, 21, 36, 8, 7, 9, 23]
#
# firstMax = 0
# secondMax = 0
#
# for i in range(len(list)):
#     if firstMax < list[i]:
#         max = list[i]
#         secondMax = max
#     elif secondMax < list[i] and secondMax != max:
#         secondMax = list[i]
#
# print(secondMax)

# WAPP to sort the element in list
# list = [12, 21, 36, 8, 7, 9, 23]
#
# length = len(list)
#
# for i in range(length):
#     for j in range(i+1, length):
#         if list[i] > list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
#
# print(list)

# if([]):
#     print("a")
# else:
#     print("b")

# a=[1,2,3]
# for i in a:
#       print(i+1,end=" ")
#
# x=7
# y = 3
# print(x%y)

# a=10
# b=20
# a,b = b,a
# print("a =", a,"b =",b)

# i = 1
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#
#     i += 1
#
# x=7
# y = 3
# print(x//y)
#
# x=[1,2,3]
# print(x*2)

# a = []
# n = int(input())
# for i in range(n):
#     ele = int(input())
#     a.append(ele)
#
# print(a)
#
# a = input()
# l = [int(x) for x in a.split(' ')]
# print(l)

