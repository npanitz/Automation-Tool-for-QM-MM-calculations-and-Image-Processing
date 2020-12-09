# This project is a pipeline for QM/MM calculations with NAMD and Gaussian, image processing with Gaussian, VMD and ImageMagick, and subsequent data analysis with Python.
### Creator: Naftali Panitz
### Acknowledgement: SUNY Binghamton, Chemistry Department: Goyal Lab.

## Installation of NAMD2, Gaussian g09, ImageMagick, and VMD are required for this process.
  - NAMD2 and Gaussian g09 can be downloaded at their respective websites and require Academic registration/license.
  - ImageMagick is free and can be downloaded at: https://imagemagick.org/script/download.php

## The breakdown of the major components of this pipeline are:
1. Setup of initial directory for NAMD calculations and submission of calculations for generation of Gaussian input files.
2. Submission of TDDFT Gaussian calculation and Automation of NTO Creation and Submission.
3. File Formatting and Cubefile Generation.
4. Image processing of cube files.
5. Data Analysis


### 1. Setup of initial directory for NAMD calculations and submission of calculations for generation of Gaussian input files.
- Information on NAMD is available at http://www.ks.uiuc.edu/Research/namd/
- Setup all initial files in the NAMD_calc directory
- Initial files needed:
  - your_structure.pdb
  - your_structure.psf
  - toppar parameterization directory
  - namd_input.namd
    - Information on how to setup and parameterize .namd input file can be found at http://www.ks.uiuc.edu/Research/qmmm/ 
  - namd_submission.sb
- Parameterization
  - link_assignment.py - Use this script to parameterize your pdb file for hybrid QM/MM Calculations. 
    - Find the index of atoms you would like to treat quantum mechanically and write them into the QM_ATOMS list.  
    - Find the index of atoms that define your QM/MM boundary and write them into the BOUNDARY_ATOMS dictionary as key:value pairs where QM_index is the key and MM_index is the value. (QM_index:MM_index)
    - Define "PDB_FILE" as the name of your pdb file.
  - Parameterize your .namd input file accordingly.
  - Open the run_gaussian.py script that is available at http://www.ks.uiuc.edu/Research/qmmm/Scripts/run_gaussian.py and change the Command file parameters to the appropriate gaussian header for a gaussian input file. 
- Submission
  1. It is recommended to write a submission script for the cluster or system you are using. Make sure to include the command: "namd2 example.namd +stdout example.log"
  2. Submit the NAMD calculation and wait until the qm base dir is created (it will be called 0 by default). Wait until the .com file is fully finished being generated by NAMD and then the job can be killed as this submission was just to generate a Gaussian input file with the MM atoms passed to it as point charges in order to assign partial charges to the QM atoms. 

### 2. Submission of TDDFT Gaussian calculations and Automation of NTO Creation and Submission.
#### TDDFT Calculation
1. Move the qmmm.com input file generated from the NAMD calculation to the Gaussian_calc directory 
2. Make sure gaussian module is loaded and submit g09 < qmmm.com > qmmm.out either on the head node or write a submission script.
#### Automation of NTO Creation and Submission.
1. After checking the .out file from tddft calculation, move the corresponding chk file to the NTO_calc directory.
2. An nto_1.com is included. Simply edit the num_nto_files to the number of excited states you are generating NTO calculations for and run "./nto_creator.py"
3. After the NTO input files are generated edit the nto_submitter.sh script's range to be the amount of total input files you have and run "./nto_submitter.sh"

### 3. File Formatting and Cubefile Generation
1. Check some of the last .out files for the nto calculation and make sure Gaussian terminated normally.
2. Open the fchk_creator.sh script and change the range to the number of NTO chk files you have.
  - Format the .chk files generated from the nto calculation by running "./fchk_creator.sh"
3. Change the range in cube_creator.sh to the number of NTO fchk files you now have.
  - Generate a homo cube and lumo cube for each .fchk file  by running "./cube_creator.sh" 

### 4. Image Processing of cube files.
#### vmd_cube.py is a script provided by psi4 at: https://github.com/psi4/psi4/blob/master/psi4/share/psi4/scripts/vmd_cube.py
#### psi4 provides prerequisites for vmd_cube.py at: http://www.psicode.org/psi4manual/master/cubeprop.html#orbital-visualization-with-vmd

1. Move the cube files to the Image_Processing directory and execute "./start_out.sh"
  - Directories will be created and the cube files will be sorted into their respective directories by the start_out.sh script.
  - Additionally a template directory will be created with a copy of the first nto HOMO cube. This is for subjective determination of rotational constants prior to automation.
2. Execute the command "python vmd_cube.py path/to/template/ --scale 1.5 --imageh 1000 --imagew 1000 --rx 0 --ry 0 --rz 0"
  - The script converts all cube files in a directory to .tga files. The purpose of the template is to fine tune the orientation of the structure before running the script on all of the HOMO and LUMO cubes.
  - You can also play around with the other parameters and get a list of the attributes available by executing "python vmd_cube.py --help"
3. Once you have optimized the rotational constants, edit the x, y and z variables in the script, image_creator.py accordingly. You should also change the pdf_file_name variable to whatever is appropriatefor your structure.
4. Now to gather the information required to label your images, copy the .out file from the main tddft calculation to the image processing directory and open the get_wavelengths_eV_and_osc.py script.
  - edit the read file name to be the name of the output tddft file and run the script.
  - This will generate a wv_ev_osc.txt file that contains three lists. Copy the whole file and paste it into the section labelled "paste lists here" in the make_images_better.py script.
5. Once the lists are pasted in, just run "./image_creator.py" This script will run the make_images_better.py script so you don't have to run it manually!
  - The result is a pdf with all of the appended and labelled pngs of your NTO states.