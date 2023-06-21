import tkinter,time,sys,os

os.chdir("D:\\")
last = open("date.txt",'r+')
b = open('classes.txt','r')
a = list(eval(last.read()))
lasttoday = a.pop()#上一周周五日期
times = a.pop()#次数
a.clear()
today = time.strftime('%d')#这周周五日期
day = time.strftime('%a')#今天的星期
screen = tkinter.Tk()

screenwidth = screen.winfo_screenwidth()
screenheight = screen.winfo_screenheight()
width = 1050
height = 70
size = "%dx%d+%d+0" % (width, height, (screenwidth - width) / 2)
screen.geometry(size)

screen.overrideredirect(True)
screen.attributes('-alpha',0.7)
menu = tkinter.Menu(screen,tearoff=0)
v = tkinter.StringVar()
classes = eval(b.read())

def popupmenu(event):
	menu.post(event.x_root,event.y_root)

def show(day):
	v.set(classes[day])

screen.bind("<Button-3>",popupmenu)

if day == 'Mon':
	show(0)
elif day == 'Tue':
	show(1)
elif day == 'Wed':
	show(2)
elif day == 'Thu':
	show(3)
elif day == 'Fri':
	if int(today) == int(lasttoday):#如果还是今天，就不做出反应
		pass
	else:#如果不是今天，次数加一
		times += 1
		last.write(','+str(int(times)))
		last.write(','+str(int(today)))
		last.close()
	if times == 10:
		last.close()
		last = open('date.txt','w')
		last.write('1'+','+str(int(today)))
	if times == 5:
		times += 1
		last.write(','+str(int(times)))
		last.write(','+str(int(today)))
	if times == 4 or times == 9:
		show(8)
	elif times %2 == 1:
		show(4)
	else:
		show(5)
elif day == 'Sat':
	if times %2 == 1:
		show(6)
	else:
		show(7)

a = tkinter.Label(screen,textvariable=v,anchor='nw',font='宋体 50',height=70,width=50)
a.pack()
menu.add_command(label="周一",command=lambda : show(0))
menu.add_command(label="周二",command=lambda : show(1))
menu.add_command(label="周三",command=lambda : show(2))
menu.add_command(label="周四",command=lambda : show(3))
menu.add_command(label="周五一",command=lambda : show(4))
menu.add_command(label="周五二",command=lambda : show(5))
menu.add_command(label="第一轮",command=lambda : show(6))
menu.add_command(label="第二轮",command=lambda : show(7))
menu.add_command(label="周五",command=lambda : show(8))
last.close()
screen.mainloop()