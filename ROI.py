import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from matplotlib.font_manager import FontProperties

def str_of_size(num, level):
    if level >= 2: return num, level
    elif num >= 10000: num /= 10000; level += 1; return str_of_size(num, level)
    else: return num, level

def change(num):
    units = ['', '萬', '億']
    num, level = str_of_size(num, 0)
    if level > len(units): level -= 1
    return '{}{}'.format(round(num, 2), units[level])

def Interest(now_year):
    return now_year*ROI*0.01  

def Now_year_ROI(now_year):
    return now_year + Interest(now_year)

def png(year_type, value_1, value_2, value_3):
    font = FontProperties(fname = "C:/Windows/Fonts/msjhbd.ttc", size = 12)
    plt.xlabel("歲數" , fontproperties = font)
    if value_1 == "累積總資金": check = data[2][-1]
    else: check = data[4][-1]
    if 1000000000 > check > 100000000: plt.ylabel("億" , fontproperties = font)
    elif 10000000000 > check > 1000000000: plt.ylabel("十億" , fontproperties = font)
    elif 100000000000 > check > 10000000000: plt.ylabel("百億" , fontproperties = font)
    elif check > 100000000000: plt.ylabel("千億" , fontproperties = font)
    else: plt.ylabel("萬" , fontproperties = font)
    plt.grid(True)
    if year_type == "工作年": plt.plot(df_1[year_type], df_1[value_1]); plt.legend([value_1], loc="upper left", prop = font); 
    else: plt.plot(df_2[year_type], df_2[value_1]); plt.plot(df_2[year_type], df_2[value_2]); plt.legend([value_1, value_2], loc="upper left", prop = font); 
    plt.title(value_3, fontproperties = font)
    plt.savefig("results/"+ value_3 + ".png")
    plt.clf()
    
