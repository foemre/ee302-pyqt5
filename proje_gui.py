# -*- coding: utf-8 -*-
#PyQT5 adaptation of EE302 Term Project software
#Emre Erdem (fo.emre@gmail.com)

#EE302 Term Project Graphical User Interface description code
#Written by BARKIN TUNCER (tuncer.barkin@gmail.com)
#Please send an email if you have any suggestions or find any bugs
#All rights are reserved

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.Error = PlotWidget(self.centralwidget)
        self.Error.setObjectName("Error")
        self.gridLayout.addWidget(self.Error, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.MotorCommand = PlotWidget(self.centralwidget)
        self.MotorCommand.setObjectName("MotorCommand")
        self.gridLayout.addWidget(self.MotorCommand, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        
        
   
        
        self.Desired_slider = QtWidgets.QSlider(self.centralwidget)
        self.Desired_slider.setMaximum(9000)
        self.Desired_slider.setMinimum(-9000)
        self.Desired_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Desired_slider.setObjectName("Desired_slider")
        
        
        
        
        self.Desired_slider.valueChanged.connect(self.valueHandler)
        
        
        
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setMaximum(90.00)
        self.doubleSpinBox.setMinimum(-90.00)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        
        
        
        
        self.doubleSpinBox.valueChanged.connect(self.valueHandler2)
        
        
        
        
        self.horizontalLayout_9.addWidget(self.doubleSpinBox)
        self.horizontalLayout_9.addWidget(self.Desired_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Kp_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Kp_spin.setMaximum(100.00)
        self.Kp_spin.setObjectName("Kp_spin")
        
        
        self.horizontalLayout.addWidget(self.Kp_spin)
        self.Kp_slider = QtWidgets.QSlider(self.centralwidget)
        self.Kp_slider.setMaximum(10000)
        self.Kp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Kp_slider.setObjectName("Kp_slider")
        
        self.Kp_spin.valueChanged.connect(self.valueHandler2_K_p)
        self.Kp_slider.valueChanged.connect(self.valueHandler_K_p)


        
        self.horizontalLayout.addWidget(self.Kp_slider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.Kd_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Kd_spin.setMaximum(100.00)
        self.Kd_spin.setObjectName("Kd_spin")
        self.horizontalLayout_5.addWidget(self.Kd_spin)
        self.Kd_slider = QtWidgets.QSlider(self.centralwidget)
        self.Kd_slider.setMaximum(10000)
        self.Kd_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Kd_slider.setObjectName("Kd_slider")
        
        self.Kd_spin.valueChanged.connect(self.valueHandler2_K_d)
        self.Kd_slider.valueChanged.connect(self.valueHandler_K_d)        
        
        
        self.horizontalLayout_5.addWidget(self.Kd_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.Ki_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Ki_spin.setMaximum(255.00)
        self.Ki_spin.setObjectName("Ki_spin")
        self.horizontalLayout_7.addWidget(self.Ki_spin)
        self.Ki_slider = QtWidgets.QSlider(self.centralwidget)
        self.Ki_slider.setMaximum(25500)
        self.Ki_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Ki_slider.setObjectName("Ki_slider")
        
        self.Ki_spin.valueChanged.connect(self.valueHandler2_K_i)
        self.Ki_slider.valueChanged.connect(self.valueHandler_K_i)           
        
        self.horizontalLayout_7.addWidget(self.Ki_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.DIrect_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.DIrect_spin.setMaximum(254.90)
        self.DIrect_spin.setObjectName("Direct_spin")
        self.horizontalLayout_6.addWidget(self.DIrect_spin)
        self.Direct_slider = QtWidgets.QSlider(self.centralwidget)
        self.Direct_slider.setMaximum(25490)
        self.Direct_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Direct_slider.setObjectName("Direct_slider")
        
        self.DIrect_spin.valueChanged.connect(self.valueHandler2_direct)
        self.Direct_slider.valueChanged.connect(self.valueHandler_direct)           
        
        self.horizontalLayout_6.addWidget(self.Direct_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.SumMAX_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SumMAX_spin.setMaximum(255.00)
        self.SumMAX_spin.setObjectName("SumMAX_spin")
        self.horizontalLayout_8.addWidget(self.SumMAX_spin)
        self.SumMAX_slider = QtWidgets.QSlider(self.centralwidget)
        self.SumMAX_slider.setMaximum(25500)
        self.SumMAX_slider.setOrientation(QtCore.Qt.Horizontal)
        self.SumMAX_slider.setObjectName("SumMAX_slider")
        
        self.SumMAX_spin.valueChanged.connect(self.valueHandler2_summax)
        self.SumMAX_slider.valueChanged.connect(self.valueHandler_summax)                
        
        self.horizontalLayout_8.addWidget(self.SumMAX_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout, 3, 2, 1, 1)
        self.ArmAngle = PlotWidget(self.centralwidget)
        self.ArmAngle.setObjectName("ArmAngle")
        self.gridLayout.addWidget(self.ArmAngle, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.save_csv_button = QtWidgets.QCheckBox(self.centralwidget)
        self.save_csv_button.setChecked(False)
        self.save_csv_button.setObjectName("save_csv_button")
        self.enble = QtWidgets.QCheckBox(self.centralwidget)
        self.enble.setChecked(True)
        self.enble.setObjectName("enble")
		
        self.horizontalLayout_10.addWidget(self.save_csv_button)
        self.horizontalLayout_10.addWidget(self.enble)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Kp_spin.setKeyboardTracking(False)
        self.Kd_spin.setKeyboardTracking(False)
        self.Ki_spin.setKeyboardTracking(False)
        self.DIrect_spin.setKeyboardTracking(False)
        self.SumMAX_spin.setKeyboardTracking(False)
        self.doubleSpinBox.setKeyboardTracking(False)

        self.retranslateUi(MainWindow)
        
        self.save_csv_button.toggled[bool].connect(MainWindow.save_csv)
        self.enble.toggled[bool].connect(MainWindow.enble_)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def enble_(self):
	    return self.enble.isChecked()
        
    def save_csv(self):
        return self.save_csv_button.isChecked()
    
    def valueHandler(self,value):    # slider değiştiğinde
        if(self.Desired_slider.isSliderDown()):
            scaledValue = float(value)/100.00    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
            #print (float(value)/100.00 , type(scaledValue)) 
            self.doubleSpinBox.setValue(scaledValue)   
#            print(self.doubleSpinBox.value())
            return scaledValue
        else:
            return value
        
    def valueHandler2(self,value):    #spinbox değiştiginde
        if(self.Desired_slider.isSliderDown()==False):
            scaledValue = 100.00*value    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
            #print (scaledValue/100.00 , value) 
            self.Desired_slider.setValue(scaledValue)
#            print(self.Desired_slider.value())
            return scaledValue
        else:
            return value
            
    def valueHandler_K_p(self,value):    # slider değiştiğinde
        if(self.Kp_slider.isSliderDown()):
            scaledValue = float(value)/100.00    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , type(scaledValue)) 
            self.Kp_spin.setValue(scaledValue)   
#            print(self.Kp_spin.value())
            return scaledValue
        else:
            return value
        
    def valueHandler2_K_p(self,value):    #spinbox değiştiginde
        if(self.Kp_slider.isSliderDown()==False):
            scaledValue = 100.00*value    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , value) 
            self.Kp_slider.setValue(scaledValue)
#            print(self.Kp_slider.value())
            return scaledValue
        else:
            return value
    def valueHandler_K_d(self,value):    # slider değiştiğinde
        if(self.Kd_slider.isSliderDown()):
            scaledValue = float(value)/100.00    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , type(scaledValue)) 
            self.Kd_spin.setValue(scaledValue)   
#            print(self.Kd_spin.value())
            return scaledValue
        else:
            return value
        
    def valueHandler2_K_d(self,value):    #spinbox değiştiginde
        if(self.Kd_slider.isSliderDown()==False):
            scaledValue = 100.00*value    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , value) 
            self.Kd_slider.setValue(scaledValue)
#            print(self.Kd_slider.value())
            return scaledValue
        else:
            return value
            
    def valueHandler_K_i(self,value):    # slider değiştiğinde
        if(self.Ki_slider.isSliderDown()):
            scaledValue = float(value)/100.00    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , type(scaledValue)) 
            self.Ki_spin.setValue(scaledValue)   
#            print(self.Ki_spin.value())
            return scaledValue
        else:
            return value
        
    def valueHandler2_K_i(self,value):    #spinbox değiştiginde
        if(self.Ki_slider.isSliderDown()==False):
            scaledValue = 100.00*value    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , value) 
            self.Ki_slider.setValue(scaledValue)
#            print(self.Ki_slider.value())
            return scaledValue
        else:
            return value
    def valueHandler_direct(self,value):    # slider değiştiğinde
        if(self.Direct_slider.isSliderDown()):
            scaledValue = float(value)/100.00    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , type(scaledValue)) 
            self.DIrect_spin.setValue(scaledValue)   
#            print(self.DIrect_spin.value())
            return scaledValue
        else:
            return value
        
    def valueHandler2_direct(self,value):    #spinbox değiştiginde
        if(self.Direct_slider.isSliderDown()==False):
            scaledValue = 100.00*value    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , value) 
            self.Direct_slider.setValue(scaledValue)
