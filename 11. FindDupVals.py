# Find the Duplicate Number in an Array

# store the elements in ListA
listA = []

# accept the size of the list
n = int(input())

# initialize the repeated element value to be 0
rep_val = 0

# accept the elements of the list
for i in range(0, n):
    listA.append(int(input()))

# logic to find the duplicate element
for i in range(0, n):
    #count the number of times the element is repeated
    temp = listA.count(listA[i])

    # if the element is repeated more than once
    if(temp >= 2):

        # store the repeated element value
        rep_val = listA[i]

# print the repeated element value
print(rep_val)