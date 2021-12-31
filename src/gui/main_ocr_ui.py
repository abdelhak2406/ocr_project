# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/main_ocr.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.brows_btn = QtWidgets.QPushButton(self.centralwidget)
        self.brows_btn.setGeometry(QtCore.QRect(1080, 570, 87, 27))
        self.brows_btn.setObjectName("brows_btn")
        self.display_selected_file = QtWidgets.QTextBrowser(self.centralwidget)
        self.display_selected_file.setGeometry(QtCore.QRect(400, 570, 661, 31))
        self.display_selected_file.setObjectName("display_selected_file")
        self.img_display = QtWidgets.QLabel(self.centralwidget)
        self.img_display.setGeometry(QtCore.QRect(380, 50, 811, 471))
        self.img_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.img_display.setMidLineWidth(1)
        self.img_display.setText("")
        self.img_display.setObjectName("img_display")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 351, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.laplacian_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.laplacian_cbx.setObjectName("laplacian_cbx")
        self.verticalLayout.addWidget(self.laplacian_cbx)
        self.laplacian_8_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.laplacian_8_cbx.setObjectName("laplacian_8_cbx")
        self.verticalLayout.addWidget(self.laplacian_8_cbx)
        self.laplacian_rob_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.laplacian_rob_cbx.setObjectName("laplacian_rob_cbx")
        self.verticalLayout.addWidget(self.laplacian_rob_cbx)
        self.gauss_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.gauss_cbx.setObjectName("gauss_cbx")
        self.verticalLayout.addWidget(self.gauss_cbx)
        self.mean_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.mean_cbx.setObjectName("mean_cbx")
        self.verticalLayout.addWidget(self.mean_cbx)
        self.median_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.median_cbx.setObjectName("median_cbx")
        self.verticalLayout.addWidget(self.median_cbx)
        self.delate_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.delate_cbx.setObjectName("delate_cbx")
        self.verticalLayout.addWidget(self.delate_cbx)
        self.erode_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.erode_cbx.setObjectName("erode_cbx")
        self.verticalLayout.addWidget(self.erode_cbx)
        self.ouverture_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.ouverture_cbx.setObjectName("ouverture_cbx")
        self.verticalLayout.addWidget(self.ouverture_cbx)
        self.fermeture_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fermeture_cbx.setObjectName("fermeture_cbx")
        self.verticalLayout.addWidget(self.fermeture_cbx)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.adapt_th_int_img_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.adapt_th_int_img_cbx.setObjectName("adapt_th_int_img_cbx")
        self.verticalLayout.addWidget(self.adapt_th_int_img_cbx)
        self.otsu_cbx = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.otsu_cbx.setObjectName("otsu_cbx")
        self.verticalLayout.addWidget(self.otsu_cbx)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.apply_btn = QtWidgets.QPushButton(self.centralwidget)
        self.apply_btn.setGeometry(QtCore.QRect(90, 530, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.apply_btn.setFont(font)
        self.apply_btn.setObjectName("apply_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1229, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.brows_btn.setText(_translate("MainWindow", "Browse"))
        self.laplacian_cbx.setText(_translate("MainWindow", "Laplacian filter"))
        self.laplacian_8_cbx.setText(_translate("MainWindow", "laplacien 8 connec"))
        self.laplacian_rob_cbx.setText(_translate("MainWindow", "Laplacin robinson"))
        self.gauss_cbx.setText(_translate("MainWindow", "Gaussian filter"))
        self.mean_cbx.setText(_translate("MainWindow", "Mean filter"))
        self.median_cbx.setText(_translate("MainWindow", "Median filter"))
        self.delate_cbx.setText(_translate("MainWindow", "delate function"))
        self.erode_cbx.setText(_translate("MainWindow", "Erode function"))
        self.ouverture_cbx.setText(_translate("MainWindow", "Ouvertuer function"))
        self.fermeture_cbx.setText(_translate("MainWindow", "fermeture function"))
        self.label.setText(_translate("MainWindow", "Binarisation"))
        self.adapt_th_int_img_cbx.setText(_translate("MainWindow", "Adaptative threashold integral img"))
        self.otsu_cbx.setText(_translate("MainWindow", "otsu binarisation"))
        self.apply_btn.setText(_translate("MainWindow", "Apply "))

