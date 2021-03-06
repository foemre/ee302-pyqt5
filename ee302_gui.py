#PyQT5 adaptation of EE302 Term Project software
#Emre Erdem (fo.emre@gmail.com)

#EE302 Term Project Graphical User Interface initialization code
#Written by BARKIN TUNCER (tuncer.barkin@gmail.com)
#Please send an email if you have any suggestions or find any bugs
#All rights are reserved

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import proje_gui
import numpy as np
import pyqtgraph as pg
import serial
import serial.tools.list_ports
import numpy
import os.path
import struct
import argparse
import time

parser = argparse.ArgumentParser(description='EE302 Term Project GUI. If you have any questions, suggestions or comments, feel free to send an email to tuncer.barkin@gmail.com.')
parser.add_argument('--port', help='The USB port which is connected to Arduino Board. Example: COM4 or /dev/tty0')
parser.add_argument('--window',type=int ,default = 100 ,help='Window length for plotting the data. Cannot be less than 10. Default = 100')
args = parser.parse_args()

ports = serial.tools.list_ports.comports()
default_port = [p[0] for p in ports if 'CH340' in p[1] or 'Arduino' in p[1]][0]
if args.port is not None:
	port = args.port
else:
	port = default_port

print("Your Arduino is in: " + str(default_port))

def splitInt(val):
    val1 = val*100
    valLeft = int(val1/100)
    valRight= int(val1%100)
    return (valLeft, valRight)
	
