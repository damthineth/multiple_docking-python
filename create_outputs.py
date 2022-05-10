# import required module
import os					#library needed for file handling
import subprocess				#library needed for runs .sh files and make variables

# assign directory
directory = 'config'				#assign directory to config

# iterate over files in that directory
for filename in os.listdir(directory):
	file = filename[:-4]			#remove .txt (new name "config6"). previous name "config6.txt"
	logname = file[6:]			#remove config (new name "6"). previous name "config6"
	subprocess.call(["./docking.sh",file,logname])	#run docking.sh script and make 2 variables 
	


