#This python script generates the theoretical/analytical results for the harmonic trap discrete control system
#
#Steven Large
#March 25th 2018

import os
import numpy as np
import matplotlib.pyplot as plt
from math import *

import seaborn as sns


def GenerateProtocol(NumCPVals,TotalDist):

	CPVals = []

	CPStep = float(TotalDist)/(float(NumCPVals))

	CurrentCP = 0

	for index in range(NumCPVals+1):
		CPVals.append(CurrentCP)
		CurrentCP = CurrentCP + CPStep

	return CPVals


def ExactProtocolWork(CPVals,TotalTime):

	CPDiff = []
	WorkAcc = 0
	LagTimes = []

	StepTime = float(TotalTime)/float(len(CPVals)-2)
	TimeAcc = 0

	for index in range(len(CPVals)-1):
		CPDiff.append(CPVals[index+1]-CPVals[index])

	for index in range(len(CPVals)-2):
		TimeAcc = TimeAcc + StepTime
		LagTimes.append(TimeAcc)

	WorkAcc = WorkAcc + 0.5*CPDiff[0]*CPDiff[0]

	for index in range(len(CPDiff)-1):
		WorkTemp = 0
		for index2 in range(index+1):
			WorkTemp = WorkTemp + exp(-LagTimes[index2])

		WorkTemp = CPDiff[index+1]*CPDiff[index+1]*(0.5 + WorkTemp)
		WorkAcc = WorkAcc + WorkTemp

	return WorkAcc


def AdjustedExactWork(CPVals,TotalTime):

	WorkExact = ExactProtocolWork(CPVals,TotalTime)
	WorkInfinite = InfiniteTimeProtocolWork(CPVals)

	CorrectedWork = WorkExact - WorkInfinite

	return CorrectedWork


def LinearResponseProtocolWork(CPVals,TotalTime):

	CPDiff = []
	WorkAcc = 0

	StepTime = float(TotalTime)/float(len(CPVals)-2)

	for index in range(len(CPVals)-1):
		CPDiff.append(CPVals[index+1]-CPVals[index])

	WorkAcc = WorkAcc + 0.5*CPDiff[0]*CPDiff[0]

	for index in range(len(CPDiff)-1):
		WorkTemp = CPDiff[index]*CPDiff[index]*(0.5 + exp(-StepTime))
		WorkAcc = WorkAcc + WorkTemp

	return WorkAcc


def AdjustedLinearResponseWork(CPVals,TotalTime):

	WorkLR = LinearResponseProtocolWork(CPVals,TotalTime)
	WorkInfinite = InfiniteTimeProtocolWork(CPVals)

	CorrectedWork = WorkLR - WorkInfinite

	return CorrectedWork


def InfiniteTimeProtocolWork(CPVals):

	CPDiff = []
	WorkAcc = 0

	for index in range(len(CPVals)-1):
		CPDiff.append(CPVals[index+1]-CPVals[index])

	for index in range(len(CPDiff)):
		WorkAcc = WorkAcc + 0.5*CPDiff[index]*CPDiff[index]

	return WorkAcc


#NumSteps = [5,10,20,40]
#NumSteps = [10]
TotalDist = 10
#TotalTime = [0.25,0.5,1,2,4,8,16,32,64]
WorkArray_Exact = []
WorkArray_Approx = []
WorkArray_Space = []
StepArray = []

WorkArray_Exact_Corr = []
WorkArray_Approx_Corr = []

WorkArray_Approx2 = []
WorkArray_Approx2_Corr = []

Relaxation_Array = [0.125,0.25,0.5,1,2,4]

RelaxationTime = 0.1
TimeTracker = []
#for index in range(len(Relaxation_Array)):
while RelaxationTime < 4:

	NumSteps = 10

	#TotalTime = Relaxation_Array[index]*NumSteps
	TotalTime = RelaxationTime*NumSteps

	CPVals = GenerateProtocol(NumSteps,TotalDist)

	CPStep = CPVals[1] - CPVals[0]


	WorkSpace = InfiniteTimeProtocolWork(CPVals)
	WorkApprox = LinearResponseProtocolWork(CPVals,TotalTime)
	WorkExact = ExactProtocolWork(CPVals,TotalTime)

	WorkArray_Exact.append(WorkExact - WorkSpace)
	WorkArray_Approx.append(WorkApprox - WorkSpace)
	WorkArray_Space.append(WorkSpace)
	TimeTracker.append(RelaxationTime)

	RelaxationTime += 0.1

