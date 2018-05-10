#This python script plots the optimal time and space protocols
#
#Steven Large
#February 29th 2018

import os
import matplotlib.pyplot as plt
import seaborn as sns

def ReadProtocol(Path,BaseFilename,NumCPVals,TotalTimes):

	CPVals = []
	CPTimes = []

	Filename = BaseFilename + str(NumCPVals) + "_T" + str(TotalTimes) + ".dat"

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		CPVals.append(eval(Parsed[0]))
		CPTimes.append(eval(Parsed[1]))

	return CPVals,CPTimes

def TimeProportion(Times,CPTimes,CPVals):

	NewTimes = []

	for index in range(len(Times)):

		NewTimes.append(Times[index]*float(CPVals-2)/float(CPTimes))

	return NewTimes

def TimeRelative(Times,CPTimes,CPVals):

	NewTimes = [0]
	TimeAcc = Times[1]

	for index in range(len(Times)-2):
		NewTimes.append(TimeAcc)
		TimeAcc = TimeAcc + Times[index+2]

	NewTimes.append(0)

	return NewTimes


ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Protocols/"
WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Plots/"

BaseName_Time = "TimeOpt_CP"
BaseName_Space = "SpaceOpt_CP"
BaseName_Naive = "Naive_CP"
BaseName_Full = "FullOpt_CP"

sns.set()

CPVals = [7,17,25]
CPTimes = [50,100,500]

fig = plt.figure(figsize = (10.0,7.0))

'''
plt.subplot(3,3,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[0])
TimesProp = TimeProportion(Times,CPTimes[0],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[0])
TimesPropN = TimeProportion(TimesN,CPTimes[0],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])
'''

plt.subplot(3,2,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[0])
TimesProp = TimeProportion(Times,CPTimes[0],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[0])
TimesPropN = TimeProportion(TimesN,CPTimes[0],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.title("NSteps = 17")
plt.ylabel("Time = 50")
#plt.title("Time-optimized discrete protocols")
#plt.ylim([0, 2])

plt.subplot(3,2,2)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[0])
TimesProp = TimeProportion(Times,CPTimes[0],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[0])
TimesPropN = TimeProportion(TimesN,CPTimes[0],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.title("NSteps = 25")
#plt.ylim([0, 2])

'''
plt.subplot(3,3,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[1])
TimesProp = TimeProportion(Times,CPTimes[1],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[1])
TimesPropN = TimeProportion(TimesN,CPTimes[1],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])
'''

plt.subplot(3,2,3)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[1])
TimesProp = TimeProportion(Times,CPTimes[1],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[1])
TimesPropN = TimeProportion(TimesN,CPTimes[1],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.ylabel("Time = 100")
#plt.ylim([0, 2])

plt.subplot(3,2,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[1])
TimesProp = TimeProportion(Times,CPTimes[1],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[1])
TimesPropN = TimeProportion(TimesN,CPTimes[1],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])

'''
plt.subplot(3,3,7)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[2])
TimesProp = TimeProportion(Times,CPTimes[2],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[2])
TimesPropN = TimeProportion(TimesN,CPTimes[2],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label="Naive")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.xlabel("Control Parameter Value")
plt.ylabel("Proportional Time Allocation")
#plt.ylim([0, 2])
plt.legend()
'''

plt.subplot(3,2,5)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[2])
TimesProp = TimeProportion(Times,CPTimes[2],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[2])
TimesPropN = TimeProportion(TimesN,CPTimes[2],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label="Naive")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal Time")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])
plt.ylabel("Time = 500")
#plt.ylim([0, 2])
plt.legend()


