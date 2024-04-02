# Functions
# Author: Jean
#26 Feb 2024

# Recieve user input whilst asking for their credit card number 
# if user input is 123456, reply with "No seriously, what is your cred card num", and ask them for their number again

# Create a function called say_hello
#   It's going to print "hello"

# def say_hello():
#     print("Hello!")



# # Create a function called say_hello_params
# # Print "Hello {param}!"

# def say_hello_params(name):
#     print(f"Hello {name}! ")

# say_hello_params("Jim")

# say_hello()

# #create a function called how_big
# # Takes a number as an input/param
# #   it returns how big the number is 

def how_big(num):
    if num < 0:
        return "Very small"
    if num < 10: 
        return "Pretty small"
    if num < 1000: 
        return "Pretty big"
    return "REALLY BIG"

print(how_big(-1))
result = how_big(1_000_000)
print(result)

#Create a function called adder
    # accpets two inputs that are numbers
#   Return the sum of both number

def adder (x: int,y: int):
    return x + y 

# print(adder(1,3))
result = adder(1,4)
print(result)

