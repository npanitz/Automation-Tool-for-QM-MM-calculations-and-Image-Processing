#!/usr/bin/python

import os

### Paste lists from wv_ev_osc.txt below:

num_ntos = ENTER NUMBER OF STATES HERE 
index = 1

for i in range(num_states):
	if index <= 9:
		join_cmd = 'convert nto_homo_' + str(index) + '.png nto_lumo_' + str(index) + '.png +append 0' + str(index) + '.png'
        	os.system(join_cmd)

		nto_label_cmd = 'convert 0' + str(index) + '.png -gravity North -pointsize 50 -annotate 0' + " 'NTO " + str(index) + ": HOMO -> LUMO' 0" + str(index) + '.png'
		os.system(nto_label_cmd)


		wavelength_cmd = 'convert 0' + str(index) + '.png -gravity South -pointsize 40 -annotate 0 ' + "'" + list_of_wavelengths[i] + "'" + ' 0' + str(index) + '.png'
		os.system(wavelength_cmd)

		eV_cmd = 'convert 0' + str(index) + '.png -gravity Southeast -pointsize 40 -annotate 0 ' + "'" + list_of_eV[i] + "'" + ' 0' + str(index) + '.png'
		os.system(eV_cmd)

		osc_cmd = 'convert 0' + str(index) + '.png -gravity Southwest -pointsize 40 -annotate 0 ' + "'" + list_of_osc[i] + "'" + ' 0' + str(index) + '.png'
		os.system(osc_cmd)
	else:
		join_cmd = 'convert nto_homo_' + str(index) + '.png nto_lumo_' + str(index) + '.png +append ' + str(index) + '.png'
        	os.system(join_cmd)
	

		nto_label_cmd = 'convert ' + str(index) + '.png -gravity North -pointsize 50 -annotate 0' + " 'NTO " + str(index) + ": HOMO -> LUMO' " + str(index) + '.png'
        	os.system(nto_label_cmd)


		wavelength_cmd = 'convert ' + str(index) + '.png -gravity South -pointsize 40 -annotate 0 ' + "'" + list_of_wavelengths[i] + "'" + ' ' + str(index) + '.png'
		os.system(wavelength_cmd)

		eV_cmd = 'convert ' + str(index) + '.png -gravity Southeast -pointsize 40 -annotate 0 ' + "'" + list_of_eV[i] + "'" + ' ' + str(index) + '.png'
                os.system(eV_cmd)

		osc_cmd = 'convert ' + str(index) + '.png -gravity Southwest -pointsize 40 -annotate 0 ' + "'" + list_of_osc[i] + "'" + ' ' + str(index) + '.png'
                os.system(osc_cmd)


	index += 1

