from PyQt5.QtWidgets import QFrame, QPushButton, QSizePolicy

class BBSControlFrame(QFrame):
    def __init__(self, data, reset_data, next_step, next_loc):
        super().__init__()

        # self.setStyleSheet("background-color:red;")
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setVerticalStretch(1)
        self.setSizePolicy(sp)
        self.data = data

        self.init_btn = QPushButton(self)
        self.init_btn.setText("Reset")
        self.init_btn.move(0, 0) # x, y
        self.init_btn.show()
        self.init_btn.clicked.connect(reset_data)

        # self.next_btn = QPushButton(self)
        # self.next_btn.setText("Next")
        # self.next_btn.move(100, 0) # x, y
        # self.next_btn.show()
        # self.next_btn.clicked.connect(lambda: [print("next"), self._deactive_buttons(), next_step()])

        self.next_loc_btn = QPushButton(self)
        self.next_loc_btn.setText("Next")
        self.next_loc_btn.move(100, 0) # x, y
        self.next_loc_btn.show()
        self.next_loc_btn.clicked.connect(lambda: [self._deactive_buttons(), next_loc(lambda: None)])
    
    def _deactive_buttons(self):
        self.init_btn.setEnabled(False)
        # self.next_btn.setEnabled(False)
        self.next_loc_btn.setEnabled(False)
    
    def _active_buttons(self):
        self.init_btn.setEnabled(True)
        # self.next_btn.setEnabled(True)
        self.next_loc_btn.setEnabled(True)
    
    def rerender(self):
        self._active_buttons()

    def next_step_finish(self):
        print("finish")
        self._active_buttons()

    def next_loc_finish(self, callback):
        self._active_buttons()
        callback()
