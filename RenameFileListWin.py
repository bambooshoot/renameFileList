# coding=utf-8
import os,glob,re,sys

try:
  from PySide2.QtCore import * 
  from PySide2.QtGui import * 
  from PySide2.QtWidgets import *
except ImportError:
  from PySide.QtCore import * 
  from PySide.QtGui import * 

import RenameFileListUI

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.ui=RenameFileListUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.ui.btn_Preview.clicked.connect(self.Preview)
        self.ui.btn_Rename.clicked.connect(self.Rename)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/uri-list'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.ui.listWidget_Source.clear()
        
        fileList=[]
        for url in e.mimeData().urls():
            fileName=url.toLocalFile()
            fileList.append(fileName)

        extStr=re.search("\\.[a-zA-Z]+$",fileList[0]).group(0)
        print "ext",extStr
        numList=[]
        self.fileDict={}
        for curFile in fileList:
            num_ext=re.search("\d+%s$"%extStr,curFile).group(0)
            l=len(num_ext)-len(extStr)
            num=num_ext[:l]
            numList.append(num)
            self.fileDict[num]=curFile

        numList.sort()
        for num in numList:
            self.ui.listWidget_Source.addItem(self.fileDict[num])

        targetPattern=fileList[0]
        targetPattern=re.sub("\d+[\.a-zA-Z]+$","%%04d%s"%extStr,targetPattern)
        self.ui.lineEdit_NewName.setText(targetPattern)

    def Preview(self):
        self.ui.listWidget_Target.clear()
        targetPattern=self.ui.lineEdit_NewName.text()
        for i in range(self.ui.listWidget_Source.count()):
            self.ui.listWidget_Target.addItem(targetPattern%(i+self.ui.spinBox_StartFrame.value()))

    def Rename(self):
        targetPattern=self.ui.lineEdit_NewName.text()
        for i in range(self.ui.listWidget_Source.count()):
            os.rename(self.ui.listWidget_Source.item(i).text(),targetPattern%(i+self.ui.spinBox_StartFrame.value()))
        


if __name__ == '__main__':
    app = QApplication.instance()
    if app==None:
        app=QApplication(sys.argv)

    mainWin=MainWindow()
    mainWin.show()

    app.exec_()
    sys.exit()