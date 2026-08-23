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
ls = [23, 34, 45, 56, 67, 78, 80, 90, 85, 85, 85, 90, 70]

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



import random

sys = random.randint(1, 10)

tries = 0
while True:
    user = int(input("Enter a number between 1 to 10: "))   
    
    if user < 1 or user > 10:
        print("Invalid input. Please try again.")
        continue
    
    if user == sys:
        tries += 1
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break
    
    elif user < sys:
        tries += 1
        print("Oops! Too low! Try again.")
    
    elif user > sys:
        tries += 1
        print("Oops! Too high! Try again.")
    
    else:
        tries += 1
        break
    