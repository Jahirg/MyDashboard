#############################################################################################
# CREATOR:  ANJAL.P                                                                         #
# ON:       2020 NOV.                                                                       #
# AIM:      To Extend the capability of the PySide2 and PyQt5 Python library with easy to   #
#           use extension containing commonly used widgets which is not natively supported  #
#           by the Qt Frame work (or atleast for Python version of Qt).                     #
# VERSION:  v1.0.0                                                                          #
# NOTES:    CLASS : SpiralProgressBar : Can be accessed by : importing                      #
#           from PySide2extn.SpiralProgressBar import spiralProgressBar                     #
# REFER:    Github: https://github.com/anjalp/PySide2extn                                   #
#############################################################################################


from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import* 

class SpiralProgressBar(QWidget):

	def __init__(self, parent=None):
		super(SpiralProgressBar, self).__init__(parent)

		self.positionX = 0 
		self.positionY = 0
		self.spb_Size = 0
		self.posFactor = 0
		self.sizeFactor = 0

		self.spb_maximSize = (0, 0)
		self.spb_minimSize = (0, 0)

		self.spb_dynamicMin = True
		self.spb_dynamicMax = True

		self.noProgBar = 3

		self.spb_value = [-48*16, -24*16, -12*16]
		self.spb_minimValue = [0, 0, 0]
		self.spb_maximValue = [100, 100, 100]
		self.spb_startPos = [180*16, 180*16, 180*16]
		self.spb_direction = [-1, -1 , -1]

		self.lineWidth = 5
		self.lineColor = [[255, 128, 128], [128, 255, 128], [128, 180, 255]]   
		self.lineStyle = [Qt.SolidLine, Qt.SolidLine, Qt.SolidLine]
		self.lineCap = [Qt.RoundCap, Qt.RoundCap, Qt.RoundCap]
		self.varWidth = False
		self.widthIncr = 1
		
		self.pathWidth = 2
		self.pathColor = [[160, 160, 160], [160, 160, 160], [160, 160, 160]]
		self.pathPresent = False
		self.pathStyle = [Qt.SolidLine, Qt.SolidLine, Qt.SolidLine]
		self.pathIndepend = True

		self.spb_gap = self.lineWidth*1.5   #GAP BETWEEN THE ROUNDPROGRESS BAR MAKING A SPIRAL PROGRESS BAR.
		self.gapCngd = True
		self.spb_cngSize = 1

#------------------------------------------------------CLASS ENUMERATORS

	class lineCapFlags:
		SquareCap = Qt.SquareCap
		RoundCap = Qt.RoundCap


