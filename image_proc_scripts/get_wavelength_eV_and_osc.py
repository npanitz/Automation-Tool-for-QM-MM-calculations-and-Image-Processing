#!/usr/bin/python


read_file_name = ENTER YOUR .out FILENAME HERE

read_file = open(read_file_name, 'r')

read_file_contents = read_file.readlines()

write_file_name = 'wv_ev_osc.txt'
write_file = open (write_file_name, 'a')

write_file.write('list_of_wavelengths = [')

skip_first_counter = 0
es_index = 0

for line in read_file_contents:
	if line[:8] == ' Excited':
		if skip_first_counter == 0:
			skip_first_counter += 1
			es_index += 1
		elif es_index == 119:
			new_wavelength = "'" + (line[50:60] + "'")
                        write_file.write(new_wavelength)
		else:
			new_wavelength = "'" + (line[50:60] + "',")
			write_file.write(new_wavelength)
			es_index += 1
write_file.write(']\n\n\n')

write_file.write('list_of_eV = [')

skip_first_counter = 0
es_index = 0

for line in read_file_contents:
        if line[:8] == ' Excited':
		if skip_first_counter == 0:
			skip_first_counter += 1
			es_index += 1
		elif es_index == 119:
			new_osc = "'" + (line[62:70] + "'")
			write_file.write(new_osc)
		else:
			new_osc = "'" + (line[62:70] + "',")
			write_file.write(new_osc)
			es_index += 1
write_file.write(']\n\n\n')

write_file.write('list_of_osc = [')

skip_first_counter = 0
es_index = 0

for line in read_file_contents:
        if line[:8] == ' Excited':
		if skip_first_counter == 0:
			skip_first_counter += 1
			es_index += 1
		elif es_index == 119:
			new_eV = "'" + (line[40:49] + "'")
                        write_file.write(new_eV)
		else:
			new_eV = "'" + (line[40:49] + "',")
			write_file.write(new_eV)
			es_index += 1
write_file.write(']')
