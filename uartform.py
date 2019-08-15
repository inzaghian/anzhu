#coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QThread,QTimer,Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from ui.uart import Ui_uartform
from comsetform import Comsetwindow
from pinsetform import Pinsetwindow
from testform import Testwindow
from com import opencom
from xmlreadandwrite import WriteXml,ReadXml
import time


class Uthread(QThread):   
    _signal = pyqtSignal(bytes)  
  
    def __init__(self, parent=None):  
        super(Uthread, self).__init__()

    def initcom(self,com):
        self.com=com

    def SetAlive(self,alive):
        self.alive=alive
    
    def run(self):
        while self.alive:
            try:
                sdata=self.com.comreadbytes()
                self._signal.emit(sdata)
            except Exception as e:
                print(e)
                break

class Uartwindow(QtWidgets.QWidget):
    
    def __init__(self):  
        super(Uartwindow,self).__init__()  
        self.new = Ui_uartform()
        self.new.setupUi(self)
        self.InitData()

    def InitData(self):
        self.cw=Comsetwindow()
        self.PinWin=Pinsetwindow()
        self.PinWin._signal.connect(self.PinSet)
        self.com=opencom()
        self.cw._signal.connect(self.callcw)
        self.TestWin = Testwindow()
        self.new.btn_setcom.clicked.connect(self.ShowCw)
        self.new.btn_search.clicked.connect(self.searchcom)
        #self.new.btn_open.clicked.connect(self.OpneCom)
        self.new.btn_open.clicked.connect(self.btn_opencom)
        self.new.btn_send.clicked.connect(self.WriteData)
        self.new.btn_receive.clicked.connect(self.ReadData)
        self.new.btn_clear.clicked.connect(self.ClearMsg)
        self.searchcom()
        #self.new.cb_receive.setChecked(False)
        self.thread = None
        self.rtim=QTimer()
        self.rtim.setTimerType(Qt.TimerType.PreciseTimer)
        self.rtim.timeout.connect(self.callrtim)
        self.logpath="./log/" + str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())) + '_log.txt'
        self.ShowLog(self.logpath)
        self.svaedata=""
        try:
            self.sl=ReadXml('setmsg.xml')
            self.callcw(self.sl,b=1)
        except Exception as e:
            self.ShowLog(str(e))
        self.setWindowIcon(QIcon('./Icon/dqy.png'))
        self.new.btn_help_cmd.clicked.connect(self.HelpCmd)
        self.new.btn_reboot_cmd.clicked.connect(self.RebootCmd)
        self.new.btn_dev_info_cmd.clicked.connect(self.DevInfoCmd)
        self.new.btn_log_on_cmd.clicked.connect(self.LogOnCmd)
        self.new.btn_log_off_cmd.clicked.connect(self.LogOffCmd)
        self.new.btn_pin_cmd.clicked.connect(self.InputPinCmd)
        self.new.btn_dev_reset_cmd.clicked.connect(self.DevResetCmd)
        self.new.btn_test.clicked.connect(self.TestStart)
        png=QtGui.QPixmap('./Icon/dqy.png')
        self.new.l1.setPixmap(png)
     
    def starttim(self):
        self.rtim.start(10)

    def stoptim(self):
        self.rtim.stop()

    def callrtim(self):
        sdata=self.com.comreadbytes()
        self.callbacklog(sdata)

    #开始串口接收线程	
    def StartThread(self):
        # 创建线程  
        self.thread = Uthread()  
        self.thread.initcom(self.com)
        self.thread.SetAlive(True)		
        self.thread._signal.connect(self.callbacklog)		
        # 开始线程  
        self.thread.start()  

    #停止串口线程
    def StopThread(self):
        if self.thread is not None:
            self.thread.SetAlive(False)
            self.thread.quit()
            self.thread.wait()
            self.thread.exit()
            self.thread = None
        
    def callbacklog(self,msg):
        if len(msg)>0:
            cbcheck=self.new.cb_receive.checkState()
            hdata=""
            try:
                if cbcheck:
                    hdata=self.com.HexToString(msg)
                    self.ShowMsg(hdata)
                else:
                    hdata=msg.decode('utf-8','replace')
                    self.ShowMsg(hdata)
                self.WriteLog(hdata+"\r\n")
            except Exception as e:
                self.ShowMsg(str(e))

    def ShowCw(self):
        self.searchcom()
        self.cw.set_com(self.sl)
        self.cw.show()

    def callcw(self,msg,b=0):
        if msg:
            self.ShowLog(str(msg))
            try:
                com=msg['com']
                bsp=msg['bsp']
                d=msg['d']
                s=msg['s']
                p=msg['p']
                rp=self.com.Get_p(p)
                self.com.initcom(com,int(bsp),int(d),int(s),rp)
                if b==0:
                    WriteXml(msg)
                self.ShowLog("串口设置成功")
                if self.com.isopen():
                    self.OpenCom("关闭")
                self.btn_opencom()
            except Exception as e:
                self.ShowBox(str(e))

    def WriteLog(self,sdata,b=0):
        self.svaedata+=sdata
        if len(self.svaedata)>=512 or b==1:
            with open(self.logpath,'a',encoding='utf-8') as f: 
                f.write(self.svaedata)
                f.close()
            self.svaedata=""
            
    def btn_opencom(self):
        t=self.new.btn_open.text()
        self.OpenCom(t)
    
    def OpenCom(self,t):
        try:
            if t=="打开":
                comname=self.new.cb_comname.currentText()
                self.com.initcom(comname=comname)
                if(self.com.opencom()):
                    self.new.btn_open.setText("关闭")
                    self.new.btn_open.setStyleSheet("background-color:gold")
                    self.ShowLog("串口打开")
                    #self.StartThread()
                    self.starttim()
                else:
                    self.ShowLog("打开失败")
            elif t=="关闭":
                self.com.CloseCom()
                if(self.com.isopen()):
                    self.ShowLog("关闭失败！")
                else:
                    #self.StopThread()
                    self.stoptim()
                    self.ShowLog("串口关闭")
                    self.new.btn_open.setText("打开")
                    self.new.btn_open.setStyleSheet("")
        except Exception as e:
            self.ShowBox(str(e))        

    def searchcom(self):
        clist=self.com.Get_ports()
        self.new.cb_comname.clear()
        self.new.cb_comname.addItems(clist)
        self.cw.initcom(clist)

    def ShowMsg(self, msg):
        #self.new.txt_show.append(msg+"\r\n")
        self.new.txt_show.append(msg)
        self.new.txt_show.moveCursor(QtGui.QTextCursor.End)
    
    def ShowLog(self, msg):
        #self.new.log_show.append(msg+"\r\n")
        self.new.log_show.append(msg)
        self.new.log_show.moveCursor(QtGui.QTextCursor.End)

    def ClearMsg(self):
        self.new.txt_show.clear()

    def ShowBox(self,msg,title="串口收发数据"):
        QMessageBox.information(self,title, msg, QMessageBox.Ok)

    def closeEvent(self, event):
        try:
            self.cw.close()
            self.StopThread()
            self.stoptim()
            self.com.CloseCom()
            self.WriteLog("",b=1)
        except Exception as e:
            self.ShowLog(str(e))

    def HexToBytes(self): #11 22 33 44 55 
        bl=[]
        try:
            text=self.new.txt_send.text()
            slist=text.split(" ")
            for e in slist:
                b=int(e,16)
                bl.append(b)
        except Exception as e:
            self.ShowBox(str(e))
        return bl

    def WriteData(self):
        try:
            slen=0
            msg=self.new.txt_send.text()
            cbcheck=self.new.cb_send.checkState()
            if cbcheck:
                bl=self.HexToBytes()
                slen=self.com.comwritebytes(bl)
            else:
                slen=self.com.comwritestring(msg)
            self.ShowLog("发送数据长度"+str(slen))
        except Exception as e:
            self.ShowBox(str(e))

    def ReadData(self):
        sdata=self.com.comreadbytes()
        if len(sdata)>0:
            cbcheck=self.new.cb_receive.checkState()
            try:
                if cbcheck:
                    hdata=self.com.HexToString(sdata)
                    self.ShowMsg(hdata)
                else:
                    hdata=sdata.decode('utf-8','replace')
                    self.ShowMsg(hdata)
            except Exception as e:
                self.ShowLog(str(e))
    
    def CmdSend(self, cmd):
        len = self.com.comwritestring(cmd)
        self.ShowLog("发送数据长度"+str(len))

    def HelpCmd(self):
        self.CmdSend("HELP")

    def RebootCmd(self):
        self.CmdSend("REBOOT")

    def DevInfoCmd(self):
        self.CmdSend("DEV_INFO")

    def LogOnCmd(self):
        self.CmdSend("LOG:ON")

    def LogOffCmd(self):
        self.CmdSend("LOG:OFF")

    def InputPinCmd(self):
        self.PinWin.show()

    def PinSet(self,msg):
        self.CmdSend("PIN:"+ msg.decode("utf-8"))
        self.ShowLog(msg.decode("utf-8"))

    def DevResetCmd(self):
        self.CmdSend("DEV_RESET")

    def TestStart(self):
        self.TestWin.show()
    
if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    from uartform import Uartwindow

    app = QtWidgets.QApplication(sys.argv)
    uf = Uartwindow()
    uf.show()
    sys.exit(app.exec_())