#------------------------------------------------------METHODS FOR CHANGING THE PROPERTY OF THE SPIRALPROGRESSBAR :SOLTS


	def spb_setValue(self, value):                                 #value: TUPLE OF (value1, value2, value3)
		"""
		Set the current value of the Progress Bar. maximum value >= Value >= minimum Value
		The user can set the value of each progress bar within the spiralprogressbar independely.
		The 'value' tuple element order corresponds to the outer to inner most progressbar.
		...
		Parameters
		--------------
		value : tuple
			Ex: value = xxx..spb_setValue ((34 , 56, 80)), this means value of outermost progress bar has the value of 0, 
			midden one to 50, and innermost to 22.
		"""

		if type(value)!=type(()):                                  #IF INPUT IS NOT A TUPLE
			raise Exception("Value should be a Tuple and not " + str(type(value)))
		elif len(value) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(value) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		elif self.spb_value!=value:                                #IF EVERY THING GOES RIGHT
			for each in range(0, self.noProgBar, 1):
				if value[each]!='nc':                           #nc: NOC CHANGE STRING FOR ELEIMINATING THE NO CHANGE PROGRESS VALUES
					if value[each] < self.spb_minimValue[each]:
						SpiralProgressBar.convValue(self, self.spb_minimValue[each], each)
					elif value[each] > self.spb_maximValue[each]:
						SpiralProgressBar.convValue(self, self.spb_maximValue[each], each)
					else:
						SpiralProgressBar.convValue(self, value[each], each)
			self.update()


	def spb_setInitialPos(self, position):
		"""
		Sets the statring point of the progress bar or the 0% position.
		Default is 'West'
		...
		Parameters
		--------------
		position : tuple
			The tuple elements accepts only string of : 'North', 'South', 'East' and 'West'.
			The order of arrangment matters i.e. the first element corresponds to the outer most concentric 
			progress bar and the last element correspinds to the innermost circle. 
			Ex : position = xxx.spb_setInitialPos(('North', 'South', 'East'))
		"""

		if type(position)!=type(()):                                  #IF INPUT IS NOT A TUPLE
			raise Exception("Position should be a Tuple and not " + str(type(position)))
		elif len(position) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(position) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		else:
			for each in range(0, self.noProgBar, 1):
				if type(position[each])!=type("string"):
					raise Exception("Position Tuple elements should be String and not: " + str(type(position[each])))
				elif position[each]=='North':
					self.spb_startPos[each] = 90*16
				elif position[each]=='South':
					self.spb_startPos[each] = -90*16
				elif position[each]=='East':
					self.spb_startPos[each] = 0*16
				elif position[each]=='West':
					self.spb_startPos[each] = 180*16
				else:
					raise Exception("Position can hold Property: 'North', 'South', 'East' and 'West' and not: " + position[each])
			self.update()

	def spb_setDirection(self, direction):
		"""
		Direction of rotation of the spiral progress bar.
		...
		Parameters
		--------------
		direction : tuple
			Direction that the round progress bar can hold are : 'Clockwise' and 'AntiClockwise'
			Default is 'Clockwise'. The tuple take string as elements corresponding to the direction of
			each of the concentric circles.
			Ex : ditection = xxxx.spb_setDirection(('AntiClockwise','AntiClockwise','AntiClockwise'))
		"""

		if type(direction)!=type(()):                                  #IF INPUT IS NOT A TUPLE
			raise Exception("Direction should be a Tuple and not " + str(type(direction)))
		elif len(direction) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(direction) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		else:
			for each in range(0, self.noProgBar, 1):
				if type(direction[each])!=type("String"):
					raise Exception("Direction Tuple elements should be String and not: " + str(type(direction[each])))
				elif direction[each]=='Clockwise':
					self.spb_direction[each] = -1
				elif direction[each]=='AntiClockwise':
					self.spb_direction[each] = 1
				else:
					raise Exception("Direction can hold Property: 'Clockwise'/'AntiClockwise' and not: " + str(type(direction[each])))
			self.update()




	def spb_lineColor(self, color):
		"""
		Color of line in the spiral progress bar. Each concentric progress bar has its own color settings. 
		...
		Parameters
		--------------
		color : tuple
			Color tuple corresponds to the color of each line which is a tuple of (R, G, B).
			Ex : color = xxxx.spb_lineColor((R, G, B), (R, G, B), (R, G, B))
			Elements of the color tuple is in correspondance with the order : outer to innermost circles in progress bar.
		"""

		if type(color)!=type(()):
			raise Exception("Color should be a Tuple and not " + str(type(Color)))
		elif type(color[0])!=type(()):
			raise Exception("Color should be in Format: ((R, G, B), (R, G, B), (R, G, B)) and not any other")
		elif len(color) > self.noProgBar:
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(color) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		else:
			for each in range(0, self.noProgBar, 1):
				if len(color[each])!=3:
					raise Exception('Color should be in format (R, G, B)')
				elif self.lineColor[each]!=color[each]:
					self.lineColor[each] = color[each]
			self.update()


	def spb_lineStyle(self, style):
		"""
		line style of the spiral progress bar.
		...
		Parameters
		--------------
		style : tuple
			Users can pass the style for each progress bar in the order : first element corresponds 
			to the styleof outermost progressbar and viceversa.
		Ex : lineStyle = xxxx.spb_lineStyle(('DashLine','DotLine','SolidLine'))
		"""

		if type(style)!=type(()):
			raise Exception("Style should be a tuple and not: " + str(type(style)))
		elif len(style) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(style) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		else:
			for each in range(0, self.noProgBar, 1):
				if type(style[each])!=type("String"):
					raise Exception("Style Tuple element should be a String and not: " + str(type(style[each])))
				elif style[each]=='SolidLine':
					self.lineStyle[each] = Qt.SolidLine
				elif style[each]=='DotLine':
					self.lineStyle[each] = Qt.DotLine
				elif style[each]=='DashLine':
					self.lineStyle[each] = Qt.DashLine
				else:
					raise Exception("Style can hold 'SolidLine', DotLine' and 'DashLine' only.")
			self.update()


	def spb_lineCap(self, cap):
		"""
		Cap i.e. the end of the line : to be Round or Square.
		...
		Parameters
		--------------
		cap : tuple
			Cap : 'RoundCap' and 'SquareCap'.
			Users can pass the desired cap of the line as a string passed in the following order of : 
			Outer progress bar : first element in the tuple and viceversa.
		Ex : lineCap = xxxx.spb_lineCap(('SquareCap','RoundCap','SquareCap'))
		"""
		
		if type(cap)!=type(()):
			raise Exception("Cap should be a tuple and not: " + str(type(cap)))
		elif len(cap) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(cap) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		else:
			for each in range(0, self.noProgBar, 1):
				if type(cap[each])!=type("String"):
					raise Exception('Cap Tuple element should be a String and not a: ' + str(type(cap[each])))
				elif cap[each]=='SquareCap':
					self.lineCap[each] = Qt.SquareCap
				elif cap[each]=='RoundCap':
					self.lineCap[each] = Qt.RoundCap
				else:
					raise Exception("Cap can hold 'SquareCap' and 'RoundCap' only")
			self.update()


	def spb_pathColor(self, color):
		"""
		Color of path in the spiral progress bar. Each concentric progress bar has its own color settings. 
		...
		Parameters
		--------------
		color : tuple
			Color tuple corresponds to the color of each path which is a tuple of (R, G, B).
			Ex : color = ((R, G, B), (R, G, B), (R, G, B))
			Elements of the color tuple is in correspondance with the order : outer to innermost circles in progress bar.
		"""

		if type(color)!=type(()):
			raise Exception("Color should be a Tuple and not " + str(type(Color)))
		elif type(color[0])!=type(()):
			raise Exception("Color should be in Format: ((R, G, B), (R, G, B), (R, G, B)) and not any other")
		elif len(color) > self.noProgBar:
			raise ValueError("Tuple length more than number of Progress Bars")
		elif len(color) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
			raise ValueError("Tuple length less than the number of Progress Bars")
		else:
			for each in range(0, self.noProgBar, 1):
				if len(color[each])!=3:
					raise Exception('Color should be in format (R, G, B)')
				elif self.pathColor[each]!=color[each]:
					self.pathColor[each] = color[each]
			self.update()


