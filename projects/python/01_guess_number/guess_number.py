# -*- coding: utf-8 -*-
"""
项目 1：猜数字游戏

玩法：电脑随机想一个 1~100 的数字，你来猜，电脑会提示「太大」或「太小」，
      直到你猜对为止，并告诉你一共猜了几次。
"""

# ---------- 1. 导入工具 ----------
import random  # random 是 Python 自带的「随机数」工具包


# ---------- 2. 准备数据 ----------
secret = random.randint(1, 100)  # 让电脑随机生成一个 1~100 的整数，存进 secret

count = 0  # 计数器：记录你猜了多少次，一开始是 0

print("我想好了一个 1 到 100 之间的数字，你来猜猜看！")


# ---------- 3. 开始循环猜 ----------
while True:  # True 意思是「一直重复」，直到遇到 break 才停下

    # input() 会停下来等你在键盘输入，返回的永远是「文字」
    guess_text = input("请输入你猜的数字：")

    # 把文字转成整数，才能和 secret 比较大小
    guess = int(guess_text)

    count = count + 1  # 每猜一次，次数加 1

    # ---------- 4. 判断 ----------
    if guess > secret:
        print("太大了！再小一点")
    elif guess < secret:
        print("太小了！再大一点")
    else:
        print("恭喜你，猜对了！")
        print("你一共猜了", count, "次")
        break  # 猜对了，跳出循环，程序结束
