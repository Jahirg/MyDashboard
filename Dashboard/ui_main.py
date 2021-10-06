# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainHtkRuC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widgets.pyswitch import PySwitch
from widgets.pyanimatedtoggle import PyAnimatedToggle
from widgets.clases_mpl_pyqt import MatplotlibWidget11_sin
from widgets.showhidewidgetsvg import ShowHideWidgetSVG
from widgets.analoggaugewidget import AnalogGaugeWidget
from widgets.termo import Termo
from widgets.verticalbar import VerticalBar
from widgets.roundprogressbar import RoundProgressBar
from widgets.spiralprogressbar import SpiralProgressBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 776)
        MainWindow.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 10px;")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(48, 64, 80);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.left_menu = QFrame(self.frame)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(44, 40))
        self.left_menu.setMaximumSize(QSize(40, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(32, 48, 64);")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.top_log = QFrame(self.left_menu)
        self.top_log.setObjectName(u"top_log")
        self.top_log.setMinimumSize(QSize(40, 40))
        self.top_log.setMaximumSize(QSize(40, 40))
        self.top_log.setFrameShape(QFrame.StyledPanel)
        self.top_log.setFrameShadow(QFrame.Raised)
        self.top_logo_layout = QHBoxLayout(self.top_log)
        self.top_logo_layout.setSpacing(5)
        self.top_logo_layout.setObjectName(u"top_logo_layout")
        self.top_logo_layout.setContentsMargins(5, 5, 5, 5)
        self.btn_menuCom = QPushButton(self.top_log)
        self.btn_menuCom.setObjectName(u"btn_menuCom")
        self.btn_menuCom.setStyleSheet(u"background-color: rgb(170, 170, 170);\n"
"border-radius: 3px;")
        icon = QIcon()
        icon.addFile(u"icons_svg/cil-hamburger-menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menuCom.setIcon(icon)
        self.btn_menuCom.setIconSize(QSize(32, 32))

        self.top_logo_layout.addWidget(self.btn_menuCom)


        self.verticalLayout.addWidget(self.top_log)

        self.top_menus = QFrame(self.left_menu)
        self.top_menus.setObjectName(u"top_menus")
        self.top_menus.setMinimumSize(QSize(40, 40))
        self.top_menus.setMaximumSize(QSize(40, 16536))
        self.top_menus.setFrameShape(QFrame.StyledPanel)
        self.top_menus.setFrameShadow(QFrame.Raised)
        self.top_menus_layout = QVBoxLayout(self.top_menus)
        self.top_menus_layout.setSpacing(5)
        self.top_menus_layout.setObjectName(u"top_menus_layout")
        self.top_menus_layout.setContentsMargins(0, 5, 0, 5)

        self.verticalLayout.addWidget(self.top_menus)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.bottom_menus = QFrame(self.left_menu)
        self.bottom_menus.setObjectName(u"bottom_menus")
        self.bottom_menus.setMinimumSize(QSize(40, 40))
        self.bottom_menus.setMaximumSize(QSize(40, 16535))
        self.bottom_menus.setFrameShape(QFrame.StyledPanel)
        self.bottom_menus.setFrameShadow(QFrame.Raised)
        self.bottom_menus_layout = QVBoxLayout(self.bottom_menus)
        self.bottom_menus_layout.setSpacing(5)
        self.bottom_menus_layout.setObjectName(u"bottom_menus_layout")
        self.bottom_menus_layout.setContentsMargins(0, 5, 0, 5)

        self.verticalLayout.addWidget(self.bottom_menus)


        self.horizontalLayout_3.addWidget(self.left_menu)

        self.frame_body = QFrame(self.frame)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"border-radius: 0px;")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.frame_body)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"background-color: rgb(32, 48, 64);")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.frame_icontitle = QFrame(self.title_bar)
        self.frame_icontitle.setObjectName(u"frame_icontitle")
        self.frame_icontitle.setMinimumSize(QSize(40, 0))
        self.frame_icontitle.setMaximumSize(QSize(40, 16777215))
        self.frame_icontitle.setFrameShape(QFrame.StyledPanel)
        self.frame_icontitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_icontitle)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_icontitle)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u"icons_svg/chip.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_icontitle)

        self.frame_8 = QFrame(self.title_bar)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 32))
        self.frame_8.setMaximumSize(QSize(16777215, 32))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(240, 240, 240);")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.title_extra_btns = QFrame(self.title_bar)
        self.title_extra_btns.setObjectName(u"title_extra_btns")
        self.title_extra_btns.setMinimumSize(QSize(40, 0))
        self.title_extra_btns.setFrameShape(QFrame.StyledPanel)
        self.title_extra_btns.setFrameShadow(QFrame.Raised)
        self.title_extra_btns_layout = QHBoxLayout(self.title_extra_btns)
        self.title_extra_btns_layout.setSpacing(4)
        self.title_extra_btns_layout.setObjectName(u"title_extra_btns_layout")
        self.title_extra_btns_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.title_extra_btns)

        self.frame_btnswindow = QFrame(self.title_bar)
        self.frame_btnswindow.setObjectName(u"frame_btnswindow")
        self.frame_btnswindow.setMinimumSize(QSize(100, 32))
        self.frame_btnswindow.setMaximumSize(QSize(100, 32))
        self.frame_btnswindow.setFrameShape(QFrame.StyledPanel)
        self.frame_btnswindow.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btnswindow)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 0, 4, 0)
        self.btn_minize = QPushButton(self.frame_btnswindow)
        self.btn_minize.setObjectName(u"btn_minize")
        self.btn_minize.setMinimumSize(QSize(0, 24))
        self.btn_minize.setMaximumSize(QSize(16777215, 24))
        self.btn_minize.setStyleSheet(u"background-color: rgba(0, 255, 0, 180);\n"
"border-radius: 5px;")
        icon1 = QIcon()
        icon1.addFile(u"icons_svg/cil-window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minize)

        self.btn_restore = QPushButton(self.frame_btnswindow)
        self.btn_restore.setObjectName(u"btn_restore")
        self.btn_restore.setMinimumSize(QSize(0, 24))
        self.btn_restore.setMaximumSize(QSize(16777215, 24))
        self.btn_restore.setStyleSheet(u"background-color: rgba(255, 165, 0, 240);\n"
"border-radius: 5px;")
        icon2 = QIcon()
        icon2.addFile(u"icons_svg/cil-window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_restore)

        self.btn_close = QPushButton(self.frame_btnswindow)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 24))
        self.btn_close.setMaximumSize(QSize(16777215, 24))
        self.btn_close.setStyleSheet(u"background-color: rgba(255, 64, 0, 240);\n"
"border-radius: 5px;")
        icon3 = QIcon()
        icon3.addFile(u"icons_svg/cil-x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btnswindow)


        self.verticalLayout_2.addWidget(self.title_bar)

        self.frame_data = QFrame(self.frame_body)
        self.frame_data.setObjectName(u"frame_data")
        self.frame_data.setMinimumSize(QSize(0, 25))
        self.frame_data.setMaximumSize(QSize(16777215, 25))
        self.frame_data.setFrameShape(QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_data)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_subtitle = QLabel(self.frame_data)
        self.label_subtitle.setObjectName(u"label_subtitle")
        self.label_subtitle.setMinimumSize(QSize(120, 0))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_subtitle.setFont(font1)
        self.label_subtitle.setStyleSheet(u"color: rgb(200, 200, 200);")

        self.horizontalLayout_8.addWidget(self.label_subtitle)

        self.horizontalSpacer = QSpacerItem(501, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_fecha = QLabel(self.frame_data)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setMinimumSize(QSize(90, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_fecha.setFont(font2)
        self.label_fecha.setStyleSheet(u"color: rgb(200, 200, 200);")

        self.horizontalLayout_8.addWidget(self.label_fecha)

        self.label_page = QLabel(self.frame_data)
        self.label_page.setObjectName(u"label_page")
        self.label_page.setMinimumSize(QSize(90, 0))
        self.label_page.setFont(font1)
        self.label_page.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_page.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_page)


        self.verticalLayout_2.addWidget(self.frame_data)

        self.frame_pages = QFrame(self.frame_body)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_pages)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.extra_LeftBox = QFrame(self.frame_pages)
        self.extra_LeftBox.setObjectName(u"extra_LeftBox")
        self.extra_LeftBox.setMinimumSize(QSize(0, 0))
        self.extra_LeftBox.setFrameShape(QFrame.StyledPanel)
        self.extra_LeftBox.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.extra_LeftBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 20, 220, 271))
        self.frame_7.setMinimumSize(QSize(220, 0))
        self.frame_7.setMaximumSize(QSize(220, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(48, 64, 80);\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(200, 200, 200);")

        self.verticalLayout_4.addWidget(self.label_8)

        self.comboBoxPort = QComboBox(self.frame_7)
        self.comboBoxPort.setObjectName(u"comboBoxPort")
        self.comboBoxPort.setMinimumSize(QSize(0, 20))
        self.comboBoxPort.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"border-radius:0px;")

        self.verticalLayout_4.addWidget(self.comboBoxPort)

        self.buttonConnect = QPushButton(self.frame_7)
        self.buttonConnect.setObjectName(u"buttonConnect")
        self.buttonConnect.setMinimumSize(QSize(0, 20))
        self.buttonConnect.setFont(font1)
        self.buttonConnect.setStyleSheet(u"background-color:rgb(200, 200, 200);\n"
"border-radius:5px;\n"
"")

        self.verticalLayout_4.addWidget(self.buttonConnect)

        self.label_idport = QLabel(self.frame_7)
        self.label_idport.setObjectName(u"label_idport")
        self.label_idport.setFont(font1)
        self.label_idport.setStyleSheet(u"color: rgb(200, 200, 200);")

        self.verticalLayout_4.addWidget(self.label_idport)

        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setFont(font2)
        self.frame_2.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.port_layout = QVBoxLayout(self.frame_2)
        self.port_layout.setObjectName(u"port_layout")

        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_13 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_13)


        self.horizontalLayout_7.addWidget(self.extra_LeftBox)

        self.app_pages = QStackedWidget(self.frame_pages)
        self.app_pages.setObjectName(u"app_pages")
        self.app_pages.setStyleSheet(u"")
        self.wellcome = QWidget()
        self.wellcome.setObjectName(u"wellcome")
        self.horizontalLayout_11 = QHBoxLayout(self.wellcome)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.wellcome)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"icons_svg/wellcome.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.app_pages.addWidget(self.wellcome)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color: rgb(0, 70, 115);")
        self.verticalLayout_10 = QVBoxLayout(self.page_1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_7)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.page_1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_9)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 10, 191, 191))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 1, 1, 1)

        self.pyswitch_3 = PySwitch(self.layoutWidget)
        self.pyswitch_3.setObjectName(u"pyswitch_3")
        self.pyswitch_3.setMinimumSize(QSize(90, 30))
        self.pyswitch_3.setMaximumSize(QSize(90, 30))

        self.gridLayout.addWidget(self.pyswitch_3, 2, 2, 1, 1)

        self.pyswitch_2 = PySwitch(self.layoutWidget)
        self.pyswitch_2.setObjectName(u"pyswitch_2")
        self.pyswitch_2.setMinimumSize(QSize(90, 30))
        self.pyswitch_2.setMaximumSize(QSize(90, 30))

        self.gridLayout.addWidget(self.pyswitch_2, 1, 2, 1, 1)

        self.pyswitch_1 = PySwitch(self.layoutWidget)
        self.pyswitch_1.setObjectName(u"pyswitch_1")
        self.pyswitch_1.setMinimumSize(QSize(90, 30))
        self.pyswitch_1.setMaximumSize(QSize(90, 30))

        self.gridLayout.addWidget(self.pyswitch_1, 0, 2, 1, 1)

        self.pyswitch_4 = PySwitch(self.layoutWidget)
        self.pyswitch_4.setObjectName(u"pyswitch_4")
        self.pyswitch_4.setMinimumSize(QSize(90, 30))
        self.pyswitch_4.setMaximumSize(QSize(90, 30))

        self.gridLayout.addWidget(self.pyswitch_4, 3, 2, 1, 1)

        self.layoutWidget_3 = QWidget(self.frame_9)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(280, 10, 191, 191))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(50, 16777215))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_15 = QLabel(self.layoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 3, 1, 1, 1)

        self.label_16 = QLabel(self.layoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 2, 1, 1, 1)

        self.pyanimated_3 = PyAnimatedToggle(self.layoutWidget_3)
        self.pyanimated_3.setObjectName(u"pyanimated_3")
        self.pyanimated_3.setMinimumSize(QSize(80, 40))
        self.pyanimated_3.setMaximumSize(QSize(80, 40))

        self.gridLayout_2.addWidget(self.pyanimated_3, 2, 2, 1, 1)

        self.pyanimated_2 = PyAnimatedToggle(self.layoutWidget_3)
        self.pyanimated_2.setObjectName(u"pyanimated_2")
        self.pyanimated_2.setMinimumSize(QSize(80, 40))
        self.pyanimated_2.setMaximumSize(QSize(80, 40))

        self.gridLayout_2.addWidget(self.pyanimated_2, 1, 2, 1, 1)

        self.pyanimated_1 = PyAnimatedToggle(self.layoutWidget_3)
        self.pyanimated_1.setObjectName(u"pyanimated_1")
        self.pyanimated_1.setMinimumSize(QSize(80, 40))
        self.pyanimated_1.setMaximumSize(QSize(80, 40))

        self.gridLayout_2.addWidget(self.pyanimated_1, 0, 2, 1, 1)

        self.pyanimated_4 = PyAnimatedToggle(self.layoutWidget_3)
        self.pyanimated_4.setObjectName(u"pyanimated_4")
        self.pyanimated_4.setMinimumSize(QSize(80, 40))
        self.pyanimated_4.setMaximumSize(QSize(80, 40))

        self.gridLayout_2.addWidget(self.pyanimated_4, 3, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.app_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_5)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(2, 32, 64);\n"
