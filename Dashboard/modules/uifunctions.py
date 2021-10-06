
########################################################################
# Basic Libraries
########################################################################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

########################################################################
# Graphic interface
########################################################################
from ui_main import Ui_MainWindow


########################################################################
# Modules Auxiliary
########################################################################
from modules.appsettings import AppSettings


########################################################################
# UI FUNCTIONS CLASS
########################################################################


# GLOBAL VARS##########################################################
_is_maximized = False

class UiFunctions:
	def __init__(self):
		super(UiFunctions, self).__init__()
		# GET WIDGETS FROM "ui_main.py"
		# Load widgets inside App Functions
		self.my_dash = Ui_MainWindow()
		self.my_dash.setupUi(self)

	# SET UI DEFINITIONS################################################
	# Set ui definitions before "self.show()" in main.py
	def maximize_restore(self):
		global _is_maximized
		
		# CHANGE UI AND RESIZE GRIP ####################################
		def change_ui():
			if not _is_maximized:
				self.resize(self.width()+1, self.height()+1)
				self.my_dash.btn_restore.setIcon(QIcon("./icons_svg/cil-window-maximize.svg"))
				
			else:
				self.my_dash.btn_restore.setIcon(QIcon("./icons_svg/cil-window-restore.svg"))

		# CHECK EVENT###################################################
		if _is_maximized == False:
			_is_maximized = True
			self.setWindowState(Qt.WindowFullScreen)
			change_ui()
		else:
			_is_maximized = False
			self.setWindowState(Qt.WindowNoState)
			change_ui()
	
	# SET UI DEFINITIONS ###############################################
	# Set ui definitions before "self.show()" in main.py

	def set_ui_definitions(self):

		# GET SETTINGS FROM JSON DESERIALIZED ##########################
		settings = AppSettings()
		self.settings = settings.items

		# REMOVE TITLE BAR TO MAIN WINDOW ##############################
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		
		#screen = QDesktopWidget().screenGeometry()     
		#self.setGeometry(0, 0, 0.5*screen.width(), 0.5*screen.height())
		#self.setAttribute(Qt.WA_TranslucentBackground)
		#self.setWindowFlags(Qt.FramelessWindowHint| Qt.WindowSystemMenuHint| Qt.WindowMinimizeButtonHint)
		#self.setWindowState(Qt.WindowFullScreen)

		# MOVE WINDOW / MAXIMIZE / RESTORE #############################
		def moveWindow(event):
			
			############################################################
			# MODE RESTRICTED: DONT LET MOVE ON FULL SCREEN WINDOW #####
			############################################################
			global _is_maximized
			if _is_maximized == False:
				# MOVE WINDOW
				if event.buttons() == Qt.LeftButton:
					self.move(self.pos() + event.globalPos() - self.dragPos)
					self.dragPos = event.globalPos()
					event.accept()
			############################################################
			
			"""
			############################################################
			# MODE NORMAL: DEFAULT WINDOWS OS ##########################
			############################################################
			if self.isMaximized():
				UiFunctions.maximize_restore(self)
				curso_x = self.pos().x()
				curso_y = event.globalPos().y() - QCursor.pos().y()
				self.move(curso_x, curso_y)
			
			# MOVE WINDOW
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()
			############################################################
			"""
		self.my_dash.title_bar.mouseMoveEvent = moveWindow

		# DOUBLE CLICK MAXIMIZE / RESTORE ##############################
		def maximize_restore(event):
			if event.type() == QEvent.MouseButtonDblClick:
				UiFunctions.maximize_restore(self)
		self.my_dash.title_bar.mouseDoubleClickEvent = maximize_restore

		# TOP BTNS #####################################################
		self.my_dash.btn_minize.clicked.connect(lambda: self.showMinimized())        
		self.my_dash.btn_restore.clicked.connect(lambda: UiFunctions.maximize_restore(self))
		self.my_dash.btn_close.clicked.connect(lambda: self.close())
		
		# DEFAULT PARAMETERS ###########################################
		self.setWindowTitle(self.settings["app_name"])
		self.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
		self.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])
		
		#  RESIZE WINDOW ###############################################
		self.sizegrip = QSizeGrip(self.my_dash.frame_grip)
		#self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin: 28px; padding: 5px; background-color:#909090;")
		self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin: 28px; padding: 5px;")
	
	
	####################################################################
	# SELECT/DESELECT MENU
	####################################################################
	
	# SELECT MENU SELECTION (LEFT : TOP & BOTTOM ) #######################
	def select_Menu(self,widget):
		# FOR LEFT MENUS
		for w in self.my_dash.left_menu.findChildren(QWidget):
			if w.objectName() == widget:
				w.set_active(True)
		
	# RESET MENU SELECTION (LEFT : TOP & BOTTOM ) ########################
	def deselect_Menu(self, widget):
		# FOR LEFT MENUS
		for w in self.my_dash.left_menu.findChildren(QWidget):
			if w.objectName() != widget:
				if hasattr(w, 'set_active'):
					w.set_active(False)
					
	
	#####################################################################
	# TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
	def toggleRightBox(self, enable, widget):
		if enable:
			# GET WIDTH
			width = self.my_dash.extra_RightBox.width()
			maxExtend = 240
			standard = 0

			# SET MAX WIDTH #########################
			if width == 0:
				widthExtended = maxExtend
				for wx in self.my_dash.title_extra_btns.findChildren(QWidget):
					if wx.objectName() == widget:
						wx.set_active(True)
			else:
				widthExtended = standard
				for wx in self.my_dash.title_extra_btns.findChildren(QWidget):
					if wx.objectName() == widget:
						wx.set_active(False)

			# ANIMATION #############################
			self.animation = QPropertyAnimation(self.my_dash.extra_RightBox, b"minimumWidth")
			self.animation.setDuration(500)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.setEasingCurve(QEasingCurve.InOutQuart)
			self.animation.start()
	
	####################################################################
	# TOGGLE USER MESSAGE BOX
    # ///////////////////////////////////////////////////////////////
	def toggleLeftBox(self, enable, widget):
		if enable:
			# GET WIDTH
			width = self.my_dash.extra_LeftBox.width()
			maxExtend = 240
			standard = 0

			# SET MAX WIDTH ############################################
			if width == 0:
				widthExtended = maxExtend
				for wx in self.my_dash.title_extra_btns.findChildren(QWidget):
					if wx.objectName() == widget:
						wx.set_active(True)
			else:
				widthExtended = standard
				for wx in self.my_dash.title_extra_btns.findChildren(QWidget):
					if wx.objectName() == widget:
						wx.set_active(False)

			# ANIMATION #############################
			self.animation = QPropertyAnimation(self.my_dash.extra_LeftBox, b"minimumWidth")
			self.animation.setDuration(500)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.setEasingCurve(QEasingCurve.InOutQuart)
			self.animation.start()
