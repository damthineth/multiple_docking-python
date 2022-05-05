# How to do multiple docking using python
Here I have given the guidline to do multiple docking using two simple python codes.

First of all, you should create 5 new folders: **protein**, **all**, **output**, **logs**, and **config**.
  - protein: protein in pdbqt format 
  - all: all the ligands in pdbqt format
  - output: that is the place where all the outputs are generated by executing create_output.py
  - logs: that is the place where all the log files are generated by executing create_output.py
  - config: that is the place where all the configuration files are generated by executing create_config.py
  
except to those 5 folders, there should be 2 .py files(**create_output.py** and **create_config.py**), **vina**, and **vina_split**.

Note: sometimes it doesn't work. That case, you have to run **docking.sh** file instead.
