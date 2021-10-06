########################################################################
# Basic Libraries
########################################################################
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_main import Ui_MainWindow

########################################################################
# CONTROL BOX CLASS
########################################################################
class TopUserInfo(QWidget):
	status = pyqtSignal(str)
	def __init__(self, parent): # ORIGINALE
		super().__init__()
		
		###### DEFAULT PARAMETERS#######################################
		self.width = 60 
		self.height = 60
		self.pos_x = 0
		self.pos_y = 0
		self.border_radius = 10
		self.parent = parent
		self.setGeometry(0, 0, self.width, self.height)
		self.setMinimumSize(self.width, self.height)
		self.image = "icons_svg/cil-locomotive.svg"
		self.color_active = "#b0ff00"
		self.width_popup = 130 
		self.height_popup = 230
		self.icon_settings = "icons_svg/icon_back_symbol.svg"
		self._status_color = "#b0ff00"
		self.color_background = "#404040"
		self.color_border_status = "#151617"
		
		gp = self.mapToGlobal(QPoint(0, 0))
		# SET WIDGET TO GET POSTION : Return absolute position of widget inside app
		pos = self.parent.mapFromGlobal(gp)
		print("gp", gp, "pos", pos, "parent", parent, )
		
		##### APP PATH #################################################
		app_path = os.path.abspath(os.getcwd())
		image_path = os.path.join(app_path, self.image)
		icon_settings_path = os.path.join(app_path, self.icon_settings)
		
		##### INITIAL SETUP ############################################
		#self.setObjectName("??")

		##### CUSTOM PARAMETERS ########################################
		self.user_name = "FQT-WER"
		self.user_status = "WORKS"
		self.user_image = image_path
		self.icon_settings = icon_settings_path

		##### DRAW BASE FRAME ########################################## 
		self.setup_ui()

		##### IMAGE FRAME EVENTS #######################################
		self.user_overlay.mousePressEvent = self.mouse_press
		self.user_overlay.enterEvent = self.mouse_enter
		self.user_overlay.leaveEvent = self.mouse_leave

		##### SETUP STATUS BOX  ########################################
		self.status_box = _ChangeStatus(parent,self.user_name,self.width_popup,self.height_popup)
		self.status_box.focusOutEvent = self.lost_focus_status_box
		self.status_box.line_edit.focusOutEvent = self.lost_focus_line_edit
		self.status_box.line_edit.keyReleaseEvent = self.change_description
		self.status_box.hide()
		self.status_box.status.connect(self.change_status)       
		
	####################################################################
	# CHANGE USER STATUS 
	####################################################################
	def change_status(self, status):
		# CHANGE STATUS
		if status == "WORKS":
			self._status_color = "#b0ff00"
			self.repaint()
		elif status == "E-FAULT":
			self._status_color = "#ffb000"
			self.repaint()
		elif status == "C-FAULT":
			self._status_color = "#00b0ff"
			self.repaint()
		elif status == "M-FAULT":
			self._status_color = "#ffff00"
			self.repaint()
		# EMIT SIGNAL
		self.status.emit(status)
		
	####################################################################
	# CHANGE TEXT DESCRIPTION
	####################################################################
	def change_description(self, event):        
		if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
			self.status_box.label_iniStatus.setText(self.status_box.line_edit.text())
			self.status_box.line_edit.setText("")
			self.status_box.hide()
	
	####################################################################
	# SHOw HIDE DIALOP POPUP
	####################################################################
	# HIDE LINE EDIT WHEN LOST FOCUS
	def lost_focus_status_box(self, event):
		if not self.status_box.line_edit.hasFocus():
			self.status_box.hide()
			self.status_box.line_edit.setText("")
	# HIDE WHEN LOST FOCUS
	def lost_focus_line_edit(self, event):
		if not self.status_box.hasFocus():
			self.status_box.hide()
			self.status_box.line_edit.setText("")
	
	####################################################################
	# OPEN STATUS BOX POPUP
	####################################################################
	def mouse_press(self, event):
		if self.status_box.isVisible():
			self.status_box.hide()
			self.status_box.line_edit.setText("")
		else:
			self.move_popup()
			self.status_box.show()
			self.status_box.line_edit.setFocus()
	
	####################################################################
	# SHOW ICON FOR SETTING
	####################################################################
	def mouse_enter(self, event):
		iconx = QPixmap(self.icon_settings)
		iconx = iconx.scaled(35, 35, Qt.KeepAspectRatio, Qt.FastTransformation)
		#self.blur_effect = QGraphicsBlurEffect()
		#self.blur_effect.setBlurRadius(3)
		#painter.setOpacity(1)
		self.user_overlay.setPixmap(iconx)
	
	####################################################################
	# HIDE ICON FOR SETTING
	####################################################################
	def mouse_leave(self, event):
		self.user_overlay.setPixmap(QPixmap(None))
	
	####################################################################
	# MOVE POP UP
	####################################################################
	def move_popup(self):
		# GET MAIN WINDOW PARENT
		gp = self.mapToGlobal(QPoint(0, 0))
		# SET WIDGET TO GET POSTION : Return absolute position of widget inside app
		pos = self.parent.mapFromGlobal(gp)
		# FORMAT POSITION: Adjust tooltip position with offset
		pos_x = pos.x() + 0
		pos_y = pos.y() + 50
		# SET POSITION TO WIDGET
		self.status_box.move(pos_x , pos_y)
	
	####################################################################
	# SET UP WIDGET
	####################################################################
	def setup_ui(self):
		# LAYOUT AND BORDER
		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0,0,0,0)
		self.border = QFrame(self)
		self.layout.addWidget(self.border)
		# FRAME IMAGE
		self.user_overlay = QLabel(self.border)
		self.user_overlay.setGeometry(0, 0, 40, 40)
		self.user_overlay.setCursor(QCursor(Qt.PointingHandCursor))
		self.user_overlay.setAlignment(Qt.AlignCenter)
		opacity = QGraphicsOpacityEffect(self)
		opacity.setOpacity(0.5)
		self.user_overlay.setGraphicsEffect(opacity)
	
	####################################################################
	# PAINT USER IMAGE EVENTS
	####################################################################
	def paintEvent(self, event):
		# PAINTER USER IMAGE
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)
		# RECT
		rect = QRect(0, 0, 40, 40)
		# CIRCLE BACKGROUND
		painter.setPen(Qt.NoPen)
		painter.setBrush(QBrush(QColor(self.color_background)))
		painter.drawRoundedRect(rect,10,10)
		# DRAW USER IMAGE
		self.draw_symbol(painter, self.user_image, rect)        
		# PAINT END
		painter.end()
		# DRAW USER IMAGE
		self.draw_status(self.user_image, rect)
	
	####################################################################
	# DRAW SYMBOL-ICON MACHINE
	####################################################################
	def draw_symbol(self, qp, image, rect):
		color = QColor(self.color_active)
		icon = QPixmap(image)
		icon = icon.scaled(35, 35, Qt.KeepAspectRatio, Qt.FastTransformation)
		painter = QPainter(icon)
		self.blur_effect = QGraphicsBlurEffect()
		self.blur_effect.setBlurRadius(3)
		painter.setOpacity(1)
		painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
		painter.fillRect(icon.rect(),color)
		qp.drawPixmap(
			(rect.width() - icon.width()) / 2, 
			(rect.height() - icon.height()) / 2,
			icon
		)       
		painter.end()
	
	####################################################################
	# DRAW STATUS
	####################################################################
	def draw_status(self, status, rect):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)
		# PEN
		pen = QPen()
		pen.setWidth(3)
		pen.setColor(QColor(self.color_border_status))
		painter.setPen(pen)
		# BRUSH/STATUS COLOR
		painter.setBrush(QBrush(QColor(self._status_color)))
		# DRAW
		painter.drawEllipse(rect.x() + 27, rect.y() + 27, 13, 13)
		painter.end()