sns.set()

fig,ax = plt.subplots(1,1)

#ax.plot(Relaxation_Array,WorkArray_Space,'r--',linewidth=2.0)
ax.plot(TimeTracker,WorkArray_Approx,'b',linewidth=3.0)
ax.plot(TimeTracker,WorkArray_Exact,'k',linewidth=3.0)

#ax.plot(Relaxation_Array,WorkArray_Space,'ro')
#ax.plot(Relaxation_Array,WorkArray_Approx,'bo')
#ax.plot(Relaxation_Array,WorkArray_Exact,'ko')

ax.set_yscale('log')
#ax.set_xscale('log')

plt.show()
plt.close()


WorkArray_Exact = []
WorkArray_Approx = []
WorkArray_Space = []
StepArray = []

WorkArray_Exact_Corr = []
WorkArray_Approx_Corr = []

WorkArray_Approx2 = []
WorkArray_Approx2_Corr = []


Relaxation_Array = [1]

SingleStepWork = float(TotalDist)*float(TotalDist)*0.5

for index in range(len(Relaxation_Array)):

	NumSteps = 2

	WorkArray_Exact.append([])
	WorkArray_Approx.append([])
	WorkArray_Space.append([])
	StepArray.append([])

	WorkArray_Exact[index].append(SingleStepWork)
	WorkArray_Approx[index].append(SingleStepWork)
	WorkArray_Space[index].append(SingleStepWork)
	StepArray[index].append(1)

	while NumSteps <= 1000:

		TotalTime = Relaxation_Array[index]*NumSteps

		CPVals = GenerateProtocol(NumSteps,TotalDist)

		CPStep = CPVals[1] - CPVals[0]

		WorkExact = ExactProtocolWork(CPVals,TotalTime)
		WorkApprox = LinearResponseProtocolWork(CPVals,TotalTime)
		WorkSpace = InfiniteTimeProtocolWork(CPVals)

		WorkArray_Exact[index].append(WorkExact)
		WorkArray_Approx[index].append(WorkApprox)
		WorkArray_Space[index].append(WorkSpace)
		StepArray[index].append(NumSteps)

		NumSteps = NumSteps*2

sns.set()

fig,ax = plt.subplots(1,1,figsize=(10,3.5))

#pal_exact = sns.light_palette("Black")
#pal_approx = sns.light_palette("Blue")
#pal_space = sns.light_palette("Red")

#ax.plot(StepArray[0],WorkArray_Space[0],color=pal_space[0],linewidth=3.0)
#ax.plot(StepArray[1],WorkArray_Space[1],color=pal_space[1],linewidth=3.0)
#ax.plot(StepArray[2],WorkArray_Space[2],color=pal_space[2],linewidth=3.0)
#ax.plot(StepArray[3],WorkArray_Space[3],color=pal_space[3],linewidth=3.0)
#ax.plot(StepArray[4],WorkArray_Space[4],color=pal_space[4],linewidth=3.0)

#ax.plot(StepArray[0],WorkArray_Exact[0],color=pal_exact[0],linewidth=3.0)
#ax.plot(StepArray[1],WorkArray_Exact[1],color=pal_exact[1],linewidth=3.0)
#ax.plot(StepArray[2],WorkArray_Exact[2],color=pal_exact[2],linewidth=3.0)
#ax.plot(StepArray[3],WorkArray_Exact[3],color=pal_exact[3],linewidth=3.0)
#ax.plot(StepArray[4],WorkArray_Exact[4],color=pal_exact[4],linewidth=3.0)

#ax.plot(StepArray[0],WorkArray_Approx[0],color=pal_approx[0],linewidth=3.0)
#ax.plot(StepArray[1],WorkArray_Approx[1],color=pal_approx[1],linewidth=3.0)
#ax.plot(StepArray[2],WorkArray_Approx[2],color=pal_approx[2],linewidth=3.0)
#ax.plot(StepArray[3],WorkArray_Approx[3],color=pal_approx[3],linewidth=3.0)
#ax.plot(StepArray[4],WorkArray_Approx[4],color=pal_approx[4],linewidth=3.0)

