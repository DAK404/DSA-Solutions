# Maximum and minimum of an array using minimum number of comparisons

# Store the inputs in a list called list1
list1 = []

# Ask the user to enter the number of elements in the list
n = int(input())

# Ask the user to enter the elements of the list
for i in range(0, n):
    list1.append(int(input()))

# Sort the array in ascending order
list1.sort()

# Print the minimum and maximum elements of the list

# Print the maximum element
print(list1[len(list1)-1])

# Print the minimum element
print(list1[0])