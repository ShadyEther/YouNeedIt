import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from widgets.math.calculator import *
from widgets.text.text_case import *

class CollapsiblePanel(ThemedTk):
    def __init__(self):
        super().__init__(theme="default")
        
        self.title("You Need It")
        # self.geometry("500x500")

        
        
        
        self.header = ttk.Frame(self, height=50)
        self.header.pack(side=tk.TOP, fill=tk.X)

        self.header_label = ttk.Label(self.header, text="You Need It", font=("Arial", 16))
        self.header_label.pack(pady=10,side=tk.RIGHT)
        


        
        self.container = ttk.Frame(self)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
        self.side_panel = ttk.Frame(self.container, width=200)
        self.side_panel.pack(side=tk.LEFT, fill=tk.Y)
        
        self.side_panel_content = ttk.Frame(self.side_panel)
        self.side_panel_content.pack(pady=10)
        

        self.calculator_button=ttk.Button(self.side_panel_content, text="Calculator", command=self.HandleCalculator)
        self.calculator_button.pack(padx=5,pady=5)
        
        self.text_case_button=ttk.Button(self.side_panel_content, text="Text Case", command=self.HandleTextCase)
        self.text_case_button.pack(padx=5,pady=5)

        
        
        self.main_content = ttk.Frame(self.container)
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.main_content_label = ttk.Label(self.main_content, text="Main Content", font=("Arial", 14))
        self.main_content_label.pack(pady=20)
        
        
        self.toggle_button = ttk.Button(self.header, text="☰", command=self.toggle_side_panel)
        self.toggle_button.place(x=10, y=10)
        
        self.side_panel_visible = True

    def toggle_side_panel(self):
        if self.side_panel_visible:
            self.side_panel.pack_forget()
        else:
            self.side_panel.pack(side=tk.LEFT, fill=tk.Y)
        self.side_panel_visible = not self.side_panel_visible

    
    def HandleCalculator(self):
        for _ in self.main_content.winfo_children():
            _.destroy()
        calculator_obj=CalculatorWidget(self.main_content)
        calculator_obj.pack(expand=True, fill="both", padx=50)
        # calculator_obj.configure(background='red')

    def HandleTextCase(self):
        for _ in self.main_content.winfo_children():
            _.destroy()
        
        text_case_obj=TextCaseWidget(self.main_content)
        text_case_obj.pack(expand=True, fill="both", padx=50)

        
        


if __name__ == "__main__":
    app = CollapsiblePanel()
    app.mainloop()
