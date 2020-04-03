# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Aug 02 08:32:04 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import sys
import cv2
import numpy as np
from PySide2 import QtCore, QtGui, QtWidgets
import io, json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1206, 633)
        self.sourcePanel = QtWidgets.QLabel(Dialog)
        self.sourcePanel.setGeometry(QtCore.QRect(20, 70, 320, 240))
        self.sourcePanel.setFrameShape(QtWidgets.QFrame.Panel)
        self.sourcePanel.setText("")
        self.sourcePanel.setObjectName("sourcePanel")
        self.destPanel_1 = QtWidgets.QLabel(Dialog)
        self.destPanel_1.setGeometry(QtCore.QRect(390, 40, 240, 180))
        self.destPanel_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.destPanel_1.setText("")
        self.destPanel_1.setObjectName("destPanel_1")
        self.destPanel_2 = QtWidgets.QLabel(Dialog)
        self.destPanel_2.setGeometry(QtCore.QRect(390, 240, 240, 180))
        self.destPanel_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.destPanel_2.setText("")
        self.destPanel_2.setObjectName("destPanel_2")
        self.destPanel_3 = QtWidgets.QLabel(Dialog)
        self.destPanel_3.setGeometry(QtCore.QRect(390, 440, 240, 180))
        self.destPanel_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.destPanel_3.setText("")
        self.destPanel_3.setObjectName("destPanel_3")
        self.comboBoxCSpaces = QtWidgets.QComboBox(Dialog)
        self.comboBoxCSpaces.setGeometry(QtCore.QRect(180, 330, 161, 31))
        self.comboBoxCSpaces.setObjectName("comboBoxCSpaces")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.comboBoxCSpaces.addItem("")
        self.imageName = QtWidgets.QLineEdit(Dialog)
        self.imageName.setGeometry(QtCore.QRect(20, 40, 281, 20))
        self.imageName.setObjectName("imageName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 330, 161, 31))
        self.label.setObjectName("label")
        self.pushButtonLoad = QtWidgets.QPushButton(Dialog)
        self.pushButtonLoad.setGeometry(QtCore.QRect(310, 40, 31, 21))
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.filteredPanel = QtWidgets.QLabel(Dialog)
        self.filteredPanel.setGeometry(QtCore.QRect(710, 90, 480, 360))
        self.filteredPanel.setFrameShape(QtWidgets.QFrame.Panel)
        self.filteredPanel.setText("")
        self.filteredPanel.setObjectName("filteredPanel")
        self.vsMinCh_1 = QtWidgets.QSlider(Dialog)
        self.vsMinCh_1.setGeometry(QtCore.QRect(640, 40, 20, 181))
        self.vsMinCh_1.setMaximum(255)
        self.vsMinCh_1.setOrientation(QtCore.Qt.Vertical)
        self.vsMinCh_1.setObjectName("vsMinCh_1")
        self.vsMaxCh_1 = QtWidgets.QSlider(Dialog)
        self.vsMaxCh_1.setGeometry(QtCore.QRect(660, 40, 20, 181))
        self.vsMaxCh_1.setMaximum(255)
        self.vsMaxCh_1.setProperty("value", 255)
        self.vsMaxCh_1.setOrientation(QtCore.Qt.Vertical)
        self.vsMaxCh_1.setObjectName("vsMaxCh_1")
        self.vsMaxCh_2 = QtWidgets.QSlider(Dialog)
        self.vsMaxCh_2.setGeometry(QtCore.QRect(660, 240, 20, 181))
        self.vsMaxCh_2.setMaximum(255)
        self.vsMaxCh_2.setProperty("value", 255)
        self.vsMaxCh_2.setOrientation(QtCore.Qt.Vertical)
        self.vsMaxCh_2.setObjectName("vsMaxCh_2")
        self.vsMinCh_2 = QtWidgets.QSlider(Dialog)
        self.vsMinCh_2.setGeometry(QtCore.QRect(640, 240, 20, 181))
        self.vsMinCh_2.setMaximum(255)
        self.vsMinCh_2.setOrientation(QtCore.Qt.Vertical)
        self.vsMinCh_2.setObjectName("vsMinCh_2")
        self.vsMaxCh_3 = QtWidgets.QSlider(Dialog)
        self.vsMaxCh_3.setGeometry(QtCore.QRect(660, 440, 20, 181))
        self.vsMaxCh_3.setMaximum(255)
        self.vsMaxCh_3.setProperty("value", 255)
        self.vsMaxCh_3.setOrientation(QtCore.Qt.Vertical)
        self.vsMaxCh_3.setObjectName("vsMaxCh_3")
        self.vsMinCh_3 = QtWidgets.QSlider(Dialog)
        self.vsMinCh_3.setGeometry(QtCore.QRect(640, 440, 20, 181))
        self.vsMinCh_3.setMaximum(255)
        self.vsMinCh_3.setOrientation(QtCore.Qt.Vertical)
        self.vsMinCh_3.setObjectName("vsMinCh_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(360, 0, 20, 631))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(673, 0, 31, 631))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_CName = QtWidgets.QLabel(Dialog)
        self.label_CName.setGeometry(QtCore.QRect(390, 6, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CName.setFont(font)
        self.label_CName.setObjectName("label_CName")
        self.lineEdit_FilterText = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_FilterText.setGeometry(QtCore.QRect(710, 60, 421, 20))
        self.lineEdit_FilterText.setText("")
        self.lineEdit_FilterText.setObjectName("lineEdit_FilterText")
        self.label_CName_2 = QtWidgets.QLabel(Dialog)
        self.label_CName_2.setGeometry(QtCore.QRect(710, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CName_2.setFont(font)
        self.label_CName_2.setObjectName("label_CName_2")
        self.pushButtonSaveOutImage = QtWidgets.QPushButton(Dialog)
        self.pushButtonSaveOutImage.setGeometry(QtCore.QRect(720, 460, 101, 23))
        self.pushButtonSaveOutImage.setObjectName("pushButtonSaveOutImage")
        self.pushButtonSaveOutMask = QtWidgets.QPushButton(Dialog)
        self.pushButtonSaveOutMask.setGeometry(QtCore.QRect(840, 460, 101, 23))
        self.pushButtonSaveOutMask.setObjectName("pushButtonSaveOutMask")
        self.pushButtonSaveFilter = QtWidgets.QPushButton(Dialog)
        self.pushButtonSaveFilter.setGeometry(QtCore.QRect(10, 430, 101, 23))
        self.pushButtonSaveFilter.setObjectName("pushButtonSaveFilter")
        self.pushButtonLoadFilter = QtWidgets.QPushButton(Dialog)
        self.pushButtonLoadFilter.setGeometry(QtCore.QRect(130, 430, 101, 23))
        self.pushButtonLoadFilter.setObjectName("pushButtonLoadFilter")
        self.pushButtonResetFilter = QtWidgets.QPushButton(Dialog)
        self.pushButtonResetFilter.setGeometry(QtCore.QRect(240, 430, 101, 23))
        self.pushButtonResetFilter.setObjectName("pushButtonResetFilter")
        self.label_CName_3 = QtWidgets.QLabel(Dialog)
        self.label_CName_3.setGeometry(QtCore.QRect(20, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CName_3.setFont(font)
        self.label_CName_3.setObjectName("label_CName_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(1020, 470, 161, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButtonMask = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMask.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButtonMask.setObjectName("radioButtonMask")
        self.radioButtonMaskedImg = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMaskedImg.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.radioButtonMaskedImg.setChecked(True)
        self.radioButtonMaskedImg.setObjectName("radioButtonMaskedImg")
        self.radioButtonReverseMask = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonReverseMask.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButtonReverseMask.setObjectName("radioButtonReverseMask")
        self.radioButtonReverseMaskedImg = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonReverseMaskedImg.setGeometry(QtCore.QRect(10, 80, 151, 17))
        self.radioButtonReverseMaskedImg.setObjectName("radioButtonReverseMaskedImg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Aded Later
        self.img = None
        self.dImg = None
        self.oImg = None
        self.chImgs = [None,None,None]
        self.fileName = ''

        #Event Connections
        self.pushButtonLoad.clicked.connect(self.selectFile)
        self.comboBoxCSpaces.currentIndexChanged.connect(self.convert_show)

        self.vsMaxCh_1.valueChanged.connect(self.on_vsChanged)
        self.vsMaxCh_2.valueChanged.connect(self.on_vsChanged)
        self.vsMaxCh_3.valueChanged.connect(self.on_vsChanged)
        self.vsMinCh_1.valueChanged.connect(self.on_vsChanged)
        self.vsMinCh_2.valueChanged.connect(self.on_vsChanged)
        self.vsMinCh_3.valueChanged.connect(self.on_vsChanged)

        self.radioButtonMask.clicked.connect(self.on_Mask)
        self.radioButtonMaskedImg.clicked.connect(self.on_Mask)
        self.radioButtonReverseMask.clicked.connect(self.on_Mask)
        self.radioButtonReverseMaskedImg.clicked.connect(self.on_Mask)

        self.pushButtonSaveOutMask.clicked.connect(self.onSaveOut)
        self.pushButtonSaveOutImage.clicked.connect(self.onSaveOut)

        self.pushButtonSaveFilter.clicked.connect(self.onSaveFilter)
        self.pushButtonLoadFilter.clicked.connect(self.onLoadFilter)

        self.Init()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Renk Filitresi", None))
        self.comboBoxCSpaces.setItemText(0, QtWidgets.QApplication.translate("Dialog", "RGB", None))
        self.comboBoxCSpaces.setItemText(1, QtWidgets.QApplication.translate("Dialog", "CIE XYZ", None))
        self.comboBoxCSpaces.setItemText(2, QtWidgets.QApplication.translate("Dialog", "YCrCb JPEG", None))
        self.comboBoxCSpaces.setItemText(3, QtWidgets.QApplication.translate("Dialog", "HSV", None))
        self.comboBoxCSpaces.setItemText(4, QtWidgets.QApplication.translate("Dialog", "HLS", None))
        self.comboBoxCSpaces.setItemText(5, QtWidgets.QApplication.translate("Dialog", "CIE Lab", None))
        self.comboBoxCSpaces.setItemText(6, QtWidgets.QApplication.translate("Dialog", "CIE Luv", None))
        self.comboBoxCSpaces.setItemText(7, QtWidgets.QApplication.translate("Dialog", "YUV", None))
        self.imageName.setText(QtWidgets.QApplication.translate("Dialog", "../datas/colorTable.jpg", None))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Dönüştürülecek Renk Uzayı       :", None))
        self.pushButtonLoad.setText(QtWidgets.QApplication.translate("Dialog", "...", None))
        self.label_CName.setText(QtWidgets.QApplication.translate("Dialog", "RGB Kanalları", None))
        self.label_CName_2.setText(QtWidgets.QApplication.translate("Dialog", "Filtrelenmiş Görüntü", None))
        self.pushButtonSaveOutImage.setText(QtWidgets.QApplication.translate("Dialog", "Görüntüyü Kaydet", None))
        self.pushButtonSaveOutMask.setText(QtWidgets.QApplication.translate("Dialog", "Maskeyi Kaydet", None))
        self.pushButtonSaveFilter.setText(QtWidgets.QApplication.translate("Dialog", "Filitreyi  Kaydet", None))
        self.pushButtonLoadFilter.setText(QtWidgets.QApplication.translate("Dialog", "Filitreyi Yükle", None))
        self.pushButtonResetFilter.setText(QtWidgets.QApplication.translate("Dialog", "Filitreyi Sıfırla", None))
        self.label_CName_3.setText(QtWidgets.QApplication.translate("Dialog", "Başlangıç Görüntüsü", None))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Seçenekler", None))
        self.radioButtonMask.setText(QtWidgets.QApplication.translate("Dialog", "Maske", None))
        self.radioButtonMaskedImg.setText(QtWidgets.QApplication.translate("Dialog", "Maskelenmiş Görüntü", None))
        self.radioButtonReverseMask.setText(QtWidgets.QApplication.translate("Dialog", "Ters Maske", None))
        self.radioButtonReverseMaskedImg.setText(QtWidgets.QApplication.translate("Dialog", "Ters Maskelenmiş Görüntü", None))

    def Init(self):
        self.fileName = self.imageName.text()
        self.load_Img()
        return;

    def load_Img(self):
        self.img = cv2.imread(self.fileName)
        self.showImg(self.sourcePanel,self.img)
        self.convert_show()
        self.reset_sliders()
        self.show_output()
        return

    def showImg(self,label,img):
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        height, width, byteValue = img.shape
        byteValue = byteValue * width
        timg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(timg.data, width, height,byteValue, QtGui.QImage.Format_RGB888)
        label.setPixmap(QtGui.QPixmap(image).scaled(label.size(),aspectMode=QtCore.Qt.KeepAspectRatio))

    def selectFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(Dialog, "Open Image", "..", "Image Files (*.png *.jpg *.bmp)")
        self.imageName.setText(fileName[0])
        self.fileName = fileName[0]
        self.load_Img()


    def convert_show(self):
        codes=[cv2.COLOR_BGR2RGB,
               cv2.COLOR_BGR2XYZ,
               cv2.COLOR_BGR2YCrCb,
               cv2.COLOR_BGR2HSV,
               cv2.COLOR_BGR2HLS,
               cv2.COLOR_BGR2Lab,
               cv2.COLOR_BGR2Luv,
               cv2.COLOR_BGR2YUV
                ];
        ix = self.comboBoxCSpaces.currentIndex()
        self.dImg = cv2.cvtColor(self.img,codes[ix]);

        # split
        self.chImgs[0] = self.dImg[:,:,0]
        self.chImgs[1] = self.dImg[:,:,1]
        self.chImgs[2] = self.dImg[:,:,2]
        self.label_CName.setText(self.comboBoxCSpaces.currentText()+ u'Kanalları')
        self.showImg(self.destPanel_1,self.chImgs[0])
        self.showImg(self.destPanel_2,self.chImgs[1])
        self.showImg(self.destPanel_3,self.chImgs[2])
        self.reset_sliders()
        self.show_output()
        return

    def reset_sliders(self):
        self.vsMinCh_1.setValue(0)
        self.vsMaxCh_1.setValue(255)
        self.vsMinCh_2.setValue(0)
        self.vsMaxCh_2.setValue(255)
        self.vsMinCh_3.setValue(0)
        self.vsMaxCh_3.setValue(255)
        return

    def show_output(self):
        lower_filt = (self.vsMinCh_1.value(),self.vsMinCh_2.value(),self.vsMinCh_3.value())
        upper_filt = (self.vsMaxCh_1.value(),self.vsMaxCh_2.value(),self.vsMaxCh_3.value())
        mask = cv2.inRange(self.dImg, lower_filt, upper_filt)

        if self.radioButtonMask.isChecked():
            self.oImg = mask
        elif self.radioButtonMaskedImg.isChecked():
            self.oImg=cv2.bitwise_and(self.img,self.img,mask = mask)
        elif self.radioButtonReverseMask.isChecked():
            self.oImg = cv2.bitwise_not(mask)
        elif self.radioButtonReverseMaskedImg.isChecked():
            self.oImg=cv2.bitwise_and(self.img,self.img,mask = cv2.bitwise_not(mask))

        self.showImg(self.filteredPanel,self.oImg)

        ft = 'Min : '+str(lower_filt)+' - Max : '+str(upper_filt)
        self.lineEdit_FilterText.setText(ft)
        return

    def on_vsChanged(self):
        if self.vsMinCh_1.value() >= self.vsMaxCh_1.value() :
            if self.vsMinCh_1.value() :
                self.vsMinCh_1.setValue(self.vsMinCh_1.value()-1)
            else:
                self.vsMaxCh_1.setValue(self.vsMaxCh_1.value()+1)

        if self.vsMinCh_2.value() >= self.vsMaxCh_2.value() :
            if self.vsMinCh_2.value() :
                self.vsMinCh_2.setValue(self.vsMinCh_2.value()-1)
            else:
                self.vsMaxCh_2.setValue(self.vsMaxCh_2.value()+1)

        if self.vsMinCh_3.value() >= self.vsMaxCh_3.value() :
            if self.vsMinCh_3.value() :
                self.vsMinCh_3.setValue(self.vsMinCh_3.value()-1)
            else:
                self.vsMaxCh_3.setValue(self.vsMaxCh_3.value()+1)

        self.show_output()

    def on_Mask(self):
        self.show_output()

    def onSaveOut(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(Dialog, "Save Out Image", "..", "Image Files (*.png *.jpg *.bmp)")
        if fileName[0] !='' :
            cv2.imwrite(fileName[0],self.oImg)

    def onSaveFilter(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(Dialog, "Save Filter Parameters ", "..", "Filter Files (*.txt)")
        if fileName[0] !='' :
            lower_filt = (self.vsMinCh_1.value(),self.vsMinCh_2.value(),self.vsMinCh_3.value())
            upper_filt = (self.vsMaxCh_1.value(),self.vsMaxCh_2.value(),self.vsMaxCh_3.value())
            data = {'Lower':lower_filt,
                    'Upper':upper_filt,
                    'ColorSpace':self.comboBoxCSpaces.currentIndex()
                    }
            with io.open(fileName[0], 'w', encoding='utf-8') as f:
                f.write(unicode(json.dumps(data, ensure_ascii=False)))

        return

    def onLoadFilter(self):
        """

        import json
        my_data = json.loads(open("xyz.json").read())

        print my_data
        """

        fileName = QtWidgets.QFileDialog.getOpenFileName(Dialog, "Load Filter Parameters ", "..", "Filter Files (*.txt)")
        if fileName[0] !='' :
            with open(fileName[0]) as json_file:
                json_data = json.load(json_file)
                print(json_data)
                lower_filt = json_data[u'Lower']
                upper_filt = json_data[u'Upper']
                ix = json_data[u'ColorSpace']
                self.comboBoxCSpaces.setCurrentIndex(ix)

                self.vsMinCh_1.setValue(lower_filt[0])
                self.vsMinCh_2.setValue(lower_filt[1])
                self.vsMinCh_3.setValue(lower_filt[2])

                self.vsMaxCh_1.setValue(upper_filt[0])
                self.vsMaxCh_2.setValue(upper_filt[1])
                self.vsMaxCh_3.setValue(upper_filt[2])

                self
        return


# Create the Qt Application
app = QtWidgets.QApplication(sys.argv)
# Create and show the form
form = Ui_Dialog()
Dialog = QtWidgets.QDialog()
form.setupUi(Dialog)
Dialog.show()
# Run the main Qt loop
sys.exit(app.exec_())
