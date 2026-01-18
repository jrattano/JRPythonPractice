"""
Activity 1: Making Decisions with Conditional Statements
Introduction
As a data analyst for an online book store, you're tasked with analyzing customer purchasing patterns. The marketing team wants to send special discount codes to customers based on the number of books they’ve purchased. If a customer has purchased enough books, they’ll receive a discount. If they’ve purchased more, they might qualify for an even better discount.

Task 1: Define a Discount Function
You need to write a function that helps the marketing team decide which customers should receive a discount.

Define a function called send_discount that accepts two arguments:

books_purchased: The number of books a customer has purchased.
discount_threshold: The minimum number of books a customer needs to purchase to receive a discount.
The function must print either of the two possible messages, as shown below. Be careful not to miss the punctuation in your print statement.

Discount applied! if the customer qualifies for a discount.
No discount. if the customer does not qualify.
Example:
send_discount(books_purchased=3, discount_threshold=5)
# Output: No discount.

send_discount(books_purchased=7, discount_threshold=5)
# Output: Discount applied!
Code Template:
"""

def send_discount(books_purchased, discount_threshold):
    if books_purchased < discount_threshold:
        print("No discount.")
    else:
        print("Discount applied!")
    pass

"""
Hints:
Hint 1
Use an if statement to check if books_purchased meets or exceeds the discount_threshold.
Hint 2
Use a print statement to display the correct message.
Test Your Function:
"""
# Checking your results 
send_discount(3, 5)  # Should print No discount.
send_discount(7, 5)  # Should print Discount applied!

"""
No discount
Discount aplied!

Task 2: Add Logical Branching for Multiple Discount Levels
The store offers an additional promotion: If a customer purchases more than a certain number of books, they’ll receive an even bigger discount. Update your function to include this second level of discounts.

Add an additional argument, bonus_threshold, which represents the number of books needed to receive the better discount.

The function must print one of three possible messages, as shown below. Be careful not to miss the punctuation in your print statement.

Big discount applied! if the customer qualifies for the higher discount.
Discount applied! if the customer qualifies for the regular discount.
No discount. if they do not qualify for any discount.
Example:
send_discount(books_purchased=3, discount_threshold=5, bonus_threshold=10)
# Output: No discount.

send_discount(books_purchased=7, discount_threshold=5, bonus_threshold=10)
# Output: Discount applied!

send_discount(books_purchased=12, discount_threshold=5, bonus_threshold=10)
# Output: Big discount applied!
Code Template:
"""

def send_discount(books_purchased, discount_threshold, bonus_threshold):
    ### YOUR CODE HERE ###
    if books_purchased < discount_threshold:
        print("No discount.")
    elif books_purchased >= discount_threshold and books_purchased < bonus_threshold:
        print("Discount applied!")
    else:
        print("Big discount applied!")
    pass

"""
Hints:
Hint 1
Start by checking if the customer qualifies for the big discount using an if statement.
Hint 2
Use an elif to check if they qualify for the regular discount.
Hint 3
Use an else statement to handle cases where they don't qualify for any discount.
Test Your Function:
"""

# Checking your results 
send_discount(3, 5, 10)   # Should print No discount.
send_discount(7, 5, 10)   # Should print Discount applied!
send_discount(12, 5, 10)  # Should print Big discount applied!

"""
No discount.
Dicount applied!
Big discount applied

Activity 2: Using Loops for Repetitive Tasks
Introduction
You are a product manager at a technology startup. Customers have been providing ratings for the company's latest app. The marketing team wants to categorize this feedback into three categories: "Low", "Medium", and "High" ratings. You will use Python's iteration techniques to process customer ratings efficiently.

Task 1: Categorize Customer Ratings
Define a function called categorize_ratings that takes a list of customer ratings as input. Each rating is a whole number between 1 and 10.

Your function will categorize the ratings as:

Low (1-4)
Medium (5-7)
High (8-10)
The output must print three statements, one for each category, in the following order (Low, then Medium, then High):
Low: {number_of_low_ratings}
Medium: {number_of_medium_ratings}
High: {number_of_high_ratings}

Example:
# There are two ratings in the range 1-4, two ratings in the range of 5-7 and two ratings in the range 8-10
categorize_ratings([1, 3, 5, 7, 8, 9])
Output:
Low: 2
Medium: 2
High: 2

Code Template:
"""

