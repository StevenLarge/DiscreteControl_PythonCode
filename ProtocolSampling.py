#This python script reads in a seed protocol and performs a protocol samplng to determine the minimum-work discrete protocol
#
#Steven Large
#February 19th 2018

import os
import random
from math import *
import ProtocolPropogation

import matplotlib.pyplot as plt

def ReadSeedProtocol(ReadPath,Filename):

	CompleteName = os.path.join(ReadPath,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	CPVals = []
	CPTimes = []

	for index in range(len(TempData)):

		Parsed = TempData[index].split()
		CPVals.append(eval(Parsed[0]))
		CPTimes.append(eval(Parsed[1]))

	return CPVals,CPTimes


def WriteOptimalProtocol(WritePath,Filename,CPVals,TimeVals):

	CompleteName = os.path.join(WritePath,Filename)
	file1 = open(CompleteName,'w')

	for index in range(len(CPVals)):
		file1.write("%lf\t%lf\n" % (CPVals,TimeVals))

	file1.close()


def ProtocolWork(CPVals,CPTimes,NumSamples):

	Work = 0

	for index in range(NumSamples):

		Work = Work + ProtocolDriver(CPVals,CPTimes)

	Work = Work/float(NumSamples)

	return Work


def ProtocolDriver(CPVals,CPTimes):

	position = -1
	velocity = 0

	WorkAcc = 0

	for index in range(len(CPVals)-1):

		time = 0
		CP = CPVals[index]

		while time < CPTimes[index]:
			time,position,velocity = ProtocolPropogation.Langevin(time,position,velocity,CPVals[index])

		WorkAcc = WorkAcc + ProtocolPropogation.CalcWork(position,CPVals[index],CPVals[index+1])

	return WorkAcc


def ProtocolPerturbation(CPVals,CPTimes,TotalTime,CPDist):

	for index in range(len(CPVals)-2):

		CPVals[index+1] = CPVals[index+1] + random.gauss(0,CPDist*0.05)
		CPTimes[index+1] = CPTimes[index+1] + random.gauss(0,CPTimes[index+1]*0.01)

	NormFactor = sum(CPTimes[1:len(CPTimes)-1])

	for index in range(len(CPTimes)-2):
		CPTimes[index+1] = CPTimes[index+1]/float(NormFactor)

	return CPVals,CPTimes


def Driver(CPVals,CPTimes,MCSteps,NumberSamples,TotalTime,CPDist):

	Flag = True
	MCCounter = 0

	for index in range(MCSteps):

		print "MCSteps --> " + str(index) 

		if Flag==True:
			Work = ProtocolWork(CPVals,CPTimes,NumberSamples)

		CPVals_Test,CPTimes_Test = ProtocolPerturbation(CPVals,CPTimes,TotalTime,CPDist)

		Work_Test = ProtocolWork(CPVals_Test,CPTimes_Test,NumberSamples)

		if Work_Test < Work:
			CPVals = CPVals_Test
			CPTimes = CPTimes_Test
			Work = Work_Test
			Flag = False
			MCCounter = MCCounter + 1
			print "\t\t*"
		else:
			if random.uniform(0,1) < exp(Work - Work_Test):
				CPVals = CPVals_Test
				CPTimes = CPTimes_Test
				Work = Work_Test
				Flag = False
				MCCounter = MCCounter + 1
				print "\t\t*"
			else:	
				Flag = False

	print "\n\nMC Acceptance ratio --> " + str(float(MCCounter)/float(MCSteps)) + "\n\n"

	return CPVals,CPTimes


ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_Feb12/"
ReadNameNaive = "Naive_CP9_T1000.dat"
ReadNameOpt = "TimeOpt_CP9_T1000.dat"

WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/PythonCode/Protocols_Feb12"
WriteName_Opt = "OptProtocol_Sampled.dat"

CPVals,CPTimes = ReadSeedProtocol(ReadPath,ReadNameOpt)

TotalTime = 1000
CPDist = 2
MCSteps = 50
NumberSamples = 75


CPValsNew,CPTimesNew = Driver(CPVals,CPTimes,MCSteps,NumberSamples,TotalTime,CPDist)

plt.plot(CPValsNew,CPTimesNew,'b--')
plt.plot(CPVals,CPTimes,'r--')
plt.plot(CPValsNew,CPTimesNew,'bo')
plt.plot(CPVals,CPTimes,'ro')
plt.show()
plt.close()

