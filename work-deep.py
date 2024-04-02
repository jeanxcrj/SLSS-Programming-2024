# Deep Thought: Answer to life, universe, and everything
# Author: Jean
# 20 Feb 2024


#Import time for better UX
import time

# Greet the user 
print("Hello there. Today, I would like  to bring you on a transformative journey ")

#pause for one second
time.sleep(1)

# ask the user for their thoughts on the meaning of life; collect user input 
#If answer is 42 or any variants, reply yes
#If the answer is anything else, reply no

answer = input("So, in your humble opinion, what is the Answer to life, the uinverse, and everything?")

if answer == "42" or answer == "fourty-two" or answer == "fourty two" or answer == "forty two" or answer == "forty-two": 
    print("yes")
else:
    print("no")