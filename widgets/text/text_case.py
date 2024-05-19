import tkinter as tk
from tkinter import ttk

import re

class TextCaseWidget(ttk.Frame):


    

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        list_of_options=["UPPERCASE","lowercase","CamelCase","snake_case"]
        self.combo=ttk.Combobox(self,values=list_of_options)
        self.combo.grid(row=0,column=0, columnspan=5, sticky="ew",padx=20,pady=20)
        self.combo.set("Select the case")

        self.combo.bind("<<ComboBoxSelected>>",self.on_select)

        self.input_field=ttk.Entry(self,justify=tk.LEFT)
        self.input_field.grid(row=1,column=0,columnspan=5,rowspan=5,sticky="ew",padx=20,pady=20)

    def on_select(self,event):
        selection=self.combo.get()
        if selection=="UPPERCASE":
            return "to Uppercase"
    


    

        

if __name__ == "__main__":
    # Example usage
    root = tk.Tk()
    calculator = CalculatorWidget(root)
    calculator.pack(expand=True, fill="both")
    root.mainloop()
