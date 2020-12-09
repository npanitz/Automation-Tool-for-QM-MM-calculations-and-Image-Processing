#!/usr/bin/python


import sys

## Initiate lists and dictionaries of types of atoms

QM_ATOMS = [1,3,5,7,9]  # List of QM atoms by index
BOUNDARY_ATOMS = {1:2,3:4,5:6}  # Dictionary of qm/mm atoms as key:value pairs

PDB_File = "example.pdb"  # Name of original pdb file it is reading from

# File name editing
INT_MODIFIED_PDB = PDB_File[:-4]
NEW_MODIFIED_PDB = INT_MODIFIED_PDB + "_new.pdb"
NEW_CUSTOMPDB = INT_MODIFIED_PDB + "_custom.pdb"

def main():
	
	# Reading from pdb file and creating list of lines
	orig_pdb = open(PDB_File, 'r')
	list_of_lines = list(orig_pdb.readlines())

	index = 0     # Initiation for iterator in for loop

	# File manipulation
	for line in list_of_lines:
		if index in (QM_ATOMS and BOUNDARY_ATOMS.keys()):
			new_line = line[:-23] + '1' + line[-22:-17] + '1' + line[-16:]
			new_custom_line = line[:-23] + '0' + line[-22:-17] + '1' + line[-16:]
		elif index in QM_ATOMS:
			new_line = line[:-23] + '0' + line[-22:-17] + '1' + line[-16:]
			new_custom_line = line[:-23] + '0' + line[-22:-17] + '1' + line[-16:]
		elif index in BOUNDARY_ATOMS.values():
			new_line = line[:-23] + '1' + line[-22:]
			new_custom_line = line[:-23] + '1' + line[-22:-17] + '0' + line[-16:] 
		else:
			new_line = line
			new_custom_line = line[:-23] + '1' + line[-22:-17] + '0' + line[-16:] 
		new_pdb_file = open(NEW_MODIFIED_PDB, "a")
		new_pdb_file.write(new_line)
		new_pdb_file.close()

		new_custompdb_file = open(NEW_CUSTOMPDB, "a")
		new_custompdb_file.write(new_custom_line)
		new_custompdb_file.close()

		index += 1

if __name__ == "__main__":
	main()
