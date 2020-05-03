from tkinter import *
from tkinter.messagebox import *
from MainPage import *
  
class LoginPage(object): 
 def __init__(self, master=None): 
  self.root = master #定义内部变量root 
  self.root.geometry('%dx%d' % (300, 180)) #设置窗口大小 
  self.username = StringVar() 
  self.password = StringVar() 
  self.createPage() 
  
 def createPage(self): 
  self.page = Frame(self.root) #创建Frame 
  self.page.pack() 
  Label(self.page).grid(row=0, stick=W) 
  Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10) 
  Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E) 
  Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10) 
  Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E) 
  Button(self.page, text='管理员登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10) 
  Button(self.page, text='注册', command=self.zhuce).grid(row=3, column=1, stick=E) 
 def zhuce(self):
    import sqlite3
    cn = sqlite3.connect('drom.db')
    cur=cn.cursor()
    b = list()
    user = self.username.get()
    flag1 = 1
    if not user.strip():
        flag1 = 0
    b.append(user)
    user = self.password.get()
    if not user.strip():
        flag1 = 0
    if flag1 == 0:
        showinfo("logo","用户名密码不为空，请输入")
        cn.close()
        return
    n = cur.execute('select * from Login where user = ?',b)
    a = n.fetchall()
    c=0
    for i in a :
        if i[0] == b[0]:
            showinfo("logo","用户名重复")
            c=1
            break
    if c==1:
        cn.commit()
        cn.close()
    else :
        b.append(user)
        b.append('no')
        cur.execute('insert into Login VALUES (?,?,?)', b)
        showinfo("logo","注册成功")
        cn.commit()
        cn.close()
 def loginCheck(self):
    import sqlite3
    name = self.username.get() 
    secret = self.password.get()
    cn = sqlite3.connect('drom.db')
    cur=cn.cursor()
    b = list()
    b2 = list()
    user = name
    flag1 = 1
    if not user.strip():
        flag1 = 0
    b.append(user)
    b2.append(user)
    user = secret
    if not user.strip():
        flag1 = 0
    b.append(user)
    b2.append(user)
    b2.append('yes')
    b2.append(name)
    b2.append(secret)
    if flag1 == 0:
        showinfo("错误","用户名密码不为空，请重新输入")
        cn.close()
        return
    n = cur.execute('select * from Login where user = ? and password = ?',b)
    cn.commit()
    a = n.fetchall()
    c=0
    b3 = list()
    b3.append('no')
    for i in a :
        if i[0] == b[0]:
            n = cur.execute('update Login set zaixian = ?',b3)
            n = cur.execute('update Login set user = ?, password = ?, zaixian = ? where user == ? and password == ?',b2)
            self.page.destroy()
            cn.commit()
            cn.close()
            MainPage(self.root) 
            c = 1
            break
    if c==1:
        a = 1
    else :
        showinfo(title='错误', message='账号或密码错误！')
        cn.close()
