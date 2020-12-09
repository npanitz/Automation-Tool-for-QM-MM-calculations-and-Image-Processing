#!/usr/bin/python

'''
This script can help you analyze nto information if it is stored in the proper format in objects with key value pairs where the keys are the excited states of interest
and the value is a tuple of the oscillator strength, wavelength and eV strenght. You can parameterize the your search through these objects by executing this script
and following the instructions.
'''

### FUNCTIONS --------------------------------------------------------------------------------------------------------------------

def validate_num(num):
	return num.isdigit()

def validate_float(decimal):
	test_decimal = decimal.replace('.','')
	return test_decimal.isdigit()

### MAIN -------------------------------------------------------------------------------------------------------------------------

def main():

## Constants ---------------------------------------------------
	valid_num_fail = "That is not a valid input. Please enter an integer:  "
	valid_float_fail = "That is not a valid input. Please enter a decimal:  "

## Initiate empty dictionaries ---------------------------------------------------------------------------------------------------
	ns_4 = {'structure':'ns_4'}
	ns_8 = {'structure':'ns_8'}
	ns_12 = {'structure':'ns_12'}
	ns_16 = {'structure':'ns_16'}
	ns_20 = {'structure':'ns_20'}
	ns_24 = {'structure':'ns_24'}
	ns_28 = {'structure':'ns_28'}
	ns_32 = {'structure':'ns_32'}
	ns_36 = {'structure':'ns_36'}
	ns_40 = {'structure':'ns_40'}
	ns_44 = {'structure':'ns_44'}
	ns_48 = {'structure':'ns_48'}
	ns_52 = {'structure':'ns_52'}
	ns_56 = {'structure':'ns_56'}
	ns_60 = {'structure':'ns_60'}
	ns_64 = {'structure':'ns_64'}
	ns_68 = {'structure':'ns_68'}
	ns_72 = {'structure':'ns_72'}
	ns_76 = {'structure':'ns_76'}
	ns_80 = {'structure':'ns_80'}
	ns_84 = {'structure':'ns_84'}
	ns_88 = {'structure':'ns_88'}
	ns_92 = {'structure':'ns_92'}
	ns_96 = {'structure':'ns_96'}
	ns_100 = {'structure':'ns_100'}

	list_of_ns_dicts = [ns_4,ns_8,ns_12,ns_16,ns_20,ns_24,ns_28,ns_32,ns_36,ns_40,ns_44,ns_48,ns_52,ns_56,ns_60,ns_64,ns_68,ns_72,ns_76,ns_80,ns_84,ns_88,ns_92,ns_96,ns_100]

## Fill Dictionaries---------------------------------------------------------------------------------------------------------------------
	debug_counter = 0
	for ns_dict in list_of_ns_dicts:
		debug_counter += 1
		read_file_name = (str(ns_dict['structure']) + '_dict.txt')
		read_file = open(read_file_name, 'r')
		read_file_contents = read_file.readlines()
		for line in read_file_contents:
			stripped_line = line.rstrip()
			excited_state, parameters = stripped_line.split(':')

			str_wavelength,str_osc,str_eV = parameters.split(',')
			wavelength = float(str_wavelength)
			osc = float(str_osc)
			eV = float(str_eV)

			new_line = {excited_state:[wavelength,osc,eV]}
			ns_dict.update(new_line)
		read_file.close()


	print("\nThis tool can help analyze a trajectory of structures.\n"
		"Please parameterize your search according to the guidance that follows\n\n")

### Get relevant duration of equilibration------------------------------------------------------------

	str_first_ns_structure = raw_input("Please enter the first timepoint in ns (just as a number):  ")
	while not validate_num(str_first_ns_structure):
		str_first_ns_structure = raw_input(valid_num_fail)
	first_ns_structure = int(str_first_ns_structure)

	str_last_ns_structure = raw_input("Please enter the last timepoint in ns (just the number):  ")
	while not validate_num(str_last_ns_structure):
		str_last_ns_structure = raw_input(valid_num_fail)
	last_ns_structure = int(str_last_ns_structure)

### Get relevant wavelengths -------------------------------------------------------------------------

	str_highest_wavelength = raw_input("Please enter the highest wavelength you are interested in:  ")
	while not validate_num(str_highest_wavelength):
		str_highest_wavelength = raw_input(valid_num_fail)
	highest_wavelength = int(str_highest_wavelength)

	str_lowest_wavelength = raw_input("Please enter the lowest wavelength you are interested in:  ")
	while not validate_num(str_lowest_wavelength):
		str_lowest_wavelength = raw_input(valid_num_fail)
	lowest_wavelength = int(str_lowest_wavelength)

### Get relevant oscillator strengths -----------------------------------------------------------------

	str_lowest_osc = raw_input("Please enter the lowest oscillator strength you are interested in:  ")
	while not validate_float(str_lowest_osc):
		str_lowest_osc = raw_input(valid_float_fail)
	lowest_osc = float(str_lowest_osc)

	str_highest_osc = raw_input("Please enter the highest oscillator strength you are interested in:  ")
        while not validate_float(str_highest_osc):
                str_highest_osc = raw_input(valid_float_fail)
        highest_osc = float(str_highest_osc)

###--------------------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------------------

	start_iter = (first_ns_structure / 4 - 1)
	end_iter = (last_ns_structure / 4)
	num_structures = (len(list(range(start_iter,end_iter))))
#	print(num_structures)

	write_file_name = ('analysis_' + (str_first_ns_structure) + '-' + (str_last_ns_structure) + 'ns_' + str_lowest_wavelength + '-' + str_highest_wavelength + 'nm_' + str_lowest_osc + '-' + str_highest_osc + '.txt')
	write_file = open(write_file_name,'a')
	for i in range(start_iter,end_iter):
		current_final_dict = {}
		current_structure_name = list_of_ns_dicts[i]['structure']
		write_file.write(current_structure_name + '\n')

		for current_entry in list_of_ns_dicts[i]:
			if (list_of_ns_dicts[i][current_entry][0] >= lowest_wavelength) \
				and (list_of_ns_dicts[i][current_entry][0] <= highest_wavelength) \
				and (list_of_ns_dicts[i][current_entry][1] >= lowest_osc) \
				and (list_of_ns_dicts[i][current_entry][1] <= highest_osc):
					current_update_string = {current_entry:list_of_ns_dicts[i][current_entry]}
					current_final_dict.update(current_update_string)

		num_MLCT_str = 'There are ' + str(len(current_final_dict)) + ' MLCT states that fit your parameters in this structure.\n'
		write_file.write(num_MLCT_str)
		for final_entry in current_final_dict:
			new_write_string = 'Excited State: ' + final_entry + ' | Wavelength: ' + str(current_final_dict[final_entry][0]) + ' nm |' + ' Oscillator Strength: ' + str(current_final_dict[final_entry][1]) + ' | Energy: ' + str(current_final_dict[final_entry][2]) + '|\n'
			write_file.write(new_write_string)

		write_file.write('-----------------------------------------------------------------------------------\n')
	write_file.close()




if __name__ == "__main__":
	main()
