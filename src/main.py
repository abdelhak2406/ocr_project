import sys


from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox,
        QFileDialog, QGraphicsPixmapItem,
         QListWidgetItem, QListWidget,
         QSlider
)

from PyQt5.QtGui import QPixmap, QImage

from PyQt5.uic import loadUi

from gui.main_ocr_ui import Ui_MainWindow
import cv2

from app  import binarisation, filtrage

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        print("hey i'm here!!")
        self.setupUi(self)
        self.connectSignalsSlots()
        self.init_list_widget()

    def init_list_widget(self):
        """init the list of widgets!"""
        # TODO use QSlider to slide the thing!
        # Use checkboxes 
        #  liste des value 
        #TODO : set the values like that!!
        self.mean_voisinage.setValue(3)
        self.median_value
        self.delate_value
        self.erode_value
        self.ouverture_value
        self.fermeture_value
        #itm = QListWidgetItem("Geeks")
        #itm = QSlider(self.listWidget,"slider")
        pass
        
        #self.listWidget.addItem(itm)

    def main_needed(self):
        """all the objects needed from the main.py in ir ect.
        
        Note: 
            TODO: we can optimize this i think """
    
    def connectSignalsSlots(self):
        """ Connecter every signal (bouton ect, to a fonction:).

        Note:
            * The equivalent of triggered of QAtion's triggered in QPushButton is: clicked
        """
        self.brows_btn.clicked.connect(self.browse) 
        self.apply_btn.clicked.connect(self.apply_filtre_bin)
        #self.search_by_query_btn.clicked.connect(self.search_by_query)
        #self.action_About.triggered.connect(self.about)

    def apply_filtre_bin(self) :
        """Here we gonna apply all the filters and display the image!"""
        # use 
        #self.get_selected_checkboxes()
        #self.list_selected

        # TODO - important- afficher les images! grayscale!

        try:
            self.img == None
        except :
            QMessageBox.about(self,"No Image Selected","please please select an image before applying any filter")
            return 
        self.transformed_img = self.img.copy()

        if(self.laplacian_cbx.isChecked()):
            # No problem with shape
            self.transformed_img = filtrage.laplacian_filter(self.transformed_img)
            
        if(self.laplacian_8_cbx.isChecked()):
            # no problem with shape
            self.transformed_img = filtrage.laplacian_8_connex(self.transformed_img)

        if(self.laplacian_rob_cbx.isChecked()):
            # No problem with shape
            self.transformed_img = filtrage.laplacian_robinson(self.transformed_img)

        if(self.gauss_cbx.isChecked()):
            # no problem with 2d 'normalement"
            self.transformed_img = filtrage.gaussian_filter(self.transformed_img)

        if(self.mean_cbx.isChecked()):
            voisinage = int(self.mean_voisinage.text())
            if (len(self.transformed_img.shape)) == 2:
                self.transformed_img = filtrage.mean_2D(self.transformed_img, voisinage)
            else:
                self.transformed_img = filtrage.mean_filter(self.transformed_img, voisinage)
            print("we entred mean!")
        if(self.median_cbx.isChecked()):
            voisinage = int(self.median_value.text())
            if (len(self.transformed_img.shape)) == 2:
                self.transformed_img = filtrage.median_2D(self.transformed_img,voisinage=3)
            else:
                self.transformed_img = filtrage.median_filter(self.transformed_img,voisinage=3)

        if(self.delate_cbx.isChecked()):
            # no problem with 2d 3d
            size_delate = int(self.delate_cbx.text())
            self.transformed_img = filtrage.delate_func(self.transformed_img, size_delate)

        if(self.erode_cbx.isChecked()):
            # no problem with 2d 3d
            size_erode = int(self.erode_cbx.text())
            self.transformed_img = filtrage.erode_func(self.transformed_img, size_erode)

        if(self.ouverture_cbx.isChecked()):
            # no problem with 2d 3d
            size_ouv = int( self.ouverture_value)
            self.transformed_img = filtrage.ouverture_func(self.transformed_img, size_ouv)

        if(self.fermeture_cbx.isChecked()):
            size_ferm = int(self.fermeture_value)
            self.transformed_img = filtrage.fermeture_func(self.transformed_img, size_ferm)





        # Binarisation
        if(self.otsu_cbx.isChecked()):
            #TODO:  add the sub_thresh! and condition maybe?
            self.transformed_img  =  binarisation.adaptive_threshold_integral_img(self.transformed_img)

        if (self.adapt_th_int_img_cbx.isChecked()):
            #TODO:this too do it!!
            self.transformed_img  =  binarisation.adaptive_threshold_otsu(self.transformed_img)
        

        # display the  new image

        self.display_img(self.transformed_img)

            

        

    def browse(self):
        """browse the files to select an image"""

        self.path_img,_=QFileDialog.getOpenFileName(filter='Image Files(*.png *.jpg *.bmp)')
        self.display_selected_file.setText(self.path_img)
        

        self.img = cv2.imread(self.path_img,cv2.IMREAD_COLOR)
        self.display_img(self.img)
        
        #self.img_display.setPixmap(QPixmap(self.path_img))

        """
        # this is something i don't know if it works
        img  = QImage(self.path_img)
        self.img_display.setPicture(img)
        self.img =  QPixmap.fromImage(img)
        self.img_display.setPixmap(self.img)
        """
    def display_img(self, img):
        """display the img in the right place!
        img     -- image in the cv2 representation! (color)or 
        #TODO: check if it can work with grayscale
        """
        img_tmp = self.convert_to_pixmap(img)
        self.img_display.setScaledContents(True)
        self.img_display.setPixmap(img_tmp)


    def put_new_img_in_label(self):
        """just a function that puts a*n imge in albl"""

        pass    

    def convert_to_pixmap(self, img):
        """convert an iamge to pixmal in order to display it!"""
        #TODO: what do this thing do?
        if len(img.shape) != 2:
            img = QImage(img.data, img.shape[1], img.shape[0], img.strides[0],QImage.Format_RGB888)
            img = img.rgbSwapped()
            img = QPixmap.fromImage(img)
        else:
            img = QImage(img.data, img.shape[1], img.shape[0], img.strides[0],QImage.Format_Grayscale8)
            img = img.rgbSwapped()
            img = QPixmap.fromImage(img)

        
        return img

    def get_selected_checkboxes(self):
        """Get all the checkboxes selected!"""
        self.list_selected = []
        
        if(self.laplacian_cbx.isChecked()):
            self.list_selected.append("laplacien")
            
        if(self.laplacian_8_cbx.isChecked()):
            self.list_selected.append("laplacien_8")

        if(self.laplacian_rob_cbx.isChecked()):
            self.list_selected.append("laplacien_rob")

        if(self.gauss_cbx.isChecked()):
            self.list_selected.append("gauss")

        if(self.mean_cbx.isChecked()):
            self.list_selected.append("mean")

        if(self.median_cbx.isChecked()):
            self.list_selected.append("median")

        if(self.delate_cbx.isChecked()):
            self.list_selected.append("delate")

        if(self.erode_cbx.isChecked()):
            self.list_selected.append("erode")

        if(self.ouverture_cbx.isChecked()):
            self.list_selected.append("ouverture")

        if(self.fermeture_cbx.isChecked()):
            self.list_selected.append("fermeture")

        # Binarisation
        if(self.otsu_cbx.isChecked()):
            self.list_selected.append("otsu")

        if (self.adapt_th_int_img_cbx.isChecked()):
            self.list_selected.append("adapt_th_int_img")
        
    def is_empty(self,word):
        """Check if a word is empy.and throw an error if it's the case!."""
        if (word==""):
            #TODO: update this lmesssagee
            QMessageBox.about(self, "Search query is empty", 
            "please write your query before clicking the search button")
        else:
            return False

    def radio_is_selected(self):
        """check if one of the QRadioButton  buttions are selected!
           TODO: UPDATE THIS ONE 

        Returns:
      
        """
        if (self.boolean_radio.isChecked() and self.vectorielle_radio.isChecked()):
            # this is normaly not possible TODO:throw an error
            exit("EROORRR")
        elif(self.boolean_radio.isChecked()):
            return 1
        elif(self.vectorielle_radio.isChecked()):
            return 2
        else:
            # No button is selected
            # TODO: prompt an Error instead of a QMessageBox
            QMessageBox.about(self, "Model not selected", 
            "please select one of the moodels boolean or vectorial")
            return False

    def about(self):

        QMessageBox.about(
            self,
            "About this Application",
            "<p>Built with &#9829; Time and lack of sleep by</p>"
            "<p>- Abdelhak Aissat</p>"
            "<p>- Youcef Azouaoui</p>"
            "<p>- The help of the guys at RealPython.com</p>",
        )


if __name__ == "__main__":

    appli = QApplication(sys.argv)

    win = Window()

    win.show()

    sys.exit(appli.exec())