"border-radius:20px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_11)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(290, 10, 138, 240))
        self.gridLayout_4 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(0, 10, 0, 10)
        self.label_21 = QLabel(self.layoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(60, 0))
        self.label_21.setMaximumSize(QSize(60, 16777215))
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)

        self.showhide_5 = ShowHideWidgetSVG(self.layoutWidget_2)
        self.showhide_5.setObjectName(u"showhide_5")
        self.showhide_5.setMinimumSize(QSize(40, 40))
        self.showhide_5.setMaximumSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.showhide_5, 0, 1, 1, 1)

        self.label_22 = QLabel(self.layoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)

        self.showhide_6 = ShowHideWidgetSVG(self.layoutWidget_2)
        self.showhide_6.setObjectName(u"showhide_6")
        self.showhide_6.setMinimumSize(QSize(40, 40))
        self.showhide_6.setMaximumSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.showhide_6, 1, 1, 1, 1)

        self.label_23 = QLabel(self.layoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font4)
        self.label_23.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_4.addWidget(self.label_23, 2, 0, 1, 1)

        self.showhide_7 = ShowHideWidgetSVG(self.layoutWidget_2)
        self.showhide_7.setObjectName(u"showhide_7")
        self.showhide_7.setMinimumSize(QSize(40, 40))
        self.showhide_7.setMaximumSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.showhide_7, 2, 1, 1, 1)

        self.label_24 = QLabel(self.layoutWidget_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_4.addWidget(self.label_24, 3, 0, 1, 1)

        self.showhide_8 = ShowHideWidgetSVG(self.layoutWidget_2)
        self.showhide_8.setObjectName(u"showhide_8")
        self.showhide_8.setMinimumSize(QSize(40, 40))
        self.showhide_8.setMaximumSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.showhide_8, 3, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.frame_11)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 10, 138, 240))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 10)
        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(60, 0))
        self.label_17.setMaximumSize(QSize(60, 16777215))
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)

        self.showhide_1 = ShowHideWidgetSVG(self.layoutWidget1)
        self.showhide_1.setObjectName(u"showhide_1")
        self.showhide_1.setMinimumSize(QSize(40, 40))
        self.showhide_1.setMaximumSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.showhide_1, 0, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.showhide_2 = ShowHideWidgetSVG(self.layoutWidget1)
        self.showhide_2.setObjectName(u"showhide_2")
        self.showhide_2.setMinimumSize(QSize(40, 40))
        self.showhide_2.setMaximumSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.showhide_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)

        self.showhide_3 = ShowHideWidgetSVG(self.layoutWidget1)
        self.showhide_3.setObjectName(u"showhide_3")
        self.showhide_3.setMinimumSize(QSize(40, 40))
        self.showhide_3.setMaximumSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.showhide_3, 2, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)

        self.showhide_4 = ShowHideWidgetSVG(self.layoutWidget1)
        self.showhide_4.setObjectName(u"showhide_4")
        self.showhide_4.setMinimumSize(QSize(40, 40))
        self.showhide_4.setMaximumSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.showhide_4, 3, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.app_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.page_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(220,220,220);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(16,32, 64);\n"
