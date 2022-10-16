from  tkinter import * #GUI for clock
from datetime import datetime
from time import strftime

window=Tk()
window.geometry('750x200')
window.minsize(750, 200)
window.maxsize(750, 200)
window.title('Digital Clock')

frame1= Frame(window, width=750, height=200, bg='#0e1013')
frame1.place(x=0, y=0)
#frame1.pack(expand=True)

day=datetime.today().strftime('%A')
day_to_upper=day.upper()
day_word_length=day_to_upper[0:3]

time_label= Label(frame1, font=('Century Gothic',60), bg='black', foreground='#d3d3d3')
time_label.place(x=270, y=35)

day_label=Label(frame1, font=('Century Gothic',60), bg='black', foreground='#d3d3d3')
day_label.config(text=day_word_length+' ')
day_label.place(x=20, y=35)


def time():
    time_stamp=strftime('%H : %M : %S')
    time_label.config(text=time_stamp)
    time_label.after(1000, time)

time()


window.mainloop()