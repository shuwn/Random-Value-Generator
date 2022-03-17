# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font as tkFont
import calculate as ca
import excel as ex
# from test import createNewWindow
from aboutdialog import AboutDialog


class Layout:
    def __init__(self):
        self.TK = tk.Tk()
        # setting title
        self.TK.title("Random Value Generator")
        # setting menubar
        self.menubar()
        # setting window size
        width=430
        height=265
        screenwidth = self.TK.winfo_screenwidth()
        screenheight = self.TK.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.TK.geometry(alignstr)
        self.TK.resizable(width=False, height=False)

        # Define text labels
        ft = tkFont.Font(family='cursive',size=12,weight='bold')
        # Project_Name
        Project_Name=tk.Label(self.TK)
        Project_Name["anchor"] = "w"
        Project_Name["font"] = ft
        Project_Name["fg"] = "#333333"
        Project_Name["justify"] = "left"
        Project_Name["text"] = "Project Name"
        Project_Name["relief"] = "flat"
        Project_Name.place(x=40,y=30,width=140,height=30)
        
        # Reference_Value
        Reference_Value=tk.Label(self.TK)
        Reference_Value["anchor"] = "w"
        Reference_Value["font"] = ft
        Reference_Value["fg"] = "#333333"
        Reference_Value["justify"] = "left"
        Reference_Value["text"] = "Reference Value"
        Reference_Value.place(x=40,y=70,width=140,height=30)
        
        # Number_of_Samples
        Number_of_Samples=tk.Label(self.TK)
        Number_of_Samples["anchor"] = "w"
        Number_of_Samples["font"] = ft
        Number_of_Samples["fg"] = "#333333"
        Number_of_Samples["justify"] = "left"
        Number_of_Samples["text"] = "Number of Samples"
        Number_of_Samples.place(x=40,y=110,width=140,height=25)
        
        # Floating_Range
        Floating_Range=tk.Label(self.TK)
        Floating_Range["anchor"] = "w"
        Floating_Range["font"] = ft
        Floating_Range["fg"] = "#333333"
        Floating_Range["justify"] = "left"
        Floating_Range["text"] = "Floating Range(%)"
        Floating_Range.place(x=40,y=150,width=140,height=30)
        
        # define input box
        self.Project_Name_Entry=tk.Entry(self.TK)
        self.Project_Name_Entry["borderwidth"] = "1px"
        self.Project_Name_Entry["font"] = ft
        self.Project_Name_Entry["fg"] = "#333333"
        self.Project_Name_Entry["justify"] = "center"
        self.Project_Name_Entry["text"] = "Project_Name"
        self.Project_Name_Entry.place(x=190,y=30,width=200,height=30)

        self.Reference_Value_Entry=tk.Entry(self.TK)
        self.Reference_Value_Entry["borderwidth"] = "1px"
        self.Reference_Value_Entry["font"] = ft
        self.Reference_Value_Entry["fg"] = "#333333"
        self.Reference_Value_Entry["justify"] = "center"
        self.Reference_Value_Entry["text"] = "Reference_Value"
        self.Reference_Value_Entry.place(x=190,y=70,width=200,height=30)

        self.Number_of_Samples_Entry=tk.Entry(self.TK)
        self.Number_of_Samples_Entry["borderwidth"] = "1px"
        self.Number_of_Samples_Entry["font"] = ft
        self.Number_of_Samples_Entry["fg"] = "#333333"
        self.Number_of_Samples_Entry["justify"] = "center"
        self.Number_of_Samples_Entry["text"] = "Number_of_Samples"
        self.Number_of_Samples_Entry.place(x=190,y=110,width=200,height=30)

        self.Floating_Range_Entry=tk.Entry(self.TK)
        self.Floating_Range_Entry["borderwidth"] = "1px"
        self.Floating_Range_Entry["font"] = ft
        self.Floating_Range_Entry["fg"] = "#333333"
        self.Floating_Range_Entry["justify"] = "center"
        self.Floating_Range_Entry["text"] = "Floating_Range"
        self.Floating_Range_Entry.place(x=190,y=150,width=200,height=30)
        
        # define Buttion
        Button_Enter=tk.Button(self.TK)
        Button_Enter["bg"] = "#efefef"
        Button_Enter["font"] = ft
        Button_Enter["fg"] = "#000000"
        Button_Enter["justify"] = "center"
        Button_Enter["text"] = "Enter"
        Button_Enter.place(x=80,y=200,width=70,height=40)
        Button_Enter["command"] = self.btn_En_Event

        Button_Cancel=tk.Button(self.TK)
        Button_Cancel["bg"] = "#efefef"
        Button_Cancel["font"] = ft
        Button_Cancel["fg"] = "#000000"
        Button_Cancel["justify"] = "center"
        Button_Cancel["text"] = "Cancel"
        Button_Cancel.place(x=275,y=200,width=70,height=40)
        Button_Cancel["command"] = self.btn_Cl_Event
        self.TK.mainloop()
    
    def menubar(self):
        menubar = tk.Menu(self.TK)
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label="About", command = AboutDialog.createNewWindow)
        filemenu.add_command(label="Close", command = self.TK.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.TK.config(menu=menubar)

    # def about(self):
    #     messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')

    def btn_En_Event(self):
        Project_Name = str(self.Project_Name_Entry.get())
        Reference_Value = float(self.Reference_Value_Entry.get())
        Number_of_Samples = int(self.Number_of_Samples_Entry.get())
        Floating_Range = float(self.Floating_Range_Entry.get())
        database_var = ca.var_Get(Reference_Value, Floating_Range, Number_of_Samples)
        database = database_var[0]
        items = database_var[1]
        ex.Table(Project_Name, database, items)

    def btn_Cl_Event(self):
        self.TK.destroy() 

