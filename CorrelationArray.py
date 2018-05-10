#This python script generates a master Correlation array file that contains a lambda,Delta t mesh as well as the Force Variance as a function of CP
#
#Steven Large
#November 22nd

import os
from math import *


def ReadFile(Path,ReadName):

	CompleteName = os.path.join(Path,ReadName)
	
	LagTime = []
	Correlation = []

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)-2):
		parsed = TempData[index+2].split()

		LagTime.append(eval(parsed[0]))
		Correlation.append(eval(parsed[1]))

	return LagTime,Correlation


def WriteCorrelationArray(Path,Filename,DataArray):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index1 in range(len(DataArray)):
		for index2 in range(len(DataArray[index1])):
			file1.write('%lf\t' % DataArray[index1][index2])
		file1.write('\n')

	file1.close()


def WriteFisherLandscape(Path,Filename,DataArray):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(DataArray)):
		file1.write('%lf\n' % DataArray[index][0])

	file1.close()


def WriteLagTime(Path,Filename,LagTime):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(LagTime)):
		file1.write('%lf\n' % LagTime[index])

	file1.close()



#ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/kLR_12_k15/AvgFiles/"
#WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_12_15/"

#ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/kLR_105_k15/AvgFiles/"
#WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_105_15/"

#ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/kLR_9_k15/AvgFiles/"
#WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_9_15/"

#ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/kLR_15_k15/AvgFiles/"
#WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_15_15/"

ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/kLR_15_k20/AvgFiles/"
WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_15_20/"

#ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/EquilibriumData_Test/"
#WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/PythonCode/CorrelationMesh_Test/"

#ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/EquilibriumData_Feb21/"
#WritePath = "CorrelationMesh_Feb21/"

CPValsStr = []
#CPVals = [-5.00]
#CP = -4.95

#while CP <= 5.0:
#	CPVals.append(round(CP,2))
#	CP = CP + 0.05

#CPVals.append(5.0)

CPVals = [-1.00]
CP = -0.995

#CPVals = [-10.0]
#CP = -9.9

while CP <= 1.0:
	#CPVals.append(round(CP,2))
	CPVals.append(CP)
	CP = CP + 0.005
	print "CP --> " + str(CP)

#CPVals.append(1.0)

#for index in range(len(CPVals)):
#	if CPVals[index] < 0.001:
#		CPValsStr.append("0.00000")
#	else:
#		CPValsStr.append(str(CPVals[index]) + "0000")

#for index in range(len(CPVals)):
#	if index == 0:
#		CPVals.append("-10.000000")
#	elif index == len(CPVals):
#		CPVals.append("10.000000") 
#	elif len(str(abs(round(CPVals[index],2)))) == 4:
#		CPValsStr.append(str(round(CPVals[index],2)) + str("0000"))
#	else:
#		CPValsStr.append(str(round(CPVals[index],2)) + str("00000"))

for index in range(len(CPVals)):
	CPValsStr.append(str(index))



#FilenameBase = 'BistableCorrelation_CP_'
FilenameBase = "BiCorr_CP_"
WriteNameMesh = 'CorrelationMesh_2.dat'
WriteNameLagTime = 'LagTime_2.dat'
WriteNameCP = 'CPVals_2.dat'
WriteNameFisher = 'FisherInformation_2.dat'

CorrelationMesh = []

for index in range(len(CPVals)):

	ReadName = FilenameBase + CPValsStr[index] + '_2.dat'

	print "ReadName --> " + ReadName

	LagTime,Correlation = ReadFile(ReadPath,ReadName)

	CorrelationMesh.append(Correlation)


WriteCorrelationArray(WritePath,WriteNameMesh,CorrelationMesh)
WriteFisherLandscape(WritePath,WriteNameFisher,CorrelationMesh)
WriteLagTime(WritePath,WriteNameLagTime,LagTime)
WriteLagTime(WritePath,WriteNameCP,CPVals)







