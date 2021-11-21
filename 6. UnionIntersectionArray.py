# Find the Union and Intersection of the two sorted arrays

# store the input in two lists
l1 = []
l2 = []

# store the union in unionList
unionList = []

# store the intersection in intersectionList
intersection = []

# accept tthe sizes of the list
n1 = int(input())
n2 = int(input())

# accept the elements of the list1
for i in range(0, n1):
    l1.append(int(input()))

# accept the elements of the list2
for i in range(0, n2):
    l2.append(int(input()))

# sort list1 and list2
l1.sort()
l2.sort()

# union of the two lists
unionList = l1 + l2

# intersection of the two lists
for i in range(0, len(l1)):
    for j in range(0, len(l2)):
        if(l1[i] == l2[j]):
            intersection.append(l1[i])

# remove the repeated values in the list
unionList = list(set(unionList))

# print the union and intersection
print("Union: ", unionList)
print("intersection: ", intersection)