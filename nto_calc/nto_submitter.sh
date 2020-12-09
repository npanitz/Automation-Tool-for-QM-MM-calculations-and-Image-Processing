#!/bin/bash

for i in {1..60}
do
	g09 < nto_$i.com > nto_$i.out
done
