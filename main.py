


import random
from add import add_window



words = ['голяки', 'мегера', 'курдюк', 'кутерьма']

meanings = {'голяки':'нищие', 'мегера':'богиня мести', 'курдюк':'жир барана', 'кутерьма':'суматоха, беспорядок'}

rnd_value = random.randint(0, len(words)-1)

rnd_word = words[rnd_value]

def chk_answer1(): # проверить ответ
    root.geometry("230x208+600+400") # change window geometry

    if rnd_value == 0:
        lb2 = tk.Label(root, text="Верно!", bg="Lime", font=20,)
        lb2.grid(column=0,row=3 , columnspan=2, stick='we')
    else:
        lb2 = tk.Label(root, text="Подумай еще...", bg="Red", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')
def chk_answer2(): # проверить ответ
    root.geometry("230x208+600+400")

    if rnd_value == 1:
        lb2 = tk.Label(root, text="Верно!", bg="Lime", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')
    else:
        lb2 = tk.Label(root, text="Подумай еще...", bg="Red", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')
def chk_answer3(): # проверить ответ
    root.geometry("230x208+600+400")

    if rnd_value == 2:
        lb2 = tk.Label(root, text="Верно!", bg="Lime", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')
    else:
        lb2 = tk.Label(root, text="Подумай еще...", bg="Red", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')
def chk_answer4(): # проверить ответ
    root.geometry("230x208+600+400")

    if rnd_value == 3:
        lb2 = tk.Label(root, text="Верно!", bg="Lime", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')
    else:
        lb2 = tk.Label(root, text="Подумай еще...", bg="Red", font=20,)
        lb2.grid(column=0, row=3, columnspan=2, stick='we')




import tkinter as tk
root = tk.Tk()
root.title("Quiz")

icon = tk.PhotoImage(file="icon.png")
root.iconphoto(False, icon)

###########################
root.geometry("230x135+600+400")
root.config(bg='#BAF4FF')
root.resizable(False, True)

label1 = tk.Label(root, text=f"""Что за слово?
{meanings[rnd_word]}""",
                  bg='#BAF4FF',
                  font=20,
                  )
label1.grid(row=0, column=0, columnspan=2)


###########################################

bt1 = tk.Button(root, text=words[0], command=chk_answer1, font=20, height=1, width=9, bg="#7FBED5")
bt2 = tk.Button(root, text=words[1], command=chk_answer2, font=20, height=1, width=9, bg="#7FBED5")
bt3 = tk.Button(root, text=words[2], command=chk_answer3, font=20, height=1, width=9, bg="#7FBED5")
bt4 = tk.Button(root, text=words[3], command=chk_answer4, font=20, height=1, width=9, bg="#7FBED5")
bt5 = tk.Button(root, text="Добавить новые слова", command=add_window, font=20, height=1, width=18, bg="Grey")

bt1.grid(column=0, row=1)
bt2.grid(column=0, row=2)
bt3.grid(column=1, row=1)
bt4.grid(column=1, row=2)
bt5.grid(columnspan=2, column=0, row=4, stick="we")






############################################

root.mainloop()







