import sys
import random
import time
import threading
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import QPoint, Qt
from bubble_sort.BBSForm import BBSForm
# from ChartItem import ChartItem

class BBS:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.data = {
            "n": 5,
            "arr": list(),
            "i": 0,
            "j": 1,
            "state": 0, # NORMAL
            "cur_loc": 0,
            "loc": 8,
        }
        self.form = BBSForm(
            self.app.primaryScreen().availableGeometry().size(), 
            "Bubble Sort", 
            self.data,
            self.reset_data,
            self.next_step,
            self.next_loc,
        )
        
        self.form.show()
        self.reset_data()

        # new_thread = threading.Thread(target=self._do_something)
        # new_thread.start()

        sys.exit(self.app.exec_())
            
    def _do_something(self):
        while True:
            if self.data["state"] == 1:
                print("do something 0.5")
                time.sleep(0.5)
                self.data["state"] = 0
            else:
                print("do something 0.1")
                time.sleep(0.1)
    
    def _validate_ij(self):
        return not (self.data["i"] >= self.data["n"] - 1 or self.data["j"] > self.data["n"] - 1)

    def _increase_ij(self):
        print("increase", self.data["i"], self.data["j"])
        if self.data["j"] < self.data["n"] - 1:
            self.data["j"] += 1
        else:
            self.data["i"] += 1
            self.data["j"] = self.data["i"] + 1
        self.data["state"] = 0

    def reset_data(self):
        self.data["arr"] = list()
        for i in range(self.data["n"]):
            self.data["arr"].append({"value": random.randint(20, 100)})
        max_value = max([i["value"] for i in self.data["arr"]])
        for i in self.data["arr"]:
            i["ratio"] = i["value"] / max_value
        self.data["i"] = 0
        self.data["j"] = 1
        self.data["state"] = 0 # NORMAL
        self.data["cur_loc"] = 0
        self.data["loc"] = 8
        self.form.rerender()
            
    def next_step(self):
        # print("bbs next")
        # if not self._validate_ij():
        #     return
        # self.data["state"] = 1
        # self.form.next_step(self._increase_ij)
        # time.sleep(0.1)
        
        if self.data["state"] == 0:
            def _tmp():
                self.data["state"] = 1
                self.next_step()
            self.next_loc(_tmp)
        elif self.data["state"] == 1:
            print("next step 0.1")
            time.sleep(0.1)
            self.next_step()
    
    def _loc_0(self, callback):
        self.data["i"] = 0
        self.form.init_i(callback)

    def _loc_1(self, callback):
        self.form.compare_in(callback)
    
    def _loc_2(self, callback):
        self.data["j"] = self.data["i"] + 1
        self.form.init_j(callback)
    
    def _loc_3(self, callback):
        self.form.compare_jn(callback)
    
    def _loc_4(self, callback):
        self.form.compare_aij(callback)
    
    def _loc_5(self, callback):
        i, j = self.data["i"], self.data["j"]
        (self.data["arr"][i], self.data["arr"][j]) = (self.data["arr"][j], self.data["arr"][i])
        self.form.swap_aij(callback)
    
    def _loc_6(self, callback):
        self.data["j"] += 1
        self.form.increase_j(callback)
    
    def _loc_7(self, callback):
        self.data["i"] += 1
        self.form.increase_i(callback)
    
    def _loc_8(self):
        self.data["state"] = 2 # ENDING
        self.form.end(self.reset_data)
    
    def next_loc(self, callback):
        self.data["state"] = 0 # NORMAL

        if self.data["cur_loc"] == 0:
            # i = 0
            def _tmp():
                self.data["cur_loc"] = 1
                callback()
            self._loc_0(_tmp)
        
        elif self.data["cur_loc"] == 1:
            # while i < n - 1:
            def _tmp():
                if self.data["i"] < self.data["n"]:
                    self.data["cur_loc"] = 2
                else:
                    self.data["cur_loc"] = 8 # END
                callback()
            self._loc_1(_tmp)
            
        
        elif self.data["cur_loc"] == 2:
            #   j = i + 1
            def _tmp():
                self.data["cur_loc"] = 3
                callback()
            self._loc_2(_tmp)
        
        elif self.data["cur_loc"] == 3:
            #   while j < n - 1:
            def _tmp():
                if self.data["j"] < self.data["n"]:
                    self.data["cur_loc"] = 4
                else:
                    self.data["cur_loc"] = 7
                callback()
            self._loc_3(_tmp)
        
        elif self.data["cur_loc"] == 4:
            #     if a[i] > a[j]:
            def _tmp():
                i, j = self.data["i"], self.data["j"]
                if self.data["arr"][i]["value"] > self.data["arr"][j]["value"]:
                    self.data["cur_loc"] = 5
                else:
                    self.data["cur_loc"] = 6
                callback()
            self._loc_4(_tmp)
        
        elif self.data["cur_loc"] == 5:
            #       swap(a[i], a[j])
            def _tmp():
                self.data["cur_loc"] = 6
                callback()
            self._loc_5(_tmp)
        
        elif self.data["cur_loc"] == 6:
            #     j += 1
            def _tmp():
                self.data["cur_loc"] = 3
                callback()
            self._loc_6(_tmp)
        
        elif self.data["cur_loc"] == 7:
            #   i += 1
            def _tmp():
                self.data["cur_loc"] = 1
                callback()
            self._loc_7(_tmp)

        else: # == 8, END
            self._loc_8()