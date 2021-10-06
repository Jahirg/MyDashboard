'''
In this example, we create a custom 
Thermometer widget.

Original author: Tomasz Ziobrowski
Adopted by: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import*   
from PyQt5.QtGui import* 
from PyQt5.QtCore import* 
import sys 

OFFSET = 15
SCALE_HEIGHT = 224

class Termo(QWidget):
	def __init__(self, parent=None):
		super(Termo, self).__init__(parent)
		
		######## SET UP VALUES  ###########
		self.marks=5
		self.units=" °K"
		self.value = 50
		self.loAlarm = 10
		self.hiAlarm = 120
		self.value_min = -50
		self.value_max = 150
		
		#self.widthText = 6
		#self.heightText = 6
		
		self.colorBg = "transparent" # "transparent"
		self.colorHI = "#ff0000"
		self.colorLOW = "#0000ff"
		self.colorOK = "#20d020"
		self.colorTextmarks = "#32ff32"
		self.colorTickmarks = "#64ffae"
		self.colorValue = "#00a5ff"
		self.colorOutline = "#a5ff00"
		
		######## Enable/disable scale / fill
		self.enable_draw_Outline = True
		self.enable_draw_textmarks = True
		self.enable_draw_tickmarks = True
		self.enable_draw_Temperature= True
		self.enable_draw_ValueTexto = True
	
	def sizeHint(self):
		return QSize(100, 400)
	
	def update_value(self, value):
		
		if value <= self.value_min:
			self.value = self.value_min
		elif value >= self.value_max:
			self.value = self.value_max
		else:
			self.value = value
		 
		self.update()

	
	###################################
	def paintEvent(self, e):
		self.create_background()
		
		# draw outline thermometer
		if self.enable_draw_Outline:
			self.draw_Outline()
		
		# draw temperature bar
		if self.enable_draw_Temperature:
			self.draw_Temperature()
			
		if self.enable_draw_tickmarks:
			self.draw_tickmarks()
		
		# draw text marks
		if self.enable_draw_textmarks:
			self.draw_textmarks()
		
		if self.enable_draw_ValueTexto:
			self.draw_ValueTexto()
	#######################################
	
	def create_background(self):
		painter = QPainter(self)        
		painter.setPen(QColor(self.colorBg))
		painter.setBrush(QBrush(QColor(self.colorBg), Qt.SolidPattern))
		rect = QRect(0, 0, painter.device().width(), painter.device().height())
		painter.drawRoundedRect(rect,10,10) # Rounded corners 
		
		self.widthText = painter.device().width()
		
	def draw_Outline(self):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(painter.device().width()/3.0, 0)
		painter.scale((painter.device().height())/300, (painter.device().height())/300)
		path = QPainterPath()
		path.moveTo(-7.5, 257)
		path.quadTo(-12.5, 263, -12.5, 267.5)
		path.quadTo(-12.5, 278, 0, 280)
		path.quadTo(12.5, 278, 12.5, 267.5)
		path.moveTo(12.5, 267.5) 
		path.quadTo(12.5, 263, 7.5, 257) 
		
		path.lineTo(7.5, 25)
		path.quadTo(7.5, 12.5, 0, 12.5)
		path.quadTo(-7.5, 12.5, -7.5, 25)
		path.lineTo(-7.5, 257)
		
		p1 = QPointF(-2.0, 0)
		p2 = QPointF(12.5, 0)
		
		linearGrad = QLinearGradient(p1, p2)
		linearGrad.setSpread(QGradient.ReflectSpread)
		linearGrad.setColorAt(1, QColor(0, 150, 255, 170))
		linearGrad.setColorAt(0, QColor(255, 255, 255, 0))

		painter.setBrush(QBrush(linearGrad))
		painter.setPen(QColor(self.colorOutline))
		painter.drawPath(path)
		
	def draw_tickmarks(self):
		painter = QPainter(self)       
		painter.translate(painter.device().width()/3, 0)
		painter.scale((painter.device().height())/300, (painter.device().height())/300)
		pen = QPen()
		pen.setColor(QColor(self.colorTickmarks))  
		length = 50
		for i in range(33):
			pen.setWidthF(2.0)
			length = 12
			if i % 4:
				length = 8 
				pen.setWidthF(1.0)
			if i % 2:
				length = 5
				pen.setWidthF(0.6)
			painter.setPen(pen)
			painter.drawLine(-7, 28+i*7, -7+length, 28+i*7)
		
	def draw_textmarks(self):
		pen = QPen()          
		pen.setColor(QColor(self.colorTextmarks))
		painter = QPainter(self)        
		painter.setPen(pen)
		painter.translate(painter.device().width()/3, 0)
		painter.scale((painter.device().height())/300, (painter.device().height())/300)
		for i in range(9):    
			num = self.value_min + i*(self.value_max-self.value_min)/8
			val = str(int(num)) 
			#val = "{0}".format(num) ## decimals
			fm = painter.fontMetrics()
			size = fm.size(Qt.TextSingleLine, val)
			point = QPointF(OFFSET, 252-i*28+size.width()/4.0)
			font = QFont()        
			font.setFamily("Times")        
			#font.setBold(True)        
			#font.setPointSize(self.widthText /10)        
			painter.setFont(font)
			painter.drawText(point,val)
		
	def draw_Temperature(self):
		painter = QPainter(self)
		painter.translate(painter.device().width()/3, 0)
		painter.scale(painter.device().height()/300, painter.device().height()/300)

		if self.value >= self.hiAlarm:
			color = QColor(self.colorHI) 
		elif self.value <= self.loAlarm:
			color = QColor(self.colorLOW)
		else:
			color = QColor(self.colorOK)
			
		scale = QLinearGradient(0, 0, 5, 0)
		bulb = QRadialGradient(0, 267.0, 10, -5, 262)
		scale.setSpread(QGradient.ReflectSpread)
		bulb.setSpread(QGradient.ReflectSpread)
		color.setHsv(color.hue(), color.saturation(),color.value())
		scale.setColorAt(1, color)
		bulb.setColorAt(1, color)
		color.setHsv(color.hue(), color.saturation()-200, color.value())
		scale.setColorAt(0, color)
		bulb.setColorAt(0, color)
		
		pc = (self.value - self.value_min) / (self.value_max-self.value_min) 
		factor = self.value-self.value_min 
		factor = (factor/self.value_max)-self.value_min
		#temp = SCALE_HEIGHT * factor
		temp = SCALE_HEIGHT * pc
		height = temp + OFFSET # 224 from zero to span

		painter.setPen(Qt.NoPen)
		painter.setBrush(scale)
		painter.drawRect(-5, int(252+OFFSET-height), 10, int(height))
		painter.setBrush(bulb)
		rect = QRectF(-10, 258, 20, 20)
		painter.drawEllipse(rect)
	
	def draw_ValueTexto(self):
		pen = QPen()         
		pen.setColor(QColor(self.colorValue))
		painter = QPainter(self)        
		painter.setPen(pen)
		font = QFont()        
		font.setFamily("Times")        
		font.setBold(True)        
		font.setPointSize(int(4+painter.device().height()/50))        
		painter.setFont(font)
		val = str(round(self.value,1))+ self.units
		painter.drawText(0, int( 0.91*painter.device().height() ), painter.device().width(), 40, Qt.AlignCenter, val) # DECIMALES
	
	#########################################
	
