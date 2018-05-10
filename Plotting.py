#This python script contains relevant plotting script for discrete control simulations
#
#Steven Large
#February 9th 2018

import matplotlib.pyplot as plt
import numpy as np
import CorrelationFit

def PlotFunctionFits(CorrMesh,IndexValues,A,B,C,D,LagTime):

	X_Data = np.asarray(LagTime)

	for index in range(len(IndexValues)):

		plt.plot(LagTime,CorrMesh[IndexValues[index]])

	for index in range(len(IndexValues)):

		Y_Data = CorrelationFit.Function(X_Data, A[index], B[index], C[index], D[index])
		plt.plot(X_Data,Y_Data,'--')


	hfont = {'fontname':'Times New Roman'}

	plt.ylabel('Force Correlation',fontsize=18,**hfont)
	plt.xlabel('Lag Time',fontsize=18,**hfont)

	plt.savefig('Plots/FitCompare.png',format='png')









