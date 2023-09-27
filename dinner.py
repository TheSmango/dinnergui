#!/usr/bin/env python3
#Randomly selects a restaurant to eat at
#Marcus Dean Adams (gerowen@pm.me)
#27 September 2023

import random, time

choices = [ "McDonald's", "Wendy's", "Mi Hacienda", "Applebee's", "Bob Evans", \
"Red Robin", "Cracker Barrel", "Texas Steakhouse", "Chinese", "Golden Corral", "Dairy Queen", \
"Lee's Chicken", "Taco Bell", "Subway", "Farmhouse Diner", "1 2 3 Food Court", "Arbys", \
"Hardee's", "KFC", "Little Caesars", "Billy Ray's", "The Brickhouse", "El Dorado",  \
"Giovanni's", "Pig in a Poke", "Fazoli's", "Long John Silver's", "Buffalo Wild Wings" ]

time.sleep (1)

print ( "\nDinner tonight is....\n\nDramatic drum roll please...\n" )
time.sleep (5)

print ( choices[random.randint(0,len(choices)-1)] + "!!!!!\n" )

exit