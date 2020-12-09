#!/bin/bash

for i in {1..60}
do
	formchk nto_$i.chk > nto_$i.fchk
done
