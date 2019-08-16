#coding:utf-8
import serial
import serial.tools.list_ports
class opencom():
    def __init__(self):
        self.com=serial.Serial()

    def initcom(self,comname,bsp=115200,bs=8,s=1,p=serial.PARITY_NONE):
        try:
            self.com.port = comname
            self.com.baudrate = bsp
            self.com.bytesize = bs 
            self.com.stopbits = s
            self.com.parity = p
        except Exception as e:
            print(e)

    def isopen(self):
        return self.com.isOpen()

    def opencom(self):
        try:
            self.com.open()
        except Exception as e:
            print(e)
        return self.com.isOpen()

    def CloseCom(self):
        if self.com.isOpen():
            self.com.close()
            print("串口关闭")

    def Get_ports(self):
        clist=[]
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list)> 0:
            clist=[]
            for e in port_list:
                port_list_0 =list(e)
                port_serial = port_list_0[0]
                clist.append(port_serial)
        return clist

    def Get_p(self,p):
        pstate=serial.PARITY_NONE
        if p=="ODD":
            pstate=serial.PARITY_ODD
        elif p=="EVEN":
            pstate=serial.PARITY_EVEN
        return pstate

    def comwritebytes(self,b):
        wlen=self.com.write(b)
        return wlen

    def comwritestring(self,b):
        wlen=self.com.write(b.encode("utf-8"))
        return wlen    

    def HexToString(self,b):
        rdata=""
        for e in b:
            rdata+=hex(e)+" "
        rdata=rdata[:-1]
        return rdata

    def comreadbytes(self):
        slen=self.com.in_waiting
        sdata=b''
        if slen>0:
            sdata = self.com.read(slen)
        return sdata

"""
c1=opencom()
clist=c1.Get_ports()
if len(clist)>0:
    comname=clist[0]
    c1.initcom(comname)
    if c1.opencom():
        c1.CloseCom()
"""