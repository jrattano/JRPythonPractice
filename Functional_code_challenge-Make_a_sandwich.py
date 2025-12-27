# Add your code here
def make_sandwich(bread_type, filling, cheese="none", toasted=False):
    """
    Creates a sandwich with optional cheese and toasted state.

    Args:
        bread_type (str): The type of bread (required).
        filling (str): The filling for the sandwich (required).
        cheese (str, optional): The type of cheese (defaults to "none").
        toasted (bool, optional): Whether the sandwich is toasted (defaults to False).
    """
    if toasted == True and cheese != "none":
        return f'Making a toasted {bread_type} sandwich with {filling} and {cheese} cheese.'
    elif toasted == True:
        return f'Making a toasted {bread_type} sandwich with {filling}.'
    else:
        return f'Making a {bread_type} sandwich with {filling}.'

# Usage examples
sandwich1 = make_sandwich("wheat", "turkey", "cheddar", True)
sandwich2 = make_sandwich("rye", "ham")
print(sandwich1)
print(sandwich2)