########################################################################
# SET STYLE TO POPUP
########################################################################

style = """
/* QFrame */
QFrame {
    background: #333436; border-radius: 10px;
}
/* Search Message */
.QLineEdit {
	border: 2px solid rgb(47, 48, 50);
	border-radius: 15px;
	background-color: rgb(47, 48, 50);
	color: rgb(121, 121, 121);
	padding-left: 10px;
	padding-right: 10px;
}
.QLineEdit:hover {
	color: rgb(230, 230, 230);
	border: 2px solid rgb(62, 63, 66);
}
.QLineEdit:focus {
	color: rgb(230, 230, 230);
	border: 2px solid rgb(53, 54, 56);
	background-color: rgb(14, 14, 15);
}
/* QPushButton */
.QPushButton{
    background-color: transparent;
    border: none;
    border-radius: 10px;
    background-repeat: no-repeat;
    background-position: left center;
    text-align: left;
    color: #999999;
    padding-left: 38px;
}
.QPushButton:hover{
    background-color: #151617;
    color: #E0E0E0;
}
"""
########################################################################
# CHANGE  STATUS POPUP CLASS
########################################################################
class _ChangeStatus(QFrame):
	status = pyqtSignal(str)
	def __init__(self, parent,tag,width, height):
		self.tag = tag
		QFrame.__init__(self)
		
		##### SETUP ####################################################
		self.setFixedSize(width, height)
		self.setStyleSheet(style)
		self.setParent(parent)

		##### LAYOUT AND BORDER ########################################
		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(10,10,10,10)
		self.border = QFrame(self)
		self.layout.addWidget(self.border)

		##### LINEEDIT AND BTNS BOX ####################################
		self.layout_content = QVBoxLayout(self.border)
		self.layout_content.setContentsMargins(0,0,0,0)
		self.layout_content.setSpacing(1)

		##### CHANGE DESCRIPTION #######################################
		self.line_edit = QLineEdit()
		self.line_edit.setMinimumHeight(30)
		self.line_edit.setPlaceholderText("Insert Date")
		self.line_edit.setStyleSheet("color: #f0f0f0;")

		##### TOP LABEL ################################################
		self.label_tag = QLabel(self.tag)
		self.label_tag.setStyleSheet("padding-top: 5px; padding-bottom: 5px; color: #bdff00; font: 700 12pt 'Segoe UI';")
		self.label_iniStatus = QLabel("D/M/A")
		self.label_iniStatus.setStyleSheet("padding-top: 5px; padding-bottom: 5px; color: #e0e0e0; font: 700 12pt 'Segoe UI';")
		self.label = QLabel("Change status:")
		self.label.setStyleSheet("padding-top: 5px; padding-bottom: 5px; color: rgb(221, 221, 221);")
		
		##### BTN ONLINE ###############################################
		self.btn_online = QPushButton()
		self.btn_online.setText("Works OK")
		self.btn_online.setMinimumHeight(30)
		self.btn_online.setStyleSheet("background-image: url(icons_svg/icon_online.svg)")
		self.btn_online.clicked.connect(lambda: self.send_signal("WORKS"))
		self.btn_online.setCursor(Qt.PointingHandCursor)

		##### BTNL ELECTRICAL ##########################################
		self.btn_electrical = QPushButton()
		self.btn_electrical.setText("Electrical")
		self.btn_electrical.setMinimumHeight(30)
		self.btn_electrical.setStyleSheet("background-image: url(icons_svg/icon_ele.svg)")
		self.btn_electrical.clicked.connect(lambda: self.send_signal("E-FAULT"))
		self.btn_electrical.setCursor(Qt.PointingHandCursor)

		##### BTN CONTROL ##############################################
		self.btn_control = QPushButton()
		self.btn_control.setText("Control")
		self.btn_control.setMinimumHeight(30)
		self.btn_control.setStyleSheet("background-image: url(icons_svg/icon_con.svg)")
		self.btn_control.clicked.connect(lambda: self.send_signal("C-FAULT"))
		self.btn_control.setCursor(Qt.PointingHandCursor)

		##### BTN MECHANICAL ###########################################
		self.btn_mechanical = QPushButton()
		self.btn_mechanical.setText("Mechanical")
		self.btn_mechanical.setMinimumHeight(30)
		self.btn_mechanical.setStyleSheet("background-image: url(icons_svg/icon_mec.svg)")
		self.btn_mechanical.clicked.connect(lambda: self.send_signal("M-FAULT"))
		self.btn_mechanical.setCursor(Qt.PointingHandCursor)

		##### ADD WIDGETS TO LAYOUT ####################################
		self.layout_content.addWidget(self.label_tag)
		self.layout_content.addWidget(self.label_iniStatus)
		self.layout_content.addWidget(self.line_edit)
		self.layout_content.addWidget(self.label)
		self.layout_content.addWidget(self.btn_online)
		self.layout_content.addWidget(self.btn_electrical)
		self.layout_content.addWidget(self.btn_control)
		self.layout_content.addWidget(self.btn_mechanical)

		##### SET DROP SHADOW ##########################################
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 160))
		self.setGraphicsEffect(self.shadow)
	
	####################################################################
	# SEND SIGNAL TO TOP USER WIDGET
	####################################################################
	def send_signal(self, status):
		self.status.emit(status)
