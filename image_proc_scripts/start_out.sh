#!/bin/bash


mkdir homo_cubes
mkdir lumo_cubes 


mv *homo* homo_cubes
mv *lumo* lumo_cubes

mkdir template
cp homo_cubes/nto_homo_1.cube template/
