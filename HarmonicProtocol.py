#This code propogates a naive discrete protocol of a harmonic trap 
#
#Steven Large
#February 2nd 2018

import os
import random
from math import *

import matplotlib.pyplot as plt

def Langevin(time,position,velocity,CPVal):

	velocity = sqrt(a)*(velocity) + sqrt((1-a)/(beta*mass))*random.gauss(0,1)
	velocity = velocity + 0.5*dt*ForceTrap(position,CPVal)/mass
	position = position + 0.5*dt*(velocity)

	time += dt

	position = position + 0.5*dt*(velocity)
	velocity = velocity + 0.5*dt*ForceTrap(position,CPVal)/mass
	velocity = sqrt(a)*(velocity) + sqrt((1-a)/(beta*mass))*random.gauss(0,1)
	
	return time, position, velocity


def ForceTrap(Position,CP):

	return -1*kTrap*(position - CP)


def CalcWork(position, CPOld, CPNew):

	E1 = 0.5*kTrap*(position - CPOld)*(position - CPOld)
	E2 = 0.5*kTrap*(position - CPNew)*(position - CPNew)

	dE = E2 - E1

	return dE


def WriteData(Path,Filename,Work,ProtocolTime):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(Work)):

		file1.write("%lf\t%lf\n" % (ProtocolTime[index],Work[index]))

	file1.close()


beta = 1
mass = 1
a = 0.25
kTrap = 1.0
dt = 0.1

CP = 0
Equilibration = 100
ProtocolTime = 1

MaxTime = 1000
CPSteps = 10

Repetitions = 100

WorkTime = []
ProtocolArray = []

while ProtocolTime < MaxTime:

	WorkAcc = 0

	CPTime = ProtocolTime/float(CPSteps)

	print "Protocol Time --> " + str(ProtocolTime)

	for index2 in range(Repetitions):

		time = 0
		position = 0
		velocity = 0
		CP = 0

		while time < Equilibration:
			time,position,velocity = Langevin(time,position,velocity,CP)

		for index3 in range(CPSteps):

			time = 0

			while time < CPTime:

				time,position,velocity = Langevin(time,position,velocity,CP)

			CPOld = CP
			CP = CP + 0.25

			WorkAcc = WorkAcc + CalcWork(position,CPOld,CP)

	WorkTime.append(WorkAcc/float(Repetitions))
	ProtocolArray.append(ProtocolTime)

	ProtocolTime = ProtocolTime*2


WritePath = "GaussianWork/"
Filename = "WorkTotal_k" + str(kTrap) + ".dat"

plt.plot(ProtocolArray,WorkTime)
plt.xscale('log')
plt.yscale('log')
plt.plot()
plt.show()
plt.close()

WriteData(WritePath,Filename,WorkTime,ProtocolArray)




