#This script contains all of the data writing routines for the discrete protocol optimization
#
#Steven Large
#February 12th 2018

import os

def WriteProtocol(Path,Filename,CP,Time):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(CP)):
		file1.write("%lf\t%lf\n" % (CP[index], Time[index]))

	file1.close()


def OptimizerLog(Path,Filename,OptRes):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	file1.write("Result --> " + str(OptRes.x) + "\n\n")
	file1.write("Message --> " + str(OptRes.message) + "\n\n")
	file1.write("Evaluations of objective function --> " + str(OptRes.nfev) + "\n\n")
	file1.write("Number of Optimizer iterations --> " + str(OptRes.nit))

	file1.close()

def OptimizerLog_Cost(Path,Filename,CostTracker):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	file1.write("#This file contains the objective function cost value for succesive interations of the full optimizer\n\n")

	for index in range(len(CostTracker)):
		file1.write("%lf\n" % (CostTracker[index]))

	file1.close()




