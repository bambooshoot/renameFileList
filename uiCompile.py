from pysideuic import compileUi
import py_compile,glob,os

uiPath=os.curdir
preIndex=len(uiPath)+1
uiFiles=glob.glob("%s\*.ui"%uiPath)
for uiFile in uiFiles:
    fileBaseName=uiFile[preIndex:-3]
    pyFile="%s/%sUI.py"%(uiPath,fileBaseName)
    print uiFile,pyFile
    pyFileP = open(pyFile, 'w')
    compileUi(uiFile, pyFileP, False, 4, False)
    pyFileP.close()
