import glob
import os
import sys
path= os.getcwd()
if len(sys.argv) == 4:
    protein = sys.argv[1]
    centroid = sys.argv[2]
    nrun = sys.argv[3]
    files = glob.glob(path + '/*.pdb') #taking all pdb files from the current directory
    coord = []
    for f in files:
        ligand = f.split("/")[-1][:-4] + ".pdb "
        cord_split = centroid.split(",")
        x_cord = str(cord_split[0])
        y_cord = str(cord_split[1])
        z_cord = str(cord_split[2])
        coord.append(x_cord)
        coord.append(y_cord)
        coord.append(z_cord)
        os.system("python gpu_filecr.py " + f'{protein} ' + ligand +str(coord[0])+","+str(coord[1])+","+str(coord[2])+ f' {nrun}')
else:
    print('''python3 gpu_hts.py <protein_pdb_file> <x,y,z> <nrun>
eg.
python3 gpu_hts.py 7k15.pdb 1.9392312138728325,-8.92228901734104,18.28384393063584 10
    ''')




