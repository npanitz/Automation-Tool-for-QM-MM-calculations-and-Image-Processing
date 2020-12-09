#!/usr/bin/python

import os

rx = 110
ry = -18
rz = -85

pdf_file_name = 'ns_28_GLU129_mutant.pdf'
### COMMANDS --------
lumo_images_cmd = 'python ../vmd_cube.py lumo_cubes/ --rx ' + str(rx) + ' --ry ' + str(ry) + ' --rz ' + str(rz) + ' --scale 1.5 --imageh 1000 --imagew 1000'
homo_images_cmd = 'python ../vmd_cube.py homo_cubes/ --rx ' + str(rx) + ' --ry ' + str(ry) + ' --rz ' + str(rz) + ' --scale 1.5 --imageh 1000 --imagew 1000'

mv_homo_tga_cmd = 'mv homo_cubes/*tga ./'
mv_lumo_tga_cmd = 'mv lumo_cubes/*tga ./'

mogrify_cmd = 'mogrify -format png *tga'
rm_tga_cmd = 'rm *tga'

make_images_better_cmd = './make_images_better.py'
mv_homo_png_cmd = 'mv *homo* homo_cubes'
mv_lumo_png_cmd = 'mv *lumo* lumo_cubes'
convert_to_pdf_cmd = 'convert *png ' + pdf_file_name 
### EXECUTE ---------
os.system(lumo_images_cmd)
os.system(homo_images_cmd)
os.system(mv_homo_tga_cmd)
os.system(mv_lumo_tga_cmd)
os.system(mogrify_cmd)
os.system(rm_tga_cmd)
os.system(make_images_better_cmd)
os.system(mv_homo_png_cmd)
os.system(mv_lumo_png_cmd)
os.system(convert_to_pdf_cmd)


