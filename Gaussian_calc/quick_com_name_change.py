#!/usr/bin/python
import os

start = ENTER START TIME HERE AS VALUE
end = ENTER END TIME HERE AS VALUE
span = ENTER INTERVAL OF TIME


for i in range(start,end,span):
	cmd = ('mv ns_' + str(i) + '/ns_' + str(i) + '_new.com ns_' + str(i) + '/ns_' + str(i) + '_states_1-60.com') 
	os.system(cmd)
