#  Unit 1 Activity - Weather predictor
#  Author:Jean 
#  03/04/2024

import time
#It should have all of the following:
# At least one conditional that uses if, elif, and else ✅
# At least one input() function call ✅
# At least one print() function call ✅
# At least one custom function that you've created:✅
#   the function should have at least one parameter✅
#   the function should also return a value
# Named unit-1-activity.py ✅
# Contain a header at the top of the file ✅

#Creat function for weather prediction
def predict_weather(user_input):
    if "cloudy" in user_input.lower():
        return "It might rain today, so don't forget your umbrella!🫣 "
    elif "foggy" in user_input.lower():
        return "Hmm... might be quite cold today. Wear a jacket! 🥶"
    elif "clear" in user_input.lower():
        return "Looks like a sunny day ahead. Enjoy the sunshine! 😉"
    else:
        return "I'm not too sure about the weather; ask me about cloudy/foggy/clear!"

#Main Program --
def main():
    print("Hey there! I'm your weather predictor:) Let's check the weather together 😁")
    time.sleep(1)
    #Input function call
    user_input = input("Is the sky clear, foggy, or cloudy?")

    prediction = predict_weather(user_input)

    #Print Function call
    print(prediction) 

    time.sleep(1)
    #Ask again
    user_input = input("Ask again! Is the sky clear, foggy, or cloudy?")
    prediction = predict_weather(user_input)
    print(prediction) 

    time.sleep(1)
    print("Have a great day! Bye!")

main()
    

    
