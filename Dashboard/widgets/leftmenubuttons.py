########################################################################
# Basic Libraries
########################################################################
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


########################################################################
# Modules Auxiliary
########################################################################
from modules.appsettings import AppSettings
#import modules.uifunctions as UiFunctions


########################################################################
# CUSTOM LEFT MENU CLASS
########################################################################

class LeftMenuButton(QWidget):
	# SIGNALS ##########################################################
	clicked = pyqtSignal() 
	released = pyqtSignal()  

	def __init__(self, id, custom_btn, btn_image, btn_description, is_active, parent):
		super().__init__()
		# APP PATH #####################################################
		app_path = os.path.abspath(os.getcwd())
		icon_path = os.path.join(app_path, btn_image)

		# GET SETTINGS##################################################
		settings = AppSettings()
		self.settings = settings.items

		# DEFAULT PARAMETERS############################################
		self.width = 40	
		self.height = 40
		self.pos_x = 0
		self.pos_y = 0
		self.border_radius = 10
		self.parent = parent
		self.setGeometry(0, 0, self.width, self.height)
		self.setMinimumSize(self.width, self.height)
		self.setObjectName(custom_btn)
		
		# BG COLORS#####################################################
		self.color_default = QColor(self.settings["left_menu"]["color_idle"])
		self.color_hover = QColor(self.settings["left_menu"]["color_hover"])
		self.color_pressed = QColor(self.settings["left_menu"]["color_pressed"])
		self.color_actived = QColor(self.settings["left_menu"]["color_actived"])
		self._set_color = self.color_default

		# ICON #########################################################
		self.icon_color_default = QColor(self.settings["left_menu"]["icon_color_idle"])
		self.icon_color_hover = QColor(self.settings["left_menu"]["icon_color_hover"])
		self.icon_color_pressed = QColor(self.settings["left_menu"]["icon_color_pressed"])
		self.icon_color_actived = QColor(self.settings["left_menu"]["icon_color_actived"])
		self._set_icon_color = self.icon_color_default
		self._set_icon_path = icon_path        

		# TOOLTIP / LABEL StyleSheet ###################################
		tooltip_bg_color = self.settings["left_menu"]["tooltip_bg"]
		tooltip_boder_color = self.settings["left_menu"]["tooltip_border"]
		style_tooltip_basic = """ 
		QLabel {
			color: rgb(0, 255, 0);
			padding-left: 10px;
			padding-right: 10px;
			border-radius: 17px;
			border: 1px solid #2f3032;
			font: 800 9pt "Segoe UI";
		"""
		style_tooltip = style_tooltip_basic +"background-color:" + tooltip_bg_color+";" + " border-left: 3px solid " +tooltip_boder_color+"}"
		self.tooltip = _ToolTip(parent, btn_description, style_tooltip)
		self.tooltip.hide()
		
		# CONDITIONS  BUTTONS ##########################################
		self._is_active = is_active

	# RETURN IF IS ACTIVE MENU #########################################
	def set_active(self, active):
		self._is_active = active
		self._set_color = self.color_actived
		self._set_icon_color = self.icon_color_actived
		if not active:
			self._set_color = self.color_default
			self._set_icon_color = self.icon_color_default
		self.repaint()

	# PAINT EVENT ######################################################
	# Responsible for painting the button, as well as the icon
	def paintEvent(self, event):
		# PAINTER
		paint = QPainter()
		paint.begin(self)
		paint.setRenderHint(QPainter.RenderHint.Antialiasing)
		
		# BRUSH
		brush = QBrush(self._set_color)

		# CREATE RECTANGLE
		rect = QRect(0, 0, self.width, self.height)
		paint.setPen(Qt.NoPen)
		paint.setBrush(brush)
		paint.drawRoundedRect(rect, self.border_radius, self.border_radius)

		# DRAW ICONS
		self.icon_paint(paint, self._set_icon_path, rect, self._set_icon_color)

		# END PAINTER
		paint.end()

	# DRAW ICON WITH COLORS ############################################
	def icon_paint(self, qp, image, rect, color):
		icon = QPixmap(image)
		icon = icon.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation) # resize ICONS
		painter = QPainter(icon)
		
		self.blur_effect = QGraphicsBlurEffect()
		self.blur_effect.setBlurRadius(3)
		#painter.setOpacity(0.5)
		
		painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
		painter.fillRect(icon.rect(),color)
		qp.drawPixmap(
			(rect.width() - icon.width()) / 2, 
			(rect.height() - icon.height()) / 2,
			icon
		)       
		painter.end()

	# REPAINT BTN  #####################################################
	# Reaload/Repaint BTN
	def repaint_btn(self, event):
		if event == QEvent.Enter:            
			self.repaint()
		if event == QEvent.Leave:            
			self.repaint()
		if event == QEvent.MouseButtonPress:
			self.repaint()
		if event == QEvent.MouseButtonRelease:            
			self.repaint()

	# CHANGE STYLES ####################################################
	# Functions with custom styles
	def change_style(self, event):
		if event == QEvent.Enter:
			if not self._is_active:
				self._set_color = self.color_hover
				self._set_icon_color = self.icon_color_hover
			self.repaint_btn(event)          
		elif event == QEvent.Leave:
			if not self._is_active:
				self._set_color = self.color_default
				self._set_icon_color = self.icon_color_default
			self.repaint_btn(event)
		"""
		elif event == QEvent.MouseButtonPress:            
			if not self._is_active:
				self._set_color = self.color_pressed
				self._set_icon_color = self.icon_color_pressed
			self.repaint_btn(event)
 
		elif event == QEvent.MouseButtonRelease:
			if not self._is_active:
				self._set_color = self.color_hover
				self._set_icon_color = self.icon_color_actived
			self.repaint_btn(event)
		""" 

	# MOVE TOOLTIP #####################################################
	def move_tooltip(self):
		# GET MAIN WINDOW PARENT
		gp = self.mapToGlobal(QPoint(0, 0))

		# SET WIDGET TO GET POSTION
		# Return absolute position of widget inside app
		pos = self.parent.mapFromGlobal(gp)

		# FORMAT POSITION
		# Adjust tooltip position with offset
		pos_x = pos.x() + self.width + 12
		pos_y = pos.y() + (self.width - self.tooltip.height()) // 2

		# SET POSITION TO WIDGET
		# Move tooltip position
		self.tooltip.move(pos_x, pos_y)
	 

	# MOUSE OVER #######################################################
	# Event triggered when the mouse is over the BTN
	def enterEvent(self, event):
		self.change_style(QEvent.Enter)
		self.move_tooltip()  
		self.tooltip.show()

	# MOUSE LEAVE ######################################################
	# Event fired when the mouse leaves the BTN
	def leaveEvent(self, event):
		self.change_style(QEvent.Leave)
		self.move_tooltip() 
		self.tooltip.hide()

	# MOUSE PRESS ######################################################
	# Event triggered when the left button is pressed
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.change_style(QEvent.MouseButtonPress)
			# EMIT SIGNAL
			self.clicked.emit()
			# SET FOCUS
			self.setFocus()

	# MOUSE RELEASED ###################################################
	# Event triggered after the mouse button is released
	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.change_style(QEvent.MouseButtonRelease)
			# EMIT SIGNAL
			self.released.emit()

########################################################################
# CUSTOM TOOLTIP FOR LEFT MENU CLASS
########################################################################
class _ToolTip(QLabel):
	def __init__(self, parent, btn_description, style_tooltip):
		QLabel.__init__(self)
		self.setWindowFlag(Qt.FramelessWindowHint)

		# LABEL SETUP
		self.setObjectName(u"label_tooltip")
		self.setStyleSheet(style_tooltip)
		self.setMinimumHeight(36)
		self.setParent(parent)
		self.setText(btn_description)
		self.adjustSize()

		# SET DROP SHADOW
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 160))
		self.setGraphicsEffect(self.shadow)

		# SET OPACITY
		self.opacity = QGraphicsOpacityEffect(self)
		self.opacity.setOpacity(0.85)
		self.setGraphicsEffect(self.opacity)
