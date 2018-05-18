#This python script generates theoretical predictions for protocol work values
#
#Steven Large
#May 19th 2018

import os
import numpy as np
from math import *
import matplotlib.pyplot as plt
import seaborn as sns


def LoadCorrelationArray(Path,Filename):

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


def ReadVector(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	Data = []

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		Data.append(eval(Parsed[0]))

	return Data


def ReadProtocol(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	CPVals = []
	Times = []

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		CPVals.append(eval(Parsed[0]))
		Times.append(eval(Parsed[1]))

	return CPVals,Times


def FindIndex(Array,Value):

	IndexArray = []

	TargetIndex = min(range(len(Array)), key=lambda i: abs(Value - Array[i]))

	return TargetIndex


def CalcTheoryWork(CorrMesh,CPValArray,TimeArray,CPVals,LagTimes):
	
	CPIndex = []
	LagTimeIndex = []

	CPDiff = []

	for index in range(len(CPVals)):
		CPIndex.append(FindIndex(CPValArray,CPVals[index]))
		LagTimeIndex.append(FindIndex(TimeArray,LagTimes[index]))

	for index in range(len(CPVals)-1):
		CPDiff.append(CPVals[index+1] - CPVals[index])

	BoundaryWork = CPDiff[0]*CPDiff[0]*CorrMesh[0][0]
	WorkAccumulator = 0

	for index in range(len(CPDiff)-1):
		WorkAccumulator = WorkAccumulator + CPDiff[index+1]*CPDiff[index+1]*CorrMesh[CPIndex[index+1]][0] + CPDiff[index+1]*CPDiff[index]*CorrMesh[CPIndex[index+1]][LagTimeIndex[index+1]]

	TotalWork = WorkAccumulator + BoundaryWork

	return TotalWork

def Driver(CorrPath,CorrName,CPName,LagTimeName,ProtoPath,ProtocolName):

	CorrMesh = LoadCorrelationArray(CorrPath,CorrName)
	CPValArray = ReadVector(CorrPath,CPName)
	LagTimeArray = ReadVector(CorrPath,LagTimeName)

	print "\t\t--- Equilibrium Data Read ---"

	CPVals,LagTimes = ReadProtocol(ProtoPath,ProtocolName)

	Work = CalcTheoryWork(CorrMesh,CPValArray,LagTimeArray,CPVals,LagTimes)

	return Work


def Driver_PreRead(CorrMesh,CPValArray,LagTimeArray,ProtoPath,ProtocolName):

	CPVals,LagTimes = ReadProtocol(ProtoPath,ProtocolName)

	Work = CalcTheoryWork(CorrMesh,CPValArray,LagTimeArray,CPVals,LagTimes)

	return Work


def WriteWorkData(Time,Work,Filename):

	if(os.path.exists("TheoryWork")==False):
		os.mkdir("TheoryWork")

	CompleteName = os.path.join("TheoryWork",Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(Time)):
		file1.write("%lf\t%lf\n" % (Time[index],Work[index]))

	file1.close()


CorrPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_12_15/"
CorrName = "CorrelationMesh_2.dat"
CPValName = "CPVals_2.dat"
LagTimeName = "LagTime_2.dat"

ProtoPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/Protocols_Mar21/Protocols_12_15/"
#ProtocolName = "TimeOpt_CP25_T2000.dat"
#ProtocolName2 = "Naive_CP25_T2000.dat"
#ProtocolName = "TimeOpt_CP25_T500.dat"
#ProtocolName2 = "Naive_CP25_T500.dat"

CorrMesh = LoadCorrelationArray(CorrPath,CorrName)
CPValArray = ReadVector(CorrPath,CPValName)
LagTimeArray = ReadVector(CorrPath,LagTimeName)

ProtocolTimes = [50,100,150,200,250,300,350,400,450,500,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800,5000]

WorkOpt = []
WorkNaive = []

for index in range(len(ProtocolTimes)):

	ProtocolName_Opt = "TimeOpt_CP25_T" + str(ProtocolTimes[index]) + ".dat"
	ProtocolName_Naive = "Naive_CP25_T" + str(ProtocolTimes[index]) + ".dat"

	WorkOpt.append(Driver_PreRead(CorrMesh,CPValArray,LagTimeArray,ProtoPath,ProtocolName_Opt))
	WorkNaive.append(Driver_PreRead(CorrMesh,CPValArray,LagTimeArray,ProtoPath,ProtocolName_Naive))

#OptWork = Driver(CorrPath,CorrName,CPValName,LagTimeName,ProtoPath,ProtocolName)
#NaiveWork = Driver(CorrPath,CorrName,CPValName,LagTimeName,ProtoPath,ProtocolName2)

#print "\n\nOptimal work --> " + str(OptWork) + "\n"
#print "Naive work --> " + str(NaiveWork) + "\n\n"

WriteWorkData(ProtocolTimes,WorkOpt,"TimeOptimizedWork_Theory.dat")
WriteWorkData(ProtocolTimes,WorkNaive,"TimeNaiveWork_Theory.dat")

sns.set(style='darkgrid',palette='muted',color_codes=True)

fig,ax = plt.subplots(1,1)

ax.plot(ProtocolTimes,WorkNaive,'r--',linewidth=2.5)
ax.plot(ProtocolTimes,WorkOpt,'b--',linewidth=2.5)
ax.plot(ProtocolTimes,WorkNaive,'ro',label="Naive Work")
ax.plot(ProtocolTimes,WorkOpt,'bo',label="Time-Optimized Work")

ax.legend(loc='upper right',fontsize=14)
ax.set_yscale('log')
ax.set_xlabel(r'Protocol duration $\tau$',fontsize=16)
ax.set_ylabel(r'Mean excess work $\langle W_{\rm ex}\rangle_{\Lambda}$',fontsize=16)

plt.show()
plt.close()








	






	

	





