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

#NumberCPVals = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#NumberCPVals = [5,9,13,17,21,25,29,33,37,41]
#NumberCPVals = [17,21,25,29,33,37,41]
#NumberCPVals = [25,29,33,37,41]
NumberCPVals = [37,41]
#ProtocolTimes = [5,10,50,100,500]
ProtocolTimes = [10,50,100,150,200,250,300,350,400,450,500]

#Param_Ext = ["9_15/","105_15/","12_15/","15_15/"]
#Param_Ext = ["9_10/","9_15/","9_20/","12_10/","12_15/","12_20/","15_10/","15_15/","15_20/"]
Param_Ext = ["15_20/"]

CPStart = -1

PaddingTime = 100

CorrelationPath_Base = "CorrelationMesh_"
FilenameCorr = "CorrelationMesh.dat"
FilenameCP = "CPVals.dat"
FilenameLagTime = "LagTime.dat"

FullOptimizerIterations = 5

for ParameterIndex in range(len(Param_Ext)):

	WritePath = WritePathBase + Param_Ext[ParameterIndex]
	WritePathLog = WritePath + "Logs/"
	CorrelationPath = CorrelationPath_Base + Param_Ext[ParameterIndex]

	CorrelationArray = FullOpt.ReadCorrelationArray(CorrelationPath,FilenameCorr)
	LagTime_Vector = FullOpt.ReadVector(CorrelationPath,FilenameLagTime)
	CPVals_Vector = FullOpt.ReadVector(CorrelationPath,FilenameCP)


	for index1 in range(len(NumberCPVals)):

		for index2 in range(len(ProtocolTimes)):

			if(ProtocolTimes[index2] > 300 || index1!=0):

				OptimalCP,OptimalTime,NaiveCP,NaiveTime,CostTracker = FullOpt.Driver_PreRead_Brute(FullOptimizerIterations,NumberCPVals[index1],ProtocolTimes[index2],CPVals_Vector,LagTime_Vector,CorrelationArray)

				OptimalTime.append(PaddingTime)
				OptimalTime.insert(0,PaddingTime)
				NaiveTime.append(PaddingTime)
				NaiveTime.insert(0,PaddingTime)

				WriteNameFull = "FullOpt_CP" + str(NumberCPVals[index1]) + "_T" + str(ProtocolTimes[index2]) + ".dat"
				WriteNameLog = "OptimizerLogFile-Full_CP" + str(NumberCPVals[index1]) + "_T" + str(ProtocolTimes[index2]) + ".dat"

				WriteData.WriteProtocol(WritePath,WriteNameFull,OptimalCP,OptimalTime)
				WriteData.OptimizerLog_Cost(WritePathLog,WriteNameLog,CostTracker)



