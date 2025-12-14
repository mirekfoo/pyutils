
# TODO Add metadata as in https://packaging.python.org/en/latest/specifications/core-metadata/, so it can be read with https://docs.python.org/3/library/importlib.metadata.html

"""
Tool Context.
"""
 
cmd = None
home_dir = None
argv = None
usage = None
tool = None
 
def getCmd():
    global cmd
    return cmd
 
def getHomeDir():
    global home_dir
    return home_dir
 
def getArgV():
    global argv
    return argv
 
def setUsagePrintProc(p):
    global usage
    usage = p
 
def printUsage():
    global usage
    if usage:
        usage()
 
def setToolShortName(name):
    global tool
    tool = name
 
def getToolShortName():
    global tool
    return tool if tool else ''
 
# -----------------------------
 
import os
import sys
 
cmd = ' '.join(sys.argv)
home_dir = os.path.dirname(sys.argv[0])
argv = sys.argv[1:]
setToolShortName(os.path.splitext(os.path.basename(sys.argv[0]))[0])
 

 
