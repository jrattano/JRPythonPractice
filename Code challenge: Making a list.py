"""
Code challenge: Making a list
Your Task:
Write the Python code required to take a list of numbers as input and return a new list containing only the unique numbers from the original list, maintaining their original order, and then print the result.

Tips:
Sets are designed to store unique elements.

Use set() to only get the unique numbers from the original array.

Save the results in the unique_set variable.

Example input:
Python

numbers = [1, 2, 2, 3, 1, 4, 5, 3]

Expected output:
[1, 2, 3, 4, 5]
"""
# Values provided (do not change)
array = [1, 2, 2, 3, 1, 4, 5, 3]

# The following line will need to change to only store unique values
unique_set = set(array) #your code here

# List conversion and print provided (do not change)
unique_array = list(unique_set)
print(unique_array)