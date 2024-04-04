#notes-2-1-modules.py
#Jean
#11 March 2024

import random

# Demonstrate some parts of the random module
# random.random() -> (0, 1.0]

def coin_flip():
    # Return either heads, tails, or other?
    # Heads -- (0 - 0.5]
    # Tails -- (0.5, 0.9999999]
    # Other --- the rest

    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.9999999:
        return "tails"
    else:
        return "other"

def draw_card():
    #simulate drawing a card
    #Return a card value from A,2,3,... Q,K
        #randon.randrange() -> int in some range 
    reult = random.ranrange(1, 14)

    if result == 1:
        return "A"
    elif result == 11:
        return "J"
    elif result == 12:
        return "Q"
    elif result == 13:
        return "K"
    else:
        return str(result)
    





def main():
    heads = 0
    tails = 0
    others = 0

    for _ in range(10000000):
        # Flip coin
        result = coin_flip()

        if result == "heads":
            heads += 1
        elif result == "tails":
            tails += 1
        else:
            others += 1

# Print results
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Others: {others}")
    

main()
