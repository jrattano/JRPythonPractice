age= int(input("Enter your age: "))

if age < 12:
    price = 8
elif age <=64:
    price = 12
else:
    price = 10

print("Your ticket price is $" + str(price))
print("Your age is : " + str(age) + ".")