#            print(self.Direct_slider.value())
            return scaledValue
        else:
            return value
            
            
    def valueHandler_summax(self,value):    # slider değiştiğinde
        if(self.SumMAX_slider.isSliderDown()):
            scaledValue = float(value)/100.00    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , type(scaledValue)) 
            self.SumMAX_spin.setValue(scaledValue)   
#            print(self.SumMAX_spin.value())
            return scaledValue
        else:
            return value
        
    def valueHandler2_summax(self,value):    #spinbox değiştiginde
        if(self.SumMAX_slider.isSliderDown()==False):
            scaledValue = 100.00*value    #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
#            print (scaledValue , value) 
            self.SumMAX_slider.setValue(scaledValue)
#            print(self.SumMAX_slider.value())
            return scaledValue
        else:
            return value

        

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EE302 Bonus Project GUI v1.3 Part 1", None))
        self.label_9.setText(_translate("MainWindow", "Motor Command", None))
        self.label_7.setText(_translate("MainWindow", "Motor Speed", None))
        self.label_8.setText(_translate("MainWindow", "Error", None))
        self.label_10.setText(_translate("MainWindow", "Parameters", None))
        self.label_5.setText(_translate("MainWindow", "Desired", None))
        self.label.setText(_translate("MainWindow", "K_p", None))
        self.label_2.setText(_translate("MainWindow", "K_d", None))
        self.label_3.setText(_translate("MainWindow", "K_i", None))
        self.label_4.setText(_translate("MainWindow", "Direct", None))
        self.label_6.setText(_translate("MainWindow", "SumMAX", None))
        self.label_12.setText(_translate("MainWindow", "Please report any bugs to tuncer.barkin@gmail.com", None))
        self.label_11.setText(_translate("MainWindow", "METU EE 302 FEEDBACK SYSTEMS TERM PROJECT GUI", None))
        self.save_csv_button.setText(_translate("MainWindow", "Save CSV?", None))
        self.enble.setText(_translate("MainWindow", "Enable PWM?", None))


if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

