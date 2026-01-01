"""
Coding challenge: Shopping cart
Your task: 
Write a Python program that stores a list of items in a shopping cart using a mutable data structure and then prints the contents of the shopping cart.

Create a list named shopping_cart to store the items as it allows for easy addition and removal of items.

Add the following items to the list using three separate append methods:
apple
banana
milk

Note: This could also be done with the extend method, but this example is focusing on the more common append method.

Use a for loop to iterate through each item in the shopping_cart list and print each item. Ensure you use the variable name item for each item in the list. Ensure you do not use any extra functions.

Expected output:
Shopping Cart:

apple

banana

milk
"""

# Create an empty list to represent the shopping cart
shopping_cart = []

# Add items to the shopping cart
shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")

print("Shopping Cart:")
# Print the contents of the shopping cart

for item in shopping_cart:
    print(item)