#------------------------------------------------------METHODS FOR GETTING THE PROPERTY OF SPIRALPROGRESSBAR SLOTS

#------------------------------------------------------ENGINE: WHERE ALL THE REAL STUFF TAKE PLACE: WORKING OF THE SPIRALPROGRESSBAR


	def spb_MinimumSize(self, dynMax, minim, maxim):
		"""
		Realtime automatic minimum size determiner for the spiral progress bar.
		For this to achieve the function first checks the size of the layout, where the spiralprogressbar lies.
		From that info the, it calculate the minimum size for the spiral progressbar so that all the circles in the spiral
		progress bar is clearly visible.
		"""

		spb_Height = self.height()
		spb_Width = self.width()

		if dynMax:
			if spb_Width >= spb_Height and spb_Height >= minim[1]:
				self.spb_Size = spb_Height
			elif spb_Width < spb_Height and spb_Width >= minim[0]:
				self.spb_Size = spb_Width
		else:
			if spb_Width >= spb_Height and spb_Height <= maxim[1]:
				self.spb_Size = spb_Height
			elif spb_Width < spb_Height and spb_Width <= maxim[0]:
				self.spb_Size = spb_Width


	def geometricFactor(self):
		"""
		Width of the line should be subrtracted from the size of the progrress bar, inorder to properly 
		fit inot the layout properly without any cut in the widget margins.
		"""
		self.posFactor = self.lineWidth/2 + 1
		self.sizeFactor = self.lineWidth + 1


	def convValue(self, value, pos):
		"""
		Convert the value from the user entered to the percentage depending on the maximum and minimum value.
		Calculagted by the relation : (value - minimum)/(maximum - minimum)
		"""

		self.spb_value[pos] = ((value - self.spb_minimValue[pos])/(self.spb_maximValue[pos] - self.spb_minimValue[pos]))*360*16
		self.spb_value[pos] = self.spb_direction[pos]*self.spb_value[pos]

