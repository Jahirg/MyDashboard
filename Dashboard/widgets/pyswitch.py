from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
#===============================================================================
# Personalized CheckBox as PySwitch
#===============================================================================
#className
class PySwitch(QCheckBox):
#|-----------------------------------------------------------------------------|
# class Variables
#|-----------------------------------------------------------------------------| 
# no classVariables
#|-----------------------------------------------------------------------------|
# Constructor  
#|-----------------------------------------------------------------------------|
	def __init__(self, *args, **kwargs):
			QCheckBox.__init__(self, *args, **kwargs)
 
			self.setChecked(False)
			self.setEnabled(True)
			#@self._enable = False
			self.onColor = "#00bcff"
			self.offColor ="#d0d0d0"
			self.onCircleColor ="#ffffff"
			self.offCircleColor ="#808080"
#|--------------------------End of Constructor---------------------------------| 
#|-----------------------------------------------------------------------------|
#   mousePressEvent
#|-----------------------------------------------------------------------------|
#overrite 
	def mousePressEvent(self, *args, **kwargs):
			#tick on and off set here
			if self.isChecked():
				self.setChecked(False)
			else:
				self.setChecked(True)
			#print(f"Status: {self.isChecked()}")
			return QCheckBox.mousePressEvent(self, *args, **kwargs)
#|--------------------------End of mousePressEvent-----------------------------| 

	def sizeHint(self):
		return QSize(50, 20)
	
	#def hitButton(self, pos: QPoint):
	#	return self.contentsRect().contains(pos)

#|-----------------------------------------------------------------------------| 
# paintEvent
#|-----------------------------------------------------------------------------|
	def paintEvent(self,event):
			# SETTINGS SIZE
			
			contRect = self.contentsRect()
			handleRadius = round(0.24 * contRect.height())

			self.resize(self.contentsRect().width(),self.contentsRect().height())
			painter = QPainter()
			pen = QPen()
			painter.begin(self)

			#FOR BACKGROUND
			brush = QBrush(QColor("transparent"),style=Qt.SolidPattern)
			painter.fillRect(self.rect(),brush)

			#SMOOTH CURVES
			painter.setRenderHint(QPainter.Antialiasing)

			#FOR ON /OFF FONT
			font  = QFont()
			font.setFamily("Times")
			font.setBold(True)
			font.setPixelSize(int(0.5*self.height()))
			painter.setFont(font)
			
			# SET AS NO PEN
			painter.setPen(Qt.NoPen)
			
			# DRAW RECTANGLE
			rect = QRect(0,0,self.width()-2,self.height()-2)        

			#LOOK FOR ON/OFF
			if self.isChecked():
				#RECATNGLE ON
				brush = QBrush(QColor(self.onColor),style=Qt.SolidPattern)
				painter.setBrush(brush)
				painter.drawRoundedRect(0,0,self.width()-2,self.height()-2, \
								   self.height()/2,self.height()/2)

				#CIRCLE ON 
				brush = QBrush(QColor(self.onCircleColor),style=Qt.SolidPattern)
				painter.setBrush(brush)
				painter.drawEllipse(self.width()-self.height(),int(0.15*self.height()),int(0.7*self.height()),int(0.7*self.height()))

				#TEXT ON
				pen.setColor(QColor("black"))        
				painter.setPen(pen)
				painter.drawText(int(0.1*(self.width()-self.height())),int(self.height()/1.5), "ON")

			else:
				# RECTANGLE OFF
				brush = QBrush(QColor(self.offColor),style=Qt.SolidPattern)
				painter.setBrush(brush)
				painter.drawRoundedRect(0,0,self.width()-2,self.height()-2, \
								   self.height()/2,self.height()/2)

				#CIRCLE OFF
				brush = QBrush(QColor(self.offCircleColor),style=Qt.SolidPattern)
				painter.setBrush(brush)
				painter.drawEllipse(int(0.1*(self.width()-self.height())),int(0.15*self.height()),int(0.7*self.height()),int(0.7*self.height()))

				# TEXT  OFF    
				pen.setColor(QColor("gray"))        
				painter.setPen(pen) 
				painter.drawText(int(self.width()-self.height()-0.35*self.height()),int(self.height()/1.5), "OFF")

