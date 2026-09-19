# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
        
# if sum == n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")
        

# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1 

# if count == 2:
#     print(f"{n} is a prime number.")
# else:   
#     print(f"{n} is not a prime number.")


# Reverse string
# str = "AMITKUMAR"

# for i in range(len(str)-1, -1, -1):
#     print(str[i], end="")


# str = "MADAM"
# rev = ""
# for i in range(len(str)-1, -1, -1):
#     rev += str[i]
     
# if str == rev:
#     print(f"{str} is a palindrome.")
# else:
#     print(f"{str} is not a palindrome.")


# str = "kanak"
# res = ""
# for i in str:
#     res = i + res
# print(res)



# str = "P@#yn26at^&i5ve"
# char = 0
# digit = 0
# symbol = 0
# for i in range(len(str)):
#     if str[i] >= "A" and str[i] <= "Z" or str[i] >= "a" and str[i] <= "z":
#         char += 1

#     elif str[i] >= "0" and str[i] <= "9":
#         digit += 1
        
#     else:
#         symbol += 1
        
# print(f"Characters: {char} \nDigits: {digit} \nSymbols: {symbol}")

# for i in str:
#     if i.isalpha():
#         char += 1
#     elif i.isdigit():
#         digit += 1
#     else:
#         symbol += 1
# print(f"Characters: {char} \nDigits: {digit} \nSymbols: {symbol}")


# a = 1
# while a <= 5:
#     print(a)
#     a += 1

#reverse number
# a = 256
# n = a
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
    
# if rev == a:
#     print(f"{a} is a palindrome.")
# else:
#     print(f"{a} is not a palindrome.")
    

# Positive/Negative number count
# ls = [-34, -45, 56, 75, -89, 90, -100, 23, -1, 0, 34, -67]
# pos = []
# neg = []
# for i in ls:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# print(f"Positive: {sorted(pos)} \nNegative: {sorted(neg)}")



# Second max number
# ls = [23, 34, 45, 56, 67, 78, 80, 90, 85, 85, 85, 90, 70]

# max = ls[0]
# sec_max = ls[0]
# for i in ls:
#     if i > max:
#         sec_max = max
#         max = i
#     elif i > sec_max:
#         sec_max = i

# print("Second max number =", sec_max, "\nMax number =", max)


# def second_largest(numbers):
#     unique = list(set(numbers))
#     print(unique)

#     unique.sort()
#     print(unique)

#     print(unique[-2])

# second_largest(ls)


    
# Check sorted list
# ls = [1, 1, 2, 4, 5]

# for i in range(len(ls) - 1):
#     if ls[i] <= ls[i+1]:
#         continue
#     else:
#         print("Not sorted")
#         break
# else:
#     print("Sorted")


# d = {}
# for i in ls:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# Find duplicates
# b = [2,3,1,2,3]
# seen = set()
# duplicates = []
# for i in b:
#     if i in seen and i not in duplicates:
#         duplicates.append(i)
#     seen.add(i)
# print("Duplicate elements:", duplicates)

# print(ord('😎'))


# a = {10:100, 20:200, 30:300, 40:400}
# b = {40:500, 50:500, 60:600, 70:700}

# for i in b:
#     if i in a:
#         a[i] += b[i]
#     else:
#         a[i] = b[i]
# print(a)


# Frequency of each character

# result = {}
# for num in ls:
#     result[num] = result.get(num, 0) + 1

# print(result)



# import random

# sys = random.randint(1, 10)

# tries = 0
# while True:
#     user = int(input("Enter a number between 1 to 10: "))   
    
#     if user < 1 or user > 10:
#         print("Invalid input. Please try again.")
#         continue
    
#     if user == sys:
#         tries += 1
#         print(f"Congratulations! You guessed the number in {tries} tries.")
#         break
    
#     elif user < sys:
#         tries += 1
#         print("Oops! Too low! Try again.")
    
#     elif user > sys:
#         tries += 1
#         print("Oops! Too high! Try again.")
    
#     else:
#         tries += 1
#         break
    


# DSA New Questions----------------------------------------------------------------------------
# 
# 1. Find Pairs With Given Sum
# ls = [2,3,4,5,6,7]
# key = 7

# for i in range(len(ls)):
#     for j in range(i+1, len(ls)):
#         if ls[i] + ls[j] == key:
#             print(ls[i], ls[j])


# arr = [2, 4, 3, 5, 7, 8, 1]
# target = 9

# seen = set()

# for num in arr:
#     complement = target - num

#     if complement in seen:
#         print(complement, num)

#     seen.add(num)


# seen = {}
# for i, num in enumerate(arr):
#     complement = target - num

#     if complement in seen:
#         return [seen[complement], i]
    
#     seen[num] = i


# Prefix

strings = ["flower", "flow", "flight"]

prefix = ""

for chars in zip(*strings):
    if len(set(chars)) == 1:
        prefix += chars[0]
    else:
        break
print(prefix)


# str = "madam"
# print("Palindrome") if str == str[::-1] else print("Not palindrome")


# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40}
# result = {}
# for key in dict1:
#     result[key] = dict1[key]
# for key in dict2:
#     result[key] = dict2[key]
# print(result)


