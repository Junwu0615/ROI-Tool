# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from package.ROI import ROI
from package.ArgumentParser import AP

class Entry:
    def __init__(self):
        self.work_year = None
        self.year = None
        self.dead = None
        self.money_month = None
        self.roi = None
        self.object_num = None
        self.money_once = None
        self.money_year = None
        self.break_life = None

    def main(self):
        ap = AP(self)
        ap.config_once()
        roi = ROI(self)
        roi.main()

if __name__ == '__main__':
    entry = Entry()
    entry.main()