#TYPE COMVERSIONS - Converting one data type --> other data type
# EXPLICIT TYPE CONVERSION - Converting one data type to another data type using predefined functions
num1 = int(input("Enter first number: "))  # Input is taken as string

string= str(num1)
print(num1) ; print(type(num1))
print(string) ; print(type(string))

# IMPLICIT TYPE CONVERSION - Automatically converting one data type to another data type by Python interpreter

x= 5 ; print(type(x))  # int
y= 2.5 ; print(type(y))  # float
z= x + y  # int + float --> float
print(z) ; print(type(z))
