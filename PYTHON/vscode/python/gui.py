from tkinter import *
from tkinter import font

# 
root = Tk()

# root.title("Hello World!")
# root.geometry("400x300")
# root.wm_iconbitmap("the_eye.ico")
# list_fonts = list(font.families())
# print(list_fonts)

c = Canvas(root, bg="#091e42", height=700, width=1200)
# file1 = PhotoImage(file="minion.gif")
# file2 = PhotoImage(file="leo3.gif")
# id = c.create_image(500, 200, anchor=NE, image=file1, activeimage=file2)
# id = c.create_text(500, 500, text="This is a thrilling photo", font=('Helvetica', 30, 'bold'), fill= 'blue')


# id = c.create_line(50, 50, 200, 50, 200, 150, width=4, fill="white")
# id = c.create_oval(100, 100, 400, 300, width=5, fill="yellow", outline='red', activefill='green')
# id = c.create_polygon(600, 250,700,200,800,250,800,400,600,400, width=2, fill="yellow", outline="red")
# c.create_line(600,250,800,250, width=2, fill="red")
# c.create_rectangle(650,275, 750, 375, fill="red")
# x1,y1= 0,350
# x2, y2=200, 450
# for i in range(3):
#     c.create_arc(x1,y1,x2, y2, start=0, extent=180, fill='green')
#     x1+= 200
#     x2 += 200
# c.create_arc(800,350,1000,450,start=0, extent= 180, fill='green')
# c.create_arc(1000, 350, 1200, 450, start=0, extent= 180, fill='green')
# file1 = PhotoImage(file="minion.gif")
# c.create_image(10,100, anchor=NW, image= file1)
# id = c.create_text(600,600,text="Hello friends I live here...", font=('Helvetica', 30, 'bold'),fill="magenta")

# fnt = ('Times', 40, 'bold italic underline')
# id = c.create_text(500, 100, text="My name is satyam, and i am doing really well...", font=fnt, fill='yellow', activefill='green')
c.pack()



root.mainloop()
