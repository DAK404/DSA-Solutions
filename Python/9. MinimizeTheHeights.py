# Minimize the heights of the towers

###########################################
# Function to Minimize the heights of the 
# towers
#
# Arguments used
# l1: List of heights of the towers
# k: The offset to be applied to heights
###########################################
def maxHeight(l1, k):

    for i in range(0, len(l1)):
        if(l1[i] - k <= 0):
            l1[i] = l1[i] + k
        elif(l1[i] - k > 0):
            l1[i] = l1[i] - k
        print(l1)
    maxList = max(l1)
    minList = min(l1)
    diff = maxList - minList
    print(diff)

# store the sizes of the towers
n = int(input())

# Store the inputs in a list called list1
l1 = []

# Ask the user to enter the elements of the list
for i in range(0, n):
    l1.append(int(input()))

# Ask the user to enter the offset
k = int(input())

# Call the function
maxHeight(l1, k)