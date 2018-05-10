#This python script plots the optimal-time vs naive protocols for comparison
#
#Steven Large
#February 13th 2018

import os
import matplotlib.pyplot as plt

def ReadData(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	CPVals = []
	TimeVals = []

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)-2):
		Parsed = TempData[index+1].split()

		CPVals.append(eval(Parsed[0]))
		TimeVals.append(eval(Parsed[1]))

	return CPVals,TimeVals


def PlotProtocolCompare(CP_Naive,Time_Naive,CP_Opt,Time_Opt):

	plt.plot(CP_Naive,Time_Naive,'r--',linewidth=2.0)
	plt.plot(CP_Opt,Time_Opt,'b--',linewidth=2.0)

	plt.plot(CP_Naive,Time_Naive,'ro',linewidth=2.0)
	plt.plot(CP_Opt,Time_Opt,'bo',linewidth=2.0)
	plt.savefig("Allocation.pdf",format='pdf')
	plt.show()
	plt.close()



def PlotFractionalProtocolCompare(CP_Naive,Time_Naive,CP_Opt,TimeOpt):

	return None



ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/Protocols_Feb12/"
ReadNameNaive = "Naive_CP9_T1000.dat"
ReadNameOpt = "TimeOpt_CP9_T1000.dat"

CPVals_Naive,CPTime_Naive = ReadData(ReadPath,ReadNameNaive)
CPVals_Opt,CPTime_Opt = ReadData(ReadPath,ReadNameOpt)

PlotProtocolCompare(CPVals_Naive,CPTime_Naive,CPVals_Opt,CPTime_Opt)


