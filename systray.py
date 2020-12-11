from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from win32api import GetKeyState
from win32con import VK_CAPITAL, VK_SCROLL, VK_NUMLOCK

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

#Adds an icon
icon = QIcon("icons/all.svg")
cap = QIcon("icons/caps.svg")
scroll = QIcon("icons/scroll.svg")
num = QIcon("icons/num.svg")
capsScroll = QIcon("icons/capsscroll.svg")
capsNum = QIcon("icons/capsnum.svg")
numScroll = QIcon("icons/numscroll.svg")
all = QIcon("icons/all.svg")
none = QIcon("icons/none.svg")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating options
menu = QMenu()

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)



# Setting timer function
def checkCaps():
    if GetKeyState(VK_CAPITAL) == 1 and GetKeyState(VK_NUMLOCK) == 0 and GetKeyState(VK_SCROLL) == 0:
        tray.setIcon(cap)
    elif GetKeyState(VK_CAPITAL) == 0 and GetKeyState(VK_NUMLOCK) == 1 and GetKeyState(VK_SCROLL) == 0:
        tray.setIcon(num)
    elif GetKeyState(VK_CAPITAL) == 1 and GetKeyState(VK_NUMLOCK) == 0 and GetKeyState(VK_SCROLL) == 1:
        tray.setIcon(capsScroll)
    elif GetKeyState(VK_CAPITAL) == 1 and GetKeyState(VK_NUMLOCK) == 1 and GetKeyState(VK_SCROLL) == 0:
        tray.setIcon(capsNum)
    elif GetKeyState(VK_CAPITAL) == 0 and GetKeyState(VK_NUMLOCK) == 1 and GetKeyState(VK_SCROLL) == 1:
        tray.setIcon(numScroll)
    elif GetKeyState(VK_NUMLOCK) == 1 and GetKeyState(VK_SCROLL) == 1 and GetKeyState(VK_CAPITAL) == 1:
        tray.setIcon(allIcon)
    elif GetKeyState(VK_CAPITAL) == 0 and GetKeyState(VK_NUMLOCK) == 0 and GetKeyState(VK_SCROLL) == 0:
        tray.setIcon(none)
        

if __name__ == "__main__":
    checkCaps
    timer = QTimer()
    timer.start()
    timer.setInterval(3000)
    timer.timeout.connect(checkCaps)
    app.exec_()