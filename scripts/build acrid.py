import os
import subprocess
import paths

#Python used instead of a bash script to take advantage of paths.py
#must change directory because mdtool build throws exceptions when path is specified

startingDir = os.getcwd()
os.chdir(paths.solutionDir)
exitCode = subprocess.call([
	"mdtool",
	"build"
])
os.chdir(startingDir)
exit(exitCode)
