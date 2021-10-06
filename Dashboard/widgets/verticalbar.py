from PyQt5.QtWidgets import * 
from PyQt5.QtGui import  * 
from PyQt5.QtCore import * 

class VerticalBar(QWidget):
	def __init__(self, parent=None):
		super(VerticalBar, self).__init__(parent)
		
		self.value_min = 0
		self.value_max = 100
		self.value = 50
		self.value_offset = 0
		self.marks = 10
		self.submarks = 5
		self.hiAlarm = 80
		self.loAlarm = 30
		
		self.BackgroundColor = "transparent"
		self.AxisColor = "#a0a0a0"
		self.TextoColor = "#a5ff00"
		self.LinePrimaryColor = "#a0a0a0"
		self.LineSecondaryColor = "#202020"
		self.ValueTextColor = "#00a5ff"
		self.BarColor = "transparent"
		self.BarColorLow = "#ffff00"
		self.BarColorOK = "#ff00ff00"
		self.BarColorHi = "#ff0000"
		self.TextoFontSize = 9
		self.padding = 12
		self.units = "°C"
		
		# En/disable scale / fill
		self.enable_AxisLine = True
		self.enable_LinePrimary = True
		self.enable_LineSecondary = True
		self.enable_ScaleTexto = True
		self.enable_ValueTexto = True
	
	#def sizeHint(self):
	#	return QtCore.QSize(180, 500)
		
	def update_value(self, value):
		
		if value <= self.value_min:
			self.value = self.value_min
		elif value >= self.value_max:
			self.value = self.value_max
		else:
			self.value = value
		
		if value >= self.hiAlarm: 
			self.BarColor = self.BarColorHi
		elif value <= self.loAlarm:
			self.BarColor = self.BarColorLow
		else:
			self.BarColor = self.BarColorOK
		 
		self.update()
	
	################################################################
	# Get Methods
	################################################################
	
	def get_value_max(self,span):
		self.value_max = span
	
	def get_value_min(self,zero):
		self.value_min = zero
		
	def get_hiAlarm(self,hialarm):
		self.hiAlarm = hialarm
		
	def get_loAlarm(self,loalarm):
		self.loAlarm = loalarm
		
	def get_marks(self,marks):
		self.marks = marks
		
	def get_submarks(self,submarks):
		self.submarks = submarks
		
	def get_BarColorOK(self,BarColorOK):
		self.BarColorOK = BarColorOK
	
	####################################################################
	# Events to draw in widget
	####################################################################
		
	def paintEvent(self, event):
		self.create_background()
		self.draw_Bar()
		
		if self.enable_AxisLine:
			self.draw_AxisLine()
		
		# draw scale marker lines
		if self.enable_LineSecondary:
			self.draw_LineSecondary()
		
		if self.enable_LinePrimary :
			self.draw_LinePrimary()
		
		# draw Scale texto
		if self.enable_ScaleTexto:
			self.create_ScaleTexto()
		
		# Display Value
		if self.enable_ValueTexto:
			self.create_ValueTexto()
		
	####################################################################
	# Painter draw de widget
	####################################################################
	def create_background(self):
		painter = QPainter(self)        
		brush = QBrush()         
		brush.setColor(QColor(self.BackgroundColor))        
		brush.setStyle(Qt.SolidPattern)        
		rect = QRect(0, 0, painter.device().width(), painter.device().height())        
		painter.fillRect(rect, brush)     

		self.pc = (self.value -self.value_min)/(self.value_max-self.value_min)
		d_xheight =  painter.device().height() - (self.padding * 2) 
		self.d_height=d_xheight*0.95       
		d_width = painter.device().width()- (self.padding *2 )
		self.d_width=d_width
	
	def draw_Bar(self):
		painter = QPainter(self)        
		brush = QBrush()
		brush.setColor(QColor(self.BarColor))
		brush.setStyle(Qt.SolidPattern)
		padding=self.padding
		d_width=self.d_width
		d_height=self.d_height
		pc = self.pc
		rect = QRect(
				5*padding,
				padding + d_height - int(pc*d_height),
				d_width,int(d_height*pc),
			) 
		painter.fillRect(rect, brush)
		
	def draw_AxisLine(self):
		pen = QPen()        
		pen.setWidth(4)        
		pen.setColor(QColor(self.AxisColor))
		painter = QPainter(self)        
		painter.setPen(pen)
		padding=self.padding
		d_width=self.d_width
		d_height=self.d_height     
		painter.drawLine(QPoint(padding*5, padding), QPoint(padding*5,d_height+padding))
		
	def draw_LineSecondary(self):
		pen = QPen()
		pen.setWidth(1)        
		pen.setColor(QColor(self.LineSecondaryColor))
		painter = QPainter(self)        
		painter.setPen(pen)
		markas=5*self.marks
		padding=self.padding
		d_width=self.d_width
		d_height=self.d_height
		for x in range(markas+1): 
			painter.drawLine(QPoint(padding*5, int(d_height*x/markas+padding)), QPoint(6*padding,int(d_height*x/markas+padding)))
		
	def draw_LinePrimary(self):
		pen = QPen() 
		pen.setWidth(2)        
		pen.setColor(QColor(self.LinePrimaryColor)) 
		painter = QPainter(self)        
		painter.setPen(pen) 
		marks=self.marks
		padding=self.padding
		d_width=self.d_width
		d_height=self.d_height
		for x in range(marks+1): 
			painter.drawLine(QPoint(padding*4, int(d_height*x/marks+padding)), QPoint(8*padding,int(d_height*x/marks+padding)))
		
	def create_ScaleTexto(self):
		pen = QPen()  
		pen.setWidth(1)        
		pen.setColor(QColor(self.TextoColor))
		painter = QPainter(self)        
		painter.setPen(pen)        
		font = QFont()        
		font.setFamily("Times")        
		font.setBold(True)        
		font.setPointSize(self.TextoFontSize)        
		painter.setFont(font)
		marks=self.marks
		padding=self.padding
		d_width=self.d_width
		d_height=self.d_height
		span= self.value_max
		zero= self.value_min
		for x in range(self.marks+1):  #text      
			#painter.drawText(1*padding, int(d_height*x/marks+0*padding), 30, 20, Qt.AlignRight,str(round(100-x*100/marks,1))) # ENTEROS
			painter.drawText(1*padding, int(d_height*x/marks+0*padding), 30, 20, Qt.AlignRight,str(int(span-x*(span-zero)/marks))) # ENTEROS
		
	def create_ValueTexto(self):
		pen = QPen()
		pen.setWidth(1)
		pen.setColor(QColor(self.ValueTextColor))
		painter = QPainter(self)
		painter.setPen(pen)        
		font = QFont()        
		font.setFamily("Times")        
		font.setBold(True)        
		font.setPointSize(11)        
		painter.setFont(font)
		padding=self.padding
		d_width=self.d_width
		d_height=self.d_height
		painter.drawText(2*padding, int(1.07*d_height), 60, 20, Qt.AlignRight, str(round(self.value,1))+self.units) # DECIMALES
