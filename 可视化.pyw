import tkinter,time,os,sys

screen = tkinter.Tk()
screen.geometry('800x700')
os.chdir("D:\\")
j = open('date.txt','w')
j.write('0,0')
j.close()
date = open('classes.txt','w')
label_tishi = tkinter.Label(screen,font=('宋体',20),text="按照“早自习，上午课程，下午课程，听力，晚自习”的顺序填写\n例如“语语数外物化政史地生语政史地”")

text_shuru = []
classes = []
classes_extra = []
final = []
class Label_show():
	def __init__(self,num):
		text = ["周一课程","周二课程","周三课程","周四课程","周五课程"]
		self.entry = tkinter.Entry(screen,font=('宋体',25),width = 30)
		self.label = tkinter.Label(screen,font=('宋体',25),text=text[num])
label_tishi.pack()
entry1 = tkinter.Entry(screen,font=('宋体',25),width = 30)
entry2 = tkinter.Entry(screen,font=('宋体',25),width = 30)

def chucun():
	for c in text_shuru:
		c = c.entry.get()
		classes.append(c)
	classes_extra.append(str(entry1.get()))
	classes_extra.append(str(entry2.get()))
	for f in classes:
		final.append(f[:1]+'|'+f[1:6]+'|'+f[6:10]+'|'+f[10:14])
	for f in classes_extra:
		final.append(f[:1]+'|'+f[1:6]+'|'+f[6:9])
	date.write(str(final))
	date.close()
	sys.exit()

button = tkinter.Button(screen,text='确认',font=('宋体',15),height=3,width=30,command=chucun)
label_sat1 = tkinter.Label(screen,font=('宋体',25),text='周六第一轮')
label_sat2 = tkinter.Label(screen,font=('宋体',25),text='周六第二轮')



for x in range(5):
	x = Label_show(num=x)
	text_shuru.append(x)
for b in text_shuru:
	b.label.pack()
	b.entry.pack()


label_sat1.pack()
entry1.pack()
label_sat2.pack()
entry2.pack()
button.pack(side = 'bottom')


screen.mainloop()