#!/usr/bin/python

## FILE NAMES (STRINGS)
#--------------------------------------------------
paramPDB = "equil.pdb"
customQMFile = "customQMFile.pdb"

newPDB = "ns_param.pdb"
newcustomPDB = "custom_ns.pdb"


## INITIATE READ FILE OBJECTS
#---------------------------------------------------
paramPDB_file = open(paramPDB, 'r')
paramPDB_file_contents = paramPDB_file.readlines()
paramPDB_file.close()

customPDB_file = open(customQMFile, 'r')
customPDB_file_contents = customPDB_file.readlines()
customPDB_file.close()

newPDB_read_file = open(newPDB, 'r')
newPDB_file_contents = newPDB_read_file.readlines()
newPDB_read_file.close()

newcustomPDB_read_file = open(newcustomPDB, 'r')
newcustomPDB_file_contents = newcustomPDB_read_file.readlines()
newcustomPDB_read_file.close()


## INITIATE WRITE FILE OBJECT AND WRITE
#---------------------------------------------------
newPDB_write_file = open(newPDB, 'w')
new_pdb_index = 0
for line in newPDB_file_contents:
	if line[0] == 'A':
		current_line = paramPDB_file_contents[new_pdb_index]
		new_line = line[:56] + current_line[56:]
	else:
		new_line = line
	new_pdb_index += 1
	newPDB_write_file.write(new_line)

newPDB_write_file.close()

new_customPDB_write_file = open(newcustomPDB, 'w')
new_custom_pdb_index = 0
for line in newcustomPDB_file_contents:
	if line[0] == 'A':
		current_custom_line = customPDB_file_contents[new_custom_pdb_index]
		new_line = line[:56] + current_custom_line[56:]
	else:
		new_line = line
	new_custom_pdb_index += 1
	new_customPDB_write_file.write(new_line)
new_customPDB_write_file.close()
