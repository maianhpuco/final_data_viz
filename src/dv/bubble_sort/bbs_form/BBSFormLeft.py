from PyQt5.QtWidgets import QFrame, QVBoxLayout, QSizePolicy
from bubble_sort.bbs_form.bbs_form_left.BBSChartFrame import BBSChartFrame
from bubble_sort.bbs_form.bbs_form_left.BBSControlFrame import BBSControlFrame


class BBSFormLeft(QFrame):
    def __init__(self, data, reset_data, next_step, next_loc):
        super().__init__()

        # self.setStyleSheet("background-color:green;")
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(2)
        self.setSizePolicy(sp)
        self.data = data

        self.chart = BBSChartFrame(data)
        self.control = BBSControlFrame(data, reset_data, next_step, next_loc)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.chart)
        layout.addWidget(self.control)

    def rerender(self):
        self.chart.rerender()
        self.control.rerender()
    
    def next_step(self, callback):
        print("left")
        self.chart.next_step(lambda: self._next_step_callback(callback))
        # self.control.next_step()
    
    def _next_step_callback(self, callback):
        if self.data["state"] == 1:
            callback()
            self.control.next_step_finish()
        else:
            print("state 0 but callback")
        
    def init_i(self):
        self.chart.init_ij(-1, self.data["i"])
    
    def compare_in(self):
        pass
    
    def init_j(self):
        self.chart.init_ij(self.data["i"], self.data["j"])
    
    def compare_jn(self):
        pass
    
    def compare_aij(self):
        self.chart.compare_aij()
    
    def swap_aij(self, callback):
        self.chart.swap_aij(callback)
    
    def increase_j(self):
        self.chart.init_ij(self.data["i"], self.data["j"])
    
    def increase_i(self):
        self.chart.init_ij(-1, self.data["i"])
    
    def next_loc_finish(self, callback):
        self.control.next_loc_finish(callback)
