import tkinter as tk
from tkinter import ttk
import helpwindow


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.configure_root()

        # declare widgets
        self.container = tk.Frame(self.root)

        self.help_button = ttk.Button(self.container)

        self.configure_widgets()
        self.configure_frame()
        self.pack_widgets()

        self.root.mainloop()
        return

    def configure_root(self):
        self.root.title("CryptoApp")
        self.root.geometry("1000x600")
        return

    def configure_widgets(self):
        self.help_button.configure(text="Help", command=self.open_help_window)
        return

    def configure_frame(self):
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        return

    def pack_widgets(self):
        self.help_button.grid(row=0, column=0)

        self.container.pack()
        return

    # callback functions
    def open_help_window(self):
        helpwindow.HelpWindow()
        return
