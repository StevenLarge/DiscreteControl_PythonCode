#This python script generates the Space-Optimized protocols Discrete nonequilibrium control simulations
#
#Steven Large
#March 5th 2018

import numpy as np
import scipy.optimize

import os

import OptimizeSpace as SpaceOpt
import WriteData

WritePathBase = "Protocols_"

#NumberCPVals = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#NumberCPVals = [5,9,13,17,21,25,29]
#NumberCPVals = [33,37,41]
NumberCPVals = [29]
#ProtocolTimes = [1,5,10,50,100,500]
#ProtocolTimes = [10,50,100,150,200,250,300,350,400,450,500]
ProtocolTimes = [450,500]

#Param_Ext = ["9_15/","105_15/","12_15/","15_15/"]
#Param_Ext = ["9_10/","9_15/","9_20/","12_10/","12_15/","12_20/","15_10/","15_15/","15_20/"]
Param_Ext = ["15_20/"]

CPStart = -1

PaddingTime = 100

CorrelationPath_Base = "CorrelationMesh_"
FilenameCorr = "CorrelationMesh.dat"
FilenameCP = "CPVals.dat"
FilenameLagTime = "LagTime.dat"


for ParameterIndex in range(len(Param_Ext)):

	WritePath = WritePathBase + Param_Ext[ParameterIndex]
	WritePathLog = WritePath + "Logs/"
	CorrelationPath = CorrelationPath_Base + Param_Ext[ParameterIndex]

	CorrelationArray = SpaceOpt.ReadCorrelationArray(CorrelationPath,FilenameCorr)
	LagTime_Vector = SpaceOpt.ReadVector(CorrelationPath,FilenameLagTime)
	CPVals_Vector = SpaceOpt.ReadVector(CorrelationPath,FilenameCP)

	for index1 in range(len(NumberCPVals)):

		for index2 in range(len(ProtocolTimes)):

			OptimalResult,NaiveCP,TimeAlloc = SpaceOpt.Driver_PreRead(NumberCPVals[index1],ProtocolTimes[index2],CPVals_Vector,LagTime_Vector,CorrelationArray)

			OptimalSpace = list(OptimalResult.x)
			OptimalCP = [CPStart]
			CPCounter = CPStart

			for index3 in range(len(OptimalSpace)):
				CPCounter = CPCounter + OptimalSpace[index3]
				OptimalCP.append(CPCounter)

			TimeAlloc.append(PaddingTime)
			TimeAlloc.insert(0,PaddingTime)
			NaiveCP.append(1)
			NaiveCP.insert(0,-1)

			WriteNameSpace = "SpaceOpt_CP" + str(NumberCPVals[index1]) + "_T" + str(ProtocolTimes[index2]) + ".dat"
			WriteNameLog = "OptimizerLogFile-Space_CP" + str(NumberCPVals[index1]) + "_T" + str(ProtocolTimes[index2]) + ".dat"

			WriteData.WriteProtocol(WritePath,WriteNameSpace,OptimalCP,TimeAlloc)
			WriteData.OptimizerLog(WritePathLog,WriteNameLog,OptimalResult)




