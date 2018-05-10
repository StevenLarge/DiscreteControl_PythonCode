#!/usr/bin/env python

import os
import sys

Prot_Ex = ["9_10","9_15","9_20","12_10","12_15","12_20","15_10","15_15","15_20"]

os.chdir("..")

for index in range(len(Prot_Ex)):

	ReadPath = "DiscreteControl_Optimization/Protocols_" + Prot_Ex[index] + "/*.dat" 
	WritePath = "DiscreteControl_NonEquilibrium_Mar19/Protocols_" + Prot_Ex[index]

	CopyCommand = "cp " + ReadPath + " " + WriteFile
	os.system(CopyCommand)

os.chdir("DiscreteControl_NonEquilibrium_Mar19")

os.system("echo")
os.system("echo")
os.system("echo ----- Protocol Copying Finished -----")
os.system("echo")
os.system("echo")

