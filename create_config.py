# import required module
import os
# assign directory
directory = 'ligands'        
 
# iterate over files in that directory
for filename in os.listdir(directory):
    file = filename[:-6]												#remove .pdbqt part in name
    with open('config/config' + file + '.txt', 'w') as f:				#config6.txt (create a file named config6.txt in config folder)
        f.write('receptor = protein/protein_1ebz.pdbqt\n')				#receptor = protein/protein_1ebz.pdbqt
        f.write('ligand = ./ligands/'+filename)							#ligand = ./ligands/6.pdbqt
        f.write('\ncenter_x = 15.9333\n')								#center_x = 15.9333
        f.write('center_y = 25.690944378\n')							#center_y = 25.690944378
        f.write('center_z = 5.10902631076\n')							#center_z = 5.10902631076
        f.write('size_x = 42.5046873093\n')								#size_x = 42.5046873093
        f.write('size_y = 31.7088621758\n')								#size_y = 31.7088621758
        f.write('size_z = 19.3347771771\n')								#size_z = 19.3347771771
        f.write('out = output/'+filename)								#out = output/6.pdbqt (the place where the coordinates of the docked ligand to be saved)
        f.write('\nnum_modes = 1\n')									#num_modes = 1 (taken only best docking pose)
        f.write('exhaustiveness = 8')									#exhaustiveness = 8
