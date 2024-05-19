import tkinter as tk
from tkinter import ttk

class CalculatorWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self.expression = ""

        # Entry widget to display the expression
        self.entry = ttk.Entry(self, font=("Arial", 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Buttons for digits and operators
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for btn_text, row, col in buttons:
            ttk.Button(
                self, text=btn_text, command=lambda text=btn_text: self.append_to_expression(text)
            ).grid(row=row, column=col, sticky="nsew")

        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def append_to_expression(self, text):
        if text == "=":
            try:
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += text
            self.entry.insert(tk.END, text)

if __name__ == "__main__":
    # Example usage
    root = tk.Tk()
    calculator = CalculatorWidget(root)
    calculator.pack(expand=True, fill="both")
    root.mainloop()
