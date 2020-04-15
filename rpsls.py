#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：植产四班冉禧玥
日期：2020年4月13日
"""

import random  #利用random使计算机产生随机数



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀


def name_to_number(choice_name):
    """
    将游戏对象对应到不同的整数
    """
    if choice_name == "石头":
       player_choice_number=0
    elif choice_name == "史波克":
       player_choice_number=1
    elif choice_name == "纸":
       player_choice_number=2
    elif choice_name == "蜥蜴":
       player_choice_number=3
    elif choice_name == "剪刀":
       player_choice_number=4
    else:
       print("Error:No correct Name")
    return choice_name
             
    # 使用if/elif/else语句将各游戏对象对应到不同的整数


import random
comp_number=random.randint(0,5)

def number_to_name(comp_number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if comp_number == 0:
       comp_name="石头"
    elif comp_number == 1:
       comp_name="史波克"
    elif comp_number == 2:
       comp_name="纸"
    elif comp_number == 3:
       comp_name="蜥蜴"
    elif comp_number == 4:
       comp_name="剪刀"
    return comp_name
    
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象


def rpsls(choice_name):
	if choice_name == comp_name:
	   print("平局")
	elif (choice_name == "纸" and comp_name == "石头")or(choice_name == "石头" and comp_name == "蜥蜴")or(choice_name == "蜥蜴" and comp_name == "史波克")or(choice_name == "史波克" and comp_name == "剪刀")or(choice_name == "剪刀" and comp_name == "蜥蜴")or(choice_name == "蜥蜴" and comp_name == "纸")or(choice_name == "史波克" and comp_name == "石头")or(choice_name == "石头" and comp_name == "剪刀")or(choice_name == "剪刀" and comp_name == "纸")or(choice_name == "纸" and comp_name == "史波克"):
	   print("你赢了！")
	else:
	   print("你输了！")
"""
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
"""



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
choice_name=name_to_number(choice_name)
print("您的选择是:"+choice_name)
comp_name=number_to_name(comp_number)
print("计算机的选择是："+comp_name)
rpsls(choice_name)
