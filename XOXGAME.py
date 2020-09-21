from PyQt5 import QtWidgets
import sys
import os
from XOXGameUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

PATH = os.path.join(application_path)

class Game(QtWidgets.QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton_1.clicked.connect(self.pressBtn00)
        self.ui.toolButton_2.clicked.connect(self.pressBtn01)
        self.ui.toolButton_3.clicked.connect(self.pressBtn02)
        self.ui.toolButton_4.clicked.connect(self.pressBtn10)
        self.ui.toolButton_5.clicked.connect(self.pressBtn11)
        self.ui.toolButton_6.clicked.connect(self.pressBtn12)
        self.ui.toolButton_7.clicked.connect(self.pressBtn20)
        self.ui.toolButton_8.clicked.connect(self.pressBtn21)
        self.ui.toolButton_9.clicked.connect(self.pressBtn22)
        self.ui.resetButton.clicked.connect(self.pressReset)

        self.isContinue = True
        self.ui.infoText.setText("player 1's turn")
        self.ui.infoText.setStyleSheet("color:red;")

        self.state = [["", "", ""],["", "", ""],["", "", ""]]
        self.isTurn1 = True

    def changeTurn(self):
        if self.isContinue:
            self.isTurn1 = not self.isTurn1

            if self.isTurn1:
                self.ui.infoText.setText("player 1's turn")
                self.ui.infoText.setStyleSheet('color:red;')
            else:
                self.ui.infoText.setText("player 2's turn")
                self.ui.infoText.setStyleSheet("color:blue;")

    def end(self, endCase):
        if self.isTurn1:
            self.ui.infoText.setText("!!! Player 1 Won !!!")
            self.ui.infoText.setStyleSheet('color:red;')
        else:
            self.ui.infoText.setText("!!! Player 2 Won !!!")
            self.ui.infoText.setStyleSheet("color:blue;")

        if endCase == 1:
            self.ui.toolButton_1.setStyleSheet("background-color:yellow")
            self.ui.toolButton_2.setStyleSheet("background-color:yellow")
            self.ui.toolButton_3.setStyleSheet("background-color:yellow")
        elif endCase == 2:
            self.ui.toolButton_4.setStyleSheet("background-color:yellow")
            self.ui.toolButton_5.setStyleSheet("background-color:yellow")
            self.ui.toolButton_6.setStyleSheet("background-color:yellow")
        elif endCase == 3:
            self.ui.toolButton_7.setStyleSheet("background-color:yellow")
            self.ui.toolButton_8.setStyleSheet("background-color:yellow")
            self.ui.toolButton_9.setStyleSheet("background-color:yellow")
        elif endCase == 4:
            self.ui.toolButton_1.setStyleSheet("background-color:yellow")
            self.ui.toolButton_4.setStyleSheet("background-color:yellow")
            self.ui.toolButton_7.setStyleSheet("background-color:yellow")
        elif endCase == 5:
            self.ui.toolButton_2.setStyleSheet("background-color:yellow")
            self.ui.toolButton_5.setStyleSheet("background-color:yellow")
            self.ui.toolButton_8.setStyleSheet("background-color:yellow")
        elif endCase == 6:
            self.ui.toolButton_3.setStyleSheet("background-color:yellow")
            self.ui.toolButton_6.setStyleSheet("background-color:yellow")
            self.ui.toolButton_9.setStyleSheet("background-color:yellow")
        elif endCase == 7:
            self.ui.toolButton_1.setStyleSheet("background-color:yellow")
            self.ui.toolButton_5.setStyleSheet("background-color:yellow")
            self.ui.toolButton_9.setStyleSheet("background-color:yellow")
        elif endCase == 8:
            self.ui.toolButton_3.setStyleSheet("background-color:yellow")
            self.ui.toolButton_5.setStyleSheet("background-color:yellow")
            self.ui.toolButton_7.setStyleSheet("background-color:yellow")
        elif endCase == 9:
            self.ui.infoText.setText("No moves left")
            self.ui.infoText.setStyleSheet("color:black;")

        

    def isFinished(self):
        if self.isTurn1:
            target = "X"
        else:
            target = "O"

        if  self.state[0][0] == target and self.state[0][1] == target and self.state[0][2] == target:
            self.isContinue = False
            self.end(1)
        
        elif self.state[1][0] == target and self.state[1][1] == target and self.state[1][2] == target:
            self.isContinue = False
            self.end(2)

        elif self.state[2][0] == target and self.state[2][1] == target and self.state[2][2] == target:
            self.isContinue = False
            self.end(3)

        elif self.state[0][0] == target and self.state[1][0] == target and self.state[2][0] == target: 
            self.isContinue = False
            self.end(4)
        
        elif self.state[0][1] == target and self.state[1][1] == target and self.state[2][1] == target:
            self.isContinue = False
            self.end(5)

        elif self.state[0][2] == target and self.state[1][2] == target and self.state[2][2] == target:
            self.isContinue = False
            self.end(6)

        elif self.state[0][0] == target and self.state[1][1] == target and self.state[2][2] == target:
            self.isContinue = False
            self.end(7)
        
        elif self.state[0][2] == target and self.state[1][1] == target and self.state[2][0] == target:
            self.isContinue = False
            self.end(8)
        else:
            #checks if there is any move left
            for i in self.state:
                if "" in i:
                    break
            else:
                self.isContinue = False
                self.end(9)



    def pressBtn00(self):
        if(self.state[0][0] == "" and self.isContinue):
            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[0][0] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[0][0] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_1.setIcon(icon)
            self.ui.toolButton_1.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()


    def pressBtn01(self):
        if(self.state[0][1] == "" and self.isContinue):

            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[0][1] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[0][1] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_2.setIcon(icon)
            self.ui.toolButton_2.setIconSize(QtCore.QSize(90,90))
            
            self.isFinished()
            self.changeTurn()

    def pressBtn02(self):
        if(self.state[0][2] == "" and self.isContinue):

            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[0][2] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[0][2] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_3.setIcon(icon)
            self.ui.toolButton_3.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressBtn10(self):
        if(self.state[1][0] == "" and self.isContinue):

            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[1][0] = "X"

            else:
                path = PATH + "/assets/OIcon.png"
                self.state[1][0] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_4.setIcon(icon)
            self.ui.toolButton_4.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressBtn11(self):
        if(self.state[1][1] == "" and self.isContinue):
            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[1][1] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[1][1] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_5.setIcon(icon)
            self.ui.toolButton_5.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressBtn12(self):
        if(self.state[1][2] == "" and self.isContinue):
            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[1][2] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[1][2] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_6.setIcon(icon)
            self.ui.toolButton_6.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressBtn20(self):
        if(self.state[2][0] == "" and self.isContinue):
            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[2][0] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[2][0] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_7.setIcon(icon)
            self.ui.toolButton_7.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressBtn21(self):
        if(self.state[2][1] == "" and self.isContinue):
            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[2][1] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[2][1] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_8.setIcon(icon)
            self.ui.toolButton_8.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressBtn22(self):
        if(self.state[2][2] == "" and self.isContinue):
            if(self.isTurn1):
                path = PATH + "/assets/XIcon.png"
                self.state[2][2] = "X"
            else:
                path = PATH + "/assets/OIcon.png"
                self.state[2][2] = "O"

            icon = QtGui.QIcon() 
            icon.addPixmap(QtGui.QPixmap(path), 
                            QtGui.QIcon.Normal, QtGui.QIcon.Off) 
            self.ui.toolButton_9.setIcon(icon)
            self.ui.toolButton_9.setIconSize(QtCore.QSize(90,90))

            self.isFinished()
            self.changeTurn()

    def pressReset(self):
        self.state = [["", "", ""],["", "", ""],["", "", ""]]
        self.isTurn1 = True
        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap(PATH + "/assets/EmptyIcon.png"), 
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.ui.infoText.setText("player 1's turn")
        self.ui.infoText.setStyleSheet("color:red;")
        self.isContinue = True
        
        self.ui.toolButton_2.setIcon(icon)
        self.ui.toolButton_3.setIcon(icon)
        self.ui.toolButton_1.setIcon(icon)
        self.ui.toolButton_4.setIcon(icon)
        self.ui.toolButton_5.setIcon(icon)
        self.ui.toolButton_6.setIcon(icon)
        self.ui.toolButton_7.setIcon(icon)
        self.ui.toolButton_8.setIcon(icon)
        self.ui.toolButton_9.setIcon(icon)

        self.ui.toolButton_1.setStyleSheet("")
        self.ui.toolButton_2.setStyleSheet("")
        self.ui.toolButton_3.setStyleSheet("")
        self.ui.toolButton_4.setStyleSheet("")
        self.ui.toolButton_5.setStyleSheet("")
        self.ui.toolButton_6.setStyleSheet("")
        self.ui.toolButton_7.setStyleSheet("")
        self.ui.toolButton_8.setStyleSheet("")
        self.ui.toolButton_9.setStyleSheet("")


game = QtWidgets.QApplication(sys.argv)
win = Game()
win.show()
sys.exit(game.exec())