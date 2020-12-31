import tkinter as tk
from logic import say_hello

root = tk.Tk() # главное окно
root.title("Quiz")
###############################################
def add_label():
    label1 = tk.Label(root, text=f'{entry.get()}',
                      bg = "#BAF4FF",
                      font=('Arial', 20),
                      padx = 20,
                      pady = 20,
                      height=2 , # в знаках!
                      relief=tk.RAISED, # граница
                      bd=3,

                      ) # окно, текст
    label1.pack() # располагаем label на окне
###############################################
icon = tk.PhotoImage(file="icon.png") # загружаем фото
root.iconphoto(False, icon) # ставим фото в качестве иконки

root.config(bg="#BAF4FF") # background

root.geometry("500x600+700+400")
root.minsize(300, 400)

root.resizable(False, False)

########################################
# кнопки
btn1 = tk.Button(root, text="Нажми",
                 command=add_label, ) # объявляем кнопку (окно, текст, функция)
btn1.pack()
########################################


entry = tk.Entry()
entry.pack()


root.mainloop() # главный цикл
