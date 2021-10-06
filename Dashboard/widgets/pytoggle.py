from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PyToggle(QCheckBox):
	def __init__(self, *args, **kwargs):
		QCheckBox.__init__(self, *args, **kwargs)
		self.setCursor(Qt.PointingHandCursor)

		self.bg_color = "#c0c0c0"
		self.circle_color = "#99ffffff"
		self.circle_color_x = "#ff0000ff"
		self.active_color = "#00b0ff"

		self._circle_position = 0
		self.animation = QPropertyAnimation(self, b"circle_position")
		self.animation.setEasingCurve(QEasingCurve.OutBounce)
		self.animation.setDuration(500)

		self.stateChanged.connect(self.debstar_transitionug)
	
	def sizeHint(self):
		return QSize(65, 45)
	
	#def hitButton(self, pos: QPoint):
	#	return self.contentsRect().contains(pos)
	
	def paintEvent(self, e):
		
		contRect = self.contentsRect()
		handleRadius = round(0.24 * contRect.height())
		self.setMinimumHeight(contRect.height())
		self.setMinimumWidth(contRect.width())


		self.resize(contRect.width(),contRect.height())
		p = QPainter(self)
		p.setRenderHint(QPainter.Antialiasing)
		p.setPen(Qt.NoPen)
		
		barRect = QRectF(0, 0, contRect.width() - handleRadius, 0.40 * contRect.height())
		barRect.moveCenter(contRect.center())
		rounding = barRect.height() / 2
		trailLength = contRect.width() - 2 * handleRadius
		xPos = 1*handleRadius + (trailLength-handleRadius) * self._circle_position

		rect = QRect(0, 0, self.width(), self.height())
		
		if not self.isChecked():
			p.setBrush(QColor(self.bg_color))
			p.drawRoundedRect(barRect, rounding, rounding)
			p.setBrush(QColor(self.circle_color))
			
			p.drawEllipse(xPos, barRect.center().y()-handleRadius/2, handleRadius, handleRadius)
			
		else:
			p.setBrush(QColor(self.active_color))
			p.drawRoundedRect(barRect, rounding, rounding)
			p.setBrush(QColor(self.circle_color_x))
			
			p.drawEllipse(xPos, barRect.center().y()-handleRadius/2, handleRadius, handleRadius)

		
	@pyqtProperty(float)
	def circle_position(self):
		return self._circle_position
		
	@circle_position.setter
	def circle_position(self, pos):
		self._circle_position = pos
		self.update()

	def debstar_transitionug(self, value):
		self.animation.stop()
		if value:
			self.animation.setEndValue(1)

		else:
			self.animation.setEndValue(0)

		self.animation.start()

	def hitButton(self, pos = QPoint):
		return self.contentsRect().contains(pos)

