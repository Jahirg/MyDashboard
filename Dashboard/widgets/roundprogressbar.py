#############################################################################################
# CREATOR:  ANJAL.P                                                                         #
# ON:       2020 SEP.                                                                       #
# AIM:      To Extend the capability of the PySide2 and PyQt5 Python library with easy to   #
#           use extension containing commonly used widgets which is not natively supported  #
#           by the Qt Frame work (or atleast for Python version of Qt).                     #
# VERSION:  v1.0.0                                                                          #
# NOTES:    CLASS : RoundProgressBar : Can be accessed by : importing                       #
#           from PySide2extn.RoundProgressBar import roundProgressBar                       #
# REFER:    Github: https://github.com/anjalp/PySide2extn                                   #
#############################################################################################


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont


class RoundProgressBar(QtWidgets.QWidget):

	def __init__(self, parent=None):
		super(RoundProgressBar, self).__init__(parent)

		self.positionX = 0 
		self.positionY = 0
		self.posFactor = 0
		self.rpb_Size = 1

		self.rpb_minimumSize = (0, 0)
		self.rpb_maximumSize = (0, 0)
		self.rpb_dynamicMin = True
		self.rpb_dynamicMax = True
		self.sizeFactor = 0

		self.rpb_maximum = 100
		self.rpb_minimum = 0

		self.rpb_type = 0
		self.startPosition = 90*16 
		self.rpb_direction = -1

		self.rpb_textType = 0
		self.rpb_textColor = (0, 180, 255)
		self.rpb_textWidth = 1
		self.rpb_textFont = 'Segoe UI'
		self.rpb_textValue = '24%'
		self.rpb_textRatio = 8
		self.textFactorX = 0
		self.textFactorY = 0
		self.dynamicText = True
		self.rpb_textActive = True

		self.lineWidth = 15
		self.pathWidth = 2
		self.rpb_lineStyle = Qt.SolidLine
		self.rpb_lineCap = Qt.SquareCap
		self.lineColor = (0, 255, 64)
		self.pathColor = (218, 218, 218)

		self.rpb_circleColor = (255, 196, 0)
		self.rpb_circleRatio = 0.8
		self.rpb_circlePosX = 0
		self.rpb_circlePosY = 0

		self.rpb_pieColor = (255, 196, 0)
		self.rpb_pieRatio = 1
		self.rpb_piePosX = 0
		self.rpb_piePosY = 0

		self.rpb_value = 0

		if self.rpb_dynamicMin:
			self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

#------------------------------------------------------METHODS FOR CHANGING THE PROPERTY OF THE ROUNDPROGRESSBAR :SOLTS

	def rpb_setInitialPos(self, pos):
		if pos=='North':
			self.startPosition = 90*16 
		elif pos=='South':
			self.startPosition = -90*16
		elif pos=='East':
			self.startPosition = 0*16 
		elif pos=='West':
			self.startPosition = 180*16 
		else:
			raise Exception("Initial Position String can be: 'South', 'North'")
			return

	def rpb_setValue(self, value):
		
		if self.rpb_value != value:
			if value >= self.rpb_maximum:
				RoundProgressBar.convertInputValue(self, self.rpb_maximum)
			elif value < self.rpb_minimum:
				RoundProgressBar.convertInputValue(self, self.rpb_minimum)
			else:
				RoundProgressBar.convertInputValue(self, value)
			self.update()

	def rpb_setLineColor(self, rgb):
		if type(rgb)!=type(()):
			raise Exception("Line Color accepts a tuple: (R, G, B).")
			return
		if self.lineColor != rgb:
			self.lineColor = rgb
			self.update()

	def rpb_setPathColor(self, rgb):
		if type(rgb)!=type(()):
			raise Exception("Path Color accepts a tuple: (R, G, B).")
			return
		if self.pathColor != rgb:
			self.pathColor = rgb
			self.update()

	def rpb_setDirection(self, direction):
		if direction == 'Clockwise' or direction == -1:
			self.rpb_direction = -1
		elif direction == 'AntiClockwise' or direction == 1:
			self.rpb_direction = 1
		else:
			raise Exception("Direction can only be: 'Clockwise' and 'AntiClockwise' and Not: " + str(direction))
			return
		self.update()

	def rpb_setBarStyle(self, style):
		if style=='Donet':
			self.rpb_type = 0
		elif style=='Line':
			self.rpb_type = 1
		elif style=='Pie':
			self.rpb_type = 2
		elif style=='Pizza':
			self.rpb_type = 3
		elif style=='Hybrid1':
			self.rpb_type = 4
		elif style=='Hybrid2':
			self.rpb_type = 5
		else:
			raise Exception("Round Progress Bar has only the following styles: 'Line', 'Donet', 'Hybrid1', 'Pizza', 'Pie' and 'Hybrid2'")
			return
		self.update()

	def rpb_setLineStyle(self, style):
		if style == 'SolidLine':
			self.rpb_lineStyle = Qt.SolidLine
		elif style == 'DotLine':
			self.rpb_lineStyle = Qt.DotLine
		elif style == 'DashLine':
			self.rpb_lineStyle = Qt.DashLine
		else:
			self.rpb_lineStyle = Qt.SolidLine

	def rpb_setLineCap(self, cap):
		if cap=='SquareCap':
			self.rpb_lineCap = Qt.SquareCap
		elif cap == 'RoundCap':
			self.rpb_lineCap = Qt.RoundCap

	def rpb_setTextFormat(self, textTyp):
		if textTyp == 'Value':
			self.rpb_textType = 0 #self.textFlags.Value
		elif textTyp == 'Percentage':
			self.rpb_textType = 1 #self.textFlags.Percentage
		else:
			self.rpb_textType = 1 #self.textFlags.Percentage

	def rpb_setCircleColor(self, rgb):
		if self.rpb_circleColor != rgb:
			self.rpb_circleColor = rgb
			self.update()

	def rpb_setPieColor(self, rgb):
		if self.rpb_pieColor != rgb:
			self.rpb_pieColor = rgb
			self.update()




