import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Customized Tkinter Application")
        # self.geometry("800x600")

        # Create custom style
        self.style = ttk.Style()
        self.style.theme_use("clam") 

        
        self.style.configure("Header.TFrame", background="red")
        self.style.configure("SidePanel.TFrame", background="gray")
        self.style.configure("MainContent.TFrame", background="white")
        self.style.configure("TLabel", foreground="black", background="#E0E0E0",relief="flat",highlightthickness=0)  # Set text color

        self.header_frame = ttk.Frame(self, style="Header.TFrame", height=50)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.search_var = tk.StringVar()
        self.search_bar = ttk.Entry(self.header_frame, textvariable=self.search_var)
        self.search_bar.pack(pady=10, padx=10, side=tk.LEFT)

        self.search_button = ttk.Button(self.header_frame, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10, padx=10,  side=tk.LEFT)

        
        self.side_panel = ttk.Frame(self, style="SidePanel.TFrame", width=200)
        self.side_panel.pack(side=tk.LEFT, fill=tk.Y)
        
        self.side_panel_content = ttk.Label(self.side_panel, text="Side Panel Content",)
        self.side_panel_content.pack(pady=20, padx=10)
        
        self.collapse_button = ttk.Button(self, text="Collapse", command=self.toggle_side_panel)
        self.collapse_button.pack(pady=10, padx=10, side=tk.BOTTOM)

        
        self.main_content = ttk.Frame(self, style="MainContent.TFrame")
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.main_label = ttk.Label(self.main_content, text="Main")
        self.main_label.pack(pady=20, padx=20)

        self.side_panel_visible = True

    def perform_search(self):
        search_term = self.search_var.get()
        print(f"Searching for: {search_term}")

    def toggle_side_panel(self):
        if self.side_panel_visible:
            self.side_panel.pack_forget()
            self.collapse_button.config(text="Expand")
        else:
            self.side_panel.pack(side=tk.LEFT, fill=tk.Y)
            self.collapse_button.config(text="Collapse")
        self.side_panel_visible = not self.side_panel_visible

if __name__ == "__main__":
    app = App()
    app.mainloop()