plt.subplot(3,2,6)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[2])
TimesProp = TimeProportion(Times,CPTimes[2],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[2])
TimesPropN = TimeProportion(TimesN,CPTimes[2],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.xlabel("Control Parameter Value")
plt.ylabel("Proportional Time Allocation")
#plt.ylim([0, 2])

SaveName = WritePath + "TimeOpt-Protocols.pdf"
plt.savefig(SaveName,format='pdf')
plt.show()
plt.close()



fig = plt.figure(figsize = (10.0,7.0))
'''
plt.subplot(3,3,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])
'''

plt.subplot(3,2,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.title("NSteps = 17")
plt.ylabel("Time = 50")
#plt.title("Time-optimized discrete protocols")
#plt.ylim([0, 2])

plt.subplot(3,2,2)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.title("NSteps = 25")
#plt.ylim([0, 2])

'''
plt.subplot(3,3,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])
'''

plt.subplot(3,2,3)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.ylabel("Time = 100")
#plt.ylim([0, 2])

plt.subplot(3,2,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
#plt.ylim([0, 2])

'''
plt.subplot(3,3,7)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label="Naive")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')
#plt.ylim([0, 2])
plt.legend()
'''

plt.subplot(3,2,5)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label='Naive')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal Time")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.ylabel("Time = 500")
#plt.ylim([0, 2])
#plt.ylim([0, 2])
plt.legend()

plt.subplot(3,2,6)
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlim([-1, 1])
plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')
#plt.ylim([0, 2])

SaveName = WritePath + "TimeOpt-Protocols_Cumulative.pdf"
plt.savefig(SaveName,format='pdf')
plt.show()
plt.close()



fig = plt.figure(figsize = (10.0,7.0))

'''
plt.subplot(3,3,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
'''

plt.subplot(3,2,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.title("NSteps = 17")
plt.ylabel("Time = 50")

plt.subplot(3,2,2)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.title("NSteps = 25")

'''
plt.subplot(3,3,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
'''

plt.subplot(3,2,3)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.ylabel("Time = 100")

plt.subplot(3,2,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')

'''
plt.subplot(3,3,7)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label='Naive')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label='Optimal')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')
plt.legend()
'''

plt.subplot(3,2,5)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label='Naive')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal Space")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.ylabel("Time = 500")
plt.legend()

plt.subplot(3,2,6)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')
SaveName = WritePath + "SpaceOpt-Protocols.pdf"
plt.savefig(SaveName,format='pdf')
plt.show()
plt.close()



fig = plt.figure(figsize = (10.0,7.0))
'''
plt.subplot(3,3,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
'''

plt.subplot(3,2,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
plt.title("NSteps = 17")
plt.ylabel("Time = 50")


plt.subplot(3,2,2)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
plt.title("NSteps = 25")

'''
plt.subplot(3,3,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
'''

plt.subplot(3,2,3)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
plt.ylabel("Time = 100")


plt.subplot(3,2,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')

'''
plt.subplot(3,3,7)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label='Naive')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label='Optimal space')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go',label="Optimal time")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')

plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')
plt.legend()
'''

plt.subplot(3,2,5)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label="Naive")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal space")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go',label='Optimal Time')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
plt.ylabel("Time = 500")

plt.legend()

plt.subplot(3,2,6)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')

plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')

SaveName = WritePath + "Space-TimeOpt-Protocols.pdf"
plt.savefig(SaveName,format='pdf')

plt.show()
plt.close()





fig = plt.figure(figsize = (10.0,7.0))

#plt.subplot(3,3,1)
#CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[0])
#TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
#CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[0])
#TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[0])
#plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
#plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
#CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[0])
#TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
#CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[0],CPTimes[0])
#TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')



plt.subplot(3,2,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.title("NSteps = 17")
plt.ylabel("Time = 50")


plt.subplot(3,2,2)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[0])
TimesPropN = TimeRelative(TimesN,CPTimes[0],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.title("NSteps = 25")


'''
plt.subplot(3,3,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[0],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
'''


plt.subplot(3,2,3)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.ylabel("Time = 100")



plt.subplot(3,2,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[1])
TimesPropN = TimeRelative(TimesN,CPTimes[1],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')


'''
plt.subplot(3,3,7)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[0],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[0])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label='Naive')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label='Optimal space')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go',label="Optimal time")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[0],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo',label="Full Optimal")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')


plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')
plt.legend()

'''

plt.subplot(3,2,5)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[1],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[1])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro',label="Naive")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo',label="Optimal Space")
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go',label="Optimal Time")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo',label="Full Optimal")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.ylabel("Time = 500")

plt.legend()


plt.subplot(3,2,6)
CP,Times = ReadProtocol(ReadPath,BaseName_Space,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
CPN,TimesN = ReadProtocol(ReadPath,BaseName_Naive,CPVals[2],CPTimes[2])
TimesPropN = TimeRelative(TimesN,CPTimes[2],CPVals[2])
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:len(TimesN)-1],'ro')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'bo')
plt.plot(CPN[1:(len(CPN)-1)],TimesPropN[1:(len(TimesN)-1)],'r--')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'b--')
CP,Times = ReadProtocol(ReadPath,BaseName_Time,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'go')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'g--')
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')

SaveName = WritePath + "Full-Space-TimeOpt-Protocols.pdf"
plt.savefig(SaveName,format='pdf')




plt.show()
plt.close()





fig = plt.figure(figsize = (10.0,7.0))

#plt.subplot(3,3,1)
#CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[0],CPTimes[0])
#TimesProp = TimeRelative(Times,CPTimes[0],CPVals[0])
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')



plt.subplot(3,2,1)
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[1],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.title("NSteps = 17")
plt.ylabel("Time = 50")


plt.subplot(3,2,2)
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[2],CPTimes[0])
TimesProp = TimeRelative(Times,CPTimes[0],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.title("NSteps = 25")


#plt.subplot(3,3,4)
#CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[0],CPTimes[1])
#TimesProp = TimeRelative(Times,CPTimes[1],CPVals[0])
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')



plt.subplot(3,2,3)
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[1],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.ylabel("Time = 100")


plt.subplot(3,2,4)
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[2],CPTimes[1])
TimesProp = TimeRelative(Times,CPTimes[1],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')



#plt.subplot(3,3,7)
#CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[0],CPTimes[2])
#TimesProp = TimeRelative(Times,CPTimes[2],CPVals[0])
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo',label="Full Optimal")
#plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')


plt.subplot(3,2,5)
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[1],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[1])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo',label="Full Optimal")
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')
plt.ylabel("Time = 500")

plt.legend()



plt.subplot(3,2,6)
CP,Times = ReadProtocol(ReadPath,BaseName_Full,CPVals[2],CPTimes[2])
TimesProp = TimeRelative(Times,CPTimes[2],CPVals[2])
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'mo')
plt.plot(CP[1:(len(CP)-1)],TimesProp[1:(len(Times)-1)],'m--')

plt.xlabel('Control Parameter')
plt.ylabel('Cumulative Time')

SaveName = WritePath + "FullOpt-Protocols.pdf"
plt.savefig(SaveName,format='pdf')

plt.show()
plt.close()


