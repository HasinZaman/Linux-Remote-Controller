import os

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Linux-Remote-Controller"

with open("{0}/serverStartUp.sh".format(baseDir), "w") as file:
	file.writelines(["#!/bin/bash", "python3 {0}/Server.py".format(baseDir)])