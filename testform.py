#coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QTimer,Qt
from PyQt5.QtGui import QIcon,QImage,QPixmap
from ui.test import Ui_TestForm
import cv2
from MyQR import myqr
import numpy as np

class Testwindow(QtWidgets.QWidget):

    _signal = pyqtSignal(bytes)

    def __init__(self):
        super(Testwindow,self).__init__()
        self.new=Ui_TestForm()
        self.new.setupUi(self)
        self.new.btn_generate.clicked.connect(self.QrImageCvt)
        self.new.btn_start_captrue.clicked.connect(self.startCapture)
        #self.startCapture()
        #self.QrImageCvt()

    def QrImageCvt(self):
        head = 'DQY'
        model = '19016'
        date = '1908'
        factory = '01'
        pin=self.new.lineEdit.text()
        cnt = self.new.lineEditCnt.text()
        cnt = int(cnt)
        pin = int(pin)
        for i in range(0, cnt):
            serial = str("%04d"%(pin+i))
            name = head + model + date + factory + serial
            myqr.run(words=name,save_name='./Icon/qr.png')
            p2 = cv2.imread('./Icon/qr.png')
            p1 = cv2.imread('./Icon/pic.jpg')
            image_height, image_width, image_depth = p1.shape
            x = 65
            y = 50
            w = 175
            p2 = cv2.resize(p2,(w,w))
            p1[image_height-w-y:image_height-y,image_width-w-x:image_width-x] = p2
            p1 = cv2.putText(p1, 'SN:'+name, (image_width-350,image_height-50), cv2.FONT_HERSHEY_COMPLEX_SMALL,1.0,(0,0,0),2)
            QIm = cv2.cvtColor(p1, cv2.COLOR_BGR2RGB)
            self.new.label.setGeometry(20, 10, image_width, image_height)
            QIm = QImage(QIm.data, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
            QPix = QPixmap.fromImage(QIm)
            dx1 = 50
            dx2 = dx1+10
            dy1 = 90
            dy2 = 40
            cv2.imwrite('./Icon/temp/'+name+'.png',p1[dy1:image_height-dy2,dx1:image_width-dx2])
        self.new.label.setPixmap(QPix)

    def startCapture(self):
        self.setWindowIcon(QIcon('./Icon/dqy.png'))
        png=QtGui.QPixmap('./Icon/dqy.png')
        self.timer = QTimer()
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.timer.timeout.connect(self.update)
        self.timer.start(10)
        self.cap = cv2.VideoCapture(0)
        self.image = QImage()
        self.width = 640
        self.height = 480
        self.detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
            
    def update(self):
        ret,frame = self.cap.read()
        height,width,depth = frame.shape
        gray = cv2.cvtColor(frame, code = cv2.COLOR_BGR2GRAY)
        face_zone = self.detector.detectMultiScale(gray,scaleFactor=1.2,minNeighbors = 5)
        for x,y,w,h in face_zone:
            cv2.circle(frame,center = (x+w//2,y+h//2),radius = w//2, color = [0,0,255])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.image = QImage(frame, width,height,3*width,QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(self.image)
        self.new.label.setPixmap(pixmap)
        
if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    from uartform import Uartwindow

    app = QtWidgets.QApplication(sys.argv)
    uf = Testwindow()
    uf.show()
    sys.exit(app.exec_())