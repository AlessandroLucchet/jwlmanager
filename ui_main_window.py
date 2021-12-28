# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowrXQsqt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(662, 600)
        MainWindow.setMinimumSize(QSize(560, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(self.resource_path('icons/project_36.ico'), QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(self.resource_path('icons/icons8-opened-folder-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(self.resource_path('icons/icons8-save-64.png'), QSize(), QIcon.Normal, QIcon.On)
        self.actionSave.setIcon(icon2)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionImport.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(self.resource_path('icons/icons8-download-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport.setIcon(icon3)
        self.actionReindex = QAction(MainWindow)
        self.actionReindex.setObjectName(u"actionReindex")
        self.actionReindex.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(self.resource_path('icons/icons8-database-administrator-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionReindex.setIcon(icon4)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon5 = QIcon()
        icon5.addFile(self.resource_path('icons/icons8-export-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon5)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon6 = QIcon()
        icon6.addFile(self.resource_path('icons/icons8-info-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon6)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionHelp.setEnabled(True)
        icon7 = QIcon()
        icon7.addFile(self.resource_path('icons/icons8-help-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon7)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_As.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(self.resource_path('icons/icons8-save-as-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_As.setIcon(icon8)
        self.actionExpand_All = QAction(MainWindow)
        self.actionExpand_All.setObjectName(u"actionExpand_All")
        self.actionExpand_All.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(self.resource_path('icons/icons8-expand-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionExpand_All.setIcon(icon9)
        self.actionCollapse_All = QAction(MainWindow)
        self.actionCollapse_All.setObjectName(u"actionCollapse_All")
        self.actionCollapse_All.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(self.resource_path('icons/icons8-collapse-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionCollapse_All.setIcon(icon10)
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionSelect_All.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(self.resource_path('icons/icons8-double-tick-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionSelect_All.setIcon(icon11)
        self.actionUnselect_All = QAction(MainWindow)
        self.actionUnselect_All.setObjectName(u"actionUnselect_All")
        self.actionUnselect_All.setEnabled(False)
        icon12 = QIcon()
        icon12.addFile(self.resource_path('icons/icons8-unchecked-checkbox-64.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnselect_All.setIcon(icon12)
        self.actionCode_Title = QAction(MainWindow)
        self.actionCode_Title.setObjectName(u"actionCode_Title")
        self.actionCode_Title.setCheckable(True)
        self.actionCode_Title.setChecked(False)
        self.actionShort_Title = QAction(MainWindow)
        self.actionShort_Title.setObjectName(u"actionShort_Title")
        self.actionShort_Title.setCheckable(True)
        self.actionShort_Title.setChecked(True)
        self.actionFull_Title = QAction(MainWindow)
        self.actionFull_Title.setObjectName(u"actionFull_Title")
        self.actionFull_Title.setCheckable(True)
        self.actionGrouped = QAction(MainWindow)
        self.actionGrouped.setObjectName(u"actionGrouped")
        self.actionGrouped.setCheckable(True)
        self.actionGrouped.setChecked(True)
        self.actionGrouped.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_info = QFrame(self.centralwidget)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(0, 80))
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.label_total = QLabel(self.frame_info)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setGeometry(QRect(10, 10, 45, 26))
        self.label_selected = QLabel(self.frame_info)
        self.label_selected.setObjectName(u"label_selected")
        self.label_selected.setGeometry(QRect(220, 10, 75, 26))
        self.total = QLabel(self.frame_info)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(55, 10, 80, 26))
        self.total.setTextFormat(Qt.MarkdownText)
        self.total.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.selected = QLabel(self.frame_info)
        self.selected.setObjectName(u"selected")
        self.selected.setGeometry(QRect(295, 10, 80, 26))
        self.selected.setTextFormat(Qt.MarkdownText)
        self.selected.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_category = QLabel(self.frame_info)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(10, 40, 75, 26))
        self.combo_category = QComboBox(self.frame_info)
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.setObjectName(u"combo_category")
        self.combo_category.setEnabled(False)
        self.combo_category.setGeometry(QRect(90, 40, 115, 26))
        self.label_grouping = QLabel(self.frame_info)
        self.label_grouping.setObjectName(u"label_grouping")
        self.label_grouping.setGeometry(QRect(220, 40, 75, 26))
        self.combo_grouping = QComboBox(self.frame_info)
        self.combo_grouping.addItem("")
        self.combo_grouping.addItem("")
        self.combo_grouping.addItem("")
        self.combo_grouping.addItem("")
        self.combo_grouping.addItem("")
        self.combo_grouping.setObjectName(u"combo_grouping")
        self.combo_grouping.setEnabled(False)
        self.combo_grouping.setGeometry(QRect(300, 40, 115, 26))
        self.button_export = QPushButton(self.frame_info)
        self.button_export.setObjectName(u"button_export")
        self.button_export.setEnabled(False)
        self.button_export.setGeometry(QRect(450, 10, 86, 26))
        self.button_delete = QPushButton(self.frame_info)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setEnabled(False)
        self.button_delete.setGeometry(QRect(450, 40, 86, 26))

        self.gridLayout_2.addWidget(self.frame_info, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.centralwidget)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QSize(0, 0))
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setColumnCount(2)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 662, 34))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTitle_View = QMenu(self.menuView)
        self.menuTitle_View.setObjectName(u"menuTitle_View")
        self.menuTitle_View.setEnabled(False)
        icon13 = QIcon()
        icon13.addFile(self.resource_path('icons/icons8-list-64.png'), QSize(), QIcon.Normal, QIcon.On)
        self.menuTitle_View.setIcon(icon13)
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusBar)
#if QT_CONFIG(shortcut)
        self.label_category.setBuddy(self.combo_category)
        self.label_grouping.setBuddy(self.combo_grouping)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.combo_category, self.combo_grouping)
        QWidget.setTabOrder(self.combo_grouping, self.button_export)
        QWidget.setTabOrder(self.button_export, self.button_delete)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.actionOpen)
        self.menu_file.addAction(self.actionSave)
        self.menu_file.addAction(self.actionSave_As)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionImport)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionReindex)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionQuit)
        self.menu_help.addAction(self.actionHelp)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.actionAbout)
        self.menuView.addAction(self.actionExpand_All)
        self.menuView.addAction(self.actionCollapse_All)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSelect_All)
        self.menuView.addAction(self.actionUnselect_All)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionGrouped)
        self.menuView.addAction(self.menuTitle_View.menuAction())
        self.menuTitle_View.addAction(self.actionCode_Title)
        self.menuTitle_View.addAction(self.actionShort_Title)
        self.menuTitle_View.addAction(self.actionFull_Title)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JWL Manager", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save archive", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"&Import...", None))
#if QT_CONFIG(shortcut)
        self.actionImport.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionReindex.setText(QCoreApplication.translate("MainWindow", u"&Reindex", None))
#if QT_CONFIG(shortcut)
        self.actionReindex.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"&About...", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save &As...", None))
#if QT_CONFIG(tooltip)
        self.actionSave_As.setToolTip(QCoreApplication.translate("MainWindow", u"Save archive as...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExpand_All.setText(QCoreApplication.translate("MainWindow", u"E&xpand All", None))
#if QT_CONFIG(tooltip)
        self.actionExpand_All.setToolTip(QCoreApplication.translate("MainWindow", u"Expand all items", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionExpand_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionCollapse_All.setText(QCoreApplication.translate("MainWindow", u"&Collapse All", None))
#if QT_CONFIG(tooltip)
        self.actionCollapse_All.setToolTip(QCoreApplication.translate("MainWindow", u"Collapse all items", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCollapse_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_All.setText(QCoreApplication.translate("MainWindow", u"&Select All", None))
#if QT_CONFIG(tooltip)
        self.actionSelect_All.setToolTip(QCoreApplication.translate("MainWindow", u"Select all items", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSelect_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnselect_All.setText(QCoreApplication.translate("MainWindow", u"&Unselect All", None))
#if QT_CONFIG(tooltip)
        self.actionUnselect_All.setToolTip(QCoreApplication.translate("MainWindow", u"Unselect all items", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionUnselect_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionCode_Title.setText(QCoreApplication.translate("MainWindow", u"&Code", None))
#if QT_CONFIG(tooltip)
        self.actionCode_Title.setToolTip(QCoreApplication.translate("MainWindow", u"Use publication code as title", None))
#endif // QT_CONFIG(tooltip)
        self.actionShort_Title.setText(QCoreApplication.translate("MainWindow", u"&Short Title", None))
#if QT_CONFIG(tooltip)
        self.actionShort_Title.setToolTip(QCoreApplication.translate("MainWindow", u"Use short publication title", None))
#endif // QT_CONFIG(tooltip)
        self.actionFull_Title.setText(QCoreApplication.translate("MainWindow", u"&Full Title", None))
#if QT_CONFIG(tooltip)
        self.actionFull_Title.setToolTip(QCoreApplication.translate("MainWindow", u"Use full publication title", None))
#endif // QT_CONFIG(tooltip)
        self.actionGrouped.setText(QCoreApplication.translate("MainWindow", u"&Grouped", None))
#if QT_CONFIG(tooltip)
        self.actionGrouped.setToolTip(QCoreApplication.translate("MainWindow", u"Group publications by category", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionGrouped.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"Total: ", None))
        self.label_selected.setText(QCoreApplication.translate("MainWindow", u"Selected: ", None))
        self.total.setText("")
        self.selected.setText("")
#if QT_CONFIG(tooltip)
        self.label_category.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_category.setText(QCoreApplication.translate("MainWindow", u"&Category:", None))
        self.combo_category.setItemText(0, QCoreApplication.translate("MainWindow", u"Notes", None))
        self.combo_category.setItemText(1, QCoreApplication.translate("MainWindow", u"Highlights", None))
        self.combo_category.setItemText(2, QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.combo_category.setItemText(3, QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.combo_category.setItemText(4, QCoreApplication.translate("MainWindow", u"Annotations", None))

#if QT_CONFIG(tooltip)
        self.combo_category.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_grouping.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_grouping.setText(QCoreApplication.translate("MainWindow", u"&Grouping:", None))
        self.combo_grouping.setItemText(0, QCoreApplication.translate("MainWindow", u"Publication", None))
        self.combo_grouping.setItemText(1, QCoreApplication.translate("MainWindow", u"Language", None))
        self.combo_grouping.setItemText(2, QCoreApplication.translate("MainWindow", u"Year", None))
        self.combo_grouping.setItemText(3, QCoreApplication.translate("MainWindow", u"Tag", None))
        self.combo_grouping.setItemText(4, QCoreApplication.translate("MainWindow", u"Color", None))

#if QT_CONFIG(tooltip)
        self.combo_grouping.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.button_export.setText(QCoreApplication.translate("MainWindow", u"&Export", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"&Delete", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Count", None));
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
#if QT_CONFIG(tooltip)
        self.menuTitle_View.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.menuTitle_View.setTitle(QCoreApplication.translate("MainWindow", u"&Title View", None))
    # retranslateUi

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)