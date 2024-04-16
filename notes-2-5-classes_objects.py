#Classes and Objects

#Big Ideas:
# - classes allow us to couple data and functions together
# - Objects are the ACTUAL representation of the classes

# Create a Pokemon class; this represents a Pokemon
class Pokemon: # use a capital letter for class 
    def __init__(self):
        """ A special method (function) called the Constructor. Contains all the properties/variables that describe a Pokemon"""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"

        print("A new Pokemon is born!")

#Create two pokemon using our class
#Make one pokemon that is pikachu

pokemon_one = Pokemon () 

print(pokemon_one.name)
pokemon_one.name = "Pikachu"
print(pokemon_one.name)

pokemon_one.id = 25
pokemon_one.type = "Electric"

print(pokemon_one.id)
print(pokemon_one.type)

#Make Squirtle
pokemon_two = Pokemon ()

pokemon_two.id = 4
pokemon_two.name = "Squirtle"
pokemon_two.type = "Water"

print(pokemon_two.id)
print(pokemon_two.name)
print(pokemon_two.type)