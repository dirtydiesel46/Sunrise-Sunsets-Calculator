import sys

from sunriseSunset import *
from sunrisetime import *
class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.timeout.connect(self.showlcd_sunsetDiff)
        timer.start(1000)
        self.showlcd()
        self.showlcd_sunrise()
        self.showlcd_sunset()
        self.setPicture()

    def showlcd(self):
        currentTimelcd = QtCore.QTime.currentTime()
        currentTimelcdText = currentTimelcd.toString('hh:mm:ss')
        self.ui.currentTimeLCD.display(currentTimelcdText)

    def showlcd_sunrise(self):
        self.ui.sunriseLCD.display(sunriseUtc2)

    def showlcd_sunset(self):
        self.ui.sunsetLCD.display(sunsetUtc2)

    def showlcd_sunsetDiff(self):
        sunsetToTime = self.calcTimeToSunset()
        sunsetToTimeText = sunsetToTime.toString("hh:mm:ss")
        self.ui.timeToSunsetLCD.display(sunsetToTimeText)
        sunriseFromTime = self.calcTimeFromSunrise()
        sunriseFromTimeText = sunriseFromTime.toString("hh:mm:ss")
        self.ui.timeFromSunriseLCD.display(sunriseFromTimeText)

    def calcTimeToSunset(self):
        currentTimeSunset = QtCore.QTime.currentTime()
        currentTimeSunsetText = currentTimeSunset.toString('hh:mm:ss')
        tdelta = datetime.strptime(sunsetUtc2, "%H:%M:%S") - datetime.strptime(currentTimeSunsetText, "%H:%M:%S")
        if tdelta.days < 0:
            tdelta = timedelta(days=0,
                               seconds=tdelta.seconds,
                               milliseconds=0)

        timeToSunset = QtCore.QTime((tdelta.total_seconds()) // 3600, ((tdelta.total_seconds()) % 3600) // 60,
                                    ((tdelta.total_seconds()) % 3600 % 60), QtCore.QTime.currentTime().msec())
        return timeToSunset

    def calcTimeFromSunrise(self):
        currentTimeSunset = QtCore.QTime.currentTime()
        currentTimeSunsetText = currentTimeSunset.toString('hh:mm:ss')
        tdelta = datetime.strptime(currentTimeSunsetText, "%H:%M:%S") - datetime.strptime(sunriseUtc2, "%H:%M:%S")
        if tdelta.days < 0:
            tdelta = timedelta(days=0,
                               seconds=tdelta.seconds,
                               milliseconds=0)

        timeFromSunrise = QtCore.QTime((tdelta.total_seconds()) // 3600, ((tdelta.total_seconds()) % 3600) // 60,
                                       ((tdelta.total_seconds()) % 3600 % 60), QtCore.QTime.currentTime().msec())
        return timeFromSunrise

    def setPicture(self):
        currentTime = QtCore.QTime.currentTime()
        intCurrentTime = currentTime.hour() * 3600 + currentTime.minute() * 60 + currentTime.second()
        dayTime = QtCore.QTime(5, 00, 00)
        intDayTime = dayTime.hour() * 3600 + dayTime.minute() * 60 + dayTime.second()
        nightTime = QtCore.QTime(19,00,00)
        intNightTime = nightTime.hour() * 3600 + nightTime.minute() * 60 + nightTime.second()

        if(intCurrentTime >= intNightTime):
            self.ui.dayOrNightLabel.setText("Have a good night!")
            self.ui.dayOrNightPic.setPixmap(QtGui.QPixmap("img/NightTime.jpeg"))
        else:
            self.ui.dayOrNightLabel.setText("Have good day!")



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
