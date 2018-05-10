#Protocol propogation
#
#Steven Large
#February 15th 2018

import os
from math import *
import numpy as np
import random

import matplotlib.pyplot as plt

from BistableParameters import *


def ReadProtocol(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	CPVals = []
	TimeVals = []

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Parsed = TempData[index].split()

		CPVals.append(eval(Parsed[0]))
		TimeVals.append(eval(Parsed[1]))

	return CPVals,TimeVals


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


def WriteWorkData(Work,Filename,Path):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')
	
	for index in range(len(Work)):
		file1.write("%lf\n" % Work[index])

	file1.close()

"""
ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_Feb12/"
ReadNameNaive = "Naive_CP9_T1000.dat"
ReadNameOpt = "TimeOpt_CP9_T1000.dat"

WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/PythonCode/Plots_Feb12/WorkData/"
WriteName_Opt = "OptWorkData.dat"
WriteName_Naive = "NaiveWorkData.dat"

CPVals_Naive,CPTime_Naive = ReadProtocol(ReadPath,ReadNameNaive)
CPVals_Opt,CPTime_Opt = ReadProtocol(ReadPath,ReadNameOpt)

Realizations = 5000

NaiveWorkTracker = []
OptWorkTracker = []

PositionTracker_Naive = []
CPTracker_Naive = []
Time_Naive = []

PositionTracker_Opt = []
CPTracker_Opt = []
Time_Opt = []

position = -1
velocity = 0
time = 0

for index1 in range(len(CPVals_Naive)-1):

	CP = CPVals_Naive[index1]

	time = 0

	while time < CPTime_Naive[index1]:
		time,position,velocity = Langevin(time,position,velocity,CP)
		PositionTracker_Naive.append(position)
		CPTracker_Naive.append(CP)
		Time_Naive.append(float(len(CPTracker_Naive))/dt)

while time < CPTime_Naive[-1]:
	time,position,velocity = Langevin(time,position,velocity,CPVals_Naive[-1])
	PositionTracker_Naive.append(position)
	CPTracker_Naive.append(CPVals_Naive[-1])
	Time_Naive.append(float(len(CPTracker_Naive))/dt)


plt.plot(Time_Naive,CPTracker_Naive)
plt.plot(Time_Naive,PositionTracker_Naive)
plt.show()
plt.close()

#for index1 in range(Realizations):

	#position = -1
	#velocity = 0
	#time = 0

	#print "Realization --> " + str(index1) 

	#WorkAcc_Naive = 0

	#for index2 in range(len(CPVals_Naive)-1):

		#CP = CPVals_Naive[index2]

		#time = 0

		#if(index1==0):
		#	while time < CPTime_Naive[index2]:
		#		time,position,velocity = Langevin(time,position,velocity,CP)
		#		PositionTracker_Naive.append(position)
		#		CPTracker_Naive.append(CP)
		#		Time_Naive.append(float(len(CPTracker_Naive))/dt)

		#else:
		#	while time < CPTime_Naive[index2]:
		#		time,position,velocity = Langevin(time,position.velocity,CP)

		#while time < CPTime_Naive[index2]:
		#		time,position,velocity = Langevin(time,position,velocity,CP)

		#WorkAcc_Naive = WorkAcc_Naive + CalcWork(position, CP, CPVals_Naive[index2+1])

	#time = 0

	#if(index1==0):
	#	while time < CPTime_Naive[-1]:
	#		time,position,velocity = Langevin(time,position,velocity,CPVals_Naive[-1])
	#		PositionTracker_Naive.append(position)
	#		CPTracker_Naive.append(CPVals_Naive[-1])
	#		Time_Naive.append(float(len(CPTracker_Naive))/dt)

	#NaiveWorkTracker.append(WorkAcc_Naive)


	#position = -1
	#velocity = 0
	#time = 0

	#WorkAcc_Opt = 0

	#for index2 in range(len(CPVals_Opt)-1):

		#CP = CPVals_Opt[index2]

		#time = 0

		#if(index1==0):
		#	while time < CPTime_Opt[index2]:
		#		time,position,velocity = Langevin(time,position,velocity,CP)
		#		PositionTracker_Opt.append(position)
		#		CPTracker_Opt.append(CP)
		#		Time_Opt.append(float(len(CPTracker_Opt))/dt)

		#else:
		#	while time < CPTime_Opt[index2]:
		#		time,position,velocity = Langevin(time,position.velocity,CP)

		#while time < CPTime_Opt[index2]:
		#	time,position,velocity = Langevin(time,position,velocity,CP)

		#WorkAcc_Opt = WorkAcc_Opt + CalcWork(position, CP, CPVals_Opt[index2+1])

	#time = 0

	#if(index1==0):
	#	while time < CPTime_Opt[-1]:
	#		time,position,velocity = Langevin(time,position,velocity,CPVals_Opt[-1])
	#		PositionTracker_Opt.append(position)
	#		CPTracker_Opt.append(CPVals_Opt[-1])
	#		Time_Opt.append(float(len(CPTracker_Opt))/dt)

	#OptWorkTracker.append(WorkAcc_Opt)


#plt.plot(Time_Naive,CPTracker_Naive)
#plt.plot(Time_Naive,PositionTracker_Naive)
#plt.show()
#plt.close()

#plt.plot(Time_Opt,CPTracker_Opt)
#plt.plot(Time_Opt,PositionTracker_Opt)
#plt.show()
#plt.close()


#plt.hist(NaiveWorkTracker)
#plt.show()
#plt.close()

#plt.hist(OptWorkTracker)
#plt.show()
#plt.close()

#WriteWorkData(OptWorkTracker,WriteName_Opt,WritePath)
#WriteWorkData(NaiveWorkTracker,WriteName_Naive,WritePath)

#plt.hist(NaiveWorkTracker,alpha=0.5,color='r',normed=True)
#plt.hist(OptWorkTracker,alpha=0.5,color='b',normed=True)
#plt.xlabel('Total Work (kT)')
#plt.ylabel('P(W)')
#plt.savefig('Plots_Feb12/WorkCompareHisto.pdf',format='pdf')
#plt.show()
#plt.close()


#print "\n\nAverage Naive Work --> " + str(np.mean(NaiveWorkTracker))
#print "\n\nAverage Optimal Work --> " + str(np.mean(OptWorkTracker)) + "\n\n"


"""








