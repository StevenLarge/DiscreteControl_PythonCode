#This is prototype optimization code written in Python for the restricted optimization of time allocation and/or spatial optimization in a discrete protocol
#
#Steven Large
#January 30th 2018

import os
from math import *
import random

import matplotlib.pyplot as plt
import numpy as np


def ImportCorrelationMesh(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	CorrelationArray = []

	file1 = open(CompleteName,'r')
	TotalData = file1.readlines()
	file1.close()

	for index1 in range(len(TotalData)):
		Parsed = TotalData[index1].split()
		CorrelationArray.append([])
		for index2 in range(len(Parsed)):
			CorrelationArray[index1].append(eval(Parsed[index2]))

	return CorrelationArray


def ImportVector(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	Data = []

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		Data.append(eval(Parsed[0]))

	return Data


def TangentPlane(CPTimes):

	TangentVector = []

	for index in range(len(CPTimes)):
		TangentVector.append(float(1)/float(len(CPTimes)))

	return TangentVector


def CalculateCost(CPTimes,CPVals,CorrelationMatrix):

	return 0


def ComputeGradient(CPValIndex,CPTimeIndex,CorrelationMatrix):

	GradientVector = []

	for index in range(len(CPValIndex)):

		#print "CPValIndex --> " + str(CPValIndex[index])
		#print "CPTimeIndex --> " + str(CPTimeIndex[index])

		GradientVector.append(CorrelationMatrix[CPValIndex[index]][CPTimeIndex[index]+1] - CorrelationMatrix[CPValIndex[index]][CPTimeIndex[index]-1])

	return GradientVector


def RestrictionUpdate(VectorGradient,StepSize,CPTimes,TangentVector):

	NewCPTimes = []


	#Calculate the projection of the gradient onto the tnagent vector

	Projection = []

	for index in range(len(VectorGradient)):

		Projection.append(VectorGradient[index]*TangentVector[index])


	#Calculate the vector which is needed to be subtracted from the gradient so that it lies in the tangent space

	Restriction = []

	for index in range(len(Projection)):

		Restriction.append(-1*Projection[index])


	#Now subtract that vector from the vector gradient and normalize the gradient to a magnitude of 1

	ManifoldGradient = []
	NormFactor = 0

	for index in range(len(Restriction)):

		ManifoldGradient.append(VectorGradient[index] + Restriction[index])
		NormFactor = NormFactor + abs(ManifoldGradient[index])

	for index in range(len(ManifoldGradient)):

		ManifoldGradient[index] = ManifoldGradient[index]/float(NormFactor)


	#Update the CPTimes vector by the gradient

	for index in range(len(ManifoldGradient)):

		NewCPTimes.append(CPTimes[index] + StepSize*ManifoldGradient[index])


	return NewCPTimes


def CalcCPIndex(CPVector,CPVals):

	IndexArray = []

	for index in range(len(CPVals)):

		TempIndex = min(range(len(CPVector)), key=lambda i: abs(CPVals[index] - CPVector[i]))

		IndexArray.append(TempIndex)

	return IndexArray


def CalcTimeIndex(LagTimeVector,TimeVals):

	IndexArray = []

	for index in range(len(TimeVals)):

		TempIndex = min(range(len(LagTimeVector)), key=lambda i: abs(TimeVals[index] - LagTimeVector[i]))

		IndexArray.append(TempIndex)

	return IndexArray


def OptimizeTime(NumSteps,TotalTime,CPVals):

	NaiveTime = float(NumSteps)/float(TotalTime)

	StepTime = []
	InitialTime = []

	Iterations = 10

	CostTracker = []

	StepSize = 0.1

	Path = "CorrelationMesh/"
	Filename = "CorrelationMesh.dat"
	FilenameTime = "LagTime.dat"
	FilenameForce = "CPVals.dat"

	CorrelationMatrix = ImportCorrelationMesh(Path,Filename)

	print str(np.shape(CorrelationMatrix))

	LagTime = ImportVector(Path,FilenameTime)
	CPVector = ImportVector(Path,FilenameForce)

	for index in range(NumSteps - 1):

		StepTime.append(NaiveTime)
		InitialTime.append(NaiveTime)

	CPIndex = CalcCPIndex(CPVector,CPVals)
	TimeIndex = CalcTimeIndex(LagTime,StepTime)

	TangentVector = TangentPlane(StepTime)

	print "\n\nSetting up....\n\n\n"

	CostTracker.append(CalculateCost(TimeIndex,CPIndex,CorrelationMatrix))

	for index in range(Iterations):

		print "Iteration --> " + str(index)

		TimeIndex = CalcTimeIndex(LagTime,StepTime)

		VectorGradient = ComputeGradient(CPIndex,TimeIndex,CorrelationMatrix)

		StepTime = RestrictionUpdate(VectorGradient,StepSize,StepTime,TangentVector)

		CostTracker.append(CalculateCost(TimeIndex,CPIndex,CorrelationMatrix))

	plt.plot(NaiveTime,CPVals,'o')
	plt.plot(StepTime,CPVals,'o')
	plt.show()
	plt.close()



CPVals = [-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1]
NumSteps = 7
TotalTime = 100

OptimizeTime(NumSteps,TotalTime,CPVals)