########################################################################
### PAINT EVENT ############################
########################################################################

	def paintEvent(self, event: QPaintEvent):
		self.resize(self.width(),self.height())
		rect = QRect(0, 0, self.width(), self.height())

		#if self.spb_dynamicMin:
		#	self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

		SpiralProgressBar.spb_MinimumSize(self, self.spb_dynamicMax, self.spb_minimSize, self.spb_maximSize)
		SpiralProgressBar.geometricFactor(self)
		spiralIncrem = 0
		spiralIncrem2 = 0


		if self.pathIndepend!=True:
			self.pathWidth = self.lineWidth
		self.tempWidth = self.pathWidth
		if self.pathPresent:
			for path in range(0, self.noProgBar, 1):
				if self.varWidth==True:   #CREAETS A INCREASING OR DECREASING TYPE OF WITH 
					self.tempWidth = self.tempWidth + self.widthIncr
					if self.gapCngd!=True:
						self.spb_gap = self.tempWidth*2
				self.pathPainter = QPainter(self)
				self.pathPainter.setRenderHint(QPainter.Antialiasing)
				self.penPath = QPen()
				self.penPath.setStyle(self.pathStyle[path])
				self.penPath.setWidth(self.tempWidth)
				self.penPath.setBrush(QColor(self.pathColor[path][0], self.pathColor[path][1], self.pathColor[path][2]))
				self.pathPainter.setPen(self.penPath)
				self.pathPainter.drawArc(self.positionX + self.posFactor + self.spb_cngSize*spiralIncrem2, self.positionY + self.posFactor + self.spb_cngSize*spiralIncrem2, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem2, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem2, self.spb_startPos[path], 360*16)
				self.pathPainter.end()
				spiralIncrem2 = spiralIncrem2 + self.spb_gap
				

		self.tempWidth = self.lineWidth   #TEMPWIDTH TEMPORARLY STORES THE LINEWIDTH, USEFUL IN VARIABLE WIDTH OPTION.
		for bar in range(0, self.noProgBar, 1):
			if self.varWidth==True:   #CREAETS A INCREASING OR DECREASING TYPE OF WITH 
				self.tempWidth = self.tempWidth + self.widthIncr
				if self.gapCngd!=True:
					self.spb_gap = self.tempWidth*2
			self.linePainter = QPainter(self)
			self.linePainter.setRenderHint(QPainter.Antialiasing)
			self.penLine = QPen()
			self.penLine.setStyle(self.lineStyle[bar])
			self.penLine.setWidth(self.tempWidth)
			self.penLine.setCapStyle(self.lineCap[bar])
			self.penLine.setBrush(QColor(self.lineColor[bar][0], self.lineColor[bar][1], self.lineColor[bar][2]))
			self.linePainter.setPen(self.penLine)
			self.linePainter.drawArc(self.positionX + self.posFactor + self.spb_cngSize*spiralIncrem, self.positionY + self.posFactor + self.spb_cngSize*spiralIncrem, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem, self.spb_startPos[bar], self.spb_value[bar])
			self.linePainter.end()
			spiralIncrem = spiralIncrem + self.spb_gap

