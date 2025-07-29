# gui/widgets.py
import PyQt6.QtWidgets as qtw

class MyCustomWidget(qtw.QLabel):
    def __init__(self):
        super().__init__()


class LogBox(qtw.QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setPlaceholderText("Logs will appear here...")

class ActionButton(qtw.QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setMinimumHeight(40)
        self.setMinimumWidth(120)