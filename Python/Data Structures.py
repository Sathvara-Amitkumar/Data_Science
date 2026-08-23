a = {12, 23, 34, 45, 56, 67, 78, 89}

# b = hash("Hello World")
# c = hash((123456, 123465, 13465))
# print(c)
# print(b)

# a.add(90)
# a.remove(34)
# a.pop()
# a.clear()
# print(a)


# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(b.difference(a))
# s = a | b
# print(s)


# d = {10:100, 20:200, 30:300, 40:400}

# d[50] = 500
# del d[20]
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

# for i  in d:
#     print(i, ":", d[i])
    
# help(list)

# a = [1,2,3,4,5]
# b = a.copy() # Shallow Copy
# b = a # Deep Copy
# b[0] = 100
# print(a)
# print(b)


# a = {1:'one', 2:'two', 3:'three'}
# b = {4:'four', 5:'five', 6:'six'}

# for i in b:
#     a[i] = b[i]
# print(a)

# Counting frequency of elements in a list
# a = [1,1,1,1,2,2,2,3,3,4,4,5,5,5,5,8,9,9]

# d = {}
# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# a = {10:100, 20:200, 30:300, 40:400}
# b = {40:500, 50:500, 60:600, 70:700}

# for i in b:
#     if i in a:
#         a[i] += b[i]
#     else:
#         a[i] = b[i]
# print(a)


# Exception handling

# a = int(input("Enter number: "))
# try:
#     print(10/a)
# except Exception as e:
#     print("Error occurred:", e)
# else:
#     print("No error occurred")
# finally:
#     print("I Don't care if error occurs or not!")    

# print("Program continues...")





# ls = ["flower", "flow", "floame"]

# prefix = ls[0]
# for word in ls[1:]:
#     while not word.startswith(prefix):
#         prefix = prefix[:-1]

# print(prefix)


# ls = [2,3,4,5,6,4]

# for i in range(len(ls)-1):
#     if ls[i] <= ls[i+1]:
#         continue
#     else:
#         print("List is not sorted!")
#         break
# else:
#     print("List os Sorted!")


x = int(input("Enter no : "))
try:
    print(10 / x)
except ZeroDivisionError as z:
    print("ERROR :", z)
