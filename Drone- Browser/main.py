import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

class WebClass(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.showMaximized()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.browser.setUrl(QUrl('https://google.com'))
        
        # ===Menus====
        self.menu=QToolBar()
        self.addToolBar(self.menu)

        back_btn = QAction('<--',self)
        back_btn.triggered.connect(self.browser.back)
        self.menu.addAction(back_btn)

        forward_btn = QAction('-->',self)
        forward_btn.triggered.connect(self.browser.forward)
        self.menu.addAction(forward_btn)

        reload_btn = QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        self.menu.addAction(reload_btn)

        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.home_url)
        self.menu.addAction(home_btn)

        self.url_txt = QLineEdit()
        self.url_txt.returnPressed.connect(self.navigate_url)
        self.menu.addWidget(self.url_txt)

        self.browser.urlChanged.connect(self.update_url)
# =================================================================
    

    def home_url(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_url(self):
        self.browser.setUrl(QUrl(self.url_txt.text()))

    def update_url(self,u):
        self.url_txt.setText(u.toString())

WebApp = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser")
obj=WebClass()
WebApp.exec_()