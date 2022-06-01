import sys
from PyQt5.QtWidgets import QApplication, QWidget #Instead of importing all classes, import only the needed ones from the module
app=QApplication(sys.argv) #creating an instance/object of the Qappplication class
win=QWidget() #creating an instance/object of the QWidget class
win.setWindowTitle("1st QT GUI") #setting title
win.resize(400,300)
win.show() #calling show function for the win
sys.exit(app.exec_()) #executing app, or running our application
