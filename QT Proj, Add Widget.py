import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QPushButton  #QMainwindow has more class than QWidget
from PyQt5.Qt import QLabel, QHBoxLayout, QVBoxLayout
class GUI(QMainWindow): #inheriting from Qwidget in our GUI class

    def __init__(self):
        super().__init__() #initialize super class which creates the window
        self.initUI() #refer to window as a self

    def initUI(self):
        self.setWindowTitle("PyQT5 GUI") #add widget and property
        self.resize(400,300)
        self.add_menus_and_status()
        self.positional_widget_layout()
    def positional_widget_layout(self):
        label_1= QLabel("our 1st Label", self) #instance/object of a Qlabel class
        print(self.menuBar().size())   #default size (100,30)
        mbar_height=self.menuBar().height() #storing menu bar height in a variable
        print(mbar_height) #just to check, it should be 30 by default
        label_1.move(10,mbar_height)
        label_2= QLabel("Another label", self)
        label_2.move(10,mbar_height*2)

        button_1=QPushButton("Click 1",self)
        button_2=QPushButton('Click 2', self)
        button_1.move(label_1.width(), label_1.height())
        button_2.move(label_1.width(), label_1.height()*2)
    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in statusbar')
        menubar=self.menuBar()
        file_menu=menubar.addMenu("File")
        new_action=QAction("New",self)
        file_menu.addAction(new_action)
        new_action.setStatusTip("New File")
        file_menu.addSeparator()  #adding seperator line
        exit_action=QAction("Exit",self)
        exit_action.setStatusTip("Click to exit")
        file_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut("Ctrl+Q")

        edit_menu=menubar.addMenu("Edit")


if __name__=="__main__":
    app=QApplication(sys.argv) #application created
    gui=GUI() #object of GUI class
    gui.show()  #using show attribute of Qwidget class inherited in GUI class
    sys.exit(app.exec_())