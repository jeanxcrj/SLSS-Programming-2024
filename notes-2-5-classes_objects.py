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
        self.actual_cry = "Rooooooooooooooar"

        print("A new Pokemon is born!")
    
    def cry(self):
        """Represents the sound a Pokemon makes
        
        Returns:
        - String representing the sound it makes"""
  
        return f'{self.name} says, "{self.actual_cry}"!'
    def eat(self, food:str) -> str:
        """Represents feedimg the Pokemon
        
        Params: 
            - food: wjay food you feed it
            
        ReturnL
            - what is says after eating it"""
        if food.lower() == "berry":
            return f"{self.name} ate the berry and says, \"YUM!\""
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away. "
        
class Pikachu(Pokemon):
    def __init__(self, name="Pikachu"):
        super().__init__()

        self.name = name
        self.id = 25
        self.type = "Electric"
        self.actual_cry = "Pikaaachuuuuu!"

    def thundershock(self, defender: Pokemon) -> str:
        """Simulate a thundershock attack against another Pokemon
        
        Params:
            -Defedner: Defending Pokemon
            
        Returns:
            str representing result of attack"""    
        
        response = f"{self.name} used thundershock!"

        if defender.type.lower() in ["water", "flying"]:
            response = response + "It was super effective"

        return response
    

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

pokemon_one.actual_cry = "Pikachuuuuu"
pokemon_two.actual_cry = "GRRraagrgrggg"

print(pokemon_one.cry())
print(pokemon_two.cry())

#Test eat method
print(pokemon_one.eat("berry"))
print(pokemon_one.eat("potion"))
print(pokemon_one.eat("poison"))

pikachu_one = Pikachu()
pikachu_two = Pikachu()

print(pokemon_one.name)
print(pikachu_two.name)
print(pikachu_one.cry())
print(pikachu_two.cry())

pikachu_one.thundershock(pokemon_one)

# Create a new child-class of pokemon for the type of your choic
#   - create a new child class
#   - create a constructor and set the default values for its properties
#       - i.e. its name, id, type, etc.
#   - create a new method for its attack

class Charmander(Pokemon):
    def __init__(self, name="Charmander"):
        super().__init__()
        self.name = name
        self.id = 4
        self.type = "Fire"
        self.actual_cry = "Char-char!"

    def ember(self, defender: Pokemon) -> str:
        """Simulate an Ember attack against another Pokemon
      
        Params:
            -Defender: Defending Pokemon
          
        Returns:
            str representing result of attack"""   
      
        response = f"{self.name} used Ember!"
        if defender.type.lower() == "grass":
            response += " It's super effective!"
        return response
    
class Charmander(Pokemon):
    def __init__(self, name="Charmander"):
        pass

    def ember(self, defender: Pokemon) -> str:
        pass
