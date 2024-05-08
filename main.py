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

# giveStr = "mihir"
# for i in range(len(giveStr) - 1, -1, -1):
#     print(giveStr[i], end=" ")

# a = ["ram", "raju", "ramadhir", "ramu"]
# b = a[1]
# newIndexOne = b[::-1]
#
# a.pop(1)
# a.insert(1, newIndexOne)
# print(a)

# a = ["ram", "raju", "ramadhir", "ramu"]
# b = a[::-1]
#
# print(b)

# a = ["ram", "raju", "ramadhir", "ramu"]
# rev = []
#
# for i in range(len(a)):
#     word = a[i][::-1]
#     rev.append(word)
#
# print(rev)
#
# a = []
# n = int(input("enter the matrix: "))
# for i in range(n):
#     a.append([])
#     for j in range(n):
#         element = int(input("Enter element: "))
#         a[i].append(element)
#
# print(a, end="")

# a = []
# n = int(input(""))
#
# for i in range(n):
#     ele = input("")
#     v = [int(x) for x in ele.split(" ")]
#     a.append(v)
#
# print(a)

# TUPLE

# a = [1]
# b = (1)
# print(type(a))
# print(type(b))  # will return class int
#
# c = (1,)
# print(type(c))  # class <tuple>
#
# d = [1, 2, 3, 4, 5]
# d[1] = 6
# print(d)  # [1,6,3,4,5]
#
# e = (1, 2, 3, 4, 5)
# e[1] = 6
# print(e)  # TypeError: "tuple" object doesn't support item assignment

# Second max no in tuple
#
# f = (10, 7, 9, 85, 69, 45)
#
# firstMax = 0
# secondMax = 0
#
# for i in range(len(f)):
#     if firstMax < f[i]:
#         secondMax = firstMax
#         firstMax = f[i]
#     elif secondMax < f[i] < firstMax:
#         secondMax = f[i]
#
# print(secondMax)

# Append at an index TUPLE

# a = (1, 2, 3, 4, 6)
# new_a = list(a)
# new_a.insert(len(new_a) - 1, 5)
# added_element = tuple(new_a)
# print(added_element)

# WAPP to remove duplicate element in a tuple

# a = (1, 2, 3, 3, 3, 4, 5)
# b = tuple(set(a))
# print(b)


# a = (7, 2)
# b = (7, 8)
#
# output = []
#
# for x in a:
#     for y in b:
#         output.append((x, y))
#
# for y in b:
#     for x in a:
#         output.append((y, x))
#
# print(output)
#
# i = [1,2,6,7,8]
# i.insert(9)
# print(i)

# x = [i**+1 for i in range(3)];
# # print(x)
#
# list = [True, 50, 10]
# list.insert(2,5)
# print(list, "Sum is: ", sum(list))
#
# a = [14,52,7]
# b = a.copy()
# print(b)
# print(b is a)
#
# a = list((45,) * 4)
# print((45) * 4)
# print(a)
#
# val = [
#     [3, 4, 5, 1],
#     [33, 6, 1, 2]
# ]
#
# v = val[0][0]
# print(v)
# for i in val:
#     for e in i:
#         if v > e:
#             v = e
#             print(v)

# SUM OF LIST IN ELEMENT USING FUNCTION
#
# def sumElements(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
#
#
# list = [1, 2, 3, 4]
# print(sumElements(list))


# WAPP PRINT THE Max and min number using function in a list

# def minAndMaxNums(nums):
#     if not nums:  # Check if the list is empty
#         return "List is empty"
#
#     maximum = nums[0]
#     minimum = nums[0]
#     for num in nums:
#         if maximum < num:
#             maximum = num
#         if minimum > num:
#             minimum = num
#
#     return "Max No: " + str(maximum) + " and Min No: " + str(minimum)
#
#
# numbers = [10, 20, 30, 40, 50]
# print(minAndMaxNums(numbers))

# FUNCTIONS

# WAPP TO ADD 2 numbs using function
#
#


# newList = [10, 20, 30]
# print(max(newList))

# print max num in a list using function
#
# def maxNumInTheList(nums):
#     if not nums:  # Check if the list is empty
#         return "List is empty"
#
#     maximum = nums[0]
#     for num in nums:
#         if maximum < num:
#             maximum = num
#
#     return "Max No: " + str(maximum)
#
#
# newList = [10, 20, 30]
# print(maxNumInTheList(newList))

# print second min num in a list using func

# def secondMinNumInList(nums):
#     if not nums:  # Check if the list is empty
#         return "List is empty"
#
#     firstMin = float('inf')
#     secondMin = float('inf')
#     for num in nums:
#         if firstMin > num:
#             secondMin = firstMin
#             firstMin = num
#         elif num < secondMin and num != firstMin:
#             secondMin = num
#
#     return "Sec min No: " + str(secondMin)
#
#
# newList = [10, 20, 30, 40]
# print(secondMinNumInList(newList))

# LAMBA FUNCTION
#
# v = lambda a: a + 30
# print(v(60))


# def add(s):
#     return lambda a: a * s
#
#
# v = add(20)
# print(v(10))

# wapp to print num 1-5 using recursion

def printNums(n):
    if n == 0:
        return
    printNums(n - 1)
    print(n)


printNums(5)
