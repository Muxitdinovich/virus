import os 
from time import sleep 
import keyboard as k 
from threading import Thread as thrd

key_name, flag_for, event = ("", "", "")
def key_pressed():
    def print_pressed_keys(e):
        global key_name, flag_for_key, event
        flag_for_key = True
        key_name = e.name
        event = e.event_type
        sleep(0.01)
    k.hook(print_pressed_keys)
    k.wait()

thrd(target=key_pressed).start()

sleep(1)

while key_name  != "q":
    os.system("start")

sleep(1)

os.system("taskkill /im cmd.exe")