# What are the data types in pyhton ? List any 4 with examples
# difference b/w implicit and explicit type conversion with examples
# explain the operators in python with examples

# SMART TEMPERATURE CONVERTOR :- Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.(Use explicit type conversion and arithmetic operators.)
# Formula: F = (C * 9/5) + 32 and K = C + 273.15
temp_celsius = float(input("Enter the temperature in celsius : "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
temp_kelvin = temp_celsius + 273.15
print(f'Temperature in Fahrenheit: {temp_fahrenheit}')
print(f'Temperature in Kelvin: {temp_kelvin}')

# BILL SPLIT CALCULATOR :- Write a program that takes total bill amount and number of friends as input.Calculate how much each person will pay.Also print the data type of each variable used.
total_bill = float(input("Enter the total bill amount: "))
number_of_friends = int(input("Enter the number of friends: "))
amount_per_person = total_bill / number_of_friends
print(f'Each person will pay: {amount_per_person}')
print(f'Total Bill Amount data type: {type(total_bill)}')