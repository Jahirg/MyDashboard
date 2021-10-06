import sys
from random import choice, randint

from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5 import QtSvg

class ShowHideWidgetSVG(QWidget):
	"""Fetches rows from a Bigtable.
	Args: 
		none
	"""
	def __init__(self, parent=None):
		super(ShowHideWidgetSVG, self).__init__(parent)
		self.rule= True
		self.img1=""
		self.img2=""
		self.resize(self.width(),self.height())
		self.pic = QLabel(self)
		self.top_logo= QtSvg.QSvgWidget(self)
		#self.top_logo.load("./images/circle_yellow_1.svg") # LOAD FILE
		#self.top_logo.setFixedSize(180,180)
		self.show()
	
	################################################################
	# Get Methods
	################################################################
	# please DONT FORGET define images in main Class.
	
	def set_image1(self,img1):
		self.img1 = img1
		self.top_logo.load(self.img1)
		self.top_logo.setFixedSize(self.width(), self.height())
		self.show()
	
	def set_image2(self,img2):
		self.img2= img2
	
	################################################################
	
	def fun(self, state):
		Image1=self.img1
		Image2=self.img2
		#print(self.width(),self.height() )
		if (Image1=="" or Image2==""):
			print ("Images are not defined")
			print ("example:")
			print ('   self.my_dash.widget.set_image1("./images/mute.svg")    ')
			print ('   self.my_dash.widget.set_image1("./images/mute.svg")    ')
		else:
			if state==True:
				self.top_logo.load(self.img2)
				self.top_logo.setFixedSize(self.width(), self.height())
				
			if state==False:
				self.top_logo.load(self.img1)
				self.top_logo.setFixedSize(self.width(), self.height())
			self.show()
			self.update()
			
			
			"""
			if self.rule==True:
				self.pic.setPixmap(QPixmap(Image2).scaled(self.w_img2, self.h_img2, Qt.KeepAspectRatio, Qt.FastTransformation))
				self.rule=False
			else:
				self.pic.setPixmap(QPixmap(self.img1).scaled(self.w_img1, self.h_img1, Qt.KeepAspectRatio, Qt.FastTransformation))
				self.rule=True
			self.update()
			"""
