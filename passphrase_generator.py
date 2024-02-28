import sys, random
from PySide6 import QtWidgets as qtw

from passphrase_gen_ui import Ui_passphrase_gen

class PassGen(qtw.QMainWindow, Ui_passphrase_gen):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.gen_button.clicked.connect(e_rando)

        self.show()




def e_rando(self):
    with open("english.txt", "r") as file:
        e_words = file.read().splitlines()

    random.shuffle(e_words)

    for i in range(4):
        print(e_words[i])

    
    #self.lb_output.setText(e_words[i])





if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    form = PassGen()

    sys.exit(app.exec()) 