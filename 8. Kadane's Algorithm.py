# Kadane's Algorithm

###########################################
# function implementing Kadane's Algorithm
#
# Arguments used
# a : The list to be reversed
# size : The size of the list
###########################################
def kadane(a,size):

    # Initialize the max_so_far
    max_so_far =a[0]

    # Initialize the current maximum value
    curr_max = a[0]
    
    # implement the kadane's algorithm
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
    
    # return the maximum value
    return max_so_far

a = [1, 2, 3, -2, 5]
print(kadane(a,len(a)))