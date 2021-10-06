########################################################################
# Widgest Special customs
########################################################################
from widgets.leftmenubuttons import LeftMenuButton
from widgets.top_bar_button_extra import *
from widgets.control_box import TopUserInfo


#from widgets.friend_message_button import *
#from widgets.top_user_box import * 
#from widgets.top_bar_button import *
#from widgets.top_bar_button_extra import *

########################################################################
# SETUP FOR QMAINWINDOW
########################################################################
class SetupBtnsMainWindow:
	def __init__(self):
		super().__init__()
		# SETUP MAIN WINDOw
		# Load widgets from "gui\ui_main.py"
		# ///////////////////////////////////////////////////////////////
		self.my_dash = UI_MainWindow()
		self.my_dash.setup_ui(self)
	
	####################################################################
	# AUTO LEFT TOP MENU BUTTONS 
	####################################################################
	def top_menu(self):
		add_left_top_btns = [
			{
				"custom_btn" : "btn_top_1",
				"btn_image" : "icons_svg/cil-touch-app.svg",
				"btn_description" : "SW Outputs",
				"is_active" : False
			},
			{
				"custom_btn" : "btn_top_2",
				"btn_image" : "icons_svg/cil-sun.svg",
				"btn_description" : " Digital Inputs",
				"is_active" : False
			},
			{
				"custom_btn" : "btn_top_3",
				"btn_image" : "icons_svg/cil-speedometer.svg",
				"btn_description" : "Gauges Analog In",
				"is_active" : False
			}
		]
		def add_left_top_menus(self, parameters):
			id = 0
			for parameter in parameters:
				custom_btn = parameter['custom_btn']
				btn_image = parameter['btn_image']
				btn_description = parameter['btn_description']
				is_active = parameter['is_active']

				self.menu_top = LeftMenuButton(id, custom_btn, btn_image, btn_description, is_active, self.parent) 
				self.menu_top.clicked.connect(self.btn_left_menu_clicked)
				self.menu_top.released.connect(self.btn_released)
				###### Se adiciona el widget al layout del frame
				self.my_dash.top_menus_layout.addWidget(self.menu_top)
				id += 1        

		add_left_top_menus(self, add_left_top_btns)
	
	####################################################################
	# AUTO LEFT BOTTOM MENU BUTTONS 
	####################################################################
	def bottom_menu(self):
		add_left_bottom_btns =[
			{
				"custom_btn" : "btn_down_1",
				"btn_image" : "icons_svg/cil-exposure.svg",
				"btn_description" : "PWM Outputs",
				"is_active" : False
			},
			{
				"custom_btn" : "btn_down_2",
				"btn_image" : "icons_svg/cil-chart-line.svg",
				"btn_description" : "Charts Data",
				"is_active" : False
			},
			{
				"custom_btn" : "btn_down_3",
				"btn_image" : "icons_svg/cil-burn.svg",
				"btn_description" : "Other Widgets",
				"is_active" : False
			}
		]
		def add_left_bottom_menus(self, parameters):
			id = 0
			for parameter in parameters:
				custom_btn = parameter['custom_btn']
				btn_image = parameter['btn_image']
				btn_description = parameter['btn_description']
				is_active = parameter['is_active']
				
				self.menu_bottom = LeftMenuButton(id, custom_btn, btn_image, btn_description, is_active, self.parent)
				self.menu_bottom.clicked.connect(self.btn_left_menu_clicked)
				self.menu_bottom.released.connect(self.btn_released)
				###### Se adiciona el widget al layout del frame
				self.my_dash.bottom_menus_layout.addWidget(self.menu_bottom)
				id += 1        
		
		add_left_bottom_menus(self, add_left_bottom_btns)
		
	####################################################################
	# ADD EXTRA TITLE BAR HIDE/SHOW MENUS
	####################################################################
	def bar_extra_btns (self):
		add_bar_extra_btns = [
			{
				"custom_btn" : "extra_btn_1",
				"btn_image" : "icons_svg/cil-sitemap.svg",
				"btn_description" : "Set_up COM",
				"is_active" : False,
				"parent" : None
			},
			{
				"custom_btn" : "extra_btn_2",
				"btn_image" : "icons_svg/cil-bug.svg",
				"btn_description" : "HELP",
				"is_active" : False,
				"parent" : None
			}
		]
		pass
		def add_bar_menus_extra(self, parameters):
			id = 0
			for parameter in parameters:
				custom_btn = parameter['custom_btn']
				btn_image = parameter['btn_image']
				btn_description = parameter['btn_description']
				is_active = parameter['is_active']

				self.menu_bar_extra = TopBarButtonExtra(id, custom_btn, btn_image, btn_description, is_active, self.parent) 
				self.menu_bar_extra.clicked.connect(self.btn_extra_clicked)
				self.menu_bar_extra.released.connect(self.btn_released)
				###### Se adiciona el widget al layout del frame
				self.my_dash.title_extra_btns_layout.addWidget(self.menu_bar_extra)
				id += 1        
		add_bar_menus_extra(self, add_bar_extra_btns)
	
	"""
	#################################################################	
	####################################################################
	# TOP USER BOX / Add widget to App 
	####################################################################
	def user_box(self):
		self.top_user= TopUserInfo(self.parent) 
		self.top_user.status.connect(self.status_change)
		self.my_dash.machine_layout.addWidget(self.top_user)
	
	####################################################################
	# AUTO ADD MESSAGE BTNS / FRIEND MENUS 
	####################################################################
	def friend_mesage(self):
		add_user = [
			{
				"user_image" : "images/users/cat.png",
				"user_name" : "Tom",
				"user_description" : "Did you see a mouse?",
				"user_status" : "online",
				"unread_messages" : 2,
				"is_active" : False
			},
			{
				"user_image" : "images/users/mouse.png",
				"user_name" : "Jerry",
				"user_description" : "I think I saw a cat...",
				"user_status" : "busy",
				"unread_messages" : 1,
				"is_active" : False
			},
			{
				"user_image" : "images/users/me.png",
				"user_name" : "Me From The Future",
				"user_description" : "Lottery result...",
				"user_status" : "invisible",
				"unread_messages" : 3,
				"is_active" : False
			}
		]
		def add_menus(self, parameters):
			id = 0
			for parameter in parameters:
				
				user_image = parameter['user_image']
				user_name = parameter['user_name']
				user_description = parameter['user_description']
				user_status = parameter['user_status']
				unread_messages = parameter['unread_messages']
				is_active = parameter['is_active']
				
				self.menu = FriendMessageButton(
					id, user_image, user_name, user_description, user_status, unread_messages, is_active
				)
				self.menu.clicked.connect(self.btn_clicked)
				self.menu.released.connect(self.btn_released)
				###### Se adiciona el widget al layout del frame
				self.my_dash.messages_layout.addWidget(self.menu)
				id += 1        
		
		add_menus(self, add_user)
	
	
	
	####################################################################
	# AUTO TITLE BAR MENU BUTTONS
	####################################################################
	def bar_btns(self):
		add_bar_btns = [
			{
				"custom_btn" : "custom_btn_bar_1",
				"btn_image" : "images/icons_svg/cil-functions.svg",
				"btn_description" : "Home",
				"is_active" : False,
				"parent" : None
			},
			{
				"custom_btn" : "custom_btn_bar_2",
				"btn_image" : "images/icons_svg/cil-beaker.svg",
				"btn_description" : "Chemical",
				"is_active" : False,
				"parent" : None
			},
			{
				"custom_btn" : "custom_btn_bar_3",
				"btn_image" : "images/icons_svg/cil-sitemap.svg",
				"btn_description" : "Site",
				"is_active" : False,
				"parent" : None
			}
		]
		def add_bar_menus(self, parameters):
			id = 0
			for parameter in parameters:
				custom_btn = parameter['custom_btn']
				btn_image = parameter['btn_image']
				btn_description = parameter['btn_description']
				is_active = parameter['is_active']

				self.menu_bar = TopBarButton(id, custom_btn, btn_image, btn_description, is_active, self.parent) 
				self.menu_bar.clicked.connect(self.btn_left_menu_clicked)
				self.menu_bar.released.connect(self.btn_released)
				###### Se adiciona el widget al layout del frame
				self.my_dash.title_btns_layout.addWidget(self.menu_bar)
				id += 1        
		add_bar_menus(self, add_bar_btns)
	"""
