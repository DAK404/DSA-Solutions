# --- ATTENTION ---
# SINCE THE PROGRAM IN https://geeksforgeeks.org AND THE https://450dsa.com/array
# are conflicting, please bear with me on this answer. This code is to satisfy the
# criterion speified in the 450DSA website.
# -----------------

# Merge 2 sorted arrays without using Extra space

# store the elements of the 2 lists in list1 and list2
list1 = []
list2 = []

# accept the sizes of list1 and list2
n1 = int(input())
n2 = int(input())

# accept the elements of list1
for i in range(0, n1):
    list1.append(int(input()))
    
# accept the elements of list2
for i in range(0, n2):
    list2.append(int(input()))

# sort the lists
list1.sort()
list2.sort()

# merge the lists to a single list
list1 = list1 + list2

# sort list1 again to get the correct output
list1.sort()

# print the list1
print(list1)