import tkinter as tk
from tkinter import ttk
from db import schedule_check



if __name__ == "__main__":
    window = tk.Tk()
    window.title("Rainbow TextBox")
    window.geometry("600x400")

    canvas = tk.Canvas(window, width=300, height=200)
    canvas.pack()

    elabel = ttk.Label(window, text="年月日を入力(yyyy-mm-dd)")
    canvas.create_window(0, 100, window=elabel)
    entry1 = tk.Entry(window)
    canvas.create_window(200, 100, window=entry1)

    elabel = ttk.Label(window, text="予定を入力")
    canvas.create_window(0, 130, window=elabel)
    entry2 = tk.Entry(window)
    canvas.create_window(200, 130, window=entry2)

    elabel = ttk.Label(window, text="時間を入力(hh:mm)")
    canvas.create_window(0, 160, window=elabel)
    entry3 = tk.Entry(window)
    canvas.create_window(200, 160, window=entry3)

    elabel = ttk.Label(window, text="場所を入力")
    canvas.create_window(0, 190, window=elabel)
    entry4 = tk.Entry(window)
    canvas.create_window(200, 190, window=entry4)


    def getValue():
        tval_1 = entry1.get()
        label = tk.Label(window, text=tval_1)
        canvas.create_window(0, 160, window=label)

        tval_2 = entry2.get()
        label = tk.Label(window, text=tval_2)
        canvas.create_window(0, 160, window=label)

        tval_3 = entry3.get()
        label = tk.Label(window, text=tval_2)
        canvas.create_window(0, 160, window=label)

        tval_4 = entry4.get()
        label = tk.Label(window, text=tval_2)
        canvas.create_window(0, 160, window=label)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)

        schedule_check(tval_1, tval_2, tval_3, tval_4)

    button = tk.Button(text="入力テキスト値の取得", command=getValue)
    canvas.create_window(200, 50, window=button)

    def close_window():
        window.destroy()
    button = tk.Button(text="Quit",command=close_window)
    canvas.create_window(300,50,window=button)

    window.mainloop()
