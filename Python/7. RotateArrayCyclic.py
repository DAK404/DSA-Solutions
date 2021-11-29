# Write a program to cyclically rotate an array by one.

# store the array in a list
l1 = []

# store the rotated list in l2
l2 = []

# accept the size of the array
n = int(input())

# accept the array elements
for i in range(0, n):
    l1.append(int(input()))
# add the last element to the start of the list
l2.append(l1[n-1])

# append the rest of the elements to the list
for i in range(0, n-1):
    l2.append(l1[i])

# print the rotated list
print(l2)