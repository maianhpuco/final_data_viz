from PyQt5.QtWidgets import QFrame, QSizePolicy
from PyQt5.QtCore import QPoint, QPropertyAnimation
from bubble_sort.bbs_form.bbs_form_left.BBSChartItem import BBSChartItem


class BBSChartFrame(QFrame):
    LEFT = 0
    TOP = 0
    WIDTH = 40
    PADDING = 1

    def __init__(self, data):
        super().__init__()

        # self.setStyleSheet("background-color: red;")
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setVerticalStretch(5)
        self.setSizePolicy(sp)
        self.data = data

        self.labels = list()
        self.latest_label = None
    
    def rerender(self):
        for label in self.labels:
            label.setParent(None)
            del label
        self.labels = list()

        for i in range(self.data["n"]):
            label = BBSChartItem(
                self, 
                str(self.data["arr"][i]["value"]), 
                QPoint(self.LEFT + self.WIDTH * i + self.PADDING * i, self.TOP), 
                self.WIDTH, 
                self.size().height(), 
                self.data["arr"][i]["ratio"]
            )
            anim = QPropertyAnimation(label, b'pos')
            label.show()
            self.data["arr"][i]["label"] = label
            self.data["arr"][i]["anim"] = anim
            self.labels.append(label)

    def next_step(self, callback):
        self._show_ij_items()
        
        res = self._show_compare(self.data["i"], self.data["j"])
        if res:
            self._show_pass(callback)
        else:
            self._show_swap(self.data["i"], self.data["j"], callback)
    
    def _show_ij_items(self):
        for i in range(self.data["n"]):
            if i in (self.data["i"], self.data["j"]):
                self.data["arr"][i]["label"].change_style_sheet()
            else:
                self.data["arr"][i]["label"].reset_style_sheet()
    
    def _show_compare(self, i, j):
        return self.data["arr"][i]["value"] <= self.data["arr"][j]["value"]
    
    def _show_pass(self, callback):
        print("pass")
        callback()
        pass
    
    def _show_swap(self, i, j, callback):
        print("swap")
        self._toggle_top(i)
        self.data["arr"][i]["anim"].setDuration(1000)
        self.data["arr"][i]["anim"].setStartValue(self.data["arr"][i]["label"].get_pos())
        self.data["arr"][i]["anim"].setEndValue(QPoint(self.data["arr"][j]["label"].get_pos().x(), self.data["arr"][i]["label"].get_pos().y()))
        self.data["arr"][i]["anim"].start()

        self._toggle_top(j)
        self.data["arr"][j]["anim"].setDuration(1000)
        self.data["arr"][j]["anim"].setStartValue(self.data["arr"][j]["label"].get_pos())
        self.data["arr"][j]["anim"].setEndValue(QPoint(self.data["arr"][i]["label"].get_pos().x(), self.data["arr"][j]["label"].get_pos().y()))
        self.data["arr"][j]["anim"].start()
        self.data["arr"][j]["anim"].finished.connect(callback)

        (self.data["arr"][i], self.data["arr"][j]) = (self.data["arr"][j], self.data["arr"][i])
    
    def _toggle_top(self, i):
        if self.latest_label is None:
            self.latest_label = self.data["n"] - 1
        self.data["arr"][i]["label"].stackUnder(self.data["arr"][self.latest_label]["label"])
        self.data["arr"][i]["label"].raise_()
        self.latest_label = i
    
    def init_ij(self, first, ij):
        for i in range(first + 1, self.data["n"]):
            if i == ij:
                self.data["arr"][i]["label"].change_style_sheet()
                self._toggle_top(i)
            else:
                self.data["arr"][i]["label"].reset_style_sheet()
    
    def compare_aij(self):
        pass

    def swap_aij(self, callback):
        i, j = self.data["i"], self.data["j"]
        ai, aj = self.data["arr"][i]["value"], self.data["arr"][j]["value"]
        
        self._toggle_top(i)
        self.data["arr"][i]["anim"].setDuration(1000)
        self.data["arr"][i]["anim"].setStartValue(self.data["arr"][i]["label"].get_pos())
        self.data["arr"][i]["anim"].setEndValue(QPoint(self.data["arr"][j]["label"].get_pos().x(), self.data["arr"][i]["label"].get_pos().y()))
        self.data["arr"][i]["anim"].start()

        self._toggle_top(j)
        self.data["arr"][j]["anim"].setDuration(1000)
        self.data["arr"][j]["anim"].setStartValue(self.data["arr"][j]["label"].get_pos())
        self.data["arr"][j]["anim"].setEndValue(QPoint(self.data["arr"][i]["label"].get_pos().x(), self.data["arr"][j]["label"].get_pos().y()))
        self.data["arr"][j]["anim"].start()
        self.data["arr"][j]["anim"].finished.connect(callback)
    