ax.plot(StepArray[0],WorkArray_Space[0],'r--',linewidth=2.0)
ax.plot(StepArray[0],WorkArray_Approx[0],'b--',linewidth=2.0)
ax.plot(StepArray[0],WorkArray_Exact[0],'k--',linewidth=2.0)

ax.plot(StepArray[0],WorkArray_Space[0],'ro')
ax.plot(StepArray[0],WorkArray_Approx[0],'bo')
ax.plot(StepArray[0],WorkArray_Exact[0],'ko')

ax.set_xscale('log')
ax.set_yscale('log')

plt.show()
plt.close()

#ax.set_yscale('log')
#ax.set_xscale('log')

#plt.show()
#plt.close()



#plt.plot(StepArray,WorkArray_Exact,'k',linewidth=3.0)
#plt.plot(StepArray,WorkArray_Approx,'b',linewidth=3.0)
#plt.plot(StepArray,WorkArray_Space,'r',linewidth=3.0)

#plt.yscale('log')
#plt.xscale('log')

#plt.show()
#plt.close()

WorkArray_Exact = []
WorkArray_Approx = []
WorkArray_Space = []
StepArray = []

WorkArray_Exact_Corr = []
WorkArray_Approx_Corr = []

WorkArray_Approx2 = []
WorkArray_Approx2_Corr = []

NumSteps = [10]

for index in range(len(NumSteps)):

	WorkArray_Exact.append([])
	WorkArray_Approx.append([])
	WorkArray_Space.append([])

	WorkArray_Approx2.append([])
	WorkArray_Approx2_Corr.append([])

	WorkArray_Exact_Corr.append([])
	WorkArray_Approx_Corr.append([])

	TotalTime = 0.1
	TimeArray = []

	CPVals = GenerateProtocol(NumSteps[index],TotalDist)

	CPStep = CPVals[1]-CPVals[0]

	print "\n\t\tCPStep --> " + str(CPStep) + "\n"

	#print "CPVals --> " + str(CPVals) + "\n"

	while TotalTime < 1000:

		WorkExact = ExactProtocolWork(CPVals,TotalTime)
		WorkApprox = LinearResponseProtocolWork(CPVals,TotalTime)
		WorkSpace = InfiniteTimeProtocolWork(CPVals)

		WorkExact = WorkExact/float(TotalDist*TotalDist/(2*float(NumSteps[index])))
		WorkApprox = WorkApprox/float(TotalDist*TotalDist/(2*float(NumSteps[index])))
		WorkSpace = WorkSpace/float(TotalDist*TotalDist/(2*float(NumSteps[index])))

		#WorkExact_Corr = AdjustedExactWork(CPVals,TotalTime)
		#WorkApprox_Corr = AdjustedLinearResponseWork(CPVals,TotalTime)

		WorkApprox2 = 1 + 2*exp(-float(TotalTime)/float(len(CPVals)-2))
		WorkApprox2_Corr = 2*exp(-float(TotalTime)/float(len(CPVals)-2))

		WorkExact_Corr = (WorkExact/WorkSpace) - 1
		WorkApprox_Corr = (WorkApprox/WorkSpace) - 1

		#WorkExact_Corr = WorkExact_Corr/float(TotalDist*TotalDist/(2*float(NumSteps[index])))
		#WorkApprox_Corr = WorkApprox_Corr/float(TotalDist*TotalDist/(2*float(NumSteps[index])))

		WorkArray_Exact[index].append(WorkExact)
		WorkArray_Approx[index].append(WorkApprox)
		WorkArray_Space[index].append(WorkSpace)

		WorkArray_Approx2[index].append(WorkApprox2)
		WorkArray_Approx2_Corr[index].append(WorkApprox2_Corr)

		WorkArray_Exact_Corr[index].append(WorkExact_Corr)
		WorkArray_Approx_Corr[index].append(WorkApprox_Corr)

		TimeArray.append(float(TotalTime)/(float(len(CPVals)-2)))

		TotalTime = TotalTime*1.25


