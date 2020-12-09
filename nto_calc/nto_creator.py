#!/usr/bin/python

import sys


# This python script will create a file system for calculating NTO's
nto_first_file = "nto_1.com"

num_nto_files = 60
list_of_nto_files = [nto_first_file]

orig_nto = open(nto_first_file, 'r')
lines_in_nto_file = orig_nto.readlines()
orig_nto.close()


for i in range(num_nto_files - 1):
	new_nto_filename = nto_first_file[:-5] + str(i+2) + ".com"
	new_nto_file = open(new_nto_filename, 'w')
	incrementor = 1
	for line in lines_in_nto_file:
		if incrementor == 1:
			new_line = line
		elif incrementor == 2:
			new_line = line[:-6] + str(i+2) + line[-5:]
		elif incrementor == 3:
			new_line = line[:-15] + str(i+2) + line [-14:]
		incrementor += 1

		new_nto_file.write(new_line)
	new_nto_file.close()

			



