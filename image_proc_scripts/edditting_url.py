#!/usr/bin/python

read_file_name = 'url.txt'

read_file = open(read_file_name, 'r')

read_file_contents = read_file.readlines()

read_file.close()

write_file_name = 'new_url.txt'
write_file = open(write_file_name, 'a')

for line in read_file_contents:
	new_line = line.rstrip()
	newer_line = "'" + new_line + "',"
	write_file.write(newer_line)

write_file.close()
