from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from collections import OrderedDict
import os

print("gg")
my_array = [] # массив строк
my_list = []  # список строк
val = 0       # глобальная переменная
progress = 0 # глобальная переменная
Form, Window = uic.loadUiType("menu.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.text_browser_2.setStyleSheet("color: green; font-size: 20px; font-family: monotype Corsiva")
form.label_6.setStyleSheet("color: blue; font-size: 45px; font-family: monotype Corsiva")
form.label_6.setText(" НачнЁм? ")
window.setWindowTitle("Чистильщик V1.0")
def spisok1():
    global my_array, my_list
    print("Выпад список")
def buton1():
    global val, progress  # объявляем val как глобальную переменную
    my_array = []  # массив строк
    my_list = []  # список строк

    form.label_6.setText(" Погнали !!!")
    print("Выбор файла")
    pathfile, _ = QFileDialog.getOpenFileName(
        filter="Text files (*.txt *.trc)")  # filter определяет, какие файлы будут отображаться в диалоговом окне
    print(pathfile); form.text_browser_2.append(pathfile)

    num_lines = sum(1 for line in open(pathfile))  # подсчет строк в файле
    print(num_lines)
    form.progressBar_2.setMaximum(num_lines)

    with open(pathfile) as f:

        for line in f:    #tqdm(f, total=num_lines):
            print (line)
            progress = progress + 1
            if line.startswith("Time") != True:
                result = line.split()  # print("Читаем строку --",result )# разбиваем строку на списки через зпт

                result.pop(0)
                for i in range(10 - len(result)):
                    result.append("00")  # дополняем строку нулями до полной строки
# my_list.append(result)
                new_result = ','.join(result)  # клеем строку через ЗПТ
                my_array.append(new_result)
                form.progressBar_2.setValue(progress)
                QApplication.processEvents()



    file_name, file_ext = os.path.splitext(pathfile)  # формируем строку для патча
    #form.text_browser.append('\n'.join(my_array))

    if val == 0:
        fileOUT = file_name + "_MOD_" + file_ext

    else:
        fileOUT = file_name + "_MOD_NO_Str" + file_ext
        li = list(OrderedDict.fromkeys(my_array))
        # используем модуль collections.OrderedDict.fromkeys() чтобы удалить дубликаты из списка
        my_array = li


    with open(fileOUT, "w") as f:
        for line in my_array:
            f.write(line + '\n')

            # print("Сохраняем строку--",line)

    title = " Новый файл !!!"
    form.text_browser_2.append(title)

    form.label_6.setStyleSheet("color: red; font-size: 30px; font-family: monotype Corsiva")
    if val == 0:
        form.label_6.setText(" ФАЙЛ ПРЕАБРАЗОВАН !! и Строки двойники не удалены. ")
        text = fileOUT
    else:
        text = fileOUT
        form.label_6.setText(" ФАЙЛ ПРЕАБРАЗОВАН !! Двойники удалены. ")


    #easygui.msgbox(text, title=title, ok_button="OK")
    form.text_browser_2.append(text)

def chekBox(new_val):
    global my_array, my_list
    global val
    val = new_val
    print("Галочка",new_val)



form.checkBox_2.stateChanged.connect(chekBox)
#form.Box1.select.connect(spisok1)
form.btn1_2.clicked.connect(buton1)



app.exec()




