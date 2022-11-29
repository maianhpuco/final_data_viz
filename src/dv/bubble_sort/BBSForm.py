from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QMessageBox
from bubble_sort.bbs_form.BBSFormLeft import BBSFormLeft
from bubble_sort.bbs_form.BBSFormRight import BBSFormRight


class BBSForm(QMainWindow):

    def __init__(self, size, title, data, reset_data, next_step, next_loc):
        super().__init__()

        self.resize(size)
        self.setWindowTitle(title)
        self.data = data

        self.left = BBSFormLeft(self.data, reset_data, next_step, next_loc)
        self.right = BBSFormRight(self.data, reset_data, next_step)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.left)
        layout.addWidget(self.right)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def rerender(self):
        self.left.rerender()
        self.right.rerender()
    
    def next_step(self, callback):
        print("form")
        self.right.next_step()
        self.left.next_step(callback)
    
    def init_i(self, callback):
        self.left.init_i()
        self.right.init_i()
        self.left.next_loc_finish(callback)
    
    def compare_in(self, callback):
        self.left.compare_in()
        self.right.compare_in()
        self.left.next_loc_finish(callback)
    
    def init_j(self, callback):
        self.left.init_j()
        self.right.init_j()
        self.left.next_loc_finish(callback)
    
    def compare_jn(self, callback):
        self.left.compare_jn()
        self.right.compare_jn()
        self.left.next_loc_finish(callback)
    
    def compare_aij(self, callback):
        self.left.compare_aij()
        self.right.compare_aij()
        self.left.next_loc_finish(callback)
    
    def swap_aij(self, callback):
        def _tmp():
            self.right.swap_aij_finish()
            self.left.next_loc_finish(callback)
        self.right.swap_aij()
        self.left.swap_aij(_tmp)
    
    def increase_j(self, callback):
        self.left.increase_j()
        self.right.increase_j()
        self.left.next_loc_finish(callback)
    
    def increase_i(self, callback):
        self.left.increase_i()
        self.right.increase_i()
        self.left.next_loc_finish(callback)
    
    def end(self, callback):
        ret = QMessageBox.question(self, 'MessageBox', "Finished! Reset?", QMessageBox.Yes)

        if ret == QMessageBox.Yes:
            callback()
