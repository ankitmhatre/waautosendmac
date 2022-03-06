#!/usr/bin/env python3

from cgi import print_form
from curses import echo
from datetime import date, datetime, timedelta
import pyautogui
import time
import subprocess
import sys, getopt
import requests
import webbrowser

# openCommand = ["/usr/bin/open", "-W", "-n", "-a", "/Applications/WhatsApp.app"]
# fullScreenCommand = ["keystroke 'f' using {control down, command down}"]
# closeCommand = ['osascript', '-e' 'tell application "WhatsApp" to quit']
# proc = subprocess.Popen(openCommand, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



def closeApp():
    subprocess.Popen(closeApp, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def searchAndSend(name, msg):
    pyautogui.keyDown('command')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    pyautogui.keyUp('command')
    time.sleep(2)
    pyautogui.write(name, interval=0.01)
    time.sleep(5)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('a')
    pyautogui.keyDown('backspace')
    pyautogui.keyUp('backspace')
    pyautogui.keyUp('a')
    pyautogui.keyUp('command')
    pyautogui.write(msg, interval=0.01)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(2)

def makePyRequest(name, msg):
    url = "https://api.whatsapp.com/send?phone=" + name + "&text="+ msg
    webbrowser.open(url)
    time.sleep(30)
    pyautogui.click(500, 500)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    

def main(argv):
   now = datetime.now()
   provided_datetime = ''
   days_after = ''
   name = ''
   msg = ''
   i=0
   fullScreen = False
   try:
      opts, args = getopt.getopt(argv,"d:n:m:",["datetime=","name=", "message="])
   except getopt.GetoptError:
      print('failed to recognize arguments')
      sys.exit(2)
   for opt, arg in opts:
       if opt in ('-d', "--datetime"):
            provided_datetime = arg 
            days_after = (datetime.today()+timedelta(seconds=int(provided_datetime))).isoformat()  
       elif opt in ("-n", "--name"):
            name = arg
       elif opt in ("-m", "--message"):
            msg = arg
    
   #makePyRequest(name, msg)
   print(days_after)
#    if proc.poll() is not True:
#     while i<20:
#         time.sleep(0.5)
#         i=i+1
#     searchAndSend(name, msg)
    
    #closeApp()
    #sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])