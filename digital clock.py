from tkinter import *
import time
clk = Tk()
clk.title('Clock')
clk.geometry('1350x700+0+0')
clk.config(bg='#0C1E28')

def clock():
    current_time = time.localtime()
    hr = int(current_time.tm_hour)
    mn = int(current_time.tm_min)
    sc = int(current_time.tm_sec)



    lb_hr.config(text=str(hr).zfill(2))
    lb_mn.config(text=str(mn).zfill(2))
    lb_sec.config(text=str(sc).zfill(2))

    if hr >= 12:
        lb_dn.config(text='PM')
    else:
        lb_dn.config(text='AM')



    lb_hr.after(1000,clock)





lb_hr = Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg = '#0875B7',fg = 'white')
lb_hr.place(x=350,y=200,width=150,height = 150)
lb_hr_txt = Label(clk,text='HOUR',font=('Times 20 bold',20,'bold'),bg = '#0875B7', fg = "white")
lb_hr_txt.place(x=350,y = 360,width =150,height = 50)

lb_mn = Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg = '#008E84',fg = 'white')
lb_mn.place(x=520,y=200,width=150,height = 150)
lb_mn_txt = Label(clk,text='MINUTE',font=('Times 20 bold',20,'bold'),bg = '#008E84', fg = "white")
lb_mn_txt.place(x=520,y = 360,width =150,height = 50)

lb_sec = Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg = '#06B4B8',fg = 'white')
lb_sec.place(x=690,y=200,width=150,height = 150)
lb_sec_txt = Label(clk,text='SECOND',font=('Times 20 bold',20,'bold'),bg = '#06B4B8', fg = "white")
lb_sec_txt.place(x=690,y = 360,width =150,height = 50)

lb_dn = Label(clk,text='AM',font=('Times 20 bold',70,'bold'),bg = '#9F0646',fg = 'white')
lb_dn.place(x=860,y=200,width=150,height = 150)
lb_dn_txt = Label(clk,text='NOON',font=('Times 20 bold',20,'bold'),bg = '#9F0646', fg = "white")
lb_dn_txt.place(x=860,y = 360,width =150,height = 50)


clock()
clk.mainloop()