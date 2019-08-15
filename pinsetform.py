#coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from ui.pinset import Ui_PinSetForm

class Pinsetwindow(QtWidgets.QWidget):

    _signal = pyqtSignal(bytes)

    def __init__(self):
        super(Pinsetwindow,self).__init__()
        self.new=Ui_PinSetForm()
        self.new.setupUi(self)
        self.new.lineEdit.returnPressed.connect(self.DataInput)
        self.initcom()

    def initcom(self):
        self.setWindowIcon(QIcon('./Icon/dqy.png'))
        png=QtGui.QPixmap('./Icon/dqy.png')
        self.new.label.setPixmap(png)

    def DataInput(self):
        data=self.new.lineEdit.text()
        print(data)
        self._signal.emit(data.encode("utf-8"))
        self.new.lineEdit.clear()
        self.close()

        
if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    from uartform import Uartwindow

    app = QtWidgets.QApplication(sys.argv)
    uf = Pinsetwindow()
    uf.show()
    sys.exit(app.exec_())