sns.set()
#sns.set_context("poster")
#sns.palplot(sns.color_palette("hls",3))
#sns.set_palette("hls",3)
sns.set_palette("pastel")

SaveFile = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/DocumentPlots/Harmonic_Result_2.pdf"

fig, axes = plt.subplots(2,1,figsize=(10,7),sharex=True)

fig1_exact = axes[0].plot(TimeArray,WorkArray_Exact[0],'k',linewidth=3.0,label="Exact")
fig1_LR = axes[0].plot(TimeArray,WorkArray_Approx[0],'b',alpha=0.7,linewidth=3.0,label="Linear-response")
fig1_Space = axes[0].plot(TimeArray,WorkArray_Space[0],'r',alpha=0.7,linewidth=3.0,label="Infinite-time-limit")
#fig1_2 = axes[0].plot(TimeArray,WorkArray_Approx2[1],'g',alpha=0.5,linewidth=1.0)

fig2_exact = axes[1].plot(TimeArray,WorkArray_Exact_Corr[0],'k',linewidth=3.0,label="Exact")
fig2_LR = axes[1].plot(TimeArray,WorkArray_Approx_Corr[0],'b',alpha=0.7,linewidth=3.0,label="Linear-response")
#fig2_LR_2 = axes[1].plot(TimeArray,WorkArray_Approx2_Corr[1],'g',alpha=0.5,linewidth=1.0)

axes[0].set_yscale('log')#,basey=np.e)
axes[1].set_yscale('log')#,basey=np.e)

axes[0].set_xlim([0,4])
axes[1].set_xlim([0,4])

axes[0].set_ylim([0.75,15])
axes[1].set_ylim([0.01,15])

axes[0].set_yticks([0.5,1,2,4,8,16])


#plt.savefig(SaveFile,format='pdf')

plt.show()
plt.close()

WriteWorkData()


#fig,axes = plt.subplots(2,2,figsize=(10,7),sharex=True)

#fig1_exact = axes[0,0].plot(TimeArray,WorkArray_Exact[0],'k',linewidth=3.0,label="Exact")
#fig1_LR = axes[0,0].plot(TimeArray,WorkArray_Approx[0],'b',alpha=0.7,linewidth=3.0,label="Linear-response")
#fig1_Space = axes[0,0].plot(TimeArray,WorkArray_Space[0],'r',alpha=0.7,linewidth=3.0,label="Infinite-time limit")

#fig2_exact = axes[0,1].plot(TimeArray,WorkArray_Exact[1],'k',linewidth=3.0)
#fig2_LR = axes[0,1].plot(TimeArray,WorkArray_Approx[1],'b',alpha=0.7,linewidth=3.0)
#fig2_Space = axes[0,1].plot(TimeArray,WorkArray_Space[1],'r',alpha=0.7,linewidth=3.0)


#fig1_exact = axes[1,0].plot(TimeArray,WorkArray_Exact_Corr[0],'k',linewidth=3.0,label="Exact")
#fig1_LR = axes[1,0].plot(TimeArray,WorkArray_Approx_Corr[0],'b',alpha=0.7,linewidth=3.0,label="Linear-response")

#fig2_exact = axes[1,1].plot(TimeArray,WorkArray_Exact_Corr[1],'k',linewidth=3.0)
#fig2_LR = axes[1,1].plot(TimeArray,WorkArray_Approx_Corr[1],'b',alpha=0.7,linewidth=3.0)

#axes[0,0].set_xscale('log')
#axes[0,1].set_xscale('log')
#axes[1,0].set_xscale('log')
#axes[1,1].set_xscale('log')

#axes[0,0].set_yscale('log')
#axes[0,1].set_yscale('log')
#axes[1,0].set_yscale('log')
#axes[1,1].set_yscale('log')

#axes[0,0].set_ylim([0, 7])
#axes[0,1].set_ylim([0, 7])

#axes[1,0].set_ylim([0.001,50])
#axes[1,1].set_ylim([0.001,50])

