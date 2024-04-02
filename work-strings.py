# In **VS Code**, create a file named, `work-strings.py`
import time 
# 1. Greets the user
#2. Asks the user's name
# 3. Asks them 3 question
# 4. Responds specifically to those question
# 5. Says goodbye using the user's name

# Greeting
print("Hello! Hope you're having a great day")

time.sleep(1)

# Asking for name
print("What is your name?")

name = input ()

print(f"Hi {name}! Nice to meet you :)")

time.sleep(1.5)

print("You seem like an intersting person, and I'd like to learn a bit about you")

time.sleep(1)

#Q1
print("So to begin, what is your favourite food?")

food = input ()

print(f"Mmmmm😋.. I love {food} too!")

time.sleep(1)

#Q2
print("Now, what is your favourite colour?")

favcolour = input ()

if favcolour == "purple" :
    print("GREAT CHOICE! PURPLE IS THE BEST!")
else:
    print(f"I see... {favcolour} is cool.. I think purple is the better colour tho 😆")

time.sleep(1)

#Q3

print("My last question for you today is...what is your facourite animal!")

animal = input ()

if animal == "dog" :
    print("REAL DOGS ARE THE BEST!")
else:
    print(f"{animal}.. thats a cool animal!")

time.sleep(1)

# saying goodbye 
print (f"Well, thanks for taking the time to let me know you! Have a great rest of your day {name} !")