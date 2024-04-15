#Notes - Dictionaries 

#Big ideas:
# - A dictionary is a data structure
# - Dictionaires map keys to values 

#Flashback to lists
person_dict = {

    "name": "John",
    "age": "23 years old",
    "cc num": "4500 1023 2222 1111",
    "height": "5ft6",
    "Pronouns": "He/they"

}

# Get and print the person's name(?)
# print(person[0]) #use the index
# print(person[2]) #last item in list 
# print(person[-1]) #start counting from the end

#print(person[10]) #code will break.

#Grad values from a dic
# print(person_dict["name"])
# print(person_dict["cc num"])

person_one = {

    "name": "Jim",
    "age": "21 years old",
    "ccnum": "4500 1023 2222 1111"

}

print(person_one["name"])

for info in person_dict:
    print(info)

#Iternate over the person dic
#print info 
for info in person_dict:
    print(info)