#ENGINE: WHERE ALL THE REAL STUFF TAKE PLACE: WORKING OF THE ROUNDPROGRESSBA

	def rpb_MinimumSize(self, dynamicMax, minimum, maximum):
		"""
		Minimum size calculating code: Takes consideration of the width of the line/path/circle/pie and the user defined
		width and also the size of the frame/window of the application.

		"""

		rpb_Height = self.height()
		rpb_Width = self.width()
		
		if dynamicMax:
			if rpb_Width >= rpb_Height and rpb_Height >= minimum[1]:
				self.rpb_Size = rpb_Height
			elif rpb_Width < rpb_Height and rpb_Width >= minimum[0]:
				self.rpb_Size = rpb_Width
		
		else:
			if rpb_Width >= rpb_Height and rpb_Height <= maximum[1]:
				self.rpb_Size = rpb_Height
			elif rpb_Width < rpb_Height and rpb_Width <= maximum[0]:
				self.rpb_Size = rpb_Width
		

	def convertInputValue(self, value):
		"""
		CONVERTS ANY INPUT VALUE TO THE 0*16-360*16 DEGREE REFERENCE OF THE QPainter.drawArc NEEDED.

		"""

		self.rpb_value = ((value - self.rpb_minimum)/(self.rpb_maximum - self.rpb_minimum))*360*16
		self.rpb_value = self.rpb_direction*self.rpb_value
		if self.rpb_textType==1 :
			self.rpb_textValue = str(round(((value - self.rpb_minimum)/(self.rpb_maximum - self.rpb_minimum))*100)) + "%"
		else:
			self.rpb_textValue = str(value)

	#SINCE THE THICKNESS OF THE LINE OR THE PATH CAUSES THE WIDGET TO WRONGLY FIT INSIDE THE SIZE OF THE WIDGET DESIGNED IN THE 
	#QTDESIGNER, THE CORRECTION FACTOR IS NECESSERY CALLED THE GEOMETRYFACTOR, WHICH CALCULATE THE TWO FACTORS CALLED THE
	#self.posFactor AND THE self.sizeFactor, CALCULATION THIS IS NECESSERY AS THE 
	def geometryFactor(self):
		if self.lineWidth > self.pathWidth:
			self.posFactor = self.lineWidth/2 + 1
			self.sizeFactor = self.lineWidth + 1
		else:
			self.posFactor = self.pathWidth/2 + 1
			self.sizeFactor = self.pathWidth + 1

	def rpb_textFactor(self):
		if self.dynamicText:
			self.rpb_textWidth = self.rpb_Size/self.rpb_textRatio
		self.textFactorX = self.posFactor + (self.rpb_Size - self.sizeFactor)/2 - self.rpb_textWidth*0.75*(len(self.rpb_textValue)/2)
		self.textFactorY = self.rpb_textWidth/2 + self.rpb_Size/2

	def rpb_circleFactor(self):
		self.rpb_circlePosX = self.positionX + self.posFactor +  ((self.rpb_Size)*(1 - self.rpb_circleRatio))/2
		self.rpb_circlePosY = self.positionY + self.posFactor + ((self.rpb_Size)*(1 - self.rpb_circleRatio))/2

	def rpb_pieFactor(self):
		self.rpb_piePosX = self.positionX + self.posFactor +  ((self.rpb_Size)*(1 - self.rpb_pieRatio))/2
		self.rpb_piePosY = self.positionY + self.posFactor + ((self.rpb_Size)*(1 - self.rpb_pieRatio))/2

