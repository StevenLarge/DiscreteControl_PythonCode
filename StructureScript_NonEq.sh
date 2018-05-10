#!/usr/bin/env python

import os
import sys

def WriteFile(FileName,ReadFile,CPVals):

	file1 = open(FileName,'w')

	file1.write(ReadFile + "\n")
	file1.write("%d" % CPVals)

	file1.close()


#ProtocolClass = ["Naive","TimeOpt","SpaceOpt","FullOpt"]
#Param_Ex = ["9_10", "9_15", "9_20", "12_10", "12_15", "12_20", "15_10", "15_15", "15_20"]
#CPVals = [11,13,15,17,19,21,23,25]
#TotalTimes = [50,100,500]

ProtocolClass = ["Naive"]
Param_Ex = ["9_10"]
CPVals = [21]
TotalTimes = [100]

WriteName = "ProtocolName.dat"

os.system("make clean")
os.system("make clean_ex")
os.system("make")

for ClassIndex in range(len(ProtocolClass)):

	for ParamIndex in range(len(Param_Ex)):

		for index1 in range(len(CPVals)):

			for index2 in range(len(TotalTimes)):

				DirName = "Work_" + ProtocolClass[ClassIndex] + "_" + Param_Ex[ParamIndex] + "_CP" + str(CPVals[index1]) + "_T" + str(TotalTimes[index2])
				ReadFile = os.getcwd() + "/Protocols_" + Param_Ex[ParamIndex] + "/" + ProtocolClass[ClassIndex] + "_CP" + str(CPVals[index1]) + "_T" + str(TotalTimes[index2]) + ".dat"

				os.mkdir(DirName)
				#CopyCommand1 = "cp Nonequilibrium_Cluster.cpp " + DirName
				CopyCommand1 = "cp NonEqPropogator.exe " + DirName
				CopyCommand2 = "cp Makefile " + DirName
				#CopyCommand3 = "cp SlurmSubmission.sh " + DirName

				os.system(CopyCommand1)
				os.system(CopyCommand2)
				#os.system(CopyCommand3)

				os.chdir(DirName)
				#os.system("make")
				WriteFile(WriteName,ReadFile,CPVals[index1])
				os.chdir("..")



