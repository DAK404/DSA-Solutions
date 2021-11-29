# Move all negative numbers to beginning and positive to end with constant extra space

# store the size of the list
size = int(input())

# stores the negative values in list1
list1 = []

# stores the positive values in list2
list2 = []

# ask user to enter the values
for i in range(0, size):
    temp = int(input())

    # if temp is negative, store it in list1
    if(temp < 0):
        list1.append(temp)

    # if temp is positive, store it in list2
    else:
        list2.append(temp)

# add the positive values to the end of list1
list1 = list1 + list2

# print the list1
print(list1)