class ExampleApp(QtWidgets.QMainWindow, proje_gui.Ui_MainWindow):
    def __init__(self, arduino, parent=None):
        pg.setConfigOption('background', 'w') 
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Error.plotItem.showGrid(True, True, 0.7)
        self.Error.plotItem.setLabel('left','Error')
        self.Error.plotItem.setLabel('bottom','Time',units='s')
        self.ArmAngle.plotItem.showGrid(True, True, 0.7)
        self.ArmAngle.plotItem.setLabel('left','Motor Speed')
        self.ArmAngle.plotItem.setLabel('bottom','Time',units='s')
        self.MotorCommand.plotItem.showGrid(True, True, 0.7)
        self.MotorCommand.plotItem.setLabel('left','Motor Command (pwm)')
        self.MotorCommand.plotItem.setLabel('bottom','Time',units='s')
        self.arduino = arduino
        self.arduino.flushInput()
        self.timeA = [] # declare a list
        self.cnt = 0  
        self.c = len(os.listdir('csv/'))
        self.window_length = args.window
        self.tt = np.zeros(self.window_length)
        self.desired_sign = b'n'
        self.time_init = 0
        self.first = True
        self.begin = 0
        self.x=0
        self.errorArray = np.zeros(self.window_length)
        self.angleArray = np.zeros(self.window_length)
        self.motorArray = np.zeros(self.window_length)
        self.save_arr = np.array([[0,0,0,0]])
        self.saved = False

    def update(self):
        self.arduino_read(self.arduino)
        self.save_or_not()
        self.errorPlot()
        self.data_prep()
        QtCore.QTimer.singleShot(25, self.update ) 
    
    def data_prep(self):
        kp_left, kp_right = splitInt(self.Kp_spin.value())
        #kp_st = str(self.Kp_spin.value())
        #kp_st = kp_st.split('.')
        #kp_left = int(kp_st[0])
        #kp_right = int(kp_st[1])
        
        kd_left, kd_right = splitInt(self.Kd_spin.value())
        #Kd_st = str(self.Kd_spin.value())
        #Kd_st = Kd_st.split('.')
        #kd_left = int(Kd_st[0])
        #kd_right = int(Kd_st[1])
        
        ki_left, ki_right = splitInt(self.Ki_spin.value())
        #ki_st = str(self.Ki_spin.value())
        #ki_st = ki_st.split('.')
        #ki_left = int(ki_st[0])
        #ki_right = int(ki_st[1])
        
        desired_left, desired_right = splitInt(self.doubleSpinBox.value()+90)
        #desired_st = str(self.doubleSpinBox.value()+90) # desired
        #desired_st = desired_st.split('.')
        #desired_left = int(desired_st[0])
        #desired_right = int(desired_st[1])
        
        Direct_left, Direct_right = splitInt(self.DIrect_spin.value())
        #Direct_st = str(self.DIrect_spin.value())
        #Direct_st = Direct_st.split('.')
        #Direct_left = int(Direct_st[0])
        #Direct_right = int(Direct_st[1])
        
        sumMAX_left, sumMAX_right = splitInt(self.SumMAX_spin.value())
        #sumMAX_st = str(self.SumMAX_spin.value())
        #sumMAX_st = sumMAX_st.split('.')
        #sumMAX_left = int(sumMAX_st[0])
        #sumMAX_right = int(sumMAX_st[1])
		
        if proje_gui.Ui_MainWindow.enble_(self) == True:
            enable_pwm = 1
        else:
            enable_pwm = 0

        try:
            self.arduino.write(struct.pack('>13B',kp_left,kp_right,kd_left,kd_right,ki_left,
                                           ki_right,desired_left ,desired_right,Direct_left,Direct_right,
                                           sumMAX_left,sumMAX_right,enable_pwm))
        except:
            print(kp_left,kp_right,kd_left,kd_right,ki_left,
                                           ki_right,desired_left ,desired_right,Direct_left,Direct_right,
                                           sumMAX_left,sumMAX_right,enable_pwm)
    def arduino_read(self,arduino):
        arduinoString = arduino.readline() 
        A = arduinoString.decode().split(',') 
        while(numpy.size(A)==1 ):
            print("Please check if the serial monitor(Serial Port Ekranı) is open or not. If it is open, close it.")
            arduinoString = arduino.readline() 
            A = arduinoString.decode().split(',') 
        if self.first:
            self.first = False
            self.time_init = float(A[0])
        d = A[1]
        d2 = A[2]
        d3 = A[3]
        print(A)
        for k in range(self.window_length-1):
            self.tt[k] = self.tt[k+1]
            self.tt[k+1] = float(A[0])-self.time_init;
        for k in range(self.window_length-1):
            self.errorArray[k] = self.errorArray[k+1]
            self.errorArray[k+1] = d
        for k in range(self.window_length-1):
            self.angleArray[k] = self.angleArray[k+1]
            self.angleArray[k+1] = d2
        for k in range(self.window_length-1):
            self.motorArray[k] = self.motorArray[k+1]
            self.motorArray[k+1] = d3
        
        
    def errorPlot(self):
        self.errorArray = self.errorArray.astype(np.float)
        pen=pg.mkPen(color=(255,0,0),width=1)
        self.Error.plot(self.tt,self.errorArray ,pen=pen, clear=True)
        self.ArmAngle.plot(self.tt,self.angleArray ,pen=pen, clear=True)
        self.MotorCommand.plot(self.tt,self.motorArray ,pen=pen, clear=True)
            
    def save_or_not(self):
        if proje_gui.Ui_MainWindow.save_csv(self) == False and self.saved == False:
            pass
        elif proje_gui.Ui_MainWindow.save_csv(self) == True and self.saved == False:
            self.saved = True
            
        elif proje_gui.Ui_MainWindow.save_csv(self) == True and self.saved == True:
            self.save_arr = np.concatenate((self.save_arr, np.array([[self.tt[-1] ,self.errorArray[-1] ,self.angleArray[-1], self.motorArray[-1]]])), axis=0)
            
        elif proje_gui.Ui_MainWindow.save_csv(self) == False and self.saved == True:
            self.saved = False
            if os.path.isfile("csv/"+str(self.c)+".csv") :
                self.c = self.c + 1
                np.savetxt("csv/"+str(self.c)+".csv", self.save_arr, fmt='%5.4f',delimiter=",", header="Time,Error,MotorSpeed,MotorCommand")
            else:
                np.savetxt("csv/"+str(self.c)+".csv", self.save_arr, fmt='%5.4f', delimiter=",", header="Time,Error,MotorSpeed,MotorCommand")
                    
                
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    try:
        arduino = serial.Serial(port, 19200)
        if arduino.name not in [p[0] for p in ports if 'CH340' in p[1] or 'Arduino' in p[1]]:
        	raise serial.SerialException
    except serial.SerialException:
        print('Cannot find the arduino board. Probably the usb port entered is wrong(--port).')
    else:
        form = ExampleApp(arduino)
        form.show()
#        arduino.setDTR(False)
        # toss any data already received, see
        # http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
#        arduino.flushInput()
#        arduino.setDTR(True)        
        form.update()
        sys.exit(app.exec_())
        print("DONE")
