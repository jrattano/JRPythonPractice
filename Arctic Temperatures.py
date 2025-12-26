antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures) ### Insert code here
lowest_temp = min(antarctic_temperatures) ### Insert code here

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature
average_temp = sum(antarctic_temperatures)/len(antarctic_temperatures)### Insert code here
round(average_temp,1)
print("Average temperature:", average_temp, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp) ### Insert code here
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")

int_value = 15
float_value = 4.1
text_value = "33"

type_of_float_value = type(float_value) # STEP 2: YOUR CODE HERE

# Convert text_value to an integer
text_value_as_int = int(text_value) # STEP 3: YOUR CODE HERE

# Convert int_value to text
int_value_as_text = str(int_value) # STEP 4: YOUR CODE HERE

# DO NOT CHANGE LINES BELOW
# Print the type of float_value
print("float_value type:", type_of_float_value)

# Adding text_value_as_int to int_value
print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

# Adding (concatenating) text values
print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)