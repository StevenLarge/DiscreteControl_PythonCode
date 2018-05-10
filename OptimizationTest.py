#This python script tests the scipy.optimize minimization function
#
#Steven Large
#February 9th 2018

import numpy as np
import scipy.optimize



def Function(XData, Par1, Par2):

	#Val = (XData[0] - 1)**2 + (XData[1] - 2.5)**2

	Val = np.exp(-Par1*XData[0]) + np.exp(-Par2*XData[1])

	return Val

def Function2(XData, *argv):

#	Cost = 0

#	for arg in argv:

#		Cost = Cost + np.exp(-arg*XData[arg])

	Cost = 0.0

	for index in range(len(argv)):

		Cost = Cost + np.exp(-argv[index]*XData[index])

	#eCost = np.exp(-argv[0]*XData[0]) + np.exp(-argv[1]*XData[1])

	return Cost


#fun = lambda x : (x[0] - 1)**2 + (x[1] - 2.5)**2

def EqCon(XData):

	Val = 0

	for index in range(len(XData)):
		Val = Val + XData[index]

	return Val - EqVal

#cons = ({'type':'ineq','fun':lambda x :  x[0] - 2*x[1] + 2},
#		{'type':'ineq','fun':lambda x : -x[0] - 2*x[1] + 6},
#		{'type':'ineq','fun':lambda x : -x[0] + 2*x[1] + 2})

#global Par1
#global Par2

Par1 = 1
Par2 = 0.5

#global EqVal

EqVal = 1

ParTuple = (Par1,Par2)
ParList = [Par1,Par2]

cons = ({'type':'eq','fun': EqCon})

bnds = ((0,None),(0,None))

res = scipy.optimize.minimize(Function2, (0.5,0.5), args=ParTuple, method="SLSQP", bounds=bnds, constraints=cons)

print "Result --> " + str(res.x)
print "Message --> " + str(res.message)



