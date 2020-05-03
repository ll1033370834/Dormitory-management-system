# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:02:15 2019

@author: 榕树
"""

from tkinter import *
from view import * #菜单栏对应的各个子页面 
from tkinter.scrolledtext import ScrolledText
from LoginPage import *  
class MainPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (800, 400)) #设置窗口大小 
  #self.root.geometry("800x400")
  self.createPage() 
  #w = ScrolledText(self.root,height=15,width = 110)
  #w.pack(side = 'bottom')
  
 def createPage(self): 
  self.inputPage = InputFrame(self.root) # 创建不同Frame 
  self.queryPage = QueryFrame(self.root) 
  self.countPage = CountFrame(self.root) 
  self.aboutPage = AboutFrame(self.root)
  self.inputPage.pack() #默认显示数据录入界面 
  menubar = Menu(self.root) 
  menubar.add_command(label='录入/修改', command = self.inputData) 
  menubar.add_command(label='查询', command = self.queryData) 
  menubar.add_command(label='维修', command = self.countData) 
  menubar.add_command(label='账号', command = self.aboutDisp)
  menubar.add_command(label='退出登录', command = self.dee)
  self.root['menu'] = menubar # 设置菜单栏
  
 def inputData(self): 
  self.inputPage.pack() 
  self.queryPage.pack_forget() 
  self.countPage.pack_forget() 
  self.aboutPage.pack_forget() 
  
 def queryData(self): 
  self.inputPage.pack_forget() 
  self.queryPage.pack() 
  self.countPage.pack_forget() 
  self.aboutPage.pack_forget() 
  
 def countData(self): 
  self.inputPage.pack_forget() 
  self.queryPage.pack_forget() 
  self.countPage.pack() 
  self.aboutPage.pack_forget() 
  
 def aboutDisp(self): 
  self.inputPage.pack_forget() 
  self.queryPage.pack_forget() 
  self.countPage.pack_forget() 
  self.aboutPage.pack() 
 def dee(self):
          import sqlite3
          cn = sqlite3.connect('drom.db')
          cur=cn.cursor()
          b1 = list()
          b1.append('yes')
          b = list()
          b.append('no')
          n = cur.execute('select * from Login where zaixian = ?',b1)
          a = n.fetchall()
          c = 0
          n = cur.execute('update Login set zaixian = ?',b) 
          cn.commit()
          cn.close()
          import MainPage
         # MainPage.destroy()    
          self.root.destroy()