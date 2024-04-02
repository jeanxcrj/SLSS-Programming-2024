# Mcdobot
# Author: Jean
# 22 Feb 2024

#Write a McDo not that asks if you want fries with your meal
    # It should accept Yes/yes or No/no as inputs


#Import Time to improve UX
import time 


#Greet user 
print("Beep bop🤖..Hello there! 🍟")

#Pasue for 1 sec
time.sleep(1)

#Introduce bot and Ask user if they want fries with order
print("Welcome to McDonalds! I am McDo bot")

#Pasue for 1 sec
time.sleep(1)

#store input
fries = input("Would you like fries with your order today?😋🍟 (yes/no)").strip("!,?.@#$%^& ").title().lower()

# respond accordingly
if fries == "yes":
    print("Yay! Here's your meal with fries! Have a great day 🍟")
elif fries == "no":
    print("Ok... Here's your meal without fries 🍔")
else:
    print(f" Sorry, I dont understand {fries}. Please respond with (yes/no)😞")