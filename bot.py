import pyautogui
import time

def start_bot(num):
    #time.sleep(5)
    
    try:
        pyautogui.click('discord.PNG')
    except TypeError:
        try:
            pyautogui.click('discord2.PNG')
        except TypeError:
            print("not found")
        else:
            print("lets a go")
    else:
        print("yeyeyeyeyey")
        
    time.sleep(1)
    
    try:
        pyautogui.click('signythread.PNG')
    except TypeError:
        try:
            pyautogui.click('signythread2.PNG')
        except TypeError:
            print("not found")
        else:
            ("wowowowow")
    else:
        print("we did well")
        
    time.sleep(1)
    
    #pyautogui.click('message.PNG')
    time.sleep(1)
    pyautogui.write('The signy bot is now starting.')
    pyautogui.press('enter')

    for i in range(num):
        pyautogui.write(':signy:')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('+:signy:')
        pyautogui.press('enter')
        time.sleep(2)
