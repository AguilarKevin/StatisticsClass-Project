import tkinter as tk
from view.mainframe import Application

window = tk.Tk()
app = Application(window)
app.mainloop()

#from PyQt5 import QtWidgets, uic
#import sys
#import os

#app = QtWidgets.QApplication([])


#if getattr(sys, 'frozen', False):
#    bundle_dir = sys._MEIPASS
#else:
#   bundle_dir = os.path.dirname(os.path.abspath(__file__))
#guipath = os.path.join( bundle_dir, 'main.ui' )

#win = uic.loadUi(guipath) #specify the location of your .ui file

#win.show()

#sys.exit(app.exec())