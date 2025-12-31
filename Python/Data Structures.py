# ls = [-34, -45, 56, 75, -89, 90, -100, 23, -1, 0, 34, -67]
# pos = []
# neg = []
# for i in ls:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# print(f"Positive: {sorted(pos)} \nNegative: {sorted(neg)}")




# ls = [23, 34, 45, 56, 67, 78, 89, 90]

# sum = 0
# for i in ls:
#     sum += i

# print(f"Sum: {sum/len(ls)}")



# ls = [23, 34, 45, 56, 67, 78, 89, 90]

# max = ls[0]
# for i in ls:
#     if i > max:
#         max = i

# print(f"Max element in list is {max} and its index is {ls.index(max)}")
 
 
# ls = [23, 34, 45, 56, 67, 78, 80, 90, 85]

# max = ls[0]
# sec_max = ls[0]
# for i in ls:
#     if i > max:
#         sec_max = max
#         max = i
#     elif i > sec_max:
#         sec_max = i

# print(sec_max, max)



# ls = [1, 1, 2, 4, 5]

# for i in range(len(ls) - 1):
#     if ls[i] <= ls[i+1]:
#         continue
#     else:
#         print("Not sorted")
#         break
# else:
#     print("Sorted")

# c = (10,20,30)
# print(c[2])

# a = (50,)
# print(type(a))


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
# print(a.difference(b))
# s = a | b
# print(s)


d = {10:100, 20:200, 30:300, 40:400}

# d[50] = 500
# del d[20]
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

# for i  in d:
#     print(i, ":", d[i])
    
# help(dict)

# a = [1,2,3,4,5]
# b = a.copy() # Shallow Copy
# # b = a # Deep Copy
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

a = int(input("Enter number: "))
try:
    print(10/a)
except Exception as e:
    print("Error occurred:", e)
else:
    print("No error occurred")
finally:
    print("I Dont care if error occurs or not!")    

print("Program continues...")
