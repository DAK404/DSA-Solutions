# Sort an array of 0s, 1s and 2s without any sorting algorithms

###########################################
# function to sort the list of 0, 1, 2
#
# Arguments used
# l1 : The list to be sorted
###########################################
def lsort(l1):

    # store the sorted elements in a list called l2
    l2 = []

    # list to store the count of every element in l1
    countL = [l1.count(0), l1.count(1), l1.count(2)]

    # a counter to append the values to the list
    c = 0 
    
    # loop to append the values to the list
    for i in range(0, 3):
        # append the values in a sorted order to the list
        for j in range(0, countL[i]):
            l2.append(c)
        # increment the counter to append the next value
        c += 1

    # print the sorted list
    print(l2)
        
        
# store the size of the list
n = int(input())

# list to store the user values
l1 = []

# ask the user to enter the elements of the list
for i in range (0, n):
    # temp variable to store the user input
    temp = int(input())

    # if temp is not 0, 1 or 2 discard the value
    if(temp > 2):
        continue
    
    # else append the value to the list
    else:
        l1.append()

# call the function to sort the list
lsort(l1)