def parse_args():
    parse = ArgumentParser()
    parse.add_argument("-w", "--work_year", help = "How many years do you expect to work?", default = 30, type = int)
    parse.add_argument("-y", "--year", help = "How old are you this year?", default = 26, type = int)
    parse.add_argument("-d", "--dead", help = "How old do you want to live?", default = 90, type = int)
    parse.add_argument("-e", "--money_month", help = "How much money can be invested in the stock market every month?", default = 10000, type = int)
    parse.add_argument("-r", "--ROI", help = "Return On Investment, ROI", default = 15, type = int)
    parse.add_argument("-o", "--object_num", help = "How much do you expect to achieve?", default = 300000000, type = int)
    parse.add_argument("-m", "--money_once", help = "Do you have a one-time amount? If so, fill in the number. Otherwise, fill in 0.", default = 300000, type = int)
    args = parse.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    work_year = args.work_year  # 預計工作x年
    year = args.year  # 今年年齡
    dead = args.dead  # 預期活到x歲
    money_month = args.money_month  # 每月能投入x資金
    ROI = args.ROI  # 投資報酬率
    object_num = args.object_num  # 預期想達成金額
    money_once = args.money_once  # 一次性金額，如沒填0
    money_year = money_month * 12  # 每年要投入股市資金
    break_life = dead - (year + work_year)  # 退休還能活幾年
    print("START: ROI calculation...\n")
    print("The information you enter is as follows :")
    print(f"- Expected to work for {work_year} years.\n- {year} years old this year.\n- Expected to live to {dead} years old.\n- Can invest {int(money_month/1000)}K funds every month.\n- Estimated ROI: {ROI}%.\n- Expect to achieve {int(object_num/100000000)}E.\n- The one-time amount is {int(money_once/1000)}K.\n- Invest {int(money_year/1000)}K in the stock market every year.\n- You can live for {break_life} years after retirement.")
    back_power = sys.stdout
    isExists_file = os.path.exists('./results')
    if not isExists_file: os.makedirs('./results') 
    sys.stdout = open('results/ROI_result.txt', 'w', encoding = "utf-8")
    print("======================================\n複利效應是你的好朋友\n======================================")
    print("投資報酬率: " + str(ROI) + "%")
    print("期望工作" + str(work_year) + "年後，就退休")
    print("每月能存多少，並投入股市資金: " + str(change(money_month)))
    print("到年底，總共要投入股市資金: " + str(change(money_year)))
    print("第一次投入股市，額外加碼: " + str(change(money_once)))
    print("預期活到: " + str(dead) + "歲")
    print(str(year) + "歲開始工作至老死，剩餘壽命尚有: " + str(dead - year) + "年")
    print("最終期望達成金額: " + str(change(object_num)))
    print("\n======================================")
    now_year = money_year; interest_each_year = []; count_year = 1; record_y_1_count = 0; record_y_2_count = 0; money_sum = money_year + money_once; ALL_money_year = [money_sum]; 
    data = [[], [], [], [], []]
    while count_year <= work_year + 1:
        if count_year == 1: now_year = now_year + money_once
        now_year_ROI = Now_year_ROI(now_year)
        now_year_ROI = now_year_ROI + money_year
        interest = Interest(now_year)
        now_year = now_year_ROI
        ALL_money_year.append(now_year_ROI)
        now_cost = (money_year * count_year) + money_once
        print("* 到目前為止投入成本有: %s" % change(now_cost))
        print("* 到目前為止獲得報酬有: %s" % change(ALL_money_year[-2] - now_cost))
        print("* 投資報酬率%s" % ROI + "%")
        if year == (year + work_year): print("### 今年%s歲，退休年! ###" % year)
        else: print("* 今年%s歲\n" % year)
        data[0].append(year)
        if count_year == 1: money_sum = money_year + money_once; print(f"  第{count_year}年  投資金額有: {change(money_year)}\n### 第一年投入尚無漲幅，需長期等待 ###\n   -到目前為止，累積總資金約 {change(money_year + money_once)}\n")
        else: print(f"  第{count_year}年  投資金額有: {change(money_year)}\n   -隔年，對比今年賺到差額: {change(Interest(ALL_money_year[-1]) - Interest(ALL_money_year[-2]))}\n   -今年，對比去年所賺到差額: {change(Interest(ALL_money_year[-2]) - Interest(ALL_money_year[-3]))}\n   -到目前為止，累積總資金約 {change(ALL_money_year[-2])}\n")
        year += 1
        data[2].append(ALL_money_year[-2])
        interest_each_year.append(interest)
        if now_cost < ALL_money_year[-2] - now_cost: record_y_1 = count_year; record_y_1_count += 1; 
        if record_y_1_count == 1: print("### 第" + str(record_y_1) + "年，到目前為止獲得的報酬，已超過投入的本金 ###")
        if object_num < ALL_money_year[-2]: record_y_2 = count_year; record_y_2_count += 1; 
        if record_y_2_count == 1: print("### 第" + str(record_y_2) + "年，達成當初所設立的目標金額: " + str(object_num) + " ###")
        count_year += 1; print("======================================"); 
    year -= 1
    for b_life in range(1, break_life + 1):
        print()
        if b_life == 1: now_year = ALL_money_year[-2]
        else: now_year = now_year * 1.15; interest = Interest(now_year); ALL_money_year.append(now_year); interest_each_year.append(interest); 
        print("* 今年%s歲" % year)
        print("資金運用之方案一: 被動收入")
        print("### 退休後，被動收入經換算後...每年 %s / 每月 %s / 每天 %s ###" % (change(interest_each_year[-2]), change(interest_each_year[-2] / 12), change(interest_each_year[-2] / 12 / 30)))
        print("### 如果只領利息，不賣本，前提是ROI還是穩定維持下去 ###\n")
        print("資金運用之方案二: 提領出來")
        if b_life == 1:
            print("### 而一次提領約有: %s ###" % (change(ALL_money_year[-2])))
            print("### 還能活%s年，換算...每年能花 %s元 / 每月能花 %s元 / 每日能花 %s元 ###" % (change(break_life), change(ALL_money_year[-2] / break_life), change(ALL_money_year[-2] / break_life / 12), change(ALL_money_year[-2] / break_life / 12 / 30)))
            data[3].append(interest_each_year[-2])
            data[4].append(ALL_money_year[-2])
        else:
            print("### 而一次提領約有: %s ###" % (change(ALL_money_year[-1])))
            print("### 還能活%s年，換算...每年能花 %s元 / 每月能花 %s元 / 每日能花 %s元 ###" % (change(break_life), change(ALL_money_year[-1] / break_life), change(ALL_money_year[-1] / break_life / 12), change(ALL_money_year[-1] / break_life / 12 / 30)))
            data[3].append(interest_each_year[-2])
            data[4].append(ALL_money_year[-1])
        data[1].append(year); break_life -= 1; year += 1; print("\n======================================")
    df_1 = pd.DataFrame({"工作年": data[0], "累積總資金": data[2]})
    df_2 = pd.DataFrame({"退休年": data[1], "每年退休後被動收入": data[3], "提領出來": data[4]})
    print(df_1); print("======================================"); print(df_2)
    png("工作年", "累積總資金", "無", "工作年-每年定存再投入之總資金成長走勢")
    png("退休年", "提領出來", "每年退休後被動收入", "退休年-每年退休後之被動收入&提領出來之成長走勢")
    sys.stdout.close(); sys.stdout = back_power; 
    print("\nEND: Output is complete !\nThe file is stored in the path (./results/), which contains txt*1 / png*2.")