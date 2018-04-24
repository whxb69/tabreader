# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readbook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1981, 1337)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.treeWidget = QTreeWidget(self.centralwidget)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setGeometry(QtCore.QRect(30, 110, 350, 1150))
        self.treeWidget.setMinimumSize(350, 1150)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "标题")

        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setDropIndicatorShown(True)
        self.treeWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeWidget.setMouseTracking(True)

        self.pro_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.pro_tabWidget.setGeometry(QtCore.QRect(400, 80, 1550, 1190))
        self.pro_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.pro_tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.pro_tabWidget.setObjectName("tabWidget")
        self.pro_tabWidget.tabBarDoubleClicked.connect(lambda:MainWindow.addtab(0))

        self.pro_tab = QtWidgets.QWidget()
        self.pro_tab.setObjectName("protab")
        self.pro_tabWidget.addTab(self.pro_tab, "untitled1")
        self.pro_tabWidget.setAcceptDrops(True)

        self.tabWidget = QtWidgets.QTabWidget(self.pro_tab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")

        # self.pro_tabWidget.currentChanged.connect(lambda :self.tabWidget.setCurrentIndex(0))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_0_1 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_0_1.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
        self.textEdit_0_1.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.textEdit_0_1.setFont(font)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_0_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_0_2.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
        self.textEdit_0_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.textEdit_0_2.setFont(font)

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_0_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_0_3.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
        self.textEdit_0_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.textEdit_0_3.setFont(font)

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_0_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_0_4.setGeometry(QtCore.QRect(0, 0, 1545, 1151))
        self.textEdit_0_4.setObjectName("textEdit_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.textEdit_0_4.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1981, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_merge = QPushButton()
        self.button_merge.setGeometry(QRect(100, 200, 50, 18))
        self.button_merge.setText('分段合并')
        self.button_merge.setFlat(True)
        self.button_merge.setEnabled(False)

        self.toolbar = QtWidgets.QToolBar(MainWindow)
        self.toolbar.setGeometry(QtCore.QRect(0, 35, 1357, 46))
        self.toolbar.setMovable(False)
        self.toolbar.setObjectName("toolbar")

        self.action_Open = QAction(QIcon("open.ico"), "&打开", MainWindow)
        self.action_Open.setObjectName("actionOpen")
        self.action_Open.setToolTip('打开文件')

        self.action_save = QAction(QIcon("save.ico"),"&保存",MainWindow)
        self.action_save.setObjectName("actionsave")
        self.action_save.setToolTip('保存文件')

        self.action_alter = QAction(QIcon("play.ico"), "&拆分", MainWindow)
        self.action_alter.setObjectName("actionalter")

        self.action_alter.setToolTip('开始操作！')

        self.action_addtab = QAction(QIcon("add.ico"), "&添加标签", MainWindow)
        self.action_addtab.setObjectName("actionaddtab")
        self.action_addtab.triggered.connect(lambda:MainWindow.addtab(1,0))
        self.action_addtab.setToolTip('添加标签')

        self.action_super = QAction(QIcon("super.ico"), "&整篇拆分", MainWindow)
        self.action_super.setObjectName('actionsuper')
        self.action_super.setToolTip('整篇拆分')

        self.action_merge = QAction(QIcon("merge.ico"), "&分段合并", MainWindow)
        self.action_merge.setObjectName('actionmerge')



        self.action_merge.setToolTip('分段合并')

        self.action_trans = QAction(QIcon("trans.ico"), "&翻译", MainWindow)
        self.action_trans.setObjectName("actionalter")
        self.action_trans.setToolTip('翻译')


        self.toolbar.addAction(self.action_Open)
        self.toolbar.addAction(self.action_save)
        self.toolbar.addAction(self.action_alter)
        self.toolbar.addAction(self.action_addtab)
        self.toolbar.addAction(self.action_trans)
        self.toolbar.addAction(self.action_super)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_merge)
        self.toolbar.addWidget(self.button_merge)


        self.menu = self.menuBar()
        self.menu.setGeometry(QtCore.QRect(0, 0, 500, 30))
        file = self.menu.addMenu('文件')
        file.addAction(self.action_Open)
        file.addAction(self.action_save)
        work = self.menu.addMenu('操作')
        work.addAction(self.action_alter)
        work.addAction(self.action_addtab)
        work.addAction(self.action_trans)
        work.addAction(self.action_super)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowIcon(QIcon('win.ico'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "原文"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "逗号"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "句号"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "翻译"))

