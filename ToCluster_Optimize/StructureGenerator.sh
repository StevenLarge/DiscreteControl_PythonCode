#!/usr/bin/env python

import os

Protocol_Ext = ["9_15","105_15","12_15","15_15"]

for index in range(len(Protocol_Ext)):

	if(os.path.isdir("Protocols") == False):
		DirName = "Protocols_" + Protocol_Ext[index]
		os.mkdir(DirName)
		os.chdir(DirName)
		os.mkdir("Logs")
		os.chdir("..")


os.system("echo")
os.system("echo")
os.system("echo ----- System Structure Generated -----")
os.system("echo")
os.system("echo")


