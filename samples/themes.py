import tkinter as tk
from tkinter import ttk

root = tk.Tk()
styles = ttk.Style().theme_names()

print("Available themes:")
for theme in styles:
    print(theme)

root.destroy()
