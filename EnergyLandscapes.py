#This script generates energy landscapes for the simulation parameters considered
#
#Steven Large
#February 19th 2018

import os
from math import *
import matplotlib.pyplot as plt

def WriteData(Path,Filename,xData,yData):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')
	for index in range(len(xData)):
		file1.write("%lf\t%lf\n" % (xData[index], yData[index]))
	file1.close()


def EnergyLandscape(kTrap,kBi,xData,Lambda):

	TotalEnergy = []

	Bistable = EnergyLandscape_Bi(kBi,xData)
	Trap = EnergyLandscape_Trap(kTrap,xData,Lambda)

	for index in range(len(xData)):
		TotalEnergy.append(Bistable[index] + Trap[index])

	return TotalEnergy


def EnergyLandscape_Trap(kTrap,xData,Lambda):

	Energy = []

	for index in range(len(xData)):
		TrapEnergy = kTrap*(xData[index] - Lambda)*(xData[index] - Lambda)
		Energy.append(TrapEnergy)

	return Energy


def EnergyLandscape_Bi(kBi,xData):

	Energy = []

	Xm = 10
	beta = 1

	for index in range(len(xData)):
		BistableEnergy = (-1/float(beta))*log(exp((-beta/float(2))*kBi*(xData[index] + Xm)*(xData[index] + Xm)) + exp((-beta/float(2))*kBi*(xData[index] - Xm)*(xData[index] - Xm)))
		Energy.append(BistableEnergy)

	return Energy


WritePath = "EnergyLandscapes/"
WriteNameFull = "Landscape_Full_kTrap_"
WriteNameBi = "Landscape_Bistable_kBi_" 
WriteNameTrap = "Landscape_Trap_kTrap_"

dX = 0.01
XMin = -15
XMax = 15

Counter = XMin

xData = []

while Counter <= XMax:
	xData.append(Counter)
	Counter = Counter + dX

kTrapVals = [0.006077,0.01215,0.024307,0.048614,0.09723]
kBiVals = [0.02636,0.0388,0.06386,0.11386,0.21386]

kTrapString = ["0.025","0.05","0.1","0.2","0.4"]
kBiString = ["0.625","1.25","2.5","5.0","10"]

LambdaVals = [-10,-5,0,5,10]

for index3 in range(len(LambdaVals)):

	for index1 in range(len(kTrapVals)):

		EnergyTrap = EnergyLandscape_Trap(kTrapVals[index1],xData,LambdaVals[index3])
		FilenameTrap = WriteNameTrap + kTrapString[index1] + "_L" + str(LambdaVals[index3]) + ".dat"
		WriteData(WritePath,FilenameTrap,xData,EnergyTrap)
	
		EnergyBi = EnergyLandscape_Bi(kBiVals[index1],xData)
		FilenameBi = WriteNameBi + kBiString[index1] + ".dat"
		WriteData(WritePath,FilenameBi,xData,EnergyBi)

		for index2 in range(len(kBiVals)):

			EnergyFull = EnergyLandscape(kTrapVals[index1],kBiVals[index2],xData,LambdaVals[index3])
			FilenameFull = WriteNameFull + kTrapString[index1] + "_kBi_" + kBiString[index2] + "_L" + str(LambdaVals[index3]) + ".dat"
			WriteData(WritePath,FilenameFull,xData,EnergyFull)
	
			EnergyBi = EnergyLandscape_Bi(kBiVals[index2],xData)
			FilenameBi = WriteNameBi + kBiString[index2] + ".dat"
			WriteData(WritePath,FilenameBi,xData,EnergyBi)


