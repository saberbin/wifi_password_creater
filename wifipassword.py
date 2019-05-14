# -*- coding:utf-8 -*-
# user/saberbin/wifipassword.py
# 2019-05-14

import  random

class PassWordCreater():
    '''这是关于产生随机WiFi密码的生成类，可生成包括大小写字母、数字的WiFi密码
    creat_password方法是创建不含重复元素的WiFi密码
    creat_password2方法是创建包含重复元素的WiFi密码'''
    def __init__(self):
        # self.num = [0,1,2,3,4,5,6,7,8,9]
        # 创建WiFi密码元素列表
        self.letter= ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.wifipassword = '' # 创建保存WiFi密码的字符串
        self.password_num = 10 # 循环次数（WiFi密码的位数，不能小于8）

    def creat_password(self):
        letter = self.letter.copy() # 复制列表，在新列表中进行操作
        rang_num = self.password_num # 循环次数（WiFi密码的位数，不能小于8）
        wifipassword = '' # 临时保存密码的字符串
        for i in range(rang_num):
            word = random.choice(letter) # 从列表中随机抽取一个元素
            wifipassword = wifipassword + word # 将元素拼接到保存的字符串中
            letter.pop(letter.index(word)) # 将列表中已经抽取做密码的元素去除，防止出现重复的WiFi密码元素
        self.wifipassword = wifipassword # 将WiFi密码保存到类属性
    
    def creat_password2(self):
        letter = self.letter.copy() # 复制列表，在新列表中进行操作
        rang_num = self.password_num # 循环次数（WiFi密码的位数，不能小于8）
        wifipassword = '' # 临时保存密码的字符串
        for i in range(rang_num):
            word = random.choice(letter) # 从列表中随机抽取一个元素
            wifipassword = wifipassword + word # 将元素拼接到保存的字符串中
            # letter.pop(letter.index(word)) # 将列表中已经抽取做密码的元素去除，防止出现重复的WiFi密码元素
        self.wifipassword = wifipassword # 将WiFi密码保存到类属性
        


if __name__ == "__main__":
    new_wifipassword = PassWordCreater() # 创建一个密码创建的实例
    new_wifipassword.creat_password() # 使用创建密码的方法
    print('The new password is :',new_wifipassword.wifipassword) # 输出WiFi密码
    new_wifipassword.creat_password2()
    print('The new password is :',new_wifipassword.wifipassword) # 输出WiFi密码
