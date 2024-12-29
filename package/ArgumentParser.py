# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from argparse import ArgumentParser, Namespace

class AP:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def parse_args() -> Namespace:
        parse = ArgumentParser()
        parse.add_argument("-w", "--work_year",
                           help="How many years do you expect to work?",
                           default=30, type=int)
        parse.add_argument("-y", "--year",
                           help="How old are you this year?",
                           default=26, type=int)
        parse.add_argument("-d", "--dead",
                           help="How old do you want to live?",
                           default=90, type=int)
        parse.add_argument("-e", "--money_month",
                           help="How much money can be invested in the stock market every month?",
                           default=10000, type=int)
        parse.add_argument("-r", "--roi",
                           help="Return On Investment, ROI",
                           default=15, type=int)
        parse.add_argument("-o", "--object_num",
                           help="How much do you expect to achieve?",
                           default=300000000, type=int)
        parse.add_argument("-m", "--money_once",
                           help="Do you have a one-time amount? If so, fill in the number. Otherwise, fill in 0.",
                           default=300000, type=int)
        return parse.parse_args()

    def config_once(self):
        args = AP.parse_args()
        self.obj.work_year = args.work_year  # 預計工作x年
        self.obj.year = args.year  # 今年年齡
        self.obj.dead = args.dead  # 預期活到x歲
        self.obj.money_month = args.money_month  # 每月能投入x資金
        self.obj.roi = args.roi  # 投資報酬率
        self.obj.object_num = args.object_num  # 預期想達成金額
        self.obj.money_once = args.money_once  # 一次性金額，如沒填0
        self.obj.money_year = self.obj.money_month * 12  # 每年要投入股市資金
        self.obj.break_life = self.obj.dead - (self.obj.year + self.obj.work_year)  # 退休還能活幾年