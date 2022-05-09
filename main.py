# *_* coding : UTF-8 *_*
# author  ：  Probius
# 开发时间  ：  2022/5/10  03:55
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
from time import sleep
import keyboard


class Sister():
    def __init__(self, width=1400, height=800):
        self.image_key = 1
        self.image_url = 'image/meizi/meizi_ ('
        self.image = self.image_url + str(self.image_key) + ').png'
        self.birthplace = (width, height)
        self.ract_x = width
        self.ract_y = height

    def gif(self):
        if self.image_key < 61:
            self.image_key += 1
        else:
            self.image_key = 1
        self.image = self.image_url + str(self.image_key) + ').png'


class MyLabel(QLabel):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # 声明
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 开放右键策略
        self.customContextMenuRequested.connect(self.rightMenuShow)

    # 添加右键菜单
    def rightMenuShow(self, pos):
        timer_sister = QTimer(self)
        menu = QMenu(self)
        menu.addAction(QAction(QIcon('image/NetWok.png'), '连接到校园网', self, triggered=self.connectNetWork))
        # menu.addAction(QAction(QIcon('image/net.png'), '浏览器', self, triggered=self.net))
        # menu.addAction(QAction(QIcon('image/music.ico'), '网易云', self, triggered=self.music))
        menu.addAction(QAction(QIcon('image/keyb.png'), '监听键盘', self, triggered=self.ListenKeb))
        menu.addAction(QAction(QIcon('image/dance.png'), '自己动~', self, triggered=self.dance))
        menu.addAction(QAction(QIcon('image/eye.png'), '隐藏', self, triggered=self.hide))
        menu.addAction(QAction(QIcon('image/exit.png'), '退出', self, triggered=self.quit))
        # menu.addAction(QAction(QIcon('image/exit.png'), '打开网易云', self, triggered=self.music))
        menu.exec_(QCursor.pos())

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):
        self.setVisible(False)

    def music(self):

        try:
            os.startfile(r'D:\CloudMusic\cloudmusic.exe')
        except:
            print('路径不正确')

    def net(self):
        try:
            os.startfile(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        except:
            print('路径不正确')

    def connectNetWork(self):
        try:
            location = os.getcwd() + '/tool/ZZULI_NetWorkSetUp.exe'
            os.startfile(location)
        except:
            print('工具文件丢失')

    def dance(self):
        global init
        if init == 0:
            timer_sister.timeout.connect(pet.gem)
            init = 1
        else:
            sleep(1)
        global auto
        # 检测Timer是否运行，没有则开启，运行则关闭
        if auto == 1:
            timer_sister.stop()
            auto = 0
        else:
            auto = 1
            timer_sister.start(250)
            keyboard.unhook_all()

    def ListenKeb(self):
        global auto

        def callback(x):
            print(x)
            pet.gem()

        if auto == 1:
            keyboard.on_press(callback)
            auto = 0
            timer_sister.stop()
        else:
            auto = 1
            keyboard.unhook_all()


class TablePet(QWidget):

    def __init__(self):
        super(TablePet, self).__init__()

        self.sister = Sister()

        self.is_follow_mouse = False

        self.initUi()
        self.tray()

    def gem(self):
        # 实现gif效果
        self.sister.gif()
        self.pm_sister = QPixmap(self.sister.image)
        self.lb_sister.setPixmap(self.pm_sister)

    def initUi(self):

        ##窗口大小
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        ##标签
        self.lb_sister = MyLabel(self)
        self.pm_sister = QPixmap(self.sister.image)
        self.lb_sister.setPixmap(self.pm_sister)
        self.lb_sister.move(self.sister.ract_x, self.sister.ract_y)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.showMaximized()

    # def mouseDoubleClickEvent(self, QMouseEvent):
    #     self.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.gem();
            self.is_follow_mouse = True

            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

        elif event.buttons() == Qt.MidButton:  # 中键按下
            self.hide()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.sister.ract_x = QCursor.pos().x() - 77
            self.sister.ract_y = QCursor.pos().y() - 63
            self.lb_sister.move(self.sister.ract_x, self.sister.ract_y)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 系统托盘
    def tray(self):
        tray = QSystemTrayIcon(self)
        tray.setIcon(QIcon('image/meizi/0.png'))

        display = QAction(QIcon('image/eye.png'), '显示', self, triggered=self.display)
        quit = QAction(QIcon('image/exit.png'), '退出', self, triggered=self.quit)
        menu = QMenu(self)
        menu.addAction(quit)
        menu.addAction(display)
        tray.setContextMenu(menu)
        tray.show()

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):

        self.lb_sister.setVisible(False)

    def display(self):
        self.lb_sister.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = TablePet()
    timer_sister = QTimer()
    init = 0
    auto = 0
    def callback(x):
        print(x)
        pet.gem()
    keyboard.on_press(callback)
    sys.exit(app.exec_())
