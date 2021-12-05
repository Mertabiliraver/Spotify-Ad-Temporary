
import win32con
import os
import win32gui
import psutil

import time
import ctypes
import win32api
ctypes.windll.user32.MessageBoxW(0, "Başlatıldı !", "Spotify Reklam Koruyucu", 0)



while True:

    hwnd = win32gui.FindWindow(None, 'Advertisement')
    win32gui.SendMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, hwnd)
    win32gui.SendMessage(win32con.WM_LBUTTONUP, 0, hwnd)

    if (hwnd == 0):
        pass
    else:
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        time.sleep(2)
        os.startfile("C:/Users/gamer/AppData/Roaming/Spotify/Spotify.exe")
        time.sleep(2)
        VK_MEDIA_PLAY_PAUSE = 0xB3
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)

    while True:
        ramKullanimi = psutil.virtual_memory()
        ram_yuzde = ramKullanimi.percent
        if int(ram_yuzde) >= 90:
            time.sleep(1.5)
            continue
        else:
            break

