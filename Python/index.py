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


# str = "MADAMa"
# rev = ""
# for i in range(len(str)-1, -1, -1):
#     rev += str[i]
    
# if str == rev:
#     print(f"{str} is a palindrome.")
# else:
#     print(f"{str} is not a palindrome.")


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
    