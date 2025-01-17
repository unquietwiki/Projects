from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

# import files of various UI pages used in the Project (Workflow)
from Negative_Image_Screen import Ui_Background
from Down_Sampling_Image_Screen import Ui_Dialog
from Up_Sampling_Image_Screen import Ui_Dialog_1
from Thresholding_Without_Background import Ui_Dialog_2
from Thresholding_With_Background import Ui_Dialog_3
from Blur_Image_Screen import Ui_Dialog_4
from LPF_Image_Screen import Ui_Dialog_5
from Gaussian_Image_Screen import Ui_Dialog_6
from Facial_Features_Image_Screen import Ui_Dialog_7
from Laplace_Screen import Ui_Dialog_8


class Ui_Image_Processing_Options(object):
    def setupUi(self, Image_Processing_Options):
        Image_Processing_Options.setObjectName("Image_Processing_Options")
        Image_Processing_Options.resize(1201, 801)
        self.DownSampling_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.DownSampling_Button.setGeometry(QtCore.QRect(170, 180, 211, 61))
        self.DownSampling_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.DownSampling_Button.setObjectName("DownSampling_Button")
        self.UpSampling_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.UpSampling_Button.setGeometry(QtCore.QRect(170, 310, 211, 61))
        self.UpSampling_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.UpSampling_Button.setObjectName("UpSampling_Button")
        self.Negative_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Negative_Button.setGeometry(QtCore.QRect(170, 430, 211, 61))
        self.Negative_Button.setStyleSheet("font: 11.5pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Negative_Button.setObjectName("Negative_Button")
        self.Threshold_With_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Threshold_With_Button.setGeometry(QtCore.QRect(170, 550, 211, 61))
        self.Threshold_With_Button.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Threshold_With_Button.setObjectName("Threshold_With_Button")
        self.Threshold_Without_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Threshold_Without_Button.setGeometry(QtCore.QRect(770, 180, 211, 61))
        self.Threshold_Without_Button.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Threshold_Without_Button.setObjectName("Threshold_Without_Button")
        self.Blur_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Blur_Button.setGeometry(QtCore.QRect(770, 310, 211, 61))
        self.Blur_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Blur_Button.setObjectName("Blur_Button")
        self.LPF_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.LPF_Button.setGeometry(QtCore.QRect(770, 430, 211, 61))
        self.LPF_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.LPF_Button.setObjectName("LPF_Button")
        self.Gaussian_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Gaussian_Button.setGeometry(QtCore.QRect(770, 550, 211, 61))
        self.Gaussian_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")


        

        self.Facial_Feature_Detection_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Facial_Feature_Detection_Button.setGeometry(QtCore.QRect(120, 675, 380, 61))
        
        self.Facial_Feature_Detection_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Facial_Feature_Detection_Button.setObjectName("Facial_Feature_Detection_Button")
        



        self.Laplace_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Laplace_Button.setGeometry(QtCore.QRect(770, 675, 211, 61))
        
        self.Laplace_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Laplace_Button.setObjectName("Laplace_Button")




        self.Gaussian_Button.setObjectName("Gaussian_Button")
        self.Title = QtWidgets.QLabel(Image_Processing_Options)
        self.Title.setGeometry(QtCore.QRect(330, 60, 571, 71))
        self.Title.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        self.retranslateUi(Image_Processing_Options)
        QtCore.QMetaObject.connectSlotsByName(Image_Processing_Options)

    def retranslateUi(self, Image_Processing_Options):
        _translate = QtCore.QCoreApplication.translate
        Image_Processing_Options.setWindowTitle(_translate("Image_Processing_Options", "Dialog"))
        self.DownSampling_Button.setText(_translate("Image_Processing_Options", "Down Sampling"))
        self.UpSampling_Button.setText(_translate("Image_Processing_Options", "Up Sampling"))
        self.Negative_Button.setText(_translate("Image_Processing_Options", "Negative of the Image"))
        self.Threshold_With_Button.setText(_translate("Image_Processing_Options", "Thresholding with Background"))
        self.Threshold_Without_Button.setText(_translate("Image_Processing_Options", "Thresholding without Background"))
        self.Blur_Button.setText(_translate("Image_Processing_Options", "Apply Blurring"))
        self.LPF_Button.setText(_translate("Image_Processing_Options", "LPF"))
        self.Gaussian_Button.setText(_translate("Image_Processing_Options", "Gaussian Noise"))
        self.Facial_Feature_Detection_Button.setText(_translate("Image_Processing_Options", "Facial Feature Detection Button"))
        self.Laplace_Button.setText(_translate("Image_Processing_Options", "Laplace Button"))

        self.Title.setText(_translate("Image_Processing_Options", "Image Processing Options:"))



        # When user clicks the Down Sampling button:
        self.DownSampling_Button.clicked.connect(self.DownSamplingFunction)

        # When user clicks the Up Sampling button:
        self.UpSampling_Button.clicked.connect(self.UpSamplingFunction)

        # When user clicks the Down Sampling button:
        self.Negative_Button.clicked.connect(self.NegativeFunction)

        # When user clicks the Down Sampling button:
        self.Threshold_With_Button.clicked.connect(self.Threshold_WithFunction)

        # When user clicks the Down Sampling button:
        self.Threshold_Without_Button.clicked.connect(self.Threshold_WithoutFunction)

        # When user clicks the Down Sampling button:
        self.Blur_Button.clicked.connect(self.Blur_Function)

        # When user clicks the Down Sampling button:
        self.LPF_Button.clicked.connect(self.LPF_Function)

        # When user clicks the Down Sampling button:
        self.Gaussian_Button.clicked.connect(self.Gaussian_Function)

        # When user clicks the Facial_Feature_Detection_Button button:
        self.Facial_Feature_Detection_Button.clicked.connect(self.Facial_Feature_Detection_Function)

        # When user clicks the Laplace button:
        self.Laplace_Button.clicked.connect(self.Laplace_Function)



    def DownSamplingFunction(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def UpSamplingFunction(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_1()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def NegativeFunction(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Background()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()




    def Threshold_WithFunction(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_3()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def Threshold_WithoutFunction(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_2()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def Blur_Function(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_4()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def LPF_Function(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_5()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def Gaussian_Function(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_6()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def Facial_Feature_Detection_Function(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_7()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()

    def Laplace_Function(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_8()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        self.window.show()
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image_Processing_Options = QtWidgets.QDialog()
    ui = Ui_Image_Processing_Options()
    ui.setupUi(Image_Processing_Options)
    Image_Processing_Options.show()
    sys.exit(app.exec_())
