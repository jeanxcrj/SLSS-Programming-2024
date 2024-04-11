#Alex
#loops
#apr 5

for _ in range(10):
    print("something")
    
grocery_list = [
    "a",
    "b",
    "c",
    "d",
    "e"
]

for item in grocery_list:
    print("----")
    print(f"{item}")

    if item == "e":
        break

for i in range(10):
    if i%2 == 0:
        print(f"{i} is an even number")

#while True:
   # print("This is an infinite loop")

   #ASk the user if they like icecrean
   # if they dont answer yes or no
    #Repeat the question

user_answer = input(" Do you like ice cream?").lower().strip(",.?!")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input("Seriously, do you like ice cream?").lower().strip(",.?!")

if user_answer in ["yes", "yeah"]:
    print("Nice, I love ice cream too!")
elif user_answer in ["no", "nah"]:
    print("How could you not like ice cream!!!")

