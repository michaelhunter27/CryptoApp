# Michael Hunter
# CryptoApp
# helpwindow.py

import tkinter as tk
from tkinter import ttk


class HelpWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style(self.root)
        self.configure_root()

        self.enc_header = ttk.Label(self.root)
        self.enc_body = ttk.Label(self.root)
        self.vert_line = ttk.Separator(self.root)
        self.dec_header = ttk.Label(self.root)
        self.dec_body = ttk.Label(self.root)

        self.configure_widgets()
        self.pack_widgets()

        self.root.mainloop()

    def configure_root(self):
        self.root.title("Help")
        self.style.configure("TLabel", font=("Helvetica", 10))

    def configure_geometry(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

    def configure_widgets(self):
        self.enc_header.configure(anchor="w", justify="left", font=("Helvetica", 14),
                                  text="Encryption")
        self.enc_body.configure(anchor="w", justify="left",
                                text="The encryption side of the application allows you to encrypt \n"
                                     "a message so that only people with the secret key can decode it.\n\n\n"
                                     "To encrypt a message:\n"
                                     "1. Type the message into the upper textbox.\n"
                                     "2. Enter a key into the \"key\" entry field.  Remember this key \n"
                                     "because it is required to decrypt the message later.\n"
                                     "3. Click the \"Encrypt\" button.  The encrypted message will appear\n"
                                     "in the gray textbox at the bottom.\n\n"
                                     "Other Features:\n"
                                     "Clicking the \"Clear\" button will clear all text in the upper \n"
                                     "textbox, the key, and the bottom ciphertext box.  This action \n"
                                     "cannon be undone.\n\n"
                                     "Clicking the \"Generate Text\" button will insert a random \n"
                                     "example sentence into the upper text box and a random word into \n"
                                     "the \"key\" entry field.  Click \"Encrypt\" to see the result \n"
                                     "of encrypting the example message.")
        self.vert_line.configure(orient="vertical")
        self.dec_header.configure(anchor="w", justify="left", font=("Helvetica", 14),
                                  text="Decryption")
        self.dec_body.configure(anchor="w", justify="left",
                                text="The decryption side of the application allows you to decrypt \n"
                                     "a previously encrypted message so that you can read it. This side \n"
                                     "of the application functions similarly to the encryption side.\n\n"
                                     "To decrypt a message:\n"
                                     "1. Type the text into the upper textbox.\n"
                                     "2. Enter the key with which the message was originally encrypted \n"
                                     "into the \"key\" entry field.  No other key will work.\n"
                                     "3. Click the \"Encrypt\" button.  The decrypted message will appear\n"
                                     "in the gray textbox at the bottom.\n\n"
                                     "Other Features:\n"
                                     "Clicking the \"Clear\" button will clear all text in the upper \n"
                                     "textbox, the key, and the bottom plaintext box.  This action \n"
                                     "cannon be undone."
                                     "\n\n\n\n\n")
        return

    def pack_widgets(self):
        self.enc_header.grid(row=0, column=0, padx=5, pady=5)
        self.enc_body.grid(row=1, column=0, padx=5, pady=5)
        self.vert_line.grid(row=0, column=1, rowspan=3, sticky="NS")
        self.dec_header.grid(row=0, column=2, padx=5, pady=5)
        self.dec_body.grid(row=1, column=2, padx=5, pady=5)
        return
