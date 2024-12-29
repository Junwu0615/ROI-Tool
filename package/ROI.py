# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
import os, sys
import pandas as pd
from rich.console import Console
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

class ROI:
    def __init__(self, obj):
        self.obj = obj
        self.console = Console()
        self.file_path = './sample'
        self.font = 'C:/Windows/Fonts/msjhbd.ttc'
        # self.font = ''
        self.data = [[], [], [], [], []]
        self.symbol = '=' * 38

    @staticmethod
    def check_folder(path: str):
        is_file = os.path.exists(path)
        if not is_file:
            os.makedirs(path)

    def str_of_size(self, num, level) -> tuple:
        if level >= 2:
            return num, level
        elif num >= 10000:
            num /= 10000
            level += 1
            return self.str_of_size(num, level)
        else:
            return num, level

    def change(self, num) -> str:
        units = ['', '萬', '億']
        num, level = self.str_of_size(num, 0)
        if level > len(units): level -= 1
        return '{}{}'.format(round(num, 2), units[level])

    def profit(self, now_year) -> float:
        return now_year * self.obj.roi * 0.01

    def now_roi(self, now_year) -> float:
        return now_year + self.profit(now_year)

    def png(self, todo, col_1, col_2, file_name):
        is_font = self.font if os.path.exists(self.font) else None
        font = FontProperties(fname=is_font, size=12)
        plt.xlabel('歲數', fontproperties=font)
        if col_1 == '累積總資金':
            check = self.data[2][-1]
        else:
            check = self.data[4][-1]
        if 1000000000 > check > 100000000:
            plt.ylabel('億', fontproperties=font)
        elif 10000000000 > check > 1000000000:
            plt.ylabel('十億', fontproperties=font)
        elif 100000000000 > check > 10000000000:
            plt.ylabel('百億', fontproperties=font)
        elif check > 100000000000:
            plt.ylabel('千億', fontproperties=font)
        else:
            plt.ylabel('萬', fontproperties=font)
        plt.grid(True)
        if todo == '工作年':
            plt.plot(self.df_1[todo], self.df_1[col_1])
            plt.legend([col_1], loc='upper left', prop=font)
        else:
            plt.plot(self.df_2[todo], self.df_2[col_1])
            plt.plot(self.df_2[todo], self.df_2[col_2])
            plt.legend([col_1, col_2], loc='upper left', prop=font)
        plt.title(file_name, fontproperties=font)
        plt.savefig(f'{self.file_path}/' + file_name + '.png')
        plt.clf()

    def main(self):
        self.console.print('tips: python Entry.py -h\n\n', style= 'red bold')
        print('START: ROI calculation...\n')
        print('The information you enter is as follows :')
        self.console.print(f'- Expected to work for {self.obj.work_year} years.\n'
                           f'- {self.obj.year} years old this year.\n'
                           f'- Expected to live to {self.obj.dead} years old.\n'
                           f'- Can invest {int(self.obj.money_month / 1000)}K funds every month.\n'
                           f'- Estimated ROI: {self.obj.roi} %.\n'
                           f'- Expect to achieve {int(self.obj.object_num / 100000000)}E.\n'
                           f'- The one-time amount is {int(self.obj.money_once / 1000)}K.\n'
                           f'- Invest {int(self.obj.money_year / 1000)}K in the stock market every year.\n'
                           f'- You can live for {self.obj.break_life} years after retirement.', style= 'yellow bold')

        back_power = sys.stdout
        ROI.check_folder(self.file_path)
        sys.stdout = open(f'{self.file_path}/ROI_result.txt', 'w', encoding='utf-8')
        print(f'{self.symbol}\n複利效應是你的好朋友\n{self.symbol}')
        print('投資報酬率: ' + str(self.obj.roi) + '%')
        print('期望工作' + str(self.obj.work_year) + '年後，就退休')
        print('每月能存多少，並投入股市資金: ' + str(self.change(self.obj.money_month)))
        print('到年底，總共要投入股市資金: ' + str(self.change(self.obj.money_year)))
        print('第一次投入股市，額外加碼: ' + str(self.change(self.obj.money_once)))
        print('預期活到: ' + str(self.obj.dead) + '歲')
        print(str(self.obj.year) + '歲開始工作至老死，剩餘壽命尚有: ' + str(self.obj.dead - self.obj.year) + '年')
        print('最終期望達成金額: ' + str(self.change(self.obj.object_num)))
        print(f'\n{self.symbol}')
        now_year = self.obj.money_year
        interest_each_year = []
        count_year = 1
        record_y_1_count = 0
        record_y_2_count = 0
        money_sum = self.obj.money_year + self.obj.money_once
        all_money_year = [money_sum]

        while count_year <= self.obj.work_year + 1:
            if count_year == 1: now_year = now_year + self.obj.money_once
            now_roi = self.now_roi(now_year)
            now_roi = now_roi + self.obj.money_year
            interest = self.profit(now_year)
            now_year = now_roi
            all_money_year.append(now_roi)
            now_cost = (self.obj.money_year * count_year) + self.obj.money_once
            print('* 到目前為止投入成本有: %s' % self.change(now_cost))
            print('* 到目前為止獲得報酬有: %s' % self.change(all_money_year[-2] - now_cost))
            print('* 投資報酬率%s' % self.obj.roi + '%')
            if self.obj.year == (self.obj.year + self.obj.work_year):
                print('### 今年%s歲，退休年! ###' % self.obj.year)
            else:
                print('* 今年%s歲\n' % self.obj.year)
            self.data[0].append(self.obj.year)
            if count_year == 1:
                money_sum = self.obj.money_year + self.obj.money_once
                print(f'  第{count_year}年  投資金額有: {self.change(self.obj.money_year)}\n'
                      f'### 第一年投入尚無漲幅，需長期等待 ###\n'
                      f'   -到目前為止，累積總資金約 {self.change(self.obj.money_year + self.obj.money_once)}\n')
            else:
                print(f'  第{count_year}年  投資金額有: {self.change(self.obj.money_year)}\n'
                      f'   -隔年，對比今年賺到差額: {self.change(self.profit(all_money_year[-1]) - self.profit(all_money_year[-2]))}\n'
                      f'   -今年，對比去年所賺到差額: {self.change(self.profit(all_money_year[-2]) - self.profit(all_money_year[-3]))}\n'
                      f'   -到目前為止，累積總資金約 {self.change(all_money_year[-2])}\n')
            self.obj.year += 1
            self.data[2].append(all_money_year[-2])
            interest_each_year.append(interest)
            if now_cost < all_money_year[-2] - now_cost:
                record_y_1 = count_year
                record_y_1_count += 1
            if record_y_1_count == 1: print('### 第' + str(record_y_1) + '年，到目前為止獲得的報酬，已超過投入的本金 ###')
            if self.obj.object_num < all_money_year[-2]:
                record_y_2 = count_year
                record_y_2_count += 1
            if record_y_2_count == 1:
                print('### 第' + str(record_y_2) + '年，達成當初所設立的目標金額: ' + str(self.obj.object_num) + ' ###')
            count_year += 1
            print(self.symbol)
        self.obj.year -= 1
        for b_life in range(1, self.obj.break_life + 1):
            print()
            if b_life == 1:
                now_year = all_money_year[-2]
            else:
                now_year = now_year * 1.15
                interest = self.profit(now_year)
                all_money_year.append(now_year)
                interest_each_year.append(interest)
            print('* 今年%s歲' % self.obj.year)
            print('資金運用之方案一: 被動收入')
            print('### 退休後，被動收入經換算後...每年 %s / 每月 %s / 每天 %s ###' % (
                self.change(interest_each_year[-2]), self.change(interest_each_year[-2] / 12),
                self.change(interest_each_year[-2] / 12 / 30)))
            print('### 如果只領利息，不賣本，前提是ROI還是穩定維持下去 ###\n')
            print('資金運用之方案二: 提領出來')
            if b_life == 1:
                print('### 而一次提領約有: %s ###' % (self.change(all_money_year[-2])))
                print('### 還能活%s年，換算...每年能花 %s元 / 每月能花 %s元 / 每日能花 %s元 ###' % (
                    self.change(self.obj.break_life), self.change(all_money_year[-2] / self.obj.break_life),
                    self.change(all_money_year[-2] / self.obj.break_life / 12),
                    self.change(all_money_year[-2] / self.obj.break_life / 12 / 30)))
                self.data[3].append(interest_each_year[-2])
                self.data[4].append(all_money_year[-2])
            else:
                print('### 而一次提領約有: %s ###' % (self.change(all_money_year[-1])))
                print('### 還能活%s年，換算...每年能花 %s元 / 每月能花 %s元 / 每日能花 %s元 ###' % (
                    self.change(self.obj.break_life), self.change(all_money_year[-1] / self.obj.break_life),
                    self.change(all_money_year[-1] / self.obj.break_life / 12),
                    self.change(all_money_year[-1] / self.obj.break_life / 12 / 30)))
                self.data[3].append(interest_each_year[-2])
                self.data[4].append(all_money_year[-1])
            self.data[1].append(self.obj.year)
            self.obj.break_life -= 1
            self.obj.year += 1
            print(f'\n{self.symbol}')
        self.df_1 = pd.DataFrame({'工作年': self.data[0], '累積總資金': self.data[2]})
        self.df_2 = pd.DataFrame({'退休年': self.data[1], '每年退休後被動收入': self.data[3], '提領出來': self.data[4]})
        print(self.df_1)
        print(self.symbol)
        print(self.df_2)
        self.png(todo='工作年', col_1='累積總資金', col_2='無',
                 file_name='工作年-每年定存再投入之總資金成長走勢')
        self.png(todo='退休年', col_1='提領出來', col_2='每年退休後被動收入',
                 file_name='退休年-每年退休後之被動收入&提領出來之成長走勢')
        sys.stdout.close()
        sys.stdout = back_power
        print(f'\nEND: Output is complete !\n'
              f'The file is stored in the path ({self.file_path}), which contains txt*1 / png*2.')