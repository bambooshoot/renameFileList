# usage
# RenameFileList("c:\fileBaseName.*.jpg","c:\fileTargetName.%4d.jpg")

import os,glob,re,sys
def RenameFileList(namePattern,targetPattern,startFrame):
	fileList=glob.glob(namePattern)
	extStr=re.search("\\*.+$",namePattern).group(0)
	extStr=extStr[1:]
	numList=[]
	fileDict={}
	for curFile in fileList:
		num_ext=re.search("\d+%s$"%extStr,curFile).group(0)
		l=len(num_ext)-len(extStr)
		num=num_ext[:l]
		numList.append(num)
		fileDict[num]=curFile

	numList.sort()
	for i in range(len(numList)):
		print fileDict[numList[i]],targetPattern%(i+startFrame)
		os.rename(fileDict[numList[i]],targetPattern%(i+startFrame))

if __name__ == '__main__':
	RenameFileList(sys.argv[1],sys.argv[2],int(sys.argv[3]))