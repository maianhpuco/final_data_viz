from PyQt5.QtWidgets import QFrame, QVBoxLayout, QSizePolicy
from bubble_sort.bbs_form.bbs_form_right.BBSVariableFrame import BBSVariableFrame
from bubble_sort.bbs_form.bbs_form_right.BBSCodeFrame import BBSCodeFrame

class BBSFormRight(QFrame):
    def __init__(self, data, reset_data, next_step):
        super().__init__()

        # self.setStyleSheet("background-color:green;")
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(1)
        self.setSizePolicy(sp)

        self.variable = BBSVariableFrame(data, reset_data, next_step)
        self.code = BBSCodeFrame(data, reset_data, next_step)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.variable)
        layout.addWidget(self.code)

    def rerender(self):
        self.variable.rerender()
        self.code.rerender()
    
    def next_step(self):
        self.variable.next_step()
        self.code.next_step()

    def init_i(self):
        self.variable.show_i()
        self.code.show(0)
    
    def compare_in(self):
        self.variable.compare_in()
        self.code.show(1)
    
    def init_j(self):
        self.variable.show_j()
        self.code.show(2)
    
    def compare_jn(self):
        self.variable.compare_jn()
        self.code.show(3)
    
    def compare_aij(self):
        self.variable.compare_aij()
        self.code.show(4)
    
    def swap_aij(self):
        self.code.show(5)
    
    def swap_aij_finish(self):
        self.variable.swap_aij()
    
    def increase_j(self):
        self.variable.show_j()
        self.code.show(6)
    
    def increase_i(self):
        self.variable.show_i()
        self.code.show(7)
    