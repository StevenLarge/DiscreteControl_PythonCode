#This python script contains plotting routines for Discrete control write-up documents ect.
#
#Steven Large
#March 2nd 2018

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
import matplotlib.gridspec as gridspec
from matplotlib import rc

beta = 1
m = 1


def ReadArray(Path,Filename):

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
	LagTimes = []

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		CPVals.append(eval(Parsed[0]))
		LagTimes.append(eval(Parsed[1]))

	return CPVals,LagTimes


def PlotEnergyLandscape(WritePath,WriteName,Padding=1,CPMin=-1,CPMax=1,kLR=12,kx=1.5,DeltaE=0):

	FullName = os.path.join(WritePath,WriteName)

	XData = []
	CurrentX = CPMin-Padding

	Xm = CPMax

	while CurrentX <= CPMax+Padding:
		
		XData.append(CurrentX)
		CurrentX = CurrentX + 0.01

	BistableEnergy = []
	
	TrapEnergyLeft = []
	TrapEnergyRight = []
	TrapEnergyMid = []

	TotalEnergyLeft = []
	TotalEnergyRight = []
	TotalEnergyMid = []

	for index in range(len(XData)):

		BiEnergy = (-1/float(beta))*log(exp((-beta/float(2))*kLR*(XData[index] + Xm)*(XData[index] + Xm)) + exp((-beta/float(2))*kLR*(XData[index] - Xm)*(XData[index] - Xm) + (beta/float(2))*DeltaE))
		HarmonicEnergyMid = 0.5*kx*(XData[index]**2)
		HarmonicEnergyLeft = 0.5*kx*((XData[index] - CPMin)**2)
		HarmonicEnergyRight = 0.5*kx*((XData[index] - CPMax)**2)

		BistableEnergy.append(BiEnergy)
		
		TrapEnergyMid.append(HarmonicEnergyMid)
		TrapEnergyLeft.append(HarmonicEnergyLeft)
		TrapEnergyRight.append(HarmonicEnergyRight)
		
		TotalEnergyLeft.append(BiEnergy + HarmonicEnergyLeft)
		TotalEnergyRight.append(BiEnergy + HarmonicEnergyRight)
		TotalEnergyMid.append(BiEnergy + HarmonicEnergyMid)


	sns.set()
	#sns.set_style("darkgrid", {"axis.facecolor":".9"})
	sns.set_context("paper")

	flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]


	fig = plt.figure(figsize=(15,8))
	
	outer = gridspec.GridSpec(2, 1, wspace=0.2, hspace=0.2)

	inner = gridspec.GridSpecFromSubplotSpec(1,2,subplot_spec=outer[0],wspace=0.1,hspace=0.25)

	ax_sub1 = plt.Subplot(fig, inner[0])
	ax_sub1.plot(XData,TrapEnergyMid,color=flatui[0], linewidth=3.5, label='Trap Energy')
	ax_sub1.legend(loc='upper center',fontsize=15)
	ax_sub1.set_xlabel("Position",fontsize=18)
	ax_sub1.set_ylabel("Energy",fontsize=18)
	ax_sub1.set_ylim(ymin=0,ymax=7)
	ax_sub1.tick_params(labelsize=12)
	fig.add_subplot(ax_sub1)

	ax_sub2 = plt.Subplot(fig, inner[1])
	ax_sub2.plot(XData,BistableEnergy,color=flatui[1],linewidth=3.5,label='Bistable Energy')
	ax_sub2.legend(loc="upper center",fontsize=15)
	ax_sub2.set_ylim(ymin=0,ymax=7)
	ax_sub2.tick_params(labelsize=12)
	fig.add_subplot(ax_sub2)

	inner = gridspec.GridSpecFromSubplotSpec(1,3,subplot_spec=outer[1],wspace=0.1,hspace=0.25)

	ax_sub3 = plt.Subplot(fig, inner[0])
	ax_sub3.plot(XData,TotalEnergyLeft,color=flatui[5],linewidth=3.5,label="Control Parameter = -1")
	ax_sub3.legend(loc="upper left",fontsize=15)
	ax_sub3.set_xlabel("Position",fontsize=18)
	ax_sub3.set_ylabel("Energy",fontsize=18)
	ax_sub3.set_ylim(ymin=0,ymax=10)
	ax_sub3.tick_params(labelsize=12)
	fig.add_subplot(ax_sub3)

	ax_sub4 = plt.Subplot(fig, inner[1])
	ax_sub4.plot(XData,TotalEnergyMid,color=flatui[5],linewidth=3.5,label="Control Parameter = 0")
	ax_sub4.legend(loc="upper center",fontsize=15)
	ax_sub4.set_ylim(ymin=0,ymax=10)
	ax_sub4.tick_params(labelsize=12)
	fig.add_subplot(ax_sub4)

	ax_sub5 = plt.Subplot(fig, inner[2])
	ax_sub5.plot(XData,TotalEnergyRight,color=flatui[5],linewidth=3.5,label="Control Parameter = 1")
	ax_sub5.legend(loc="upper right",fontsize=15)
	ax_sub5.set_ylim(ymin=0,ymax=10)
	ax_sub5.tick_params(labelsize=12)
	fig.add_subplot(ax_sub5)

	fig.savefig(FullName,format='pdf')
	plt.show()
	plt.close()


