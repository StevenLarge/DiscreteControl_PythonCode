#This python script generates the Fully-Optimal protocols Discrete nonequilibrium control simulations
#
#Steven Large
#March 5th 2018

import numpy as np
import scipy.optimize

import os

import OptimizeFull as FullOpt
import WriteData

WritePathBase = "Protocols_"

NumberCPVals = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,25]
ProtocolTimes = [5,10,50,100,500]

Param_Ext = ["12_15/"]

CPStart = -1

PaddingTime = 100

CorrelationPath_Base = "CorrelationMesh_"
FilenameCorr = "CorrelationMesh_2.dat"
FilenameCP = "CPVals.dat"
FilenameLagTime = "LagTime.dat"

FullOptimizerIterations = 15

for ParameterIndex in range(len(Param_Ext)):

	WritePath = WritePathBase + Param_Ext[ParameterIndex]
	WritePathLog = WritePath + "Logs/"
	CorrelationPath = CorrelationPath_Base + Param_Ext[ParameterIndex]

	CorrelationArray = FullOpt.ReadCorrelationArray(CorrelationPath,FilenameCorr)
	LagTime_Vector = FullOpt.ReadVector(CorrelationPath,FilenameLagTime)
	CPVals_Vector = FullOpt.ReadVector(CorrelationPath,FilenameCP)


	for index1 in range(len(NumberCPVals)):

		for index2 in range(len(ProtocolTimes)):

			OptimalCP,OptimalTime,NaiveCP,NaiveTime,CostTracker = FullOpt.Driver_PreRead_Brute(FullOptimizerIterations,NumberCPVals[index1],ProtocolTimes[index2],CPVals_Vector,LagTime_Vector,CorrelationArray)

			OptimalTime.append(PaddingTime)
			OptimalTime.insert(0,PaddingTime)
			NaiveTime.append(PaddingTime)
			NaiveTime.insert(0,PaddingTime)

			WriteNameFull = "FullOpt_CP" + str(NumberCPVals[index1]) + "_T" + str(ProtocolTimes[index2]) + ".dat"
			WriteNameLog = "OptimizerLogFile-Full_CP" + str(NumberCPVals[index1]) + "_T" + str(ProtocolTimes[index2]) + ".dat"

			WriteData.WriteProtocol(WritePath,WriteNameFull,OptimalCP,OptimalTime)
			WriteData.OptimizerLog_Cost(WritePathLog,WriteNameLog,CostTracker)



