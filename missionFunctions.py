# Function that counts the number of missions in a list of mission names
def count_missions(mission_list):
    
    # Variable to count mission amount in list
    mission_counter = 0

    # Loop through each item in the list passed in
    for mission in mission_list:
        mission_counter += 1 # Increment mission_counter for each element
    
    # Return value of mission_counter
    return mission_counter

# Function that takes in the mission_success list and counts the amount of successful missions
def count_succeeded_missions(mission_success):

    # Variable to count amount of successful missions
    successful_mission_counter = 0

    # Loop through each item in the list
    for result in mission_success:
        # If the result is equal to True, increment successful_mission_counter
        if result == True:
            successful_mission_counter += 1
    
    # Return the final value of successful_mission_counter
    return successful_mission_counter

# Function that prints out the mission names of missions that were conducted before the year 2000
def print_missions_before_2000(mission_names, mission_years):

    # Counter that stores iterator signifying index of list
    index_iterator = 0

    # Loop through each year in the year list
    for year in mission_years:
        # if the year is less than 2000, print the element at index_iterator of mission_names list
        if year < 2000:
            print("- " + mission_names[index_iterator])
        
        # increment the index_iterator 
        index_iterator += 1






