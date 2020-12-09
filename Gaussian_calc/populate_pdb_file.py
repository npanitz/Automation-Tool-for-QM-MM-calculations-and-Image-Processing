#!/usr/bin/python

## THIS SCRIPT TAKES IN A PDB FILE AND A CUSTOMPDB FILE AND GENERATES A LIST AND DICTIONARY OF INDEXES OF ATOMS
## CORRESPONDING TO THE QM/MM BOND ASSIGNMENTS (BASCIALLY AN INVERSION OF THE SCRIPT THAT TAKES IN A DICTIONARY
## AND LIST AND WRITES TO A PDB FILE.

pdb_file = 'equil.pdb'
custom_pdb_file = 'customQMFile.pdb'
QM_ATOMS_pdb = []
QM_ATOMS_custom_pdb = []
QM_MM_DICT = {}

read_file = open(pdb_file, 'r')
read_custom_file = open(custom_pdb_file, 'r')

pdb_file_contents = read_file.readlines()
custom_file_contents = read_custom_file.readlines()

new_results_file = open('results.txt', 'a')

for line in custom_file_contents:
	if line[0] == 'A':
		if line[62] == '1':
			int_of_index = int(line[6:10])	
			QM_ATOMS_pdb.append(int_of_index)

new_results_file.write(QM_ATOMS_pdb)
