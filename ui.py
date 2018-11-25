import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMessageBox, QApplication, QShortcut
from untitled import Ui_Dialog
import sys


# 创建鼠标点击事件
def on_click():
    replace_text = ui.lineEdit.text()
    if ui.checkBox.isChecked():
        dd = pyperclip.paste()
    else:
        dd = ui.plainTextEdit.toPlainText()
    dd = replace_text + dd.replace("\r\n", replace_text + ",\r\n" + replace_text) + replace_text
    pyperclip.copy(dd)
    QMessageBox.information(ui.toolButton, "提示", "替换成功。", QMessageBox.Yes)


def on_checked(checked):
    ui.plainTextEdit.setEnabled(not checked)


# 创建OCR点击事件
def on_click_ocr():
    clipboard = QApplication.clipboard()
    ui.label.setPixmap(clipboard.pixmap())


def on_open():
    print("Opening!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    shortcut = QShortcut(QKeySequence("Ctrl+O"), Dialog)
    shortcut.activated.connect(on_open)
    # 替换按钮
    ui.toolButton.clicked.connect(on_click)
    # 复选框
    ui.checkBox.toggled['bool'].connect(on_checked)
    # OCR按钮
    ui.toolButton_2.clicked.connect(on_click_ocr)
    sys.exit(app.exec_())
