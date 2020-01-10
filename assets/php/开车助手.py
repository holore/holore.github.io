# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:44:04 2019

@author: 鸿
"""
import tkinter as tk
import re
import webbrowser
import win32con
import win32api
import time

tiquma = ''
#键盘值
key_map = {
    "0":48,"1":49,"2":50,"3":51,"4":52,"5":53,"6":54,"7":55,"8":56,"9":57,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90, "ENTER": 13,"SHIFT" :16
}

def key_down(key):
    """
    函数功能：按下按键
    参    数：key:按键值
    """
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code,win32api.MapVirtualKey(vk_code,0),0,0)

def key_up(key):
    """
    函数功能：抬起按键
    参    数：key:按键值
    """
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)

def key_press(key):
    """
    函数功能：点击按键（按下并抬起）
    参    数：key:按键值
    """

    key_down(key)
    time.sleep(0.5)
    key_up(key)


'''定义Windows窗口的属性'''
window = tk.Tk()
window.title('开车助手')
window.geometry('500x300')
e = tk.Text(window, height=10)
e.insert('insert','输入含有链接的文本：')
e.pack()
t = tk.Text(window, height=4)
t.pack()

'''
提取用户输入文本的链接
'''
def delete_url():
    global tiquma
    var = e.get(0.0,'end')

    sub_str = re.sub(r'([^/\u0030-\u0039\u0041-\u005a\u0061-\u007a-_])',"",var)#匹配非中文字符，将中文字符删除
    #print(sub_str)

    # 筛选出链接地址
    sub_str = sub_str.replace('s/','')
    sub_str = sub_str.replace('/s/', '')
    sub_str = sub_str.replace('https://', '')
    sub_str = sub_str.replace('pan.baidu.com','')
    sub_str = sub_str.replace('/', '')

    #print(type(sub_str))
    if len(sub_str) <= 23:#用长度判定，是否含有提取码
        t.insert('insert', 'pan.baidu.com/s/' + sub_str)
        icloud_url = 'https://pan.baidu.com/s/' + sub_str
    else:
        t.insert('insert','pan.baidu.com/s/'+ sub_str[:-4])
        t.insert('insert','\n提取码：'+sub_str[-4:])
        icloud_url = 'https://pan.baidu.com/s/'+ sub_str[:-4]
        tiquma = sub_str[-4:]
    webbrowser.open(icloud_url)
    time.sleep(5)

    k = "SHIFT"   #在输入前，按下shift键               
    key_press(k)

    for i in tiquma:
        #print(i)
        key_word = '%s' % i          # 模拟键盘输入提取码，如果有大写的话，那就GG，懒得判定大写了
        #t(key_word)
        key_press(key_word)

    j = "ENTER"
    key_press(j)

    #key_press(j)





#,/,_,.,-

# 点击gkd按钮提取 链接
b1 = tk.Button(window, text='G K D！', width=10,height=2, command=delete_url)
b1.pack()
window.mainloop()





    #key_press(i)

#if __name__ == '__main__':

