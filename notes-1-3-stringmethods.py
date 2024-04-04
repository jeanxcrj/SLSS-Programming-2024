# Methods (strings)
# Author: Jean
# 22 Feb 2024


# Ask the user whta the weahter is ike

# if they reply rainy
    # Bring an unbrella

weather = input("What's the weather like?")

weather = weather.strip("!,?.@#$%^& ")

weather = weather.title()

weather = weather.lower()

if weather == "rainy" :
    print("You'll need an umbrella")
else: 
    print(f"sorry, I don't understand {weather}")