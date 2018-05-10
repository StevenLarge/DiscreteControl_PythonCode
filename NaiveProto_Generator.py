#This script generates the Naive discrete control protocols for variable control-parameter number simulations
#
#Steven Large
#April 5th 2018

import os

def WriteProtocol(Path,Filename,CPVals,Times):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(CPVals)):
		file1.write("%lf\t%lf\n" % (CPVals[index], Times[index]))

	file1.close()

def GenerateProtocol(NumCPVals,TotalTime):

	CPVals = []
	CPTimes = []

	CPStep = float(2)/float(NumCPVals-1)
	TimeAlloc = float(TotalTime)/float(NumCPVals-2)

	CurrentCP = -1

	for index in range(NumCPVals):
		CPVals.append(CurrentCP)
		CurrentCP = CurrentCP + float(CPStep)

	for index in range(NumCPVals-2):
		CPTimes.append(TimeAlloc)

	CPTimes.append(100)
	CPTimes.insert(0,100)

	return CPVals,CPTimes


CPNumber = [4,8,16,32,64,128,256,512]
WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/Protocols_12_15/"

#CPNumber = [4]

for index in range(len(CPNumber)):

	Filename = "Naive_CP" + str(CPNumber[index]) + "_T200.dat"
	CPVals,Times = GenerateProtocol(CPNumber[index],200)
	WriteProtocol(WritePath,Filename,CPVals,Times)

	#print "CPVals -->\t" + str(CPVals) + "\nTimes -->\t" + str(Times) + "\n\n"


