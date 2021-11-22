# Given an array of integers, find the minimum number of jumps to reach the end of the array.

# store the elements in List1
List1 = []

# accept the size of the list
n = int(input())

# accept the elements of the list
for i in range(0, n)
    List1.append(int(input()))

# set the index as 0 for default value
index = 0

# initialize count to be 0
count = 0

# logic to find the minimum number of jumps
while True:
    # if the index is greater than the size of the list, break and display the count
    if(index >= len(List1)-1):
        break

    # else, increment the count, and update the index
    index = index + List1[index]
    count += 1

# print the count
print(count)