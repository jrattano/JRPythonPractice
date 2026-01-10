"""
Coding challenge: Simple list membership check
Your task: 
Write a pytest test function called test_contains_five that tests if the contains_five function correctly checks if contains_five(my_list) contains 5. 

Tips:
Assume the contains_five function has already been written. This test is verifying the contains_five function works as intended when given a list containing the number 5.

Use the assert statement to check if the result of contains_five(my_list) is True.
"""

def test_contains_five():
    """
    Tests the 'contains_five' function.
    """
    # Example list for testing
    my_list = [1, 3, 5, 7, 9]
    # Write your Python assert below
    import pytest
    
    assert contains_five(my_list) is True
