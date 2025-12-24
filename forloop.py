max_value = 50

# Your code here
for max_value in range(0, max_value + 1):
    if max_value % 3 == 0 and max_value % 4 == 0:
        print (max_value)

# Even and odd practice

numbers = [3, 9, 1, 10, 5, 2, 8]

for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
        
## Timer Practice
for i in range(10, -1, -1):
    print(i)
    if i == 5:
        print("Halfway point reached!")