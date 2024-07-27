# підключеня модулів
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import  randint

app = QApplication([])#обєкт програм

# основне вікно
main_wind = QWidget()
main_wind.resize(400, 400)
main_wind.move(100,100)
main_wind.setWindowTitle('Лохотрон')

name1 = QLabel("?&77&&7")
name2 = QLabel("?&77&&7")
text = QLabel("Натисни, щоб взяти участь лохотроні")
btn = QPushButton("Випробувати удачу в лохотроні")

line = QVBoxLayout()
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(name1, alignment= Qt.AlignCenter)
line.addWidget(name2, alignment= Qt.AlignCenter)
line.addWidget(btn, alignment= Qt.AlignCenter)

main_wind.setLayout(line)

def rand():
    n1 = randint(0,9)
    n2 = randint(0,9)
    name1.setText(str(n1))
    name2.setText(str(n2))
    if n1 == n2:
        text.setText("Ви Виграли зіграйте щерас живо")
    else:
        text.setText("Ви Програли зіграйте щерас живо")

btn.clicked.connect(rand)





main_wind.show()
app.exec_()



