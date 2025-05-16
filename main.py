# filename: main.py
# developer: Rehaan Aria
# created: 5/15/2025
# description: This program prints out various information and data on space missions. By implementing the use of for loops and
#              if statements, we are able to extract particular data that we want from the lists, such as the number of missions
#              conducted, the amount of successful missions, and more. Functions were used to make the code in main more readable,
#              as well as to make it easier to edit later.

from missionFunctions import *

# Provided lists
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Store result of function call count_missions in a variable
mission_count = count_missions(mission_names)

# Print out the total number of missions
print(f"Total number of missions: {mission_count}")

# Store result of function call count_succeeded_missions in variable
successful_mission_count = count_succeeded_missions(mission_success)

# Print out the number of successful missions
print(f"Number of successful missions: {successful_mission_count}")

# Calculate success rate of missions and store into variable
mission_success_rate = (successful_mission_count / mission_count) * 100

# Print out the success rate to 2 decimal places
print(f"Success rate: {mission_success_rate:.2f}%")

print("Missions launched before the year 2000: ")
# Call the function that prints the missions launched before 2000
print_missions_before_2000(mission_names, mission_years)