def categorize_ratings(rating_list):
    # YOUR CODE HERE
    low_count = 0
    medium_count = 0
    high_count = 0
    for rating in rating_list:
        if 1 <= rating <= 4:
            low_count += 1
        elif 5 <= rating <= 7:
            medium_count += 1
        elif 8 <= rating <= 10:
            high_count += 1
    pass

# Checking your results 
# Calling categorize_ratings([1, 3, 5, 7, 8, 9])
categorize_ratings([1, 3, 5, 7, 8, 9])
print("Expected Output:\nLow: 2\nMedium: 2\nHigh: 2")
"""
Expected Output:
Low: 2
Medium: 2
High: 2

Activity 3: Sorting Test Scores with Error Handling
Introduction
You are a coder working with test scores, focusing on sorting techniques and error handling in Python. You’ll use common sorting algorithms and write robust functions that account for possible errors.

Task 1: Creating and Sorting Test Scores
You have a list of students and their corresponding test scores. Your task is to organize and analyze the scores using sorting algorithms and Python's error-handling mechanisms.

Step 1: Create the List of Students
Create a list called students that contains the following student names: John, Lisa, Mary, Chris, Linda, Matt
"""

### YOUR CODE HERE ###
students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]
"""
Step 2: Create a Dictionary of Test Scores
Create a dictionary called test_performance and assign the following scores to each student as follows:

John: 87
Lisa: 90
Mary: 75
Chris: 100
Linda: 100
Matt: 70
"""
### YOUR CODE HERE ###
test_performance = {"John": 87, "Lisa": 90, "Mary": 75, "Chris": 100, "Linda": 100, "Matt": 70}

"""
Step 3: Extract the Scores from the Dictionary
Create a list called scores and extract each student's score using a for loop.
"""
### YOUR CODE HERE ###
scores = []
for student in students:
    scores.append(test_performance[student])
"""
Step 4: Sorting the Scores with a Custom Function
Define a function called bubble_sort that sorts the list of scores in ascending order.
"""
### YOUR CODE HERE ###

def bubble_sort(score_list):
    n = len(score_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if score_list[j] > score_list[j+1]:
                score_list[j], score_list[j+1] = score_list[j+1], score_list[j]
    return score_list
"""
Step 5: Assign the Sorted Scores to sorted_scores
Call the bubble_sort function you defined above and assign the return value to sorted_scores.
"""

### YOUR CODE HERE ###
sorted_scores = bubble_sort(scores)
"""Hints for Activity 3 - Task 1:
Hint 1
Sorting: For the bubble_sort function, focus on comparing and swapping elements.
Test Your Results:¶
"""
# Checking your results 
print(sorted_scores)

"""
Task 2: Calculating and Handling Errors
Step 1: Calculate the Highest and Lowest Scores
Use the sorted_scores list you defined above to assign the correct values to highest_score and lowest_score below.
"""
### YOUR CODE HERE ###
highest_score = sorted_scores[-1]
lowest_score = sorted_scores[0]

print(highest_score)
print(lowest_score)

"""
Step 2: Define a Function to Calculate the Class Average
Define a function called average_class_score to calculate the average score. Add error handling for cases when the student list is empty.

### YOUR CODE HERE ###
"""

def average_class_score(input_scores):
    if input_scores is None:
        raise ValueError("The student list is empty.")
    try:
        sumofscores = sum(input_scores)/len(input_scores)
    except ZeroDivisionError as e:
        print("Error: Cannot calculate average for an empty list.")
        return 0
    return sumofscores
"""
Step 3: Calculate the Average Score
Use the average_class_score function you defined above to assign the average score to average_score below.
"""
### YOUR CODE HERE ###"""
average_score = average_class_score(sorted_scores)

"""
Step 4: Handle the Case of an Empty Class
Check that the average_class_score function can handle an empty class list by running the following code.
"""
empty_class = []
empty_scores = []
error_average = average_class_score(empty_scores)

"""
Hints for Activity 3 - Task 2:
Hint 1
Error Handling: Use try-except blocks to handle division by zero when calculating the average score.
Test Your Results:
"""

# Checking your results 
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

print(f"Average Score: {average_score}")