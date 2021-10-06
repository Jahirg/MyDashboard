#!/usr/bin/python3

########################################################################
# Basic Libraries
########################################################################
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


########################################################################
# WIDGET - CLASS
########################################################################

class PyAnimatedToggle(QCheckBox):

	_transparent_pen = QPen(Qt.transparent)
	_light_grey_pen = QPen(Qt.lightGray)

	def __init__(self,parent=None,bar_color=Qt.gray,handle_color=Qt.white,):
		super().__init__(parent)

		#### Save our properties on the object via self, so we can access them later
		#### in the paintEvent.
		self.checked_color="#00B0FF"  
		self.pulse_unchecked_color="#44999999"
		self.pulse_checked_color="#4400B0EE" #pulse_checked_color
		
		self._bar_brush = QBrush(bar_color)
		self._handle_brush = QBrush(handle_color)

		#### Setup the rest of the widget.
		self.setContentsMargins(8, 0, 8, 0)
		self._handle_position = 0
		self._pulse_radius = 0

		self.animation = QPropertyAnimation(self, b"handle_position", self)
		self.animation.setEasingCurve(QEasingCurve.InOutCubic)
		self.animation.setDuration(400)  # time in ms

		self.pulse_anim = QPropertyAnimation(self, b"pulse_radius", self)
		self.pulse_anim.setDuration(400)  # time in ms
		self.pulse_anim.setStartValue(10)
		self.pulse_anim.setEndValue(20)

		self.animations_group = QSequentialAnimationGroup()
		self.animations_group.addAnimation(self.animation)
		self.animations_group.addAnimation(self.pulse_anim)

		self.stateChanged.connect(self.setup_animation)

	def sizeHint(self):
		return QSize(65, 45)

	def hitButton(self, pos: QPoint):
		return self.contentsRect().contains(pos)

	@pyqtSlot(int)
	def setup_animation(self, value):
		self.animations_group.stop()
		if value:
			self.animation.setEndValue(1)
		else:
			self.animation.setEndValue(0)
		self.animations_group.start()

	@pyqtProperty(float)
	def handle_position(self):
		return self._handle_position

	@handle_position.setter
	def handle_position(self, pos):
		"""change the property
		we need to trigger QWidget.update() method, either by:
			1- calling it here [ what we doing ].
			2- connecting the QPropertyAnimation.valueChanged() signal to it.
		"""
		self._handle_position = pos
		self.update()

	@pyqtProperty(float)
	def pulse_radius(self):
		return self._pulse_radius

	@pulse_radius.setter
	def pulse_radius(self, pos):
		self._pulse_radius = pos
		self.update()

	def paintEvent(self, e: QPaintEvent):

		contRect = self.contentsRect()
		handleRadius = round(0.24 * contRect.height())

		p = QPainter(self)
		p.setRenderHint(QPainter.Antialiasing)

		p.setPen(self._transparent_pen)
		barRect = QRectF(0, 0,contRect.width() - handleRadius, 0.25 * contRect.height())
		barRect.moveCenter(contRect.center())
		rounding = barRect.height() / 2

		# the handle will move along this line
		trailLength = contRect.width() - 2 * handleRadius

		xPos = contRect.x() + handleRadius + trailLength * self._handle_position

		if self.pulse_anim.state() == QPropertyAnimation.Running:
			p.setBrush(
				QBrush(QColor(self.pulse_checked_color)) if
				self.isChecked() else QBrush(QColor(self.pulse_unchecked_color)))
			p.drawEllipse(QPointF(xPos, barRect.center().y()),
						  self._pulse_radius, self._pulse_radius)

		if self.isChecked():
			p.setBrush(QBrush(QColor(self.checked_color).lighter()))
			p.drawRoundedRect(barRect, rounding, rounding)
			p.setBrush(QBrush(QColor(self.checked_color)))

		else:
			p.setBrush(self._bar_brush)
			p.drawRoundedRect(barRect, rounding, rounding)
			p.setPen(self._light_grey_pen)
			p.setBrush(self._handle_brush)

		p.drawEllipse(
			QPointF(xPos, barRect.center().y()),
			handleRadius, handleRadius)

		p.end()
