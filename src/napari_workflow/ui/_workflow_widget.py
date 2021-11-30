# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_workflow_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 587)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.workflow = QtWidgets.QToolBox(Form)
        self.workflow.setObjectName("workflow")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 382, 542))
        self.page.setObjectName("page")
        self.workflow.addItem(self.page, "")
        self.gridLayout.addWidget(self.workflow, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.workflow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.workflow.setItemText(self.workflow.indexOf(self.page), _translate("Form", "Input"))

