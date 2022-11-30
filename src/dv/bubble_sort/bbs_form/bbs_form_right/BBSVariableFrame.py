from PyQt5.QtWidgets import QFrame, QSizePolicy, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import QColor


class BBSVariableFrame(QFrame):
    def __init__(self, data, reset_data, next_step):
        super().__init__()
        
        # self.setStyleSheet("background-color:red;")
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setVerticalStretch(1)
        self.setSizePolicy(sp)
        self.data = data
        self.table = None
        self.setStyleSheet(
            "QTableWidget {background-color: transparent;}"
            # "QHeaderView::section {background-color: transparent;}"
            # "QHeaderView {background-color: transparent;}"
            # "QTableCornerButton::section {background-color: transparent;}"
        )
        self.table_data = dict()
    
    def _show(self):
        if self.table:
            self.table.setParent(None)
            del self.table
        
        # i, j = self.data["i"], self.data["j"]
        # ai, aj = self.data["arr"][i]["value"], self.data["arr"][j]["value"]
        
        self.table = QTableWidget(len(self.table_data), 2, self)
        # self.table.setHorizontalHeaderLabels(["Variable", "Value"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

        idx = 0
        for i in self.table_data:
            (value, flag) = self.table_data[i]
            self.table.setItem(idx, 0, QTableWidgetItem(i))
            self.table.setItem(idx, 1, QTableWidgetItem(str(value)))
            if flag:
                self.table.item(idx, 1).setBackground(QColor(Qt.blue).lighter(160))
            idx += 1

        self.table.setMinimumSize(self.size())
        self.table.show()

    def rerender(self):
        self.table_data = dict()
        self._show()
    
    def next_step(self):
        self._show()
    
    def _table_data_to_false(self):
        for i in self.table_data:
            self.table_data[i] = (self.table_data[i][0], False)
    
    def show_i(self):
        self._table_data_to_false()
        self.table_data["i"] = (self.data["i"], True)
        self._show()

    def show_j(self):
        self._table_data_to_false()
        self.table_data["j"] = (self.data["j"], True)
        self._show()
    
    def compare_in(self):
        self._table_data_to_false()
        self.table_data["i"] = (self.data["i"], True)
        self.table_data["n"] = (self.data["n"], True)
        self.table_data["i < n"] = (self.data["i"] < self.data["n"], True)
        self._show()
        
    def compare_jn(self):
        self._table_data_to_false()
        self.table_data["j"] = (self.data["j"], True)
        self.table_data["n"] = (self.data["n"], True)
        self.table_data["j < n"] = (self.data["j"] < self.data["n"], True)
        self._show()
    
    def compare_aij(self):
        self._table_data_to_false()
        i, j = self.data["i"], self.data["j"]
        ai, aj = self.data["arr"][i]["value"], self.data["arr"][j]["value"]
        self.table_data["a[i]"] = (ai, True)
        self.table_data["a[j]"] = (aj, True)
        self.table_data["a[i] > a[j]"] = (ai > aj, True)
        self._show()
    
    def swap_aij(self):
        self._table_data_to_false()
        i, j = self.data["i"], self.data["j"]
        ai, aj = self.data["arr"][i]["value"], self.data["arr"][j]["value"]
        self.table_data["a[i]"] = (ai, True)
        self.table_data["a[j]"] = (aj, True)
        self.table_data["a[i] > a[j]"] = (ai > aj, True)
        self._show()