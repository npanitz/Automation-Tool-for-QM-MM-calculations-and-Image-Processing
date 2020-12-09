#!/bin/bash

for i in {1..2}
do
	cubegen 1 MO=Homo nto_$i.fchk HOMO_nto_$i.cube 
	cubegen 1 MO=Lumo nto_$i.fchk LUMO_nto_$i.cube 
done
