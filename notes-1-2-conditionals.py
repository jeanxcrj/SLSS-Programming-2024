# Conditionals
# Author: Jean
# 15 Feb 2024

# Implement the flowchart from notes

# x = 1000000

# y = -5.7

# x = input("what is your x 2")

# y = input("what is your y ")

# If x is less than y, say so 
# IF x is greater htan y, say so
# If x is equal to y, say so


# if x < y: 
#     print( " x is less than y" )
# if x > y:
#     print(" x is greater than y")
# if x == y:
#     print( " they are equal!")


# if x < y: 
#     print( " x is less than y" )
# elif x > y:
#     print(" x is greater than y")
# else:
#     print( " they are equal!")


foo = int(input("Enter a number")) #string

if foo < -1 or foo == 0:
    print( "Foo is less than 1")
    print( "or it's equal to zero.")
#check if foo is inside a range 
# greater than 1 and less than 1000
    
if foo > 1 and foo < 1000:
     print( "Foo is in the range of 2 to 999")
else:
    print(" Foo is outside the range 2 to 999")