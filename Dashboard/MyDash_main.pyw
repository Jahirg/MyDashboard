#!/usr/bin/python3

########################################################################
# Basic Libraries
########################################################################
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

########################################################################
# Special Libraries
########################################################################
import serial.tools.list_ports
# pip install matplotlib
# pip install pip install PyQt5

########################################################################
# Graphic interface
########################################################################
from ui_main import Ui_MainWindow

########################################################################
# Modules Auxiliary : SET UP BUTTONS | PAGES | MENUS
########################################################################
from modules.uifunctions import UiFunctions
from modules.appsettings import AppSettings
from modules.setupbtnsmainwindow import SetupBtnsMainWindow

########################################################################
# Widgest Special customs
########################################################################
from widgets.leftmenubuttons import LeftMenuButton
from widgets.top_bar_button_extra import *

########################################################################
# Main Class
########################################################################
class MainWindow(QMainWindow):
	def __init__(self):
		self.app = QApplication(sys.argv)
		self.app.setWindowIcon(QIcon("chip.ico"))
		QMainWindow.__init__(self)
		self.my_dash = Ui_MainWindow()
		self.my_dash.setupUi(self)
		
		###### SET UI DEFINITIONS - MINIMIZE-MAXIMIZE-CLOSE OTHERS #####
		UiFunctions.set_ui_definitions(self)
		
		###### DEFINITION POINT PARENT FOR TOOL TIP ####################
		self.parent = self.my_dash.centralwidget
		
		###### INSERT LEFT MENU BUTTONS ON FRAMES ######################
		SetupBtnsMainWindow.top_menu(self)
		SetupBtnsMainWindow.bottom_menu(self)
		SetupBtnsMainWindow.bar_extra_btns(self)
		
		###### SET DEFAULT PAGE ########################################
		self.my_dash.app_pages.setCurrentWidget(self.my_dash.wellcome)
		
		###### Set-up : Widgets | Ports  | Special Fuctions ############
		self.getAvailablePorts()
		
		###### Init Timers: CLOCK  #####################################
		self.iniClock()
		self.show()
		sys.exit(self.app.exec_())
		
	####################################################################
	# TIMER UPDATE CLOCK 
	####################################################################
	def iniClock(self):
		self.timerClk = QTimer()
		self.timerClk.setInterval(1000)
		self.timerClk.timeout.connect(self.showTime)
		self.timerClk.start()
		
	def showTime(self):
		current_time = QTime.currentTime()
		time = current_time.toString('HH:mm:ss')
		self.my_dash.label_hora.setText(time)
		
		now = QDate.currentDate()
		date = now.toString(Qt.ISODate)
		self.my_dash.label_fecha.setText(date)
	
	####################################################################
	# GET BTN CLICKED LEFT MENU AND TOP MENU
	####################################################################
	def btn_left_menu_clicked(self):
		btn = self.sender()
		#print(F"Button {btn.objectName()}, Clicked!")
		
		# UNSELECT MENUS 
		UiFunctions.deselect_Menu(self, btn.objectName())
		
		if btn.objectName() == "btn_top_1":
			self.my_dash.app_pages.setCurrentWidget(self.my_dash.page_1)
			UiFunctions.select_Menu(self, btn.objectName())
			
		if btn.objectName() == "btn_top_2":
			self.my_dash.app_pages.setCurrentWidget(self.my_dash.page_2)
			UiFunctions.select_Menu(self, btn.objectName())
			
		if btn.objectName() == "btn_top_3":
			self.my_dash.app_pages.setCurrentWidget(self.my_dash.page_3)
			UiFunctions.select_Menu(self, btn.objectName())

		if btn.objectName() == "btn_down_1":
			self.my_dash.app_pages.setCurrentWidget(self.my_dash.page_4)
			UiFunctions.select_Menu(self, btn.objectName())
			
		if btn.objectName() == "btn_down_2":
			self.my_dash.app_pages.setCurrentWidget(self.my_dash.page_5)
			UiFunctions.select_Menu(self, btn.objectName())
			
		if btn.objectName() == "btn_down_3":
			self.my_dash.app_pages.setCurrentWidget(self.my_dash.page_6)
			UiFunctions.select_Menu(self, btn.objectName())
		
		self.my_dash.label_page.setText(btn.objectName())
	
	####################################################################
	# GET BTN CLICKED EXTRA BAR BUTTONS HIDE-SHOW
	####################################################################
	def btn_extra_clicked(self):
		# GET BT CLICKED
		btn = self.sender()
		#print (btn.objectName())
		
		if btn.objectName() == "extra_btn_1":
			UiFunctions.toggleLeftBox(self, True, btn.objectName())
		
		if btn.objectName() == "extra_btn_2":
			UiFunctions.toggleRightBox(self, True, btn.objectName())
	
	####################################################################
	# GET BTN RELEASED
	####################################################################
	def btn_released(self):
		# GET BT CLICKED
		btn = self.sender()
		#print(F"Button {btn.objectName()}, Released!")
	
	def status_change(self, status):
		print(f"send signal: {status}")
		print(status)
	
	####################################################################
	# MOUSE CLICK EVENTS
	####################################################################
	def mousePressEvent(self, event):
		# SET DRAG POS WINDOW
		self.dragPos = event.globalPos()
	
	####================================================================
	####=============== FOR ARDUINO APP CODE  ==========================
	####================================================================
	
	####################################################################
	# GET AVAILABLE SERIAL PORTS
	####################################################################
	def getAvailablePorts(self):
		ports = serial.tools.list_ports.comports(include_links=False)
		for port in ports :
			#print(port.device, port.manufacturer, port.description)
			
			# INSERT DATA FROM PORT IN LABELS ANS COMBOBOX #############
			self.label_port = QLabel()
			self.label_port.setStyleSheet("color:#f0f0f0; font: 10pt;")
			self.label_port.setText(str(port.device)+" "+str(port.manufacturer))
			self.my_dash.port_layout.addWidget(self.label_port)
			self.my_dash.comboBoxPort.addItem(port.device)
	
	####################################################################
	# SELECT PORT & START COMMUNICATION
	####################################################################
	@pyqtSlot()
	def on_buttonConnect_clicked(self):
		name = self.my_dash.comboBoxPort.currentText()
		if not name:
			QMessageBox.critical(self, 'Error', 'No serial port selected')
			return
		self.my_dash.label_idport.setText("ID PORT: "+name)
		self.initUART(name)
	
	def initUART(self,port):
		baudrate = 9600	
		try: 	
			self.ser = serial.Serial(
				port,
				baudrate,
				timeout=1,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS
			)
			if self.ser.is_open:
				self.setupWidgets()
				self.iniTemporizador()
		except :
			print("PUERTO SERIAL NO RESPONDE")
			#sys.exit(-1)
	
	####################################################################
	####### Setup Widgets - status switchs - sliders - graphics -
	####################################################################
	def setupWidgets(self):
		self.my_dash.showhide_1.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_1.set_image2("icons_svg/circle_yellow_1.svg")
		self.my_dash.showhide_2.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_2.set_image2("icons_svg/circle_yellow_1.svg")
		self.my_dash.showhide_3.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_3.set_image2("icons_svg/circle_blue_1.svg")
		self.my_dash.showhide_4.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_4.set_image2("icons_svg/circle_blue_1.svg")
		self.my_dash.showhide_5.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_5.set_image2("icons_svg/circle_green_1.svg")
		self.my_dash.showhide_6.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_6.set_image2("icons_svg/circle_green_1.svg")
		self.my_dash.showhide_7.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_7.set_image2("icons_svg/circle_red_1.svg")
		self.my_dash.showhide_8.set_image1("icons_svg/circle_black.svg")
		self.my_dash.showhide_8.set_image2("icons_svg/circle_red_1.svg")
		##### UNITS / COLORS  GAUGES
		self.my_dash.gauge_2.units ="rpm"
		self.my_dash.gauge_2.BarColorSolid = "#80ffff00"
		self.my_dash.gauge_3.units ="Amp"
		self.my_dash.gauge_3.BarColorSolid = "#b0ff0000"
		self.my_dash.gauge_4.units ="m/s"
		self.my_dash.gauge_4.BarColorSolid = "#8000ff00"
		##### COLORS  SWITCHS
		self.my_dash.pyswitch_3.onColor = "#bcff00"
		self.my_dash.pyswitch_4.onColor = "#bcff00"
		self.my_dash.pyanimated_3.checked_color="#ffB000"
		self.my_dash.pyanimated_4.checked_color="#ffB000"
		##### STORE STATUS FOR SWITCHS
		self.sw1=False
		self.sw2=False
		self.sw3=False
		self.sw4=False
		self.sw5=False
		self.sw6=False
		self.sw7=False
		self.sw8=False
		##### STORE STATUS FOR SLIDERS
		self.sld1=0
		self.sld2=0
		self.sld3=0
		self.sld4=0
		self.sld5=0
		self.sld6=0
		self.sld7=0
		self.sld8=0
		##### SET UP MATPLOTLIB GRAPHICS
		n_data = 50 # Number of samples
		self.xdata = list(range(n_data))
		self.y1data = [0 for i in range(n_data)]
		self.y2data = [0 for i in range(n_data)]
		self.y3data = [0 for i in range(n_data)]
		self.y4data = [0 for i in range(n_data)]
		##### SET UP PROGRESS BAR
		self.my_dash.roundprogressbar_1.rpb_type=4
		self.my_dash.roundprogressbar_1.rpb_setLineCap('RoundCap')
	
	####################################################################
	# TIMER SAMPLER 
	####################################################################
	def iniTemporizador(self):
		self.temporizador = QTimer()
		self.temporizador.timeout.connect(lambda:self.metMuestreo())
		self.temporizador.start(250)
	
	def metMuestreo(self):
		self.readData()
		self.writeData()
		self.writePwm()
		self.update_plot_1()
	
	####################################################################
	# SEND SERIAL DATA  FROM PYTHON TO (ARDUINO)
	####################################################################
	def setLed(self, led, value):
		dataled=str(led)+value
		#print("led ",led," value ",value)
		self.ser.write(dataled.encode())
	
	def setPwm(self, pin, value):
		datapinpwm =pin+value
		#print (datapinpwm)
		self.ser.write((pin+value).encode())
	
	####################################################################
	# WRITE : PUT HIGH/LOW  TO ARDIUNO PINS
	####################################################################
	def writeData(self):
		if self.sw1!=self.my_dash.pyswitch_1.isChecked():
			if self.my_dash.pyswitch_1.isChecked()==True:
				self.sw1=True
				self.setLed(22,'H')
			else:
				self.setLed(22,'L')
				self.sw1=False
		
		if self.sw2!=self.my_dash.pyswitch_2.isChecked():
			if self.my_dash.pyswitch_2.isChecked()==True:
				self.sw2=True
				self.setLed(23,'H')
			else:
				self.setLed(23,'L')
				self.sw2=False
		
		if self.sw3!=self.my_dash.pyswitch_3.isChecked():
			if self.my_dash.pyswitch_3.isChecked()==True:
				self.sw3=True
				self.setLed(24,'H')
			else:
				self.setLed(24,'L')
				self.sw3=False
		
		if self.sw4!=self.my_dash.pyswitch_4.isChecked():
			if self.my_dash.pyswitch_4.isChecked()==True:
				self.sw4=True
				self.setLed(25,'H')
			else:
				self.setLed(25,'L')
				self.sw4=False
		
		if self.sw5!=self.my_dash.pyanimated_1.isChecked():
			if self.my_dash.pyanimated_1.isChecked()==True:
				self.sw5=True
				self.setLed(26,'H')
			else:
				self.setLed(26,'L')
				self.sw5=False
		
		if self.sw6!=self.my_dash.pyanimated_2.isChecked():
			if self.my_dash.pyanimated_2.isChecked()==True:
				self.sw6=True
				self.setLed(27,'H')
			else:
				self.setLed(27,'L')
				self.sw6=False
		
		if self.sw7!=self.my_dash.pyanimated_3.isChecked():
			if self.my_dash.pyanimated_3.isChecked()==True:
				self.sw7=True
				self.setLed(28,'H')
			else:
				self.setLed(28,'L')
				self.sw7=False
				
		if self.sw8!=self.my_dash.pyanimated_4.isChecked():
			if self.my_dash.pyanimated_4.isChecked()==True:
				self.sw8=True
				self.setLed(29,'H')
			else:
				self.setLed(29,'L')
				self.sw8=False
	####################################################################
	# WRITE : PUT PWM TO ARDIUNO PINS PWM OUTPUT
	####################################################################
	def writePwm(self):
		if self.sld1!=self.my_dash.HSlider_1.value():
			self.sld1=self.my_dash.HSlider_1.value()
			self.setPwm( 'P04', str(self.sld1))
			self.my_dash.label_HS_1.setText(str(self.sld1))
		
		if self.sld2!=self.my_dash.HSlider_2.value():
			self.sld2=self.my_dash.HSlider_2.value()
			self.setPwm( 'P05', str(self.sld2))
			self.my_dash.label_HS_2.setText(str(self.sld2))
		
		if self.sld3!=self.my_dash.HSlider_3.value():
			self.sld3=self.my_dash.HSlider_3.value()
			self.setPwm( 'P06', str(self.sld3))
			self.my_dash.label_HS_3.setText(str(self.sld3))
		
		if self.sld4!=self.my_dash.HSlider_4.value():
			self.sld4=self.my_dash.HSlider_4.value()
			self.setPwm( 'P07', str(self.sld4))
			self.my_dash.label_HS_4.setText(str(self.sld4))
			
		if self.sld5!=self.my_dash.VSlider_1.value():
			self.sld5=self.my_dash.VSlider_1.value()
			self.setPwm( 'P08', str(self.sld5))
			self.my_dash.label_VS_1.setText(str(self.sld5))
			
		if self.sld6!=self.my_dash.VSlider_2.value():
			self.sld6=self.my_dash.VSlider_2.value()
			self.setPwm( 'P09', str(self.sld6))
			self.my_dash.label_VS_2.setText(str(self.sld6))
			
		if self.sld7!=self.my_dash.VSlider_3.value():
			self.sld7=self.my_dash.VSlider_3.value()
			self.setPwm( 'P10', str(self.sld7))
			self.my_dash.label_VS_3.setText(str(self.sld7))
			
		if self.sld8!=self.my_dash.VSlider_4.value():
			self.sld8=self.my_dash.VSlider_4.value()
			self.setPwm( 'P11', str(self.sld8))
			self.my_dash.label_VS_4.setText(str(self.sld8))

	####################################################################
	# READ DATA FROM ARDUINO, ANALOGS AIN  & DIGITALS IN.
	####################################################################
	def readData(self):
		data = self.ser.read(1)
		n = self.ser.inWaiting()
		while n:
			data = data + self.ser.read(n)
			n = self.ser.inWaiting()
			####### READ ANALOGS INPUTS ARDUINO
			st1=data[0]*256+data[1]
			st2=data[2]*256+data[3]
			st3=data[4]*256+data[5]
			st4=data[6]*256+data[7]
			st5=data[8]*256+data[9]
			st6=data[10]*256+data[11]
			st7=data[12]*256+data[13]
			st8=data[14]*256+data[15]
			#print (st1," ",st2," ",st3," ",st4)
			
			######## READ DIGIATL INPUTS ARDUINO
			Din1=data[16]*256+data[17]
			Din2=data[18]*256+data[19]
			Din3=data[20]*256+data[21]
			Din4=data[22]*256+data[23]
			Din5=data[24]*256+data[25]
			Din6=data[26]*256+data[27]
			Din7=data[28]*256+data[29]
			Din8=data[30]*256+data[31]
			#print (Pin6," ",Pin7," ",Pin8," ",Pin9)
			
			######## PUT VALUES TO GAUGES
			self.my_dash.gauge_1.update_value(st1)
			self.my_dash.gauge_2.update_value(st2)
			self.my_dash.gauge_3.update_value(st3)
			self.my_dash.gauge_4.update_value(st4)
			self.my_dash.termo_1.update_value((st5/5)-50)
			self.my_dash.verticalbar_1.update_value(st6/10)
			self.my_dash.roundprogressbar_1.rpb_setValue (st5/10)
			self.my_dash.spiralprogressbar_1.spb_setValue ((st5/10,st6/10,st1/10))
			
			######## PUT VALUES TO CHARTS
			self.y1data = self.y1data[1:] + [st1]
			self.y2data = self.y2data[1:] + [st2]
			self.y3data = self.y3data[1:] + [st3]
			self.y4data = self.y4data[1:] + [st4]
			
			######## PUT VALUES TO LIGHT INDICATORS
			if Din1==621:
				self.my_dash.showhide_1.fun(1)
			else:
				self.my_dash.showhide_1.fun(0)
			
			if Din2==631:
				self.my_dash.showhide_2.fun(1)
			else:
				self.my_dash.showhide_2.fun(0)
			
			if Din3==641:
				self.my_dash.showhide_3.fun(1)
			else:
				self.my_dash.showhide_3.fun(0)
			
			if Din4==651:
				self.my_dash.showhide_4.fun(1)
			else:
				self.my_dash.showhide_4.fun(0)
			
			if Din5==661:
				self.my_dash.showhide_5.fun(1)
			else:
				self.my_dash.showhide_5.fun(0)
			
			if Din6==671:
				self.my_dash.showhide_6.fun(1)
			else:
				self.my_dash.showhide_6.fun(0)
			
			if Din7==681:
				self.my_dash.showhide_7.fun(1)
			else:
				self.my_dash.showhide_7.fun(0)
			
			if Din8==691:
				self.my_dash.showhide_8.fun(1)
			else:
				self.my_dash.showhide_8.fun(0)
			
	####################################################################
	# PLOT ANALOGS IN  AIN0 TP AIN3
	####################################################################
	def update_plot_1(self):
		self.my_dash.matplot_1.canvas.ax.set_facecolor('#022040')
		self.my_dash.matplot_1.canvas.fig.patch.set_facecolor('#011020')
		self.my_dash.matplot_1.canvas.ax.cla()  # Clear the canvas.
		self.my_dash.matplot_1.canvas.ax.set_title('Values vs Time', color='0.8',fontsize='14')
		self.my_dash.matplot_1.canvas.ax.set_xlabel('Samples', color='#d0d0d0',fontsize='10')
		self.my_dash.matplot_1.canvas.ax.set_ylabel('Values', color='#d0d0d0',fontsize='10')
		self.my_dash.matplot_1.canvas.ax.set_ylim( ymin=0, ymax=1100)
		self.my_dash.matplot_1.canvas.ax.plot(self.xdata, self.y1data, label='AIN0',color='#ff0000')
		self.my_dash.matplot_1.canvas.ax.plot(self.xdata, self.y2data, label='AIN1',color='#ffb000')
		self.my_dash.matplot_1.canvas.ax.plot(self.xdata, self.y3data, label='AIN2',color='#00b000')
		self.my_dash.matplot_1.canvas.ax.plot(self.xdata, self.y4data, label='AIN3',color='#00b0ff')
		self.my_dash.matplot_1.canvas.ax.tick_params(axis='x', colors='#9AE300')
		self.my_dash.matplot_1.canvas.ax.tick_params(axis='y', colors='#9AE300')
		self.my_dash.matplot_1.canvas.ax.legend(loc='upper left', shadow=True, fontsize='8').get_frame().set_facecolor('#80b0b0')
		# Trigger the canvas to update and redraw.
		self.my_dash.matplot_1.canvas.fig.tight_layout()
		self.my_dash.matplot_1.canvas.draw()
		
########################################################################
# Run Routine
########################################################################

if __name__ == '__main__':
	MainWindow()
	
