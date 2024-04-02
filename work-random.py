# Rate bot
# Author: Jean Chen
# March 11 24

# IMPORT
import time
import random 

# Ask user to rate bot 
#i f rating is good, reply in happy attitude
# if rating is bad, reply in sad tone
# else just assume its good lol  
print()
print("\nThanks for being here today!") 
time.sleep(1)
print( "To report back to my developer, I will need you to rate me on a scale of 1 to 5 ")
rating = input().strip("!.?,").lower()

if rating in ["1","1.5","2","2.5","3"]:
	bad_ratings = ["hmmm..okay! Thanks", "Aw.. that's fine! Thanks for being here today!", "Okay....See you next time? Hopefully :)"]
	random_comments = random.choice(bad_ratings)
	print(random_comments)

elif rating in ["3.5","4","4.5","5"]:
	good_ratings = ["AWW!THANK YOUUU!", "Thanks! See u next time <33", "thank you~~! I appreciate it :))"]
	random_comments = random.choice(good_ratings)
	print(random_comments)
else:
	print("I will assume you enjoyed today's service! Have a nice day:)")