def PlotHeatMap_All(WritePath,WriteName,CorrArray1,CorrArray2,CorrArray3,CorrArray4,CorrArray5,CorrArray6,CorrArray7,CorrArray8, CorrArray9,LagTime,CPVals):

	FullName = os.path.join(WritePath,WriteName)

	LagTimeNP = np.zeros(int(len(LagTime)/2))
	CPValsNP = np.zeros(len(LagTime))

	for index in range(int(len(LagTime)/2)):
		LagTimeNP[index] = LagTime[index]

	for index in range(len(CPVals)):
		CPValsNP[index] = CPVals[index]

	CorrMeshNP1 = np.zeros((len(CorrArray1),int(len(CorrArray1[0])/2)))
	CorrMeshNP2 = np.zeros((len(CorrArray2),int(len(CorrArray2[0])/2)))
	CorrMeshNP3 = np.zeros((len(CorrArray3),int(len(CorrArray3[0])/2)))
	CorrMeshNP4 = np.zeros((len(CorrArray4),int(len(CorrArray4[0])/2)))
	CorrMeshNP5 = np.zeros((len(CorrArray5),int(len(CorrArray5[0])/2)))
	CorrMeshNP6 = np.zeros((len(CorrArray6),int(len(CorrArray6[0])/2)))
	CorrMeshNP7 = np.zeros((len(CorrArray7),int(len(CorrArray7[0])/2)))
	CorrMeshNP8 = np.zeros((len(CorrArray8),int(len(CorrArray8[0])/2)))
	CorrMeshNP9 = np.zeros((len(CorrArray9),int(len(CorrArray9[0])/2)))

	for index1 in range(len(CorrArray1)):
		for index2 in range(int(len(CorrArray1[0])/2)):
			CorrMeshNP1[index1,index2] = CorrArray1[index1][index2]

	for index1 in range(len(CorrArray2)):
		for index2 in range(int(len(CorrArray2[0])/2)):
			CorrMeshNP2[index1,index2] = CorrArray2[index1][index2]

	for index1 in range(len(CorrArray3)):
		for index2 in range(int(len(CorrArray3[0])/2)):
			CorrMeshNP3[index1,index2] = CorrArray3[index1][index2]

	for index1 in range(len(CorrArray4)):
		for index2 in range(int(len(CorrArray4[0])/2)):
			CorrMeshNP4[index1,index2] = CorrArray4[index1][index2]

	for index1 in range(len(CorrArray5)):
		for index2 in range(int(len(CorrArray5[0])/2)):
			CorrMeshNP5[index1,index2] = CorrArray5[index1][index2]

	for index1 in range(len(CorrArray6)):
		for index2 in range(int(len(CorrArray6[0])/2)):
			CorrMeshNP6[index1,index2] = CorrArray6[index1][index2]

	for index1 in range(len(CorrArray7)):
		for index2 in range(int(len(CorrArray7[0])/2)):
			CorrMeshNP7[index1,index2] = CorrArray7[index1][index2]

	for index1 in range(len(CorrArray8)):
		for index2 in range(int(len(CorrArray8[0])/2)):
			CorrMeshNP8[index1,index2] = CorrArray8[index1][index2]

	for index1 in range(len(CorrArray9)):
		for index2 in range(int(len(CorrArray9[0])/2)):
			CorrMeshNP9[index1,index2] = CorrArray9[index1][index2]

	LagTimeNP,CPValsNP = np.meshgrid(LagTimeNP,CPValsNP)

	fig,axes = plt.subplots(nrows=3, ncols=3,sharex=True,sharey=True,figsize=(10,10))

	gs1 = gridspec.GridSpec(3,3)
	gs1.update(wspace=0.005,hspace=0.1)

	fig1 = axes[0,0].imshow(CorrMeshNP1, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig2 = axes[0,1].imshow(CorrMeshNP2, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig3 = axes[0,2].imshow(CorrMeshNP3, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig4 = axes[1,0].imshow(CorrMeshNP4, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig5 = axes[1,1].imshow(CorrMeshNP5, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig6 = axes[1,2].imshow(CorrMeshNP6, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig7 = axes[2,0].imshow(CorrMeshNP7, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig8 = axes[2,1].imshow(CorrMeshNP8, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig9 = axes[2,2].imshow(CorrMeshNP9, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')

	ax1 = axes[0,0]
	ax2 = axes[0,1]
	ax3 = axes[0,2]
	ax4 = axes[1,0]
	ax5 = axes[1,1]
	ax6 = axes[1,2]
	ax7 = axes[2,0]
	ax8 = axes[2,1]
	ax9 = axes[2,2]

	plt.colorbar(fig7, ax=ax7)
	ax7.set_xlabel("Lag Time", fontsize=18)
	ax7.set_ylabel("Control Parameter", fontsize=18)
	ax1.set_xticklabels([])
	ax2.set_xticklabels([])
	ax3.set_xticklabels([])
	ax4.set_xticklabels([])
	ax5.set_xticklabels([])
	ax6.set_xticklabels([])
	ax8.set_xticklabels([])
	ax9.set_xticklabels([])

	ax1.set_yticklabels([])
	ax2.set_yticklabels([])
	ax3.set_yticklabels([])
	ax4.set_yticklabels([])
	ax5.set_yticklabels([])
	ax6.set_yticklabels([])
	ax8.set_yticklabels([])
	ax9.set_yticklabels([])

	ax1.set_title("$k_{L/R} = 9$", fontsize = 18)
	ax2.set_title("$k_{L/R} = 12$", fontsize = 18)
	ax3.set_title("$k_{L/R} = 15$", fontsize = 18)

	ax3.yaxis.set_label_position("right")
	ax6.yaxis.set_label_position("right")
	ax9.yaxis.set_label_position("right")

	ax3.set_ylabel("$k_t = 1$",fontsize = 18)
	ax6.set_ylabel("$k_t = 1.5$", fontsize = 18)
	ax9.set_ylabel("$k_t = 2$", fontsize = 18)

	plt.savefig(FullName, format='pdf')
	plt.show()
	plt.close()


def PlotHeatMap(WritePath,WriteName,CorrArray1,CorrArray2,CorrArray3,LagTime,CPVals):

	FullName = os.path.join(WritePath,WriteName)

	LagTimeNP = np.zeros(int(len(LagTime)/2))
	CPValsNP = np.zeros(len(CPVals))

	for index in range(int(len(LagTime)/2)):
		LagTimeNP[index] = LagTime[index]

	for index in range(len(CPVals)):
		CPValsNP[index] = CPVals[index]

	CorrMeshNP1 = np.zeros((len(CorrArray1),int(len(CorrArray1[0])/2)))
	CorrMeshNP2 = np.zeros((len(CorrArray2),int(len(CorrArray2[0])/2)))
	CorrMeshNP3 = np.zeros((len(CorrArray3),int(len(CorrArray3[0])/2)))

	for index1 in range(len(CorrArray1)):
		for index2 in range(int(len(CorrArray1[0])/2)):
			CorrMeshNP1[index1,index2] = CorrArray1[index1][index2]

	for index1 in range(len(CorrArray2)):
		for index2 in range(int(len(CorrArray2[0])/2)):
			CorrMeshNP2[index1,index2] = CorrArray2[index1][index2]

	for index1 in range(len(CorrArray3)):
		for index2 in range(int(len(CorrArray3[0])/2)):
			CorrMeshNP3[index1,index2] = CorrArray3[index1][index2]


	LagTimeNP,CPValsNP = np.meshgrid(LagTimeNP,CPValsNP)

	fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharex=True,sharey=True,figsize=(15,5))

	gs1 = gridspec.GridSpec(1,3)
	gs1.update(wspace=0.005,hspace=0.1)

	fig1 = ax1.imshow(CorrMeshNP1, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig2 = ax2.imshow(CorrMeshNP2, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')
	fig3 = ax3.imshow(CorrMeshNP3, cmap='YlGnBu', interpolation='none', extent=[0,1000,-1,1], aspect='auto')

	plt.colorbar(fig3)
	ax1.set_xlabel("Lag Time", fontsize=18)
	ax1.set_ylabel("Control Parameter", fontsize=18)
	ax2.set_xticklabels([])
	ax3.set_xticklabels([])

	ax1.set_title("$k_{L/R} = 9$", fontsize = 18)
	ax2.set_title("$k_{L/R} = 12$", fontsize = 18)
	ax3.set_title("$k_{L/R} = 15$", fontsize = 18)

	plt.savefig(FullName, format='pdf')
	plt.show()
	plt.close()

def CumulativeTime(TimeArray):

	NewTime = []
	Counter = 0

	for index in range(len(TimeArray)):
		Counter = Counter + TimeArray[index]
		NewTime.append(Counter)

	return NewTime


def PlotTimeProtocols(ReadPath,Filename_Time,Filename_Naive,WritePath,Writename):

	NumCPVals = [17,21,25]
	LagTimes = [50,100,500]

	sns.set()
	sns.set_context("paper")

	fig = plt.subplots(len(NumCPVals),len(LagTimes),sharex=True,sharey=True,figsize=(10,10))

	Counter = 1

	for index1 in range(len(NumCPVals)):

		for index2 in range(len(NumCPVals)):

			ReadName_Time = Filename_Time + str(NumCPVals[index1]) + "_T" + str(LagTimes[index2]) + ".dat"
			ReadName_Naive = Filename_Naive + str(NumCPVals[index1]) + "_T" + str(LagTimes[index2]) + ".dat"

			CP_Time,Lag_Time = ReadProtocol(ReadPath,ReadName_Time)
			CP_Naive,Lag_Naive = ReadProtocol(ReadPath,ReadName_Naive)

			CumulTime = CumulativeTime(Lag_Time[1:len(Lag_Time)-1])
			CumulNaive = CumulativeTime(Lag_Naive[1:len(Lag_Naive)-1])

			plt.subplot(len(NumCPVals),len(LagTimes),Counter)
			plt.plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label="Naive")
			plt.plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
			plt.plot(CP_Time[1:len(CP_Time)-1],CumulTime,'bo',label="Time-Optimal")
			plt.plot(CP_Time[1:len(CP_Time)-1],CumulTime,'b--')

			if(Counter == 1):
				plt.ylabel("9 CP Values",fontsize=18)
				plt.title("Duration = 50",fontsize=18)

			if(Counter == 2):
				plt.title("Duration = 100",fontsize=18)

			if(Counter == 3):
				plt.title("Duration = 500",fontsize=18)

			if(Counter == 4):
				plt.ylabel("17 CP Values",fontsize=18)

			if(Counter == 7):
				plt.ylabel("25 CP Values",fontsize=18)

			if(Counter == 9):
				plt.xlabel("CP Value",fontsize=14)
				plt.ylabel("Time",fontsize=14)
				plt.legend(loc='upper left',fontsize=10)


			Counter = Counter + 1

	CompleteWrite = os.path.join(WritePath,Writename)

	plt.savefig(CompleteWrite,format='pdf')
	plt.show()
	plt.close()


def PlotSpaceProtocols(ReadPath,Filename_Space,Filename_Naive,WritePath,Writename):

	NumCPVals = [17,21,25]
	LagTimes = [50,100,500]

	sns.set()
	sns.set_context("paper")

	fig = plt.subplots(len(NumCPVals),len(LagTimes),sharex=True,sharey=True,figsize=(10,10))

	Counter = 1

	for index1 in range(len(NumCPVals)):

		for index2 in range(len(NumCPVals)):

			ReadName_Space = Filename_Space + str(NumCPVals[index1]) + "_T" + str(LagTimes[index2]) + ".dat"
			ReadName_Naive = Filename_Naive + str(NumCPVals[index1]) + "_T" + str(LagTimes[index2]) + ".dat"

			CP_Space,Lag_Space = ReadProtocol(ReadPath,ReadName_Space)
			CP_Naive,Lag_Naive = ReadProtocol(ReadPath,ReadName_Naive)

			CumulSpace = CumulativeTime(Lag_Space[1:len(Lag_Space)-1])
			CumulNaive = CumulativeTime(Lag_Naive[1:len(Lag_Naive)-1])

			plt.subplot(len(NumCPVals),len(LagTimes),Counter)
			plt.plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label="Naive")
			plt.plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
			plt.plot(CP_Space[1:len(CP_Space)-1],CumulSpace,'go',label="Space-Optimal")
			plt.plot(CP_Space[1:len(CP_Space)-1],CumulSpace,'g--')

			if(Counter == 1):
				plt.ylabel("9 CP Values",fontsize=18)
				plt.title("Duration = 50",fontsize=18)

			if(Counter == 2):
				plt.title("Duration = 100",fontsize=18)

			if(Counter == 3):
				plt.title("Duration = 500",fontsize=18)

			if(Counter == 4):
				plt.ylabel("17 CP Values",fontsize=18)

			if(Counter == 7):
				plt.ylabel("25 CP Values",fontsize=18)

			if(Counter == 9):
				plt.xlabel("CP Value",fontsize=14)
				plt.ylabel("Time",fontsize=14)
				plt.legend(loc='upper left',fontsize=10)


			Counter = Counter + 1

	CompleteWrite = os.path.join(WritePath,Writename)

	plt.savefig(CompleteWrite,format='pdf')
	plt.show()
	plt.close()


def PlotFullOptProtocols(ReadPath,Filename_Full,Filename_Naive,WritePath,Writename):

	NumCPVals = [17,21,25]
	LagTimes = [50,100,500]

	sns.set()
	sns.set_context("paper")

	fig = plt.subplots(len(NumCPVals),len(LagTimes),sharex=True,sharey=True,figsize=(10,10))

	Counter = 1

	for index1 in range(len(NumCPVals)):

		for index2 in range(len(NumCPVals)):

			ReadName_Full = Filename_Full + str(NumCPVals[index1]) + "_T" + str(LagTimes[index2]) + ".dat"
			ReadName_Naive = Filename_Naive + str(NumCPVals[index1]) + "_T" + str(LagTimes[index2]) + ".dat"

			CP_Full,Lag_Full = ReadProtocol(ReadPath,ReadName_Full)
			CP_Naive,Lag_Naive = ReadProtocol(ReadPath,ReadName_Naive)

			CumulFull = CumulativeTime(Lag_Full[1:len(Lag_Full)-1])
			CumulNaive = CumulativeTime(Lag_Naive[1:len(Lag_Naive)-1])

			plt.subplot(len(NumCPVals),len(LagTimes),Counter)
			plt.plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label="Naive")
			plt.plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
			plt.plot(CP_Full[1:len(CP_Full)-1],CumulFull,'mo',label="Fully-Optimal")
			plt.plot(CP_Full[1:len(CP_Full)-1],CumulFull,'m--')

			if(Counter == 1):
				plt.ylabel("9 CP Values",fontsize=18)
				plt.title("Duration = 50",fontsize=18)

			if(Counter == 2):
				plt.title("Duration = 100",fontsize=18)

			if(Counter == 3):
				plt.title("Duration = 500",fontsize=18)

			if(Counter == 4):
				plt.ylabel("17 CP Values",fontsize=18)

			if(Counter == 7):
				plt.ylabel("25 CP Values",fontsize=18)

			if(Counter == 9):
				plt.xlabel("CP Value",fontsize=14)
				plt.ylabel("Time",fontsize=14)
				plt.legend(loc='upper left',fontsize=10)


			Counter = Counter + 1

	CompleteWrite = os.path.join(WritePath,Writename)

	plt.savefig(CompleteWrite,format='pdf')
	plt.show()
	plt.close()


def PlotProtocolCompare(WritePath,WriteName):

	ReadPath_9_10 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_9_10/"
	ReadPath_9_15 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_9_15/"
	ReadPath_9_20 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_9_20/"
	ReadPath_12_10 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_12_10/"
	ReadPath_12_15 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_12_15/"
	ReadPath_12_20 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_12_20/"
	ReadPath_15_10 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_15_10/"
	ReadPath_15_15 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_15_15/"
	ReadPath_15_20 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_FromCluster/Protocols_15_20/"

	ReadName_Naive = "Naive_CP25_T500.dat"
	ReadName_TimeOpt = "TimeOpt_CP25_T500.dat"
	ReadName_SpaceOpt = "SpaceOpt_CP25_T500.dat"
	ReadName_FullOpt = "FullOpt_CP25_T500.dat"

	sns.set()

	fig,axes = plt.subplots(3,3,sharex=True,sharey=True,figsize=(10,10))

	CP_Naive,Time_Naive = ReadProtocol(ReadPath_15_10,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_15_10,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_15_10,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_15_10,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig1_1 = axes[0,0].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig1_2 = axes[0,0].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig1_3 = axes[0,0].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig1_4 = axes[0,0].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig1_1l = axes[0,0].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig1_2l = axes[0,0].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig1_3l = axes[0,0].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig1_4l = axes[0,0].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_15_15,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_15_15,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_15_15,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_15_15,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig2_1 = axes[0,1].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig2_2 = axes[0,1].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig2_3 = axes[0,1].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig2_4 = axes[0,1].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig2_1l = axes[0,1].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig2_2l = axes[0,1].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig2_3l = axes[0,1].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig2_4l = axes[0,1].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_15_20,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_15_20,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_15_20,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_15_20,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig3_1 = axes[0,2].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig3_2 = axes[0,2].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig3_3 = axes[0,2].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig3_4 = axes[0,2].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig3_1l = axes[0,2].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig3_2l = axes[0,2].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig3_3l = axes[0,2].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig3_4l = axes[0,2].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_12_10,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_12_10,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_12_10,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_12_10,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig4_1 = axes[1,0].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig4_2 = axes[1,0].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig4_3 = axes[1,0].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig4_4 = axes[1,0].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig4_1l = axes[1,0].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig4_2l = axes[1,0].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig4_3l = axes[1,0].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig4_4l = axes[1,0].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_12_15,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_12_15,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_12_15,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_12_15,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig4_1 = axes[1,1].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig4_2 = axes[1,1].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig4_3 = axes[1,1].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig4_4 = axes[1,1].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig4_1l = axes[1,1].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig4_2l = axes[1,1].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig4_3l = axes[1,1].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig4_4l = axes[1,1].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_12_20,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_12_20,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_12_20,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_12_20,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig4_1 = axes[1,2].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig4_2 = axes[1,2].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig4_3 = axes[1,2].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig4_4 = axes[1,2].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig4_1l = axes[1,2].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig4_2l = axes[1,2].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig4_3l = axes[1,2].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig4_4l = axes[1,2].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_9_10,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_9_10,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_9_10,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_9_10,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig4_1 = axes[2,0].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig4_2 = axes[2,0].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig4_3 = axes[2,0].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig4_4 = axes[2,0].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig4_1l = axes[2,0].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig4_2l = axes[2,0].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig4_3l = axes[2,0].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig4_4l = axes[2,0].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_9_15,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_9_15,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_9_15,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_9_15,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig4_1 = axes[2,1].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig4_2 = axes[2,1].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig4_3 = axes[2,1].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig4_4 = axes[2,1].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig4_1l = axes[2,1].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig4_2l = axes[2,1].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig4_3l = axes[2,1].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig4_4l = axes[2,1].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')




	CP_Naive,Time_Naive = ReadProtocol(ReadPath_9_20,ReadName_Naive)
	CP_TimeOpt,Time_TimeOpt = ReadProtocol(ReadPath_9_20,ReadName_TimeOpt)
	CP_SpaceOpt,Time_SpaceOpt = ReadProtocol(ReadPath_9_20,ReadName_SpaceOpt)
	CP_FullOpt,Time_FullOpt = ReadProtocol(ReadPath_9_20,ReadName_FullOpt)

	CumulNaive = CumulativeTime(Time_Naive[1:len(Time_Naive)-1])
	CumulTimeOpt = CumulativeTime(Time_TimeOpt[1:len(Time_TimeOpt)-1])
	CumulSpaceOpt = CumulativeTime(Time_SpaceOpt[1:len(Time_SpaceOpt)-1])
	CumulFullOpt = CumulativeTime(Time_FullOpt[1:len(Time_FullOpt)-1])

	fig4_1 = axes[2,2].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'ro',label='Naive')
	fig4_2 = axes[2,2].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'bo',label='Time-Optimal')
	fig4_3 = axes[2,2].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'go',label='Space-Optimal')
	fig4_4 = axes[2,2].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'mo',label='Fully-Optimal')

	fig4_1l = axes[2,2].plot(CP_Naive[1:len(CP_Naive)-1],CumulNaive,'r--')
	fig4_2l = axes[2,2].plot(CP_TimeOpt[1:len(CP_TimeOpt)-1],CumulTimeOpt,'b--')
	fig4_3l = axes[2,2].plot(CP_SpaceOpt[1:len(CP_SpaceOpt)-1],CumulSpaceOpt,'g--')
	fig4_4l = axes[2,2].plot(CP_FullOpt[1:len(CP_FullOpt)-1],CumulFullOpt,'m--')

	plt.show()
	plt.close()


WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/DocumentPlots/"
EnergyName = "EnergyLandscape.pdf"
HeatMapName = "HeatMap.pdf"

ReadPath1 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_9_10/"
ReadPath2 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_12_10/"
ReadPath3 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_15_10/"
ReadPath4 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_9_15/"
ReadPath5 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_12_15/"
ReadPath6 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_15_15/"
ReadPath7 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_9_20/"
ReadPath8 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_12_20/"
ReadPath9 = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Equilibrium_FromCluster/CorrelationMesh_15_20/"

ReadNameArray = "CorrelationMesh.dat"
ReadNameTime = "LagTime.dat"
ReadNameCP = "CPVals.dat"

ReadPathProtocol = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Protocols/"

FileName_Naive = "Naive_CP"
FileName_Space = "SpaceOpt_CP"
FileName_Time = "TimeOpt_CP"
FileName_Full = "FullOpt_CP"

WriteName_Time = "Protocol_TimeOpt.pdf"
WriteName_Space = "Protocol_SpaceOpt.pdf"
WriteName_Full = "Protocol_FullOpt.pdf"

#PlotEnergyLandscape(WritePath,EnergyName)

#PlotTimeProtocols(ReadPathProtocol,FileName_Time,FileName_Naive,WritePath,WriteName_Time)
#PlotSpaceProtocols(ReadPathProtocol,FileName_Space,FileName_Naive,WritePath,WriteName_Space)
#PlotFullOptProtocols(ReadPathProtocol,FileName_Full,FileName_Naive,WritePath,WriteName_Full)

#CorrArray1 = ReadArray(ReadPath1,ReadNameArray)
#print "Read 1"
#CorrArray2 = ReadArray(ReadPath2,ReadNameArray)
#print "Read 2"
#CorrArray3 = ReadArray(ReadPath3,ReadNameArray)
#print "Read 3"
#CorrArray4 = ReadArray(ReadPath4,ReadNameArray)
#print "Read 4"
#CorrArray5 = ReadArray(ReadPath5,ReadNameArray)
#print "Read 5"
#CorrArray6 = ReadArray(ReadPath6,ReadNameArray)
#print "Read 6"
#CorrArray7 = ReadArray(ReadPath7,ReadNameArray)
#print "Read 7"
#CorrArray8 = ReadArray(ReadPath8,ReadNameArray)
#print "Read 8"
#CorrArray9 = ReadArray(ReadPath9,ReadNameArray)
#print "Read 9"


#LagTime = ReadVector(ReadPath1,ReadNameTime)
#CPVals = ReadVector(ReadPath1,ReadNameCP)

#PlotHeatMap_All(WritePath,HeatMapName,CorrArray1,CorrArray2,CorrArray3,CorrArray4,CorrArray5,CorrArray6,CorrArray7,CorrArray8,CorrArray9,LagTime,CPVals)

PlotProtocolCompare("1","b")


