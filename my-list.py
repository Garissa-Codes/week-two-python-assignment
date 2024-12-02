# Creating an empty list
my_list = []

# Appending the elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position
my_list.insert(1, 15)

# Extending my_list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# Finding and printing the index of the value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)