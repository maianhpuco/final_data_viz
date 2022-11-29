from PyQt5.QtWidgets import QFrame, QSizePolicy
from PyQt5.QtCore import QPoint, QPropertyAnimation
from PyQt5.QtGui import QTextCursor
from bubble_sort.bbs_form.bbs_form_right.CodeEditor import CodeEditor


class BBSCodeFrame(QFrame):
    def __init__(self, data, reset_data, next_step):
        super().__init__()
        
        # self.setStyleSheet("background-color:red;")
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setVerticalStretch(1)
        self.setSizePolicy(sp)
        self.data = data
        self.full_loc = """i = 0
while i < n - 1:
  j = i + 1
  while j < n - 1:
    if a[i] > a[j]:
      swap(a[i], a[j])
    j += 1
  i += 1
"""
        self.code = CodeEditor(self)
        self.code.setReadOnly(True)
        self.code.appendPlainText(self.full_loc)
        self.code.show()
    
    def rerender(self):
        self.show(9)
    
    def next_step(self):
        pass
    
    def show(self, loc):
        self.code.moveCursor(QTextCursor.Start)
        for _ in range(loc):
            self.code.moveCursor(QTextCursor.Down)

