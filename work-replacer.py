# Replacer 
# Author: Jean
# 26 Feb 2024

# create function called tranlsate  that takes a string and replaces any  100 s with  💯 (a hundred points symbol) and also replaces  noodles  with  🍜
# Create a  main  function that asks the user for input and then uses the  translate  function

# def translate(string):
#     return input(string).strip("!@#$%^&*,.<")

# prompt =  translate("")

# print(translate(""))

def translate(prompt: str):
    translated_string = prompt.replace("100", "💯").replace("noodles", "🍜")
    return translated_string

def main():
    user_input = input("Enter '100' or 'noodles'!")

    result = translate(user_input)
    print("Here is the translated string:", result)

main()