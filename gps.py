#coding:utf-8
class gps():
    def __init__(self):
        self.realdata=b''
        self.fb=False

    def Get_gps_data(self,sdata):
        sl=[]
        for e in sdata:
            if e==0x24 and self.fb==False:
                self.fb=True
                self.realdata+=bytes([e])
            if self.fb and e==0x0a:
                self.realdata+=bytes([e])
                data=self.realdata.decode('utf-8','replace')
                sl.append(data)
                self.fb=False
                self.realdata=b''
            elif e!=0x24 and self.fb:
                self.realdata+=bytes([e])
            elif e==0x24 and self.fb and len(self.realdata)>5:
                data=self.realdata.decode('utf-8','replace')
                sl.append(data)
                self.realdata=b''
                self.realdata+=bytes([e])
        print(sl)
        return sl

    def CheckGpsBuff(self,buff):
        buff=buff.replace("\r","").replace("\n","")
        isok = False
        if len(buff)==(buff.find('*')+2):
            pass
        else:
            crc=0
            for ch in buff:
                if ch=='$':
                    pass
                elif ch=='*':
                    break
                else:
                    if crc==0:
                        crc=ord(ch)
                    else:
                        crc=crc^ord(ch)
            try:
                if buff.find('*')+3==len(buff):
                    length=buff.find('*')
                    s=buff[length+1]+buff[length+2]
                    scode=(str(hex(crc))[2:]).upper()
                    if len(scode)==2:
                        pass
                    else:
                        scode="0"+scode
                    if s==scode:
                        isok=True
            except Exception as e:
                print("gpsErr:",str(e))
        return isok

g=gps()
sdata="$GPRMC,121252.000,A,3958.3032,N,11629.6046,E,15.15,359.95,070306,,,A*54$GPRMC,121252.000,A,3958.3032,N,11629.6046,E,15.15,359.95,070306,,,A*54\r\n".encode('utf-8')
sl=g.Get_gps_data(sdata)
for e in sl:
    print(g.CheckGpsBuff(e))