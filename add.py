import tkinter as tk

new_words = []
def add_window():

    def get_data():
        data = entry.get()
        new_words.append(data)
        entry.delete(first=0, last=len(data))

        label1 = tk.Label(add_win,text=data, bg="#BAF4FF", font=20)
        label1.pack()
        print(new_words)


    add_win = tk.Tk()
    add_win.title("Add new words")

    add_win.geometry("500x500+600+400")
    add_win.config(bg="#BAF4FF")

    #icon = tk.PhotoImage(file="icon2.png")
    #add_win.iconphoto(True, icon)



    label = tk.Label(add_win, text="Введите новое слово", font=20,
                     bg="#BAF4FF"
                     )
    label.pack()


    entry = tk.Entry(add_win, bg="White")
    entry.pack()



    button = tk.Button(add_win, text="Добавить слово", command=get_data, bg="#7FBED5", font=20, padx=2)
    button.pack()



    add_win.mainloop()

#add_window()

