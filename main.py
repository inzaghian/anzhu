#coding:utf-8
from PyQt5 import QtWidgets
from uartform import Uartwindow
import sys
def main():
	app = QtWidgets.QApplication(sys.argv)
	uf = Uartwindow()
	uf.show()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()