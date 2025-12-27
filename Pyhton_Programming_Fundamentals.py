"""
Functional code block: Temperature conversion tool
Your task:
Write three Python functions that implement a simple temperature conversion tool. Be careful to spell the method names correctly.

celsius_to_fahrenheit(celsius): Takes a temperature in Celsius and converts it to Fahrenheit.

fahrenheit_to_celsius(fahrenheit): Takes a temperature in Fahrenheit and converts it to Celsius.

convert_temperature(temperature, unit): Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit). It calls the appropriate conversion function based on the unit and returns the converted temperature.

Tips:
Remember these formulas:

fahrenheit = (celsius * 9/5) + 32

celsius = (fahrenheit - 32) * 5/9

Make sure you are returning values as floating-point numbers; do not round.
"""

# Add your code here
def celsius_to_fahrenheit(celsius):
    """Takes a temperature in Celsius and converts it to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
## Test celsius to fahrenheit
print(celsius_to_fahrenheit(25))

def fahrenheit_to_celsius(fahrenheit):
    """Takes a temperature in Celsius and converts it to Fahrenheit."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius
## Test fahrenheit to celsius
print(fahrenheit_to_celsius(77))

def convert_temperature(temperature, unit):
    """ Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit). It calls the appropriate conversion function based on the unit and returns the converted temperature."""
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        print ("invalid unit entered")
        return none
