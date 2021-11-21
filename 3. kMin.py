# Kth smallest element

# store the inputs in a list called list1
list1 = []

# store the size of the list in n
n = int(input("Size:"))

# ask the user to enter the elements of the list
for i in range(0, n):
    list1.append(int(input()))

# sort the list in ascending order
list1.sort()

# ask the user to enter the kth smallest element
k = int(input("Kth:"))-1

# print the kth smallest element
if((len(list1))-1 > k):
    print(list1[k])
# reject the input if k is greater than the size of the list
else:
    print("Enter correct value")