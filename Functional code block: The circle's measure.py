"""
Your task:
Write a Python function using a precise descriptive name like calculate_diameter_circle while also incorporating snake case.

The function should take one argument: radius (with a float type hint).

It should calculate the diameter of a circle (diameter = radius * 2) and return it. As there is no requirement for the radius to be a whole number, you should assume a return of float. You have been given the instructions that if the user sends in a negative radius, the function should return -1 to indicate an error, as a negative radius is not a common situat. 

Include a clear and informative docstring explaining the function's purpose, arguments, and return value, also using type hints.

Tips:
Follow the naming convention guidance (snake_case).

Make sure your docstring is well-formatted and easy to understand, including type hints.

Keep your function concise and focused.

Do not perform any input; just define the function.

Example input:
With simple values radius = 7 and radius = 2.5.

With edge cases like radius = 0, radius = -3, and a large value like radius = 1000000.

Expected output:
Radius: 7, Diameter: 14

Radius: 2.5, Diameter: 5.0

Radius: 0, Diameter: 0

Radius: -3, Diameter: -1

Radius: 1000000, Diameter: 2000000
"""

# Add your code here
def calculate_diameter_circle(radius: float) -> float:
    """
    Function calculates diameter of circle using formula diameter = radius * 2
    It accepts input as float and returns float
    """
    if radius < 0:
        return -1
    else:
        diameter = radius * 2
    return diameter