"border-radius:20px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_14)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 10, 0)
        self.gauge_1 = AnalogGaugeWidget(self.frame_14)
        self.gauge_1.setObjectName(u"gauge_1")
        self.gauge_1.setMinimumSize(QSize(220, 200))

        self.gridLayout_5.addWidget(self.gauge_1, 0, 0, 1, 1)

        self.gauge_2 = AnalogGaugeWidget(self.frame_14)
        self.gauge_2.setObjectName(u"gauge_2")
        self.gauge_2.setMinimumSize(QSize(220, 200))

        self.gridLayout_5.addWidget(self.gauge_2, 0, 1, 1, 1)

        self.gauge_3 = AnalogGaugeWidget(self.frame_14)
        self.gauge_3.setObjectName(u"gauge_3")
        self.gauge_3.setMinimumSize(QSize(220, 200))

        self.gridLayout_5.addWidget(self.gauge_3, 0, 2, 1, 1)

        self.gauge_4 = AnalogGaugeWidget(self.frame_14)
        self.gauge_4.setObjectName(u"gauge_4")
        self.gauge_4.setMinimumSize(QSize(220, 200))

        self.gridLayout_5.addWidget(self.gauge_4, 0, 3, 1, 1)

        self.label_25 = QLabel(self.frame_14)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(60, 0))
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(self.frame_14)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(60, 0))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_26, 1, 1, 1, 1)

        self.label_27 = QLabel(self.frame_14)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(60, 0))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_27, 1, 2, 1, 1)

        self.label_28 = QLabel(self.frame_14)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(60, 0))
        self.label_28.setFont(font4)
        self.label_28.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_28, 1, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_14)

        self.verticalSpacer_2 = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.app_pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_15)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color: rgb(192, 192, 192);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_4)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: #211F1F;\n"
