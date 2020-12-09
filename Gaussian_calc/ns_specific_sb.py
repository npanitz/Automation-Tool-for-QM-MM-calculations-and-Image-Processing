#!/usr/bin/python

import os

read_file_name = 'submit.sb'
read_file = open(read_file_name,'r')
read_file_contents = read_file.readlines()
read_file.close()

start = START OF ITERATIVE FILENAMES HERE
end = END OF ITERATIVE FILENEAME HERE
span = INTERVAL BETWEEN NUMS IN FILENAMES HERE


for i in range(start,end,span):
	write_file_name = ('ns_' + str(i) + '/submit' + '_ns_' + str(i) + '.sb')
	cmd = ('cd ns_' + str(i))
	os.system(cmd)
	write_file = open(write_file_name, 'a')
	inc = 0
	for line in read_file_contents:
		if inc == 0:
			new_line = line
		elif inc == 1: 
			new_line = line[:-4] + str(i) + '"\n'
		elif inc <= 3:
			new_line = line[:-14] + str(i) + line[-12:]

		elif inc < 17:
			new_line = line
		elif inc == 17:
			new_line = line[:9] + str(i) + line[11:33] + str(i) + line[35:]
		write_file.write(new_line)
		inc += 1
	write_file.close()
