# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sunriseSunset.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(809, 565)
        self.studentInfoLayout = QtGui.QGroupBox(Dialog)
        self.studentInfoLayout.setGeometry(QtCore.QRect(510, 450, 291, 111))
        self.studentInfoLayout.setObjectName(_fromUtf8("studentInfoLayout"))
        self.layoutWidget = QtGui.QWidget(self.studentInfoLayout)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 261, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.studentLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.studentLayout.setObjectName(_fromUtf8("studentLayout"))
        self.studentLabelsLayout = QtGui.QVBoxLayout()
        self.studentLabelsLayout.setObjectName(_fromUtf8("studentLabelsLayout"))
        self.studNameDescLabel = QtGui.QLabel(self.layoutWidget)
        self.studNameDescLabel.setEnabled(True)
        self.studNameDescLabel.setObjectName(_fromUtf8("studNameDescLabel"))
        self.studentLabelsLayout.addWidget(self.studNameDescLabel)
        self.studNumDesclabel = QtGui.QLabel(self.layoutWidget)
        self.studNumDesclabel.setObjectName(_fromUtf8("studNumDesclabel"))
        self.studentLabelsLayout.addWidget(self.studNumDesclabel)
        self.studentLayout.addLayout(self.studentLabelsLayout)
        self.studentDetailsLayout = QtGui.QVBoxLayout()
        self.studentDetailsLayout.setObjectName(_fromUtf8("studentDetailsLayout"))
        self.studNameLable = QtGui.QLineEdit(self.layoutWidget)
        self.studNameLable.setEnabled(False)
        self.studNameLable.setObjectName(_fromUtf8("studNameLable"))
        self.studentDetailsLayout.addWidget(self.studNameLable)
        self.studNumLable = QtGui.QLineEdit(self.layoutWidget)
        self.studNumLable.setEnabled(False)
        self.studNumLable.setObjectName(_fromUtf8("studNumLable"))
        self.studentDetailsLayout.addWidget(self.studNumLable)
        self.studentLayout.addLayout(self.studentDetailsLayout)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 200, 131, 101))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.sunriseLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.sunriseLayout.setObjectName(_fromUtf8("sunriseLayout"))
        self.sunriseLabel = QtGui.QLabel(self.layoutWidget1)
        self.sunriseLabel.setObjectName(_fromUtf8("sunriseLabel"))
        self.sunriseLayout.addWidget(self.sunriseLabel)
        self.sunriseLCD = QtGui.QLCDNumber(self.layoutWidget1)
        self.sunriseLCD.setDigitCount(8)
        self.sunriseLCD.setObjectName(_fromUtf8("sunriseLCD"))
        self.sunriseLayout.addWidget(self.sunriseLCD)
        self.layoutWidget_2 = QtGui.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 360, 131, 101))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.sunsetLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.sunsetLayout.setObjectName(_fromUtf8("sunsetLayout"))
        self.sunseLabel = QtGui.QLabel(self.layoutWidget_2)
        self.sunseLabel.setObjectName(_fromUtf8("sunseLabel"))
        self.sunsetLayout.addWidget(self.sunseLabel)
        self.sunsetLCD = QtGui.QLCDNumber(self.layoutWidget_2)
        self.sunsetLCD.setDigitCount(8)
        self.sunsetLCD.setObjectName(_fromUtf8("sunsetLCD"))
        self.sunsetLayout.addWidget(self.sunsetLCD)
        self.layoutWidget2 = QtGui.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 50, 131, 101))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.currentTimeLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.currentTimeLayout.setObjectName(_fromUtf8("currentTimeLayout"))
        self.currentTimeLabel = QtGui.QLabel(self.layoutWidget2)
        self.currentTimeLabel.setObjectName(_fromUtf8("currentTimeLabel"))
        self.currentTimeLayout.addWidget(self.currentTimeLabel)
        self.currentTimeLCD = QtGui.QLCDNumber(self.layoutWidget2)
        self.currentTimeLCD.setDigitCount(8)
        self.currentTimeLCD.setObjectName(_fromUtf8("currentTimeLCD"))
        self.currentTimeLayout.addWidget(self.currentTimeLCD)
        self.layoutWidget_3 = QtGui.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(220, 360, 131, 101))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.timeToSunsetLayout = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.timeToSunsetLayout.setObjectName(_fromUtf8("timeToSunsetLayout"))
        self.timeToSunsetLabel = QtGui.QLabel(self.layoutWidget_3)
        self.timeToSunsetLabel.setObjectName(_fromUtf8("timeToSunsetLabel"))
        self.timeToSunsetLayout.addWidget(self.timeToSunsetLabel)
        self.timeToSunsetLCD = QtGui.QLCDNumber(self.layoutWidget_3)
        self.timeToSunsetLCD.setDigitCount(8)
        self.timeToSunsetLCD.setObjectName(_fromUtf8("timeToSunsetLCD"))
        self.timeToSunsetLayout.addWidget(self.timeToSunsetLCD)
        self.layoutWidget_4 = QtGui.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(220, 200, 131, 101))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.timeFromSunriseLayout = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.timeFromSunriseLayout.setObjectName(_fromUtf8("timeFromSunriseLayout"))
        self.timeFromSunriseLabel = QtGui.QLabel(self.layoutWidget_4)
        self.timeFromSunriseLabel.setObjectName(_fromUtf8("timeFromSunriseLabel"))
        self.timeFromSunriseLayout.addWidget(self.timeFromSunriseLabel)
        self.timeFromSunriseLCD = QtGui.QLCDNumber(self.layoutWidget_4)
        self.timeFromSunriseLCD.setDigitCount(8)
        self.timeFromSunriseLCD.setObjectName(_fromUtf8("timeFromSunriseLCD"))
        self.timeFromSunriseLayout.addWidget(self.timeFromSunriseLCD)
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(460, 41, 301, 311))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.dayOrNightLabel = QtGui.QLabel(self.splitter)
        self.dayOrNightLabel.setText(_fromUtf8(""))
        self.dayOrNightLabel.setObjectName(_fromUtf8("dayOrNightLabel"))
        self.dayOrNightPic = QtGui.QLabel(self.splitter)
        self.dayOrNightPic.setText(_fromUtf8(""))
        self.dayOrNightPic.setPixmap(QtGui.QPixmap(_fromUtf8("img/DayTime.jpeg")))
        self.dayOrNightPic.setObjectName(_fromUtf8("dayOrNightPic"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Sunrises and Sunsets", None))
        self.studentInfoLayout.setTitle(_translate("Dialog", "Student Information", None))
        self.studNameDescLabel.setText(_translate("Dialog", "Student Name:", None))
        self.studNumDesclabel.setText(_translate("Dialog", "Student Number:", None))
        self.studNameLable.setText(_translate("Dialog", "Daniel du Preez", None))
        self.studNumLable.setText(_translate("Dialog", "64245179", None))
        self.sunriseLabel.setText(_translate("Dialog", "Sunrise", None))
        self.sunseLabel.setText(_translate("Dialog", "Sunset", None))
        self.currentTimeLabel.setText(_translate("Dialog", "Current time", None))
        self.timeToSunsetLabel.setText(_translate("Dialog", "Time to Sunset", None))
        self.timeFromSunriseLabel.setText(_translate("Dialog", "Time from Sunrise", None))


