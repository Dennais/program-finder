import os
from program_lib import programs

# get user input for the programs to open
input_programs = input("Enter the programs(only lower case letters) to open (separated by a space): ")
lowercase_input = input_programs.lower()

# split the input into individual program names
program_names = input_programs.split()

# loop through the program names and open the corresponding program
for name in program_names:
    if name in programs:
        os.startfile(programs[name])
    else:
        print(f"Sorry, {name} is not in the list of available programs.")
