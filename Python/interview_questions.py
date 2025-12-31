# 1) Count the frequency of each character in a string

s = "hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# 2) Sum of digits using recursive method

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))

# 3) Find the N largest numbers in a list

import heapq
numbers = [4, 1, 7, 3, 8, 5]
n = 2
nlarge = heapq.nlargest(n, numbers)
print(nlarge)

# or

lst = [10, 4, 3, 50, 23, 90]
n = 3

lst.sort(reverse=True)
print(lst[:n])


# 4) Print the pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
    
# 5) String operations

s = "Hello How Are You?"
words = s.split()
print(words)

# 1
print(words[1])

# 2
ls = " "
for i in range(1,4):
    ls += words[i]

print(ls)   

# print("".join(words[1:]))

# 3
str = ""
for i in words:
    str += i[0]
    
print(str)

# 6) Calculate Simple Interest

P = 20000   # Principal
R = 5      # Rate
T = 2      # Time

SI = (P * R * T) / 100
print(SI)


# 6) Longest common prefix

ls = ["flower", "flow", "floame"]

prefix = ls[0]
for word in ls[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)