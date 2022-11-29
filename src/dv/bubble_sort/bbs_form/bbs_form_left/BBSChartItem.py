from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QPoint, pyqtProperty


class BBSChartItem(QLabel):

    def __init__(self, parent, text, pos, width, height, ratio):
        super().__init__(parent)

        self.r = 20 # RADIUS, pixels
        self.pos = pyqtProperty(QPoint, fset=self._set_pos)
        self.setText("  " + text)
        fix_height = int(height * ratio)
        self.move(pos.x(), pos.y() + height - fix_height)
        self.resize(width, fix_height)
        self.reset_style_sheet()

    def _set_pos(self, pos):
        self.move(pos.x(), pos.y())
    
    def get_pos(self):
        return QPoint(self.x(), self.y())
    
    def reset_style_sheet(self):
        self.setStyleSheet("border: 1px solid rgb(127, 127, 127); background-color: rgb(195, 195, 195);")
    
    def change_style_sheet(self):
        self.setStyleSheet("border: 1px solid rgb(63, 72, 204); background-color: rgb(112, 146, 190);")