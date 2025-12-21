# Create lists for Celius and Fahrenheit
celsius_temperature = []
fahrenheit_temperatures = []

# Set list to take input for celsius_temperature
input_temperatures = input("Enter temperature in celsius separated by commas: ")

# Split the input string into a list and convert to integers
celsius_temperatures = [int(temp) for temp in input_temperatures.split(",")]

# Start celsius loop to go through celsius_temperatures and covert and append to fahrenheit_temperature []
for celsius in celsius_temperatures:
    fahrenheit = ((int(celsius) * 9/5) + 32)
    fahrenheit_temperatures.append(fahrenheit)
# Print the results
print("Temp C:", celsius_temperatures)
print("Temp in F:", fahrenheit_temperatures)