"border-radius:20px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_VS = QFrame(self.frame_16)
        self.frame_VS.setObjectName(u"frame_VS")
        self.frame_VS.setGeometry(QRect(349, 10, 231, 251))
        self.frame_VS.setStyleSheet(u"background-color: #4C7300;\n"
"color: #aeff00;\n"
"border-radius:10px;")
        self.frame_VS.setFrameShape(QFrame.StyledPanel)
        self.frame_VS.setFrameShadow(QFrame.Raised)
        self.verticalLayout_VS = QVBoxLayout(self.frame_VS)
        self.verticalLayout_VS.setObjectName(u"verticalLayout_VS")
        self.label_VS = QLabel(self.frame_VS)
        self.label_VS.setObjectName(u"label_VS")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_VS.setFont(font7)
        self.label_VS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_VS.addWidget(self.label_VS)

        self.Layout_VS = QGridLayout()
        self.Layout_VS.setObjectName(u"Layout_VS")
        self.Layout_VS.setHorizontalSpacing(0)
        self.Layout_VS.setVerticalSpacing(10)
        self.label_VS_1 = QLabel(self.frame_VS)
        self.label_VS_1.setObjectName(u"label_VS_1")
        self.label_VS_1.setMinimumSize(QSize(40, 0))
        self.label_VS_1.setFont(font7)
        self.label_VS_1.setAlignment(Qt.AlignCenter)

        self.Layout_VS.addWidget(self.label_VS_1, 0, 0, 1, 1)

        self.label_VS_2 = QLabel(self.frame_VS)
        self.label_VS_2.setObjectName(u"label_VS_2")
        self.label_VS_2.setMinimumSize(QSize(40, 0))
        self.label_VS_2.setFont(font7)
        self.label_VS_2.setAlignment(Qt.AlignCenter)

        self.Layout_VS.addWidget(self.label_VS_2, 0, 1, 1, 1)

        self.label_VS_3 = QLabel(self.frame_VS)
        self.label_VS_3.setObjectName(u"label_VS_3")
        self.label_VS_3.setMinimumSize(QSize(40, 0))
        self.label_VS_3.setFont(font7)
        self.label_VS_3.setAlignment(Qt.AlignCenter)

        self.Layout_VS.addWidget(self.label_VS_3, 0, 2, 1, 1)

        self.label_VS_4 = QLabel(self.frame_VS)
        self.label_VS_4.setObjectName(u"label_VS_4")
        self.label_VS_4.setMinimumSize(QSize(40, 0))
        self.label_VS_4.setFont(font7)
        self.label_VS_4.setAlignment(Qt.AlignCenter)

        self.Layout_VS.addWidget(self.label_VS_4, 0, 3, 1, 1)

        self.VSlider_1 = QSlider(self.frame_VS)
        self.VSlider_1.setObjectName(u"VSlider_1")
        self.VSlider_1.setMinimumSize(QSize(0, 120))
        self.VSlider_1.setMaximumSize(QSize(16777215, 16777215))
        self.VSlider_1.setStyleSheet(u"QSlider::groove:horizontal{\n"
"border: 1px solid #bbb;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical{\n"
"background: #C0C0C0;\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #78d,  stop: 1 #238 );\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"background: #00b0ff;\n"
"border: 1px solid #777;\n"
"height: 12px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background: #E0e0e0;\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.VSlider_1.setMaximum(255)
        self.VSlider_1.setOrientation(Qt.Vertical)
        self.VSlider_1.setTickPosition(QSlider.TicksAbove)
        self.VSlider_1.setTickInterval(50)

        self.Layout_VS.addWidget(self.VSlider_1, 1, 0, 1, 1)

        self.VSlider_2 = QSlider(self.frame_VS)
        self.VSlider_2.setObjectName(u"VSlider_2")
        self.VSlider_2.setMinimumSize(QSize(0, 120))
        self.VSlider_2.setStyleSheet(u"QSlider::groove:horizontal{\n"
"border: 1px solid #bbb;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical{\n"
"background: #C0C0C0;\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #f88,  stop: 1 #822);\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"background: #ff0000;\n"
"border: 1px solid #777;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background: #e0e0e0;\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.VSlider_2.setMaximum(255)
        self.VSlider_2.setOrientation(Qt.Vertical)
        self.VSlider_2.setTickPosition(QSlider.TicksAbove)
        self.VSlider_2.setTickInterval(50)

        self.Layout_VS.addWidget(self.VSlider_2, 1, 1, 1, 1)

        self.VSlider_3 = QSlider(self.frame_VS)
        self.VSlider_3.setObjectName(u"VSlider_3")
        self.VSlider_3.setMinimumSize(QSize(0, 120))
        self.VSlider_3.setStyleSheet(u"QSlider::groove:horizontal{\n"
"border: 1px solid #bbb;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical{\n"
"background: #C0C0C0;\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #8d7,  stop: 1 #473);\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"background: #b0ff00;\n"
"border: 1px solid #777;\n"
"height: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background: #e0e0e0;\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}")
        self.VSlider_3.setMaximum(255)
        self.VSlider_3.setOrientation(Qt.Vertical)
        self.VSlider_3.setTickPosition(QSlider.TicksAbove)
        self.VSlider_3.setTickInterval(50)

        self.Layout_VS.addWidget(self.VSlider_3, 1, 2, 1, 1)

        self.VSlider_4 = QSlider(self.frame_VS)
        self.VSlider_4.setObjectName(u"VSlider_4")
        self.VSlider_4.setMinimumSize(QSize(0, 120))
        self.VSlider_4.setLayoutDirection(Qt.LeftToRight)
        self.VSlider_4.setStyleSheet(u"QSlider::groove:horizontal{\n"
"border: 1px solid #bbb;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical{\n"
"background: #C0C0C0;\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #fa0,  stop: 1 #a80);\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"background: #FFA500;\n"
"border: 1px solid #777;\n"
"height: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background: #e0e0e0;\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}")
        self.VSlider_4.setMaximum(255)
        self.VSlider_4.setOrientation(Qt.Vertical)
        self.VSlider_4.setInvertedAppearance(False)
        self.VSlider_4.setInvertedControls(False)
        self.VSlider_4.setTickPosition(QSlider.TicksAbove)
        self.VSlider_4.setTickInterval(50)

        self.Layout_VS.addWidget(self.VSlider_4, 1, 3, 1, 1)


        self.verticalLayout_VS.addLayout(self.Layout_VS)

        self.frame_HS = QFrame(self.frame_16)
        self.frame_HS.setObjectName(u"frame_HS")
        self.frame_HS.setGeometry(QRect(50, 10, 231, 251))
        self.frame_HS.setStyleSheet(u"background-color:#4C7300;\n"
"color: #aeff00;\n"
"border-radius:10px;")
        self.frame_HS.setFrameShape(QFrame.StyledPanel)
        self.frame_HS.setFrameShadow(QFrame.Raised)
        self.verticalLayout_HS = QVBoxLayout(self.frame_HS)
        self.verticalLayout_HS.setObjectName(u"verticalLayout_HS")
        self.label_HS = QLabel(self.frame_HS)
        self.label_HS.setObjectName(u"label_HS")
        self.label_HS.setMinimumSize(QSize(0, 20))
        self.label_HS.setMaximumSize(QSize(16777215, 20))
        self.label_HS.setFont(font7)
        self.label_HS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_HS.addWidget(self.label_HS)

        self.Layout_HS = QGridLayout()
        self.Layout_HS.setObjectName(u"Layout_HS")
        self.Layout_HS.setHorizontalSpacing(10)
        self.Layout_HS.setVerticalSpacing(20)
        self.HSlider_3 = QSlider(self.frame_HS)
        self.HSlider_3.setObjectName(u"HSlider_3")
        self.HSlider_3.setMinimumSize(QSize(0, 40))
        self.HSlider_3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"height:3px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background: #ff00a5ff;\n"
"border: 1px solid #777;\n"
"height:2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #c0c0c0;\n"
"border: 1px solid #777;\n"
"height:2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.9, fx:0.5, fy:0.5, stop:0.4 rgba(0, 196, 255, 255), stop:0.7 rgba(210, 210, 210, 10));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.3, fx:0.5, fy:0.5, stop:0.3 rgba(0, 196,255, 255), stop:0.7 rgba(255, 255, 255, 10));\n"
"}")
        self.HSlider_3.setMaximum(255)
        self.HSlider_3.setOrientation(Qt.Horizontal)

        self.Layout_HS.addWidget(self.HSlider_3, 2, 1, 1, 1)

        self.label_HS_4 = QLabel(self.frame_HS)
        self.label_HS_4.setObjectName(u"label_HS_4")
        self.label_HS_4.setFont(font7)
        self.label_HS_4.setAlignment(Qt.AlignCenter)

        self.Layout_HS.addWidget(self.label_HS_4, 3, 0, 1, 1)

        self.label_HS_1 = QLabel(self.frame_HS)
        self.label_HS_1.setObjectName(u"label_HS_1")
        self.label_HS_1.setMinimumSize(QSize(40, 0))
        self.label_HS_1.setFont(font7)
        self.label_HS_1.setAlignment(Qt.AlignCenter)

        self.Layout_HS.addWidget(self.label_HS_1, 0, 0, 1, 1)

        self.label_HS_2 = QLabel(self.frame_HS)
        self.label_HS_2.setObjectName(u"label_HS_2")
        self.label_HS_2.setFont(font7)
        self.label_HS_2.setAlignment(Qt.AlignCenter)

        self.Layout_HS.addWidget(self.label_HS_2, 1, 0, 1, 1)

        self.HSlider_4 = QSlider(self.frame_HS)
        self.HSlider_4.setObjectName(u"HSlider_4")
        self.HSlider_4.setMinimumSize(QSize(0, 40))
        self.HSlider_4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"height: 3px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background: #ffFFA500;\n"
"border: 1px solid #777;\n"
"height: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #c0c0c0;\n"
"border: 1px solid #777;\n"
"height: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.9, fx:0.5, fy:0.5, stop:0.4 rgba(255, 196, 0, 255), stop:0.7 rgba(210, 210, 210, 10));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.3, fx:0.5, fy:0.5, stop:0.3 rgba(255,196, 0, 255), stop:0.7 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.HSlider_4.setMaximum(255)
        self.HSlider_4.setOrientation(Qt.Horizontal)

        self.Layout_HS.addWidget(self.HSlider_4, 3, 1, 1, 1)

        self.HSlider_2 = QSlider(self.frame_HS)
        self.HSlider_2.setObjectName(u"HSlider_2")
        self.HSlider_2.setMinimumSize(QSize(0, 40))
        self.HSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"height: 3px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background: #ffff0000;\n"
"border: 1px solid #777;\n"
"height: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #c0c0c0;\n"
"border: 1px solid #777;\n"
"height: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.9, fx:0.5, fy:0.5, stop:0.4 rgba(255, 0, 0, 255), stop:0.7 rgba(210, 210, 210, 10));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.3, fx:0.5, fy:0.5, stop:0.3 rgba(255, 0,0, 255), stop:0.7 rgba(255, 255,255, 10));\n"
"}")
        self.HSlider_2.setMaximum(255)
        self.HSlider_2.setOrientation(Qt.Horizontal)

        self.Layout_HS.addWidget(self.HSlider_2, 1, 1, 1, 1)

        self.label_HS_3 = QLabel(self.frame_HS)
        self.label_HS_3.setObjectName(u"label_HS_3")
        self.label_HS_3.setFont(font7)
        self.label_HS_3.setAlignment(Qt.AlignCenter)

        self.Layout_HS.addWidget(self.label_HS_3, 2, 0, 1, 1)

        self.HSlider_1 = QSlider(self.frame_HS)
        self.HSlider_1.setObjectName(u"HSlider_1")
        self.HSlider_1.setMinimumSize(QSize(0, 40))
        self.HSlider_1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"height: 3px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background: #ff00ff00;\n"
