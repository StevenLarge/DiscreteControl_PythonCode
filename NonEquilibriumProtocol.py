#This python script propogates the nonequilbirium discrete protocols and calcualtes the work associated
#
#Steven Large
#March 1st 2018

import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import *
import random

from BistableParameters import *

def ReadProtocol(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	CPVals = []
	CPTimes = []

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		CPVals.append(eval(Parsed[0]))
		CPTimes.append(eval(Parsed[1]))

	return CPVals, CPTimes


def WriteWorkData(WorkArray,Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(WorkArray)):
		file1.write("%lf\n" % WorkArray[index])

	file1.close()


def PropogateProtocol(CPVals,TimeVals):

	position = CPVals[0]
	time = 0
	velocity = 0

	Work = 0

	for index in range(len(CPVals)-1):

		time = 0

		while time <= TimeVals[index]:
			time,position,velocity = Langevin(time,position,velocity,CPVals[index])

		Work = Work + CalcWork(position,CPVals[index],CPVals[index+1])

	return Work


def Langevin(time,position,velocity,CP):
	
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*mass))*random.gauss(0,1) 
	velocity = velocity+0.5*dt*BistableForce(position,CP)/mass
	position = position+0.5*dt*velocity

	time += dt

	position = position+0.5*dt*velocity 
	velocity = velocity+0.5*dt*BistableForce(position,CP)/mass
	velocity = sqrt(a)*velocity+sqrt((1-a)/(beta*mass))*random.gauss(0,1)

	return time, position, velocity


def CalcWork(position,CPInit,CPFinal):

	EnergyInit = TotalEnergy(position,CPInit)
	EnergyFinal = TotalEnergy(position,CPFinal)

	Energy = EnergyFinal - EnergyInit

	return Energy
	

def TotalEnergy(position,CP):

	BistableEnergy = (-1/float(beta))*log(exp((-beta/float(2))*kL*(position + Xm)*(position + Xm)) + exp((-beta/float(2))*kR*(position - Xm)*(position - Xm) + (beta/float(2))*DeltaE))
	TrapEnergy = (kTrap/float(2))*(position - CP)*(position - CP)

	Energy = BistableEnergy + TrapEnergy

	return Energy


def BistableEnergy(position):

	Energy = (-1/float(beta))*log(exp((-beta/float(2))*kL*(position + Xm)*(position + Xm)) + exp((-beta/float(2))*kR*(position - Xm)*(position - Xm) + (beta/float(2))*DeltaE))
	
	return Energy


def BistableForce(position,CP):

	EnergyForward = BistableEnergy(position+dX)
	EnergyBehind = BistableEnergy(position-dX)

	ForceMol = float(-1)*(EnergyForward - EnergyBehind)/(float(2)*dX)
	ForceTrap = -1*kTrap*(position - CP)

	return ForceMol + ForceTrap


def Driver(Realizations,NumCPVals,TotalTime):

	ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Protocols/"
	WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Work_12_15/"

	FilenameOpt = "TimeOpt_CP23_T500.dat"
	FilenameNaive = "Naive_CP23_T500.dat"

	WriteName = "Work_TimeOpt_CP23_T500.dat"
	WriteNameNaive = "Work_NaiveOpt_CP23_T500.dat"

	CPVals, CPTimes = ReadProtocol(ReadPath,FilenameOpt)

	WorkArray = []

	for index in range(Realizations):

		if (index%1000 == 0):
			print "Optimal Realization --> " + str(index) 

		Work = PropogateProtocol(CPVals,CPTimes)

		WorkArray.append(Work)

	AvgWork = np.mean(WorkArray)

	WriteWorkData(WorkArray,WritePath,WriteName)


	CPVals, CPTimes = ReadProtocol(ReadPath,FilenameNaive)

	WorkArray = []

	for index in range(Realizations):

		if (index%1000 == 0):
			print "Naive Realization --> " + str(index) 

		Work = PropogateProtocol(CPVals,CPTimes)

		WorkArray.append(Work)

	AvgWorkNaive = np.mean(WorkArray)

	print "\n\nAvg Work Opt   --> " + str(AvgWork)
	print "\n\nAvg Work Naive --> " + str(AvgWorkNaive)

	WriteWorkData(WorkArray,WritePath,WriteNameNaive)



Realizations = 10000
NumCPVals = 23
TotalTime = 500

Driver(Realizations,NumCPVals,TotalTime)