#axes[0,0].set_xlim([0.1,100])
#axes[0,1].set_xlim([0.1,100])
#axes[1,0].set_xlim([0.1,100])
#axes[1,1].set_xlim([0.1,100])

#plt.savefig(SaveFile,format='pdf')

#plt.show()
#plt.close()

#fig, axes = plt.subplots(2,2,figsize=(4,4),sharex=True,sharey=True)

#fig1_exact = axes[0,0].plot(TimeArray,WorkArray_Exact[0],linewidth=4.0,label="Exact")
#fig1_LR = axes[0,0].plot(TimeArray,WorkArray_Approx[0],linewidth=2.0,label="Linear-response")
#fig1_Space = axes[0,0].plot(TimeArray,WorkArray_Space[0],linewidth=2.0,label="Infinite-time limit")

#fig2_exact = axes[0,1].plot(TimeArray,WorkArray_Exact[1],linewidth=4.0)
#fig2_LR = axes[0,1].plot(TimeArray,WorkArray_Approx[1],linewidth=2.0)
#fig2_Space = axes[0,1].plot(TimeArray,WorkArray_Space[1],linewidth=2.0)

#fig3_exact = axes[1,0].plot(TimeArray,WorkArray_Exact[2],linewidth=4.0)
#fig3_LR = axes[1,0].plot(TimeArray,WorkArray_Approx[2],linewidth=2.0)
#fig3_Space = axes[1,0].plot(TimeArray,WorkArray_Space[2],linewidth=2.0)

#fig4_exact = axes[1,1].plot(TimeArray,WorkArray_Exact[3],linewidth=4.0)
#fig4_LR = axes[1,1].plot(TimeArray,WorkArray_Approx[3],linewidth=2.0)
#fig4_Space = axes[1,1].plot(TimeArray,WorkArray_Space[3],linewidth=2.0)

#axes[0,0].set_xscale('log')
#axes[0,1].set_xscale('log')
#axes[1,0].set_xscale('log')
#axes[1,1].set_xscale('log')

#axes[0,0].set_yscale('log')
#axes[0,1].set_yscale('log')
#axes[1,0].set_yscale('log')
#axes[1,1].set_yscale('log')

#plt.show()
#plt.close()


#sns.palplot(sns.color_palette("hls",2))
#sns.set_palette("hls",2)
#sns.set_palette("pastel")

#fig,axes = plt.subplots(2,2,figsize=(4,4),sharex=True,sharey=True)

#fig1_exact = axes[0,0].plot(TimeArray,WorkArray_Exact_Corr[0],'k',linewidth=2.0,label="Exact")
#fig1_LR = axes[0,0].plot(TimeArray,WorkArray_Approx_Corr[0],'b',alpha=0.7,linewidth=2.0,label="Linear-response")

#fig2_exact = axes[0,1].plot(TimeArray,WorkArray_Exact_Corr[1],'k',linewidth=2.0)
#fig2_LR = axes[0,1].plot(TimeArray,WorkArray_Approx_Corr[1],'b',alpha=0.7,linewidth=2.0)

#fig3_exact = axes[1,0].plot(TimeArray,WorkArray_Exact_Corr[2],'k',linewidth=2.0)
#fig3_LR = axes[1,0].plot(TimeArray,WorkArray_Approx_Corr[2],'b',alpha=0.7,linewidth=2.0)

#fig4_exact = axes[1,1].plot(TimeArray,WorkArray_Exact_Corr[3],'k',linewidth=2.0)
#fig4_LR = axes[1,1].plot(TimeArray,WorkArray_Approx_Corr[3],'b',alpha=0.7,linewidth=2.0)

#axes[0,0].legend(loc='upper right')

#axes[0,0].set_xscale('log')
#axes[0,1].set_xscale('log')
#axes[1,0].set_xscale('log')
#axes[1,1].set_xscale('log')

#axes[0,0].set_yscale('log')
#axes[0,1].set_yscale('log')
#axes[1,0].set_yscale('log')
#axes[1,1].set_yscale('log')

#axes[0,0].set_ylim([0.001,100])
#axes[0,1].set_ylim([0.001,100])
#axes[1,0].set_ylim([0.001,100])
#axes[1,1].set_ylim([0.001,100])

#plt.show()
#plt.show()







