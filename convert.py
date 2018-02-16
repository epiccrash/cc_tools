import cc_dat_utils
# Imported to facilitate opening and reading data
import json
import test_json_utils
import test_data
import cc_data
import cc_json_utils

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data
print(cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat"))

#Part 2
# Get json file and read it as input
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
### End Add Code Here ###

# Open the json file and read data from it
with open(input_json_file) as reader:
	json_data = json.load(reader)
# Create game library data from the json file
game_library_data = test_json_utils.make_game_library_from_json(json_data)
# Print the data
test_data.print_game_library(game_library_data)

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

# Get a custom json file
custom_json_file = "data/jperrino_cc1.json"

# Load the JSON file
with open(custom_json_file) as reader:
	json_data = json.load(reader)

# Build a basic cc data file
cc_data_file = cc_json_utils.make_cc_data_file_from_json(json_data)

# Write the data to a dat file
cc_dat_utils.write_cc_data_to_dat(cc_data_file, "data/jperrino_cc1.dat")
