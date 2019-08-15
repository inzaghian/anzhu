#coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from ui.comset import Ui_comsetform

class Comsetwindow(QtWidgets.QWidget):

    _signal = pyqtSignal(dict)

    def __init__(self):
        super(Comsetwindow,self).__init__()
        self.new=Ui_comsetform()
        self.new.setupUi(self)
        self.new.btn_save.clicked.connect(self.Get_set)

    def initcom(self,clist):
        self.new.cb_com.clear()
        self.new.cb_com.addItems(clist)
        self.setWindowIcon(QIcon('./Icon/dqy.png'))
        
    def Get_set(self):
        sl={}
        com=self.new.cb_com.currentText()
        bsp=self.new.cb_bsp.currentText()
        d=self.new.cb_data.currentText()
        p=self.new.cb_p.currentText()
        s=self.new.cb_stop.currentText()
        sl={'com':com,'bsp':bsp,'d':d,'p':p,'s':s}
        self._signal.emit(sl)
        self.close()
        
    def set_com(self,msg):
        try:
            com=msg['com']
            bsp=msg['bsp']
            d=msg['d']
            s=msg['s']
            p=msg['p']
            self.new.cb_com.setCurrentText(com)
            bsp=self.new.cb_bsp.setCurrentText(bsp)
            d=self.new.cb_data.setCurrentText(d)
            p=self.new.cb_p.setCurrentText(s)
            s=self.new.cb_stop.setCurrentText(p)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    from uartform import Uartwindow

    app = QtWidgets.QApplication(sys.argv)
    uf = Comsetwindow()
    uf.show()
    sys.exit(app.exec_())