# Import a powerful tool called "pandas" that you'll use to work with and organize data easily
import pandas as pd
import os 

file_name = 'grocery_list.csv'

if os.path.exists(file_name):
    # Load the grocery list from the CSV file
    grocery_list_df = pd.read_csv(file_name)

    # Extract the items from the DataFrame and store them in a list
    grocery_list = grocery_list_df['item'].tolist()

    # Print the grocery list and inspect the output
    print(grocery_list)
else:
    print(f"Error: The file '{file_name}' was not found in the current directory.")
    print("Please ensure you have followed the instructions on the Coursera site to extract the files from the zip archive.")

# Add "Kiwis" and "Raspberries" to the list
items_to_add = ["Kiwis", "Raspberries"]

# Add items to the grocery list 
for item in items_to_add:
    grocery_list.append(item) 

# Print the grocery list to see the added items
print(grocery_list)

# 1. Get user input
new_item = input("Enter an item to add to your grocery list: ")  # Ask the user for an item and store their input
# 2. Add the item to the list
grocery_list.append(new_item)  # Add the new item to the end of the grocery list

# 3. Print the updated list
print("Here's the updated list:")
print("Updated list:", grocery_list)  # Show the user the updated grocery list

# Add "Cinnamon" and "Paprika" to the grocery list
grocery_list.append("Cinnamon") 
grocery_list.append("Paprika") 

# Print the updated grocery list
print("\nYour Updated Grocery List:")
print(grocery_list)

# Remove "Eggs" and "Apples" from the grocery list
grocery_list.remove("Eggs")
grocery_list.remove("Apples") 

# Print the updated grocery list
print("\nYour Updated Grocery List (after removing items):")
print(grocery_list)