# from collections import Counter
# arr = [1, 2, 2, 3, 1, 2, 4, 3]
# frequency = Counter(arr)
# print(dict(frequency))


# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 5, "c": 10, "d": 15}
# result = Counter(dict1) + Counter(dict2)
# print(dict(result))


# sentence = "python is easy and python is powerful"
# words = sentence.split()
# frequency = Counter(words)
# print(dict(frequency))


# def fun(*args, **kwargs):
#     print("Args : ", args)
#     print("Kwargs : ", kwargs)

# fun(5,6,4,6,8,9,44, name="Amit", age=21, salary=24000)



# ls = [1,1,2,3,4,5,6,3,3,1,2]
# res = list(dict.fromkeys(ls))
# res2 = list(set(ls))
# print(res)
# print(res2)


# def typeof(func):
#     def wrapper(n):
#         print(type(n))
#         func(n)
#         print(type(res))
#         # return res
#     return wrapper

# @typeof
# def check_type(n):
#     return int(n[:])

# n = "123"
# check_type(n)


arr = [1, 2, 3, 2, 4, 1, 5, 3,2,3]
seen = set()
duplicates = set()
for item in arr:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(list(duplicates))
print(list(seen))

# arr = [1, 2, 3, 4, 5]

# k = 6
# k = k % len(arr)
# print(arr[-k:])
# print(arr[:-k])
# arr = arr[-k:] + arr[:-k]
# print(arr)



# arr = [(1, 5), (2, 3), (3, 8), (4, 1)]
# n = len(arr)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j][1] > arr[j + 1][1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print(arr)


# arr.sort(key=lambda x: x[1])
# print(arr[::-1])


# n = 23
# count = 0
# for i in range(2, n):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print(f"{n} is Prime Number")
# else:
#     print(f"{n} is not Prime Number")


# matrix = [
# [10, 25, 5],
# [40, 15, 30],
# [8, 50, 20]
# ]
# maximum = matrix[0][0]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > maximum:
#             maximum = matrix[i][j]

# print(maximum)


# Armstrong Number
# n = 153
# digits = str(n)
# power = len(digits)
# total = 0
# for i in digits:
#     total += int(i) ** power

# print(total)
# if n == total:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# Integer to Roman number converter
s = 'CLXXIX'
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

total = 0
for index, symbol in enumerate(s):
    value = roman[symbol]
    if index + 1 < len(s) and value < roman[s[index + 1]]:
        total -= value
    else:
        total += value

print(total)


# valid parenthesis
# def isValid(s: str) -> bool:
#         stack = []
#         for i in range(len(s)):
#             if s[i] in "([{":
#                 stack.append(s[i])
#             else:
#                 if len(stack) == 0:
#                     return False

#                 if ((stack[-1] == '(' and s[i] == ')') or
#                     (stack[-1] == '{' and s[i] == '}') or
#                     (stack[-1] == '[' and s[i] == ']')):
#                     stack.pop()
#                 else:
#                     return False

#         return len(stack) == 0

# print(isValid("({[]}[])"))

# ls = [1,2,3,3,4,4,5]
# seen = set(ls)
# print(len(seen))



# 35. Serach insert position

# def searchInsert(nums: list[int], target: int) -> int:
#     left, right = 0, len(nums)

#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid

#     return left

    # for i in range(len(nums)):
    #     if target <= nums[i]:
    #         return i
    # return len(nums) 


# print(searchInsert([2, 3, 5, 6, 8, 9], 4))


# 58. Length of Last Word

# With function
# str = " Hello word"
# print(len(str.strip().split()[-1]))

# without function
# def lengthOfLastWord(str):
#     last = len(str) - 1
#     length = 0

#     while str[last] == ' ':
#         last -= 1
#     while last >= 0 and str[last] != ' ':
#         length += 1
#         last -= 1
 
#     return length

# print(lengthOfLastWord("   fly me   to   the moon  "))


# 66. Plus one
def plusOne(digits: list[int]):
    # for i in range(len(digits) - 1, -1, -1):
    #     if digits[i] < 9:
    #         digits[i] += 1
    #         return digits        
    #     digits[i] = 0
    # return [1] + [0] * len(digits)

    # Notheer solution
    i = len(digits) - 1
    while i >= 0:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        i -= 1

    return [1] + digits

# print(plusOne([1, 2, 3]))
# print(plusOne([3, 2, 9]))
# print(plusOne([9, 9]))



# 67. Add Binary
# def addBinary(a: str, b: str):
#     return bin(int(a, 2) + int(b, 2))[2:]

# a = "1010"
# b = "1011"
# print(addBinary(a, b))


# 9. Sqrt(x)
# def sqrt(x):
#     left = 0
#     right = x
#     ans = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if mid * mid <= x:
#             ans = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     return ans
# print(sqrt(8))


# Newton's Approach
# def mySqrt(x):
#     if x == 0:
#         return 0
#     guess = x
#     while guess * guess > x:
#         guess = (guess + x // guess) // 2
#     return guess

# print(mySqrt(8))

stars = "***************234*****************"
count = 0
for i in stars:
    if i == '*':
        count += 1
print(count)


# 258. Add digits
def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

print(addDigits(404))