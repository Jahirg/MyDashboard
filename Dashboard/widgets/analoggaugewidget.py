#!/usr/bin/env python

########################################################################
# Author: Stefan Holstein
# inspired by: https://github.com/Werkov/PyQt4/blob/master/examples/widgets/analogclock.py
# Thanks to https://stackoverflow.com/
########################################################################

########################################################################
# Basic Libraries
########################################################################
import math
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

########################################################################
# WIDGET - CLASS
########################################################################

class AnalogGaugeWidget(QWidget):
	"""Fetches rows from a Bigtable.
	Args: 
		none
	"""
	valueChanged = pyqtSignal(int)  # with 130 line

	def __init__(self, parent=None):
		super(AnalogGaugeWidget, self).__init__(parent)
		self.setWindowTitle("Analog Gauge")
		
		self.NeedleColor = "#03BBCF"
		self.DisplayValueColor = "#03BBCF"
		self.ScaleValueColor = "#03BBCF"
		self.CenterPointColor = "#326432"
		self.BigMakerColor = "#03BBCF"
		self.FineMakerColor = "#03BBCF"
		self.BarColorSolid = "#00ffff"
		self.DisplayUnitsColor = "#CFcfcf"

		self.value_needle_count = 1
		#self.value_needle = QObject
		self.change_value_needle_style([QPolygon([
			QPoint(4, 4),
			QPoint(-4, 4),
			QPoint(-3, -120),
			QPoint(0, -126),
			QPoint(3, -120)
		])])

		self.value_min = 0
		self.value_max = 1000
		self.value = self.value_min
		self.value_offset = 0
		self.value_needle_snapzone = 0.05
		self.last_value = 0
		self.units = "Kw"

		self.gauge_color_outer_radius_factor = 0.55
		self.gauge_color_inner_radius_factor =0.45
		self.center_horizontal_value = 0
		self.center_vertical_value = 0
		self.debug1 = None
		self.debug2 = None
		self.scale_angle_start_value = 135
		self.scale_angle_size = 270
		self.angle_offset = 0

		self.scala_main_count = 10
		self.scala_subdiv_count = 5

		self.pen = QPen(QColor(255, 0, 255))
		self.font = QFont('Decorative', 20)

		self.scale_polygon_colors = [[.01, Qt.red],
									 [.1, Qt.yellow],
									 [.9, Qt.green],
									 [0.4, Qt.transparent]]
									 
		# initialize Scale value text
		self.enable_scale_text = True
		self.scale_fontname = "Decorative"
		self.initial_scale_fontsize = 18
		self.scale_fontsize = self.initial_scale_fontsize

		# initialize Main value text
		self.enable_value_text = True
		self.value_fontname = "Decorative"
		self.initial_value_fontsize = 40
		self.value_fontsize = self.initial_value_fontsize
		self.text_radius_factor = 0.7

		# En/disable scale / fill
		self.enable_barGraph = False
		self.enable_filled_Polygon = True
		self.enable_CenterPoint = False
		self.enable_fine_scaled_marker = True
		self.enable_big_scaled_marker = True
		self.needle_scale_factor = 0.75
		self.enable_Needle_Polygon = True
		
		# necessary for resize
		self.setMouseTracking(False)
		self.rescale_method()

	def rescale_method(self):
		# print("slotMethod")
		if self.width() <= self.height():
			self.widget_diameter = self.width()
		else:
			self.widget_diameter = self.height()
		"""
		self.change_value_needle_style([QPolygon([
			QPoint(4, -5),
			QPoint(-4, -5),
			QPoint(-2, - self.widget_diameter / 2 * self.needle_scale_factor),
			QPoint(-6, - self.widget_diameter / 2 * self.needle_scale_factor -6),
			QPoint(0, - self.widget_diameter / 2 * self.needle_scale_factor - 20),
			QPoint(6, - self.widget_diameter / 2 * self.needle_scale_factor -6),
			QPoint(2, - self.widget_diameter / 2 * self.needle_scale_factor)
		])])
		"""
		
		self.change_value_needle_style([QPolygon([
			QPoint(0, 6),
			QPoint(6, 0),
			QPoint(0, - self.widget_diameter / 3 * self.needle_scale_factor - 15),
			QPoint(-6, 0)
		])])
		
		
		self.scale_fontsize = self.initial_scale_fontsize * self.widget_diameter / 400
		self.value_fontsize = self.initial_value_fontsize * self.widget_diameter / 400
		pass

	def change_value_needle_style(self, design):
		# prepared for multiple needle instrument
		self.value_needle = []
		for i in design:
			self.value_needle.append(i)
		
	# NO SE SABE QUE HACEN

	def center_horizontal(self, value):
		self.center_horizontal_value = value
		# print("horizontal: " + str(self.center_horizontal_value))

	def center_vertical(self, value):
		self.center_vertical_value = value
		# print("vertical: " + str(self.center_vertical_value))

	####################################################################
	# Get Methods
	####################################################################

	def get_value_max(self,span):
		self.value_max = span
	
	def update_value(self, value):
		if (value == self.value):
			return
		if value <= self.value_min:
			self.value = self.value_min
		elif value >= self.value_max:
			self.value = self.value_max
		else:
			self.value = value
		
		#self.valueChanged.emit(int(value))
		self.update()
	
	####################################################################
	# Painter
	####################################################################

	def create_polygon_pie(self, outer_radius, inner_raduis, start, lenght):
		polygon_pie = QPolygonF()
		n = 360     # angle steps size for full circle
		# changing n value will causes drawing issues
		w = 360 / n   # angle per step
		# create outer circle line from "start"-angle to "start + lenght"-angle
		x = 0
		y = 0
		# todo enable/disable bar graf here
		if self.enable_barGraph==False:
			lenght = int(round((lenght / (self.value_max - self.value_min)) * (self.value - self.value_min)))
			pass

		for i in range(lenght+1):                                              # add the points of polygon
			t = w * i + start - self.angle_offset
			x = outer_radius * math.cos(math.radians(t))
			y = outer_radius * math.sin(math.radians(t))
			polygon_pie.append(QPointF(x, y))
		# create inner circle line from "start + lenght"-angle to "start"-angle
		for i in range(lenght+1):                                              # add the points of polygon
			t = w * (lenght - i) + start - self.angle_offset
			x = inner_raduis * math.cos(math.radians(t))
			y = inner_raduis * math.sin(math.radians(t))
			polygon_pie.append(QPointF(x, y))

		# close outer line
		polygon_pie.append(QPointF(x, y))
		return polygon_pie

	def draw_filled_polygon(self, outline_pen_with=0):
		if not self.scale_polygon_colors == None:
			painter_filled_polygon = QPainter(self)
			painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
			painter_filled_polygon.translate(self.width() / 2, self.height() / 2)
			painter_filled_polygon.setPen(Qt.NoPen)  ## Color border bar
			self.pen.setWidth(outline_pen_with)
			
			if outline_pen_with > 0:
				painter_filled_polygon.setPen(self.pen)

			colored_scale_polygon = self.create_polygon_pie(
				((self.widget_diameter / 2) - (self.pen.width() / 2)) * self.gauge_color_outer_radius_factor,
				(((self.widget_diameter / 2) - (self.pen.width() / 2)) * self.gauge_color_inner_radius_factor),
				self.scale_angle_start_value, self.scale_angle_size)

			gauge_rect = QRect(QPoint(0, 0), QSize(self.widget_diameter / 2 - 1, self.widget_diameter - 1))
			grad = QConicalGradient(QPointF(0, 0), - self.scale_angle_size - self.scale_angle_start_value +
									self.angle_offset - 1)

			# todo definition scale color as array here
			for eachcolor in self.scale_polygon_colors:
				grad.setColorAt(eachcolor[0], eachcolor[1])

			#painter_filled_polygon.setBrush(grad) ### color bar 
			painter_filled_polygon.setBrush(QColor(self.BarColorSolid)) ### color bar 
			painter_filled_polygon.drawPolygon(colored_scale_polygon)


	####################################################################
	# Scale Marker
	####################################################################

	def draw_big_scaled_markter(self):
		my_painter = QPainter(self)
		my_painter.setRenderHint(QPainter.Antialiasing)
		# Koordinatenursprung in die Mitte der Flaeche legen
		my_painter.translate(self.width() / 2, self.height() / 2)

		# my_painter.setPen(Qt.NoPen)
		#self.pen = QPen(QColor(0, 0, 0, 255))   #### color big makers
		self.pen.setWidth(3)
		# # if outline_pen_with > 0:
		my_painter.setPen(QPen(QColor(self.BigMakerColor)))

		my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
		steps_size = (float(self.scale_angle_size) / float(self.scala_main_count))
		scale_line_outer_start = self.widget_diameter/2.4
		scale_line_lenght = (self.widget_diameter / 2.4) - (self.widget_diameter / 10)
		# print(stepszize)
		for i in range(self.scala_main_count+1):
			my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
			my_painter.rotate(steps_size)

	def create_scale_marker_values_text(self):
		painter = QPainter(self)
		# painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setRenderHint(QPainter.Antialiasing)

		# Koordinatenursprung in die Mitte der Flaeche legen
		painter.translate(self.width() / 2, self.height() / 2)
		# painter.save()
		font = QFont(self.scale_fontname, self.scale_fontsize)
		fm = QFontMetrics(font)

		pen_shadow = QPen()

		pen_shadow.setBrush(QColor(self.ScaleValueColor))
		painter.setPen(pen_shadow)

		text_radius_factor = 0.95 ### 0.8
		text_radius = self.widget_diameter/2 * text_radius_factor

		scale_per_div = int((self.value_max - self.value_min) / self.scala_main_count)

		angle_distance = (float(self.scale_angle_size) / float(self.scala_main_count))
		for i in range(self.scala_main_count + 1):
			# text = str(int((self.value_max - self.value_min) / self.scala_main_count * i))
			text = str(int(self.value_min + scale_per_div * i))
			w = fm.width(text) + 1
			h = fm.height()
			painter.setFont(QFont(self.scale_fontname, self.scale_fontsize))
			angle = angle_distance * i + float(self.scale_angle_start_value - self.angle_offset)
			x = text_radius * math.cos(math.radians(angle))
			y = text_radius * math.sin(math.radians(angle))
			# print(w, h, x, y, text)
			text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
			painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])
		# painter.restore()

	def create_fine_scaled_marker(self):
		#  Description_dict = 0
		my_painter = QPainter(self)

		my_painter.setRenderHint(QPainter.Antialiasing)
		# Koordinatenursprung in die Mitte der Flaeche legen
		my_painter.translate(self.width() / 2, self.height() / 2)

		my_painter.setPen(QPen(QColor(self.FineMakerColor)))  ###############
		my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
		steps_size = (float(self.scale_angle_size) / float(self.scala_main_count * self.scala_subdiv_count))
		scale_line_outer_start = self.widget_diameter/2.7
		scale_line_lenght = (self.widget_diameter / 2.7) - (self.widget_diameter / 20)
		for i in range((self.scala_main_count * self.scala_subdiv_count)+1):
			my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
			my_painter.rotate(steps_size)

	def create_values_text(self):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(self.width() / 2, self.height() / 2)
		font = QFont(self.value_fontname, self.value_fontsize)
		fm = QFontMetrics(font)
		pen_shadow = QPen()
		pen_shadow.setBrush(QColor(self.DisplayValueColor))
		painter.setPen(pen_shadow)
		text_radius = self.widget_diameter / 4 * self.text_radius_factor
		text = str(int(self.value))
		w = fm.width(text) + 1
		h = fm.height()
		
		units_radius = self.widget_diameter / 2.2 * self.text_radius_factor
		units = self.units
		wu = fm.width(units) + 1
		hu = fm.height()
		
		painter.setFont(QFont(self.value_fontname, self.value_fontsize))
		angle_end = float(self.scale_angle_start_value + self.scale_angle_size - 360)
		angle = (angle_end - self.scale_angle_start_value) / 2 + self.scale_angle_start_value
		x = text_radius * math.cos(math.radians(angle))
		y = text_radius * math.sin(math.radians(angle))
		
		xu = units_radius * math.cos(math.radians(angle))
		yu = units_radius * math.sin(math.radians(angle))
		
		text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
		units = [xu - int(wu/2), yu - int(hu/2), int(wu), int(h), Qt.AlignCenter, units]
		painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])
		pen_shadow.setBrush(QColor(self.DisplayUnitsColor))
		painter.setPen(pen_shadow)
		painter.drawText(units[0], units[1], units[2], units[3], units[4], units[5])

	def draw_big_needle_center_point(self, diameter=30):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(self.width() / 2, self.height() / 2)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QColor(self.CenterPointColor))
		painter.drawEllipse(int(-diameter / 2), int(-diameter / 2), int(diameter), int(diameter))

	def draw_needle(self):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(self.width() / 2, self.height() / 2)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QColor(self.NeedleColor))
		painter.rotate(((self.value - self.value_offset - self.value_min) * self.scale_angle_size /
						(self.value_max - self.value_min)) + 90 + self.scale_angle_start_value)

		painter.drawConvexPolygon(self.value_needle[0])

	####################################################################
	# Events
	####################################################################

	def resizeEvent(self, event):
		self.rescale_method()
		pass

	def paintEvent(self, event):
		# colored pie area
		if self.enable_filled_Polygon:
			self.draw_filled_polygon()

		# draw scale marker lines
		if self.enable_fine_scaled_marker:
			self.create_fine_scaled_marker()
		if self.enable_big_scaled_marker:
			self.draw_big_scaled_markter()

		# draw scale marker value text
		if self.enable_scale_text:
			self.create_scale_marker_values_text()

		# Display Value
		if self.enable_value_text:
			self.create_values_text()

		# draw needle 1
		if self.enable_Needle_Polygon:
			self.draw_needle()

		# Draw Center Point
		if self.enable_CenterPoint:
			self.draw_big_needle_center_point(diameter=(self.widget_diameter / 6))

	####################################################################
	# MouseEvents
	####################################################################
	"""
	def setMouseTracking(self, flag):
		def recursive_set(parent):
			for child in parent.findChildren(QObject):
				try:
					child.setMouseTracking(flag)
				except:
					pass
				recursive_set(child)

		QWidget.setMouseTracking(self, flag)
		recursive_set(self)
	"""

