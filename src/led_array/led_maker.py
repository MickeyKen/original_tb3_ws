from Tkinter import *
#from tkinter import *

col_mat = []
data = [0] * 386
data[0] = 1

def color(n):
    label.configure(bg='#%02x%02x%02x' % (scale1.get() * 32, scale2.get() * 32, scale3.get() * 32))

def save():
    bank_num = str(input("Please input LED pattern number: "))
    f = open("sample" + bank_num + ".txt", "w")
    data[1] = int(bank_num)
    for x in data:
        f.write(str(x) + ",")
    f.close
    print ("Saved sample" + bank_num + ".txt")

def clear():
    for i in range(8*16):
        frame_list[i].configure(bg = "#000000")
    for i in range(384):
        data[i+2] = 0

root = Tk()
root.title("LED Matrix")
root.resizable(0,0)

menu_ROOT = Menu(root)
root.configure(menu = menu_ROOT)
 
menu_GAME = Menu(menu_ROOT, tearoff = False)
 
root_frame = Frame(root, relief = 'groove', borderwidth = 5, bg = 'LightGray')
game_frame = Frame(root_frame, relief = 'sunken', borderwidth = 0, bg = 'LightGray')
root_frame.pack()
game_frame.pack(pady = 5, padx = 5)

col_frame = Frame(root_frame, relief = 'sunken', borderwidth = 3, bg = 'LightGray')
label = Label(col_frame, text='press button', fg='#ffffff')

label.pack()

scale1 = Scale(col_frame, label='R', orient='h', from_=0, to=7, command=color)
scale2 = Scale(col_frame, label='G', orient='h', from_=0, to=7, command=color)
scale3 = Scale(col_frame, label='B', orient='h', from_=0, to=7, command=color)
scale1.pack()
scale2.pack()
scale3.pack()


button1 = Button(col_frame, text='SAVE', command=save)
button2 = Button(col_frame, text='CLEAR', command=clear)
button1.pack()
button2.pack()
col_frame.pack(side='right')

def left_click(event):
    event.widget.configure(bd = '1')
    frame_list[event.widget.num].configure(bg = '#%02x%02x%02x' % (scale1.get() * 32, scale2.get() * 32, scale3.get() * 32))
    num = event.widget.num
    r = scale1.get()
    g = scale2.get()
    b = scale3.get()
    data[3 * num + 2] = r
    data[3 * num + 3] = g
    data[3 * num + 4] = b
    
 
i = 0
frame_list = []
for x in range(8):
    for y in range(16):
        frame = Frame(game_frame, width = 30, height = 30, bd = 3, relief = 'ridge', bg = 'BLACK')
        frame.bind("<1>", left_click)
        frame.num = i
        frame_list.append(frame)
        frame.grid(row=x, column=y)
        i += 1
 
root.mainloop()
