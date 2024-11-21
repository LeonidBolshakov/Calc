# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 540)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnRun = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRun.setMinimumSize(QtCore.QSize(156, 60))
        self.btnRun.setMaximumSize(QtCore.QSize(156, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.btnRun.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnRun.setFont(font)
        self.btnRun.setObjectName("btnRun")
        self.verticalLayout_3.addWidget(self.btnRun)
        self.btnCopy = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCopy.sizePolicy().hasHeightForWidth())
        self.btnCopy.setSizePolicy(sizePolicy)
        self.btnCopy.setMinimumSize(QtCore.QSize(156, 60))
        self.btnCopy.setMaximumSize(QtCore.QSize(156, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.btnCopy.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(14)
        self.btnCopy.setFont(font)
        self.btnCopy.setObjectName("btnCopy")
        self.verticalLayout_3.addWidget(self.btnCopy)
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        self.btnClear.setMinimumSize(QtCore.QSize(156, 60))
        self.btnClear.setMaximumSize(QtCore.QSize(156, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.btnClear.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(14)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout_3.addWidget(self.btnClear)
        self.btnHelp = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHelp.sizePolicy().hasHeightForWidth())
        self.btnHelp.setSizePolicy(sizePolicy)
        self.btnHelp.setMinimumSize(QtCore.QSize(156, 60))
        self.btnHelp.setMaximumSize(QtCore.QSize(156, 60))
        self.btnHelp.setSizeIncrement(QtCore.QSize(0, 20))
        self.btnHelp.setBaseSize(QtCore.QSize(156, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.btnHelp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(14)
        self.btnHelp.setFont(font)
        self.btnHelp.setObjectName("btnHelp")
        self.verticalLayout_3.addWidget(self.btnHelp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRound = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRound.sizePolicy().hasHeightForWidth())
        self.btnRound.setSizePolicy(sizePolicy)
        self.btnRound.setMinimumSize(QtCore.QSize(108, 60))
        self.btnRound.setMaximumSize(QtCore.QSize(110, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.btnRound.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(13)
        self.btnRound.setFont(font)
        self.btnRound.setObjectName("btnRound")
        self.horizontalLayout.addWidget(self.btnRound)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(40, 10))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineRoundDigit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineRoundDigit.setMinimumSize(QtCore.QSize(31, 31))
        self.lineRoundDigit.setMaximumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineRoundDigit.setFont(font)
        self.lineRoundDigit.setObjectName("lineRoundDigit")
        self.verticalLayout_2.addWidget(self.lineRoundDigit)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(40, 10))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.btnExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnExit.setMinimumSize(QtCore.QSize(156, 60))
        self.btnExit.setMaximumSize(QtCore.QSize(156, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.btnExit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout_3.addWidget(self.btnExit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_3.setPalette(palette)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.txtFormula = CustomTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFormula.sizePolicy().hasHeightForWidth())
        self.txtFormula.setSizePolicy(sizePolicy)
        self.txtFormula.setMaximumSize(QtCore.QSize(16777215, 64))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.txtFormula.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtFormula.setFont(font)
        self.txtFormula.setObjectName("txtFormula")
        self.verticalLayout.addWidget(self.txtFormula)
        self.txtResult = QtWidgets.QTextBrowser(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtResult.sizePolicy().hasHeightForWidth())
        self.txtResult.setSizePolicy(sizePolicy)
        self.txtResult.setMaximumSize(QtCore.QSize(16777215, 38))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.txtResult.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtResult.setFont(font)
        self.txtResult.setPlaceholderText("")
        self.txtResult.setObjectName("txtResult")
        self.verticalLayout.addWidget(self.txtResult)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_4.setPalette(palette)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tblResults = QtWidgets.QTableWidget(parent=self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(151, 189, 141))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 189, 161))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 189, 141))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 189, 161))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.tblResults.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tblResults.setFont(font)
        self.tblResults.setObjectName("tblResults")
        self.tblResults.setColumnCount(0)
        self.tblResults.setRowCount(0)
        self.verticalLayout.addWidget(self.tblResults)
        self.lblInf2 = QtWidgets.QLabel(parent=self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.lblInf2.setPalette(palette)
        self.lblInf2.setObjectName("lblInf2")
        self.verticalLayout.addWidget(self.lblInf2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.btnRun.setText(_translate("MainWindow", "&Вычислить"))
        self.btnCopy.setText(_translate("MainWindow", "&Копировать\n"
"Результат"))
        self.btnClear.setText(_translate("MainWindow", "О&чистить\n"
"всё"))
        self.btnHelp.setText(_translate("MainWindow", "&Справка"))
        self.btnRound.setText(_translate("MainWindow", "&Округлить\n"
"результат"))
        self.label.setText(_translate("MainWindow", "до"))
        self.label_2.setText(_translate("MainWindow", "знаков"))
        self.btnExit.setText(_translate("MainWindow", "В&ыйти"))
        self.label_3.setText(_translate("MainWindow", "Здесь надо вводить формулу. Например, 2.74**3*(17,3-4.87)"))
        self.label_4.setText(_translate("MainWindow", "Нажатие буквы \"С\", слева от строчки истории,\n"
"копирует формулу в буфер обмена"))
        self.lblInf2.setText(_translate("MainWindow", "История формул и результатов, по окончанию работы программы,\n"
"будет записана в файл #"))
from customtextedit import CustomTextEdit
