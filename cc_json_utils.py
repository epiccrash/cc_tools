import json
import cc_data
import cc_dat_utils

def make_cc_data_file_from_json(json_data):
	# Make a cc data file
	cc_data_file = cc_data.CCDataFile()

	# Iterate through each level in the dataset
	for json_level in json_data:
		# Create a level object from the data
		cc_level = cc_data.CCLevel()
		# Get level attrbutes
		cc_level.level_number = json_level["Level Number"]
		cc_level.num_chips = json_level["Chip Number"]
		cc_level.time = json_level["Time"]
		cc_level.upper_layer = json_level["Upper Layer"]
		cc_level.lower_layer = json_level["Lower Layer"]
		# Handle optional fields
		json_fields = json_level["Fields"]
		# Iterate through all of the fields provided and sort them by type
		for json_field in json_fields:
			field_type = json_field["Type"]
			# Title field handling
			if field_type == "Title":
				# Get the title and add it to the level
				title = json_field["Map Title"]
				# Make a CCMapTitleField from the list and add it to the level
				cc_title_field = cc_data.CCMapTitleField(title)
				cc_level.add_field(cc_title_field)
			# Hint field handling
			elif field_type == "Hint":
				# Get the hint text and add it to the level
				hint = json_field["Hint Text"]
				# Make a CCMapHintField from the list and add it to the level
				cc_hint_field = cc_data.CCMapHintField(hint)
				cc_level.add_field(cc_hint_field)
			# Password field handling
			elif field_type == "Password":
				# Get the password and add it to the level
				password = json_field["Encoded Password"]
				# Make a CCEncodedPasswordField from the list and add it to the level
				cc_password_field = cc_data.CCEncodedPasswordField(password)
				cc_level.add_field(cc_password_field)
			# Monster field handling
			elif field_type == "Monsters":
				# Get the monster list
				cc_monster_list = json_field["Monster Placement"]
				monster_movement_list = []
				# Build CC coordinates from json data
				for lst in cc_monster_list:
					# Get coordinates, put them into a list
					cc_monster_coordinates = cc_data.CCCoordinate(lst[0], lst[1])
					monster_movement_list.append(cc_monster_coordinates)
				# Make a CCMonsterMovementField from the list and add it to the level
				cc_monsters_field = cc_data.CCMonsterMovementField(monster_movement_list)
				cc_level.add_field(cc_monsters_field)
			# Trap field handling
			elif field_type == "Trap":
				# Get the trap and button list
				cc_trap_list = json_field["Traps"]
				cc_button_list = json_field["Buttons"]
				trap_control_list = []
				# Iterate through the indeces of the trap list
				for i in range(len(cc_trap_list)):
					# Get coordinates of buttons and traps, put them into a list
					cc_trap_coordinates = cc_data.CCTrapControl(cc_button_list[i][0], cc_button_list[i][1], 
						cc_trap_list[i][0], cc_trap_list[i][1])
					trap_control_list.append(cc_trap_coordinates)
				# Make a CCTrapControlsField from the list and add it to the level
				cc_trap_control_field = cc_data.CCTrapControlsField(trap_control_list)
				cc_level.add_field(cc_trap_control_field)
				print(cc_trap_control_field)
			# Cloning Machine handling
			elif field_type == "Cloning":
				# Get the cloning machine and button list
				cc_cloning_list = json_field["Cloning Machines"]
				cc_button_list = json_field["Buttons"]
				cloning_control_list = []
				# Iterate through the indeces of the cloning list
				for i in range(len(cc_cloning_list)):
					# Get coordinates of buttons and cloning machines, put them into a list
					cc_cloning_coordinates = cc_data.CCCloningMachineControl(cc_button_list[i][0], cc_button_list[i][1], 
						cc_cloning_list[i][0], cc_cloning_list[i][1])
					cloning_control_list.append(cc_cloning_coordinates)
				# Make a CCCloningMachineControlsField from the list and add it to the level
				cc_cloning_control_field = cc_data.CCCloningMachineControlsField(cloning_control_list)
				cc_level.add_field(cc_cloning_control_field)
				print(cc_cloning_control_field)
			# Should not reach this point if the field type is correctly specified
			else:
				print("Invalid type!")
		# Add the completed level to the data file
		cc_data_file.add_level(cc_level)

	# Return the converted data file
	return cc_data_file
