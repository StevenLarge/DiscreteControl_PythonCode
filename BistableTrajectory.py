#This standalone python script simulates a discrete trajectory in the domain [-1,1]
#for a bistable parameter set to test for desired behaviour
#
#StevenLarge
#January 31st 2018

import os
import numpy as np
import matplotlib.pyplot as plt
from math import *
import random


#Gobal simulation parameters

kTrap = 1.0

kBiLeft = 0.5
kBiRight = 0.5
X_m = 5.0
DeltaE = 0
dX = 0.01

beta = 1
a = 0.25
mass = 1
dt = 0.05


def WriteTrace(Filename,Path,CPVals,PosVals):

	CompleteName = os.path.join(Path,Filename)
	file1 = open(CompleteName,'w')
	for index in range(len(CPVals)):
		file1.write("%lf\t%lf\n" % (CVals[index],PosVals[index]))
	file1.close()


def BistableEnergy(Position):

	Energy = -(1.0/beta)*log(exp((-0.5*kBiLeft*beta)*((Position + X_m)**2)) + exp((-0.5*kBiRight*beta)*((Position - X_m)**2) + 0.5*beta*kBiRight*DeltaE))

	#BistableEnergy = (-1.0/beta)*log(exp(-0.5*beta*kL*((position + X_m)*(position + X_m))) + exp(-0.5*beta*kR*((position - X_m)*(position - X_m)) - beta*DeltaE));

	return Energy


def TrapEnergy(Position,CPVal):

	return kTrap*((Position - CPVal)**2)


def BistableForce(Position):

	PlusPos = Position + dX
	MinusPos = Position - dX

	PlusEnergy = BistableEnergy(PlusPos)
	MinusEnergy = BistableEnergy(MinusPos)

	Force = -(PlusEnergy - MinusEnergy)/(float(2)*dX) 					#Finite difference derivative

	return Force


def TrapForce(Position,CPVal):

	return -kTrap*(Position - CPVal)


def TotalForce(Position, CPVal):

	PlusPos = Position + dX
	MinusPos = Position - dX

	PlusEnergy = BistableEnergy(PlusPos) + TrapEnergy(PlusPos,CPVal)
	MinusEnergy = BistableEnergy(MinusPos) + TrapEnergy(MinusPos,CPVal)

	Force = -(PlusEnergy - MinusEnergy)/(float(2)*dX)

	return Force


def LangevinPropogator(time, position, velocity, CPVal):

	velocity = sqrt(a)*(velocity) + sqrt((1-a)/(beta*mass))*random.gauss(0,1)
	velocity = velocity + 0.5*dt*TotalForce(position,CPVal)/mass
	position = position + 0.5*dt*(velocity)

	time += dt

	position = position + 0.5*dt*(velocity)
	velocity = velocity + 0.5*dt*TotalForce(position,CPVal)/mass
	velocity = sqrt(a)*(velocity) + sqrt((1-a)/(beta*mass))*random.gauss(0,1)
	
	return time, position, velocity


def Driver(CPVals,CPTimes):

	PositionTracker = []
	CPTracker = []

	position = CPVals[0]
	velocity = 0

	for index in range(len(CPTimes)):

		time = 0
		CP = CPVals[index]

		while time < CPTimes[index]:

			time, position, velocity = LangevinPropogator(time, position, velocity, CP)
			PositionTracker.append(position)
			CPTracker.append(CP)

	plt.plot(CPTracker)
	plt.plot(PositionTracker)
	plt.show()
	plt.close()

TotalEnergyLandscape = []
TrapLandscape = []
BistableLandscape = []
PosTrack = []

PosCounter = -7

while PosCounter <= 7:

	TrapE = TrapEnergy(PosCounter,0)
	BistableE = BistableEnergy(PosCounter)

	TrapLandscape.append(TrapE)
	BistableLandscape.append(BistableE)
	TotalEnergyLandscape.append(TrapE + BistableE)
	PosTrack.append(PosCounter)

	PosCounter += 0.01


#plt.plot(PosTrack,TrapLandscape)
#plt.plot(PosTrack,BistableLandscape)
#plt.plot(PosTrack,TotalEnergyLandscape)
#plt.show()
#plt.close()


CPVals = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
CPTimes = [500, 500, 500, 500, 500, 500, 500, 500, 500]

Driver(CPVals,CPTimes)







