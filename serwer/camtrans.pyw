import os
import sys
import json
import glob
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from des import *
from lib.host import ipadd
import socket


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def __init__(self, ip, port, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.active_socket = None
        self.ip = ip
        self.port = port
        self.command = 'screen'

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)

    def run(self):
        self.data_connection, address = self.server.accept()
        self.active_socket = self.data_connection

        while True:
            if self.command.split(' ')[0] != 'screen':
                self.send_json(self.command.split(' '))
                responce = self.receive_json()
                self.mysignal.emit([responce])
                self.command = 'screen'
            if self.command.split(' ')[0] == 'screen':
                self.send_json(self.command.split(' '))
                responce = self.receive_json()
                self.mysignal.emit([responce])

    def send_json(self, data):
        try:
            json_data = json.dumps(data.decode('utf-8'))
        except:
            json_data = json.dumps(data)

        try:
            self.active_socket.send(json_data.encode('utf-8'))
        except ConnectionResetError:
            self.active_socket = None

    def receive_json(self):
        json_data = ''
        while True:
            try:
                if self.active_socket != None:
                    json_data += self.active_socket.recv(1024).decode('utf-8')
                    return json.loads(json_data)
                else:
                    return None
            except ValueError:
                pass


class VNCServer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip = ipadd
        self.port = 112
        self.thread_handler = MyThread(self.ip, self.port)
        self.thread_handler.start()

        self.thread_handler.mysignal.connect(self.screen_handler)

    def screen_handler(self, screen_value):
        data = ['mouse_move_to', 'mouse_left_click',
                'mouse_right_click', 'mouse_double_left_click']

        if screen_value[0] not in data:
            decrypt_image = base64.b64decode(screen_value[0])
            with open('cam2.png', 'wb') as file:
                file.write(decrypt_image)

            image = QtGui.QPixmap('cam2.png')
            self.ui.label.setPixmap(image)

    def closeEvent(self):
        for file in glob.glob('*.png'):
            try:
                os.remove(file)
            except:
                pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = VNCServer()
    myapp.show()
    sys.exit(app.exec_())