########################################################################
## paint event #########################################################
########################################################################

	def paintEvent(self, event: QPaintEvent):
		self.resize(self.width(),self.height())
		rect = QRect(0, 0, self.width(), self.height())
		
		#THIS BELOW CODE AMKE SURE THAT THE SIZE OF THE ROUNDPROGRESSBAR DOESNOT REDUCES TO ZERO WHEN THE USER RESIZES THE WINDOW
		#if self.rpb_dynamicMin:
		#	self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

		RoundProgressBar.rpb_MinimumSize(self, self.rpb_dynamicMax, self.rpb_minimumSize, self.rpb_maximumSize)
		RoundProgressBar.geometryFactor(self)
		RoundProgressBar.rpb_textFactor(self)
		RoundProgressBar.rpb_circleFactor(self)
		RoundProgressBar.rpb_pieFactor(self)
		
		if self.rpb_type==0: #DONET TYPE
			RoundProgressBar.pathComponent(self)
			RoundProgressBar.lineComponent(self)
			RoundProgressBar.textComponent(self)
		elif self.rpb_type==1: #LINE TYPE
			RoundProgressBar.lineComponent(self)
			RoundProgressBar.textComponent(self)
		elif self.rpb_type==2: #Pie
			RoundProgressBar.pieComponent(self)
			RoundProgressBar.textComponent(self)
		elif self.rpb_type==3: #PIZZA
			RoundProgressBar.circleComponent(self)
			RoundProgressBar.lineComponent(self)
			RoundProgressBar.textComponent(self)
		elif self.rpb_type==4: #HYBRID1
			RoundProgressBar.circleComponent(self)
			RoundProgressBar.pathComponent(self)
			RoundProgressBar.lineComponent(self)
			RoundProgressBar.textComponent(self)
		elif self.rpb_type==5: #HYBRID2
			RoundProgressBar.pieComponent(self)
			RoundProgressBar.lineComponent(self)
			RoundProgressBar.textComponent(self)

		
	def lineComponent(self):
		linePainter = QPainter(self)
		linePainter.setRenderHint(QPainter.Antialiasing)
		penLine = QPen()
		penLine.setStyle(self.rpb_lineStyle)
		penLine.setWidth(self.lineWidth)
		penLine.setBrush(QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2]))
		penLine.setCapStyle(self.rpb_lineCap)
		penLine.setJoinStyle(Qt.RoundJoin)
		linePainter.setPen(penLine)
		linePainter.drawArc(self.positionX + self.posFactor, self.positionY + self.posFactor, self.rpb_Size - self.sizeFactor, self.rpb_Size - self.sizeFactor, self.startPosition, self.rpb_value)
		linePainter.end()

	def pathComponent(self):
		pathPainter = QPainter(self)
		pathPainter.setRenderHint(QPainter.Antialiasing)
		penPath = QPen()
		penPath.setStyle(Qt.SolidLine)
		penPath.setWidth(self.pathWidth)
		penPath.setBrush(QColor(self.pathColor[0], self.pathColor[1], self.pathColor[2]))
		penPath.setCapStyle(Qt.RoundCap)
		penPath.setJoinStyle(Qt.RoundJoin)
		pathPainter.setPen(penPath)
		pathPainter.drawArc(self.positionX + self.posFactor, self.positionY + self.posFactor, self.rpb_Size - self.sizeFactor, self.rpb_Size - self.sizeFactor, 0, 360*16)
		pathPainter.end()

	def textComponent(self):
		if self.rpb_textActive:
			textPainter = QPainter(self)
			penText = QPen()
			penText.setColor(QColor(self.rpb_textColor[0], self.rpb_textColor[1], self.rpb_textColor[2]))
			textPainter.setPen(penText)
			fontText = QFont()
			fontText.setFamily(self.rpb_textFont)
			fontText.setPointSize(self.rpb_textWidth)
			textPainter.setFont(fontText)
			textPainter.drawText(self.positionX + self.textFactorX, self.positionY + self.textFactorY, self.rpb_textValue)
			textPainter.end()

	def circleComponent(self):
		circlePainter = QPainter(self)   
		penCircle = QPen()
		penCircle.setWidth(0)
		penCircle.setColor(QColor(self.rpb_circleColor[0], self.rpb_circleColor[1], self.rpb_circleColor[2]))
		circlePainter.setRenderHint(QPainter.Antialiasing)
		circlePainter.setPen(penCircle)
		circlePainter.setBrush(QColor(self.rpb_circleColor[0], self.rpb_circleColor[1], self.rpb_circleColor[2]))
		circlePainter.drawEllipse(self.rpb_circlePosX, self.rpb_circlePosY, (self.rpb_Size - self.sizeFactor)*self.rpb_circleRatio, (self.rpb_Size - self.sizeFactor)*self.rpb_circleRatio)

	def pieComponent(self):
		piePainter = QPainter(self)   
		penPie = QPen()
		penPie.setWidth(0)
		penPie.setColor(QColor(self.rpb_pieColor[0], self.rpb_pieColor[1], self.rpb_pieColor[2]))
		piePainter.setRenderHint(QPainter.Antialiasing)
		piePainter.setPen(penPie)
		piePainter.setBrush(QColor(self.rpb_pieColor[0], self.rpb_pieColor[1], self.rpb_pieColor[2]))
		piePainter.drawPie(self.rpb_piePosX, self.rpb_piePosY, (self.rpb_Size - self.sizeFactor)*self.rpb_pieRatio, (self.rpb_Size - self.sizeFactor)*self.rpb_pieRatio, self.startPosition, self.rpb_value)

#######################################################################
## end paint event
#######################################################################