"border: 1px solid #777;\n"
"height: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #c0c0c0;\n"
"border: 1px solid #777;\n"
"height: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.9, fx:0.5, fy:0.5, stop:0.4 rgba(0, 255, 0, 255), stop:0.7 rgba(210, 210, 210, 10));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.3, fx:0.5, fy:0.5, stop:0.3 rgba(0, 255, 0, 255), stop:0.7 rgba(255, 255, 255, 10));\n"
"}")
        self.HSlider_1.setMaximum(255)
        self.HSlider_1.setOrientation(Qt.Horizontal)
        self.HSlider_1.setTickPosition(QSlider.NoTicks)
        self.HSlider_1.setTickInterval(50)

        self.Layout_HS.addWidget(self.HSlider_1, 0, 1, 1, 1)


        self.verticalLayout_HS.addLayout(self.Layout_HS)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.app_pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.page_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_17 = QFrame(self.page_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 25))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_page5_charts = QLabel(self.frame_17)
        self.label_page5_charts.setObjectName(u"label_page5_charts")
        self.label_page5_charts.setFont(font6)
        self.label_page5_charts.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_page5_charts.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_page5_charts)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.page_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_matplot = QFrame(self.frame_18)
        self.frame_matplot.setObjectName(u"frame_matplot")
        self.frame_matplot.setMinimumSize(QSize(0, 300))
        self.frame_matplot.setMaximumSize(QSize(16777215, 16777215))
        self.frame_matplot.setStyleSheet(u"background-color: rgb(1,16,32);\n"
"border-radius:20px;")
        self.frame_matplot.setFrameShape(QFrame.StyledPanel)
        self.frame_matplot.setFrameShadow(QFrame.Raised)
        self.Hlayout_matplot = QHBoxLayout(self.frame_matplot)
        self.Hlayout_matplot.setSpacing(0)
        self.Hlayout_matplot.setObjectName(u"Hlayout_matplot")
        self.Hlayout_matplot.setContentsMargins(0, 0, 0, 0)
        self.matplot_1 = MatplotlibWidget11_sin(self.frame_matplot)
        self.matplot_1.setObjectName(u"matplot_1")

        self.Hlayout_matplot.addWidget(self.matplot_1)


        self.horizontalLayout_17.addWidget(self.frame_matplot)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.app_pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_9 = QVBoxLayout(self.page_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.page_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_page1a_3 = QLabel(self.frame_19)
        self.label_page1a_3.setObjectName(u"label_page1a_3")
        self.label_page1a_3.setFont(font6)
        self.label_page1a_3.setStyleSheet(u"color: rgb(224, 224, 224);")
        self.label_page1a_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_page1a_3)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.page_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame_20)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 0, 820, 307))
        self.gridLayout_6 = QGridLayout(self.layoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.layoutWidget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(120, 0))
        self.label_30.setMaximumSize(QSize(16777215, 20))
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_31 = QLabel(self.layoutWidget_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(120, 0))
        self.label_31.setMaximumSize(QSize(16777215, 20))
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_31, 0, 1, 1, 1)

        self.label_34 = QLabel(self.layoutWidget_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(280, 0))
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setFont(font7)
        self.label_34.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_34, 0, 2, 1, 1)

        self.label_35 = QLabel(self.layoutWidget_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(280, 0))
        self.label_35.setMaximumSize(QSize(16777215, 20))
        self.label_35.setFont(font7)
        self.label_35.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_35, 0, 3, 1, 1)

        self.termo_1 = Termo(self.layoutWidget_4)
        self.termo_1.setObjectName(u"termo_1")
        self.termo_1.setMinimumSize(QSize(0, 280))
        self.termo_1.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.termo_1, 1, 0, 1, 1)

        self.verticalbar_1 = VerticalBar(self.layoutWidget_4)
        self.verticalbar_1.setObjectName(u"verticalbar_1")
        self.verticalbar_1.setMinimumSize(QSize(0, 0))
        self.verticalbar_1.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.verticalbar_1, 1, 1, 1, 1)

        self.roundprogressbar_1 = RoundProgressBar(self.layoutWidget_4)
        self.roundprogressbar_1.setObjectName(u"roundprogressbar_1")
        self.roundprogressbar_1.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.roundprogressbar_1, 1, 2, 1, 1)

        self.spiralprogressbar_1 = SpiralProgressBar(self.layoutWidget_4)
        self.spiralprogressbar_1.setObjectName(u"spiralprogressbar_1")

        self.gridLayout_6.addWidget(self.spiralprogressbar_1, 1, 3, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_20)

        self.app_pages.addWidget(self.page_6)

        self.horizontalLayout_7.addWidget(self.app_pages)

        self.extra_RightBox = QFrame(self.frame_pages)
        self.extra_RightBox.setObjectName(u"extra_RightBox")
        self.extra_RightBox.setMinimumSize(QSize(0, 0))
        self.extra_RightBox.setMaximumSize(QSize(16777215, 16777215))
        self.extra_RightBox.setFrameShape(QFrame.StyledPanel)
        self.extra_RightBox.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.extra_RightBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 220, 81))
        self.frame_3.setMinimumSize(QSize(220, 0))
        self.frame_3.setMaximumSize(QSize(220, 16777215))
        self.frame_3.setStyleSheet(u"background-color: #102040;\n"
"border-radius:20px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_29.setFont(font8)
        self.label_29.setStyleSheet(u"color: rgb(165, 255, 0);")
        self.label_29.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.label_29)

        self.frame_4 = QFrame(self.extra_RightBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 100, 220, 71))
        self.frame_4.setMaximumSize(QSize(220, 16777215))
        self.frame_4.setStyleSheet(u"background-color: #102040;\n"
"border-radius:20px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font8)
        self.label_33.setStyleSheet(u"color: rgb(255, 165, 0);")
        self.label_33.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_33)

        self.frame_32 = QFrame(self.extra_RightBox)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(10, 180, 220, 61))
        self.frame_32.setMaximumSize(QSize(220, 16777215))
        self.frame_32.setStyleSheet(u"background-color: #102040;\n"
"border-radius:20px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_36 = QLabel(self.frame_32)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font8)
        self.label_36.setStyleSheet(u"color: rgb(255, 40, 40);")
        self.label_36.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.label_36)

        self.frame_21 = QFrame(self.extra_RightBox)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(10, 250, 220, 201))
        self.frame_21.setMaximumSize(QSize(220, 16777215))
        self.frame_21.setStyleSheet(u"background-color: #102040;\n"
"border-radius:20px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_37 = QLabel(self.frame_21)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font8)
        self.label_37.setStyleSheet(u"color: rgb(0, 165, 255);")
        self.label_37.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.label_37)


        self.horizontalLayout_7.addWidget(self.extra_RightBox)


        self.verticalLayout_2.addWidget(self.frame_pages)

        self.frame_credits = QFrame(self.frame_body)
        self.frame_credits.setObjectName(u"frame_credits")
        self.frame_credits.setMinimumSize(QSize(0, 25))
        self.frame_credits.setMaximumSize(QSize(16777215, 25))
        self.frame_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_credits)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.label_autor = QLabel(self.frame_credits)
        self.label_autor.setObjectName(u"label_autor")
        self.label_autor.setMinimumSize(QSize(120, 0))
        self.label_autor.setStyleSheet(u"color: rgb(200, 200, 255);")

        self.horizontalLayout_9.addWidget(self.label_autor)

        self.horizontalSpacer_2 = QSpacerItem(486, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.label_time = QLabel(self.frame_credits)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(60, 0))
        self.label_time.setStyleSheet(u"color: rgb(200, 200, 255);")
        self.label_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_time)

        self.label_hora = QLabel(self.frame_credits)
        self.label_hora.setObjectName(u"label_hora")
        self.label_hora.setMinimumSize(QSize(45, 0))
        self.label_hora.setStyleSheet(u"color: rgb(200, 200, 255);")

        self.horizontalLayout_9.addWidget(self.label_hora)

        self.frame_grip = QFrame(self.frame_credits)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(25, 25))
        self.frame_grip.setMaximumSize(QSize(25, 25))
        self.frame_grip.setStyleSheet(u"")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_grip)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"icons_svg/cil-apps.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton)


        self.horizontalLayout_9.addWidget(self.frame_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_credits)


        self.horizontalLayout_3.addWidget(self.frame_body)


        self.horizontalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.app_pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menuCom.setText("")
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD CONTROL", None))
        self.btn_minize.setText("")
        self.btn_restore.setText("")
        self.btn_close.setText("")
        self.label_subtitle.setText(QCoreApplication.translate("MainWindow", u"MONITOR SYS", None))
        self.label_fecha.setText(QCoreApplication.translate("MainWindow", u"YYYY:MM:DD", None))
        self.label_page.setText(QCoreApplication.translate("MainWindow", u"WELLCOME", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SERIALS PORTS", None))
        self.buttonConnect.setText(QCoreApplication.translate("MainWindow", u"Select Port", None))
        self.label_idport.setText(QCoreApplication.translate("MainWindow", u"ID PORT", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ACTIVACION DE BOTONES", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"P1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"P2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"P4", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"P3", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"P5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"P6", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"P8", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"P7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DIGITAL INPUTS", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"IN 5", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"IN 6", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IN 7", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"IN 8", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"IN 1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"IN 2", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"IN 3", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"IN 4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ANALOG INPUT - GAUGE", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"AIN 0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"AIN 1", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"AIN 2", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"AIN 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" PWM OUTPUTS", None))
        self.label_VS.setText(QCoreApplication.translate("MainWindow", u"Vertical Sliders", None))
        self.label_VS_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_VS_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_VS_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_VS_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_HS.setText(QCoreApplication.translate("MainWindow", u"Horizontal Sliders", None))
        self.label_HS_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_HS_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_HS_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_HS_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_page5_charts.setText(QCoreApplication.translate("MainWindow", u"GRAPH CHARTS", None))
        self.label_page1a_3.setText(QCoreApplication.translate("MainWindow", u"OTHERS WIDGETS", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Thermo", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Vertical Bar", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Progress Bar", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Spiral Progress Bar", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Design based on Wanderson Pimenta's PyBlackBox. \n"
"A super Teacher.\n"
"https://www.youtube.com/c/WandersonIsMe", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Many of the tricks implemented here were contributed by \n"
"Martin Fitzpatrick\n"
"https://www.pythonguis.com/", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Great support of ideas by Spinn TV. https://www.youtube.com/c/spinntv", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Excellent analog meter.\n"
"Thank you. Stefan Holstein\n"
"https://github.com/StefanHol/AnalogGaugeWidgetPyQt\n"
"ANJAL.P \n"
"Spiral progress bar \n"
"https://github.com/anjalp/PySide2extn\n"
"Pete Alexandrou\n"
"QRoundProgressBar \n"
"https://sourceforge.net/projects/qroundprogressbar/\n"
"Tomasz Ziobrowski\n"
"Thermometer", None))
        self.label_autor.setText(QCoreApplication.translate("MainWindow", u"Designed by: JJGM", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TIME |  ", None))
        self.label_hora.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.pushButton.setText("")
    # retranslateUi

