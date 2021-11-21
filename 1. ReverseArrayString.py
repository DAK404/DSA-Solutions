#Write a program to reverse an array or string


###########################################
# function to reverse the list/array
#
# Arguments used
# listOne : The list to be reversed
# start : The starting index of the list
# end : The ending index of the list
###########################################
def reverseArray(listOne, start, end):
    while start < end:
        listOne[start], listOne[end] = listOne[end], listOne[start]
        start +=1
        end -=1
        
# Driver Code

# Store the inputs in a list called listOne
listOne = []

# Ask the user to enter the number of elements in the list
var = int(input())

# Ask the user to enter the elements of the list
for i in range(0, var):
    listOne.append(input())

# Reverse the list
reverseArray(listOne, 0, len(listOne)-1)

# Print the reversed list
print(listOne)