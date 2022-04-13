# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font as tkFont
import webbrowser


class CreateNewWindow():
    def aboutDialog():
        # create child window
        win = tk.Toplevel()
        # display message
        #setting title
        win.title("About")
        #setting window size
        width=300
        height=200
        screenwidth = win.winfo_screenwidth()
        screenheight = win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        win.geometry(alignstr)
        win.resizable(width=False, height=False)

        ft_t = tkFont.Font(family='cursive',size=16,weight='bold')
        ft_v = tkFont.Font(family='cursive',size=14,weight='bold')   
        ft_b = tkFont.Font(family='cursive',size=12,weight='bold')
        ft = tkFont.Font(family='cursive',size=12)

        app_Name=tk.Label(win)
        app_Name["anchor"] = "center"
        app_Name["font"] = ft_t
        app_Name["fg"] = "#333333"
        app_Name["justify"] = "center"
        app_Name["text"] = "Random Value Generator"
        app_Name["relief"] = "flat"
        app_Name.place(relx=0.5, y=25, anchor="center",width=250,height=40)

        app_Version=tk.Label(win)
        app_Version["font"] = ft_v
        app_Version["fg"] = "#333333"
        app_Version["justify"] = "center"
        app_Version["text"] = "Version 0.1"
        app_Version.place(relx=0.5, y=70, anchor="center", width=100, height=20)

        dev_Name=tk.Label(win)
        dev_Name["anchor"] = "center"
        dev_Name["font"] = ft
        dev_Name["fg"] = "#333333"
        dev_Name["justify"] = "center"
        dev_Name["text"] = "Copyright © 2022 - Shuwn Hsu"
        dev_Name.place(relx=0.5, y=90, anchor="center", width=190, height=20)

        dev_Address=tk.Label(win)
        dev_Address["font"] = ft_b
        dev_Address["fg"] = "blue"
        dev_Address["justify"] = "center"
        dev_Address["cursor"] = "hand"
        dev_Address["text"] = r"https://shuwn.dev/ →"
        dev_Address.bind("<Button-1>", lambda e: CreateNewWindow.callback(r"https://shuwn.dev/"))
        dev_Address.place(relx=0.5, y=120, anchor="center", width=130, height=25)

        win_Close=tk.Button(win)
        win_Close["bg"] = "#efefef"
        win_Close["font"] = ft_b
        win_Close["fg"] = "#000000"
        win_Close["justify"] = "center"
        win_Close["text"] = "Ok"
        win_Close.place(relx=0.5, y=165, anchor="center",width=80, height=40)
        win_Close["command"] = win.destroy

    def warningWin(txt):
        win = tk.Toplevel()
        win.title("Warning")
        width=300
        height=200
        screenwidth = win.winfo_screenwidth()
        screenheight = win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        win.geometry(alignstr)
        win.resizable(width=False, height=False)

        ft_v = tkFont.Font(family='cursive',size=14,weight='bold')   
        ft_b = tkFont.Font(family='cursive',size=12,weight='bold')

        warning_txt=tk.Label(win)
        warning_txt["font"] = ft_v
        warning_txt["fg"] = "#333333"
        warning_txt["justify"] = "center"
        warning_txt["text"] = txt
        warning_txt.place(relx=0.5, y=70, anchor="center", width=200, height=40)

        win_Close=tk.Button(win)
        win_Close["bg"] = "#efefef"
        win_Close["font"] = ft_b
        win_Close["fg"] = "#000000"
        win_Close["justify"] = "center"
        win_Close["text"] = "Ok"
        win_Close.place(relx=0.5, y=165, anchor="center",width=80, height=40)
        win_Close["command"] = win.destroy

    def callback(url):
        webbrowser.open_new(url)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    CreateNewWindow.aboutDialog()
    tk.mainloop()
