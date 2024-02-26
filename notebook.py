from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from sys import argv
import webbrowser
import sys as s
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Survey")
        self.setGeometry(300, 250, 650, 600)
        self.text = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menuBar)
        self.menu = QtWidgets.QMenu("&File", self)
        self.menuBar.addMenu(self.menu)
        self.menu.addAction("Create", self.menu_clicked)
        self.menu.addAction("New tab", self.menu_clicked)
        self.menu.addAction("Open...", self.menu_clicked)
        self.menu.addAction("Save", self.menu_clicked)
        self.menu.addAction("Save as...", self.menu_clicked)
        self.menu.addSeparator()
        self.menu.addAction("Page settings", self.menu_clicked)
        self.menu.addAction("Stamp", self.menu_clicked)
        self.menu.addSeparator()
        self.menu.addAction("Exit", self.menu_clicked)
        self.edit_menu = QtWidgets.QMenu("&Edit",self)
        self.menuBar.addMenu(self.edit_menu)
        self.edit_menu.addAction("Cancel", self.menu_clicked)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction("Cut",self.menu_clicked)
        self.edit_menu.addAction("Copy", self.menu_clicked)
        self.edit_menu.addAction("Insert", self.menu_clicked)
        self.edit_menu.addAction("Delete", self.menu_clicked)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction("Search using Bing...", self.menu_clicked)
        self.edit_menu.addAction("Search...", self.menu_clicked)
        self.edit_menu.addAction("Search further", self.menu_clicked)
        self.edit_menu.addAction("Search previously", self.menu_clicked)
        self.edit_menu.addAction("Replace", self.menu_clicked)
        self.edit_menu.addAction("Go...", self.menu_clicked)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction("Select all", self.menu_clicked)
        self.edit_menu.addAction("Time and date", self.menu_clicked)
        self.format_menu = QtWidgets.QMenu("&Format",self)
        self.menuBar.addMenu(self.format_menu)
        self.format_menu.addAction("Word wrapping",self.menu_clicked)
        self.format_menu.addAction("Font...", self.menu_clicked)
        self.view_menu = QtWidgets.QMenu("View")
        self.menuBar.addMenu(self.view_menu)
        self.view_menu.addAction("Scale", self.menu_clicked)
        self.view_menu.addAction("Status line", self.menu_clicked)
        self.reference_menu = QtWidgets.QMenu("Reference")
        self.menuBar.addMenu(self.reference_menu)
        self.reference_menu.addAction("View Help",self.menu_clicked)
        self.reference_menu.addAction("Post a review", self.menu_clicked)
        self.reference_menu.addSeparator()
        self.reference_menu.addAction("About the program", self.menu_clicked)
    def menu_clicked(self):
        action = self.sender()
        if action.text() == "Open...":
            frame = QFileDialog.getOpenFileName(self, "Open file", "", "Text Files (*.txt)")[0]
            try:
                with open(frame, 'r') as file:
                    data = file.read()
                    self.text.setText(data)
            except FileNotFoundError:
                print("No such file")
        elif action.text() == "Save as...":
            frame = QFileDialog.getSaveFileName(self, "Save file", "", "Text Files (*.txt)")[0]
            try:
                with open(frame, 'w') as file:
                    text2 = self.text.toPlainText()
                    file.write(text2)
            except FileNotFoundError:
                print("No such file")
        elif action.text() == "Exit":
            exit()
        elif action.text() == "View Help":
            webbrowser.open("https://www.bing.com/search?q=%d1%81%d0%bf%d1%80%d0%b0%d0%b2%d0%ba%d0%b0+%d0%bf%d0%be+%d0%b8%d1%81%d0%bf%d0%be%d0%bb%d1%8c%d0%b7%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d1%8e+%d0%b1%d0%bb%d0%be%d0%ba%d0%bd%d0%be%d1%82%d0%b0+%d0%b2+windows%c2%a010&filters=guid:%224466414-ru-dia%22%20lang:%22ru%22&form=T00032&ocid=HelpPane-BingIA")
def application():
    app = QApplication(argv)
    window = Window()
    window.show()
    s.exit(app.exec_())

if __name__ == "__main__":
    application()