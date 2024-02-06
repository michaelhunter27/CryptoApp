import tkinter as tk
from tkinter import ttk
import helpwindow
import crypto


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.configure_root()

        # declare variables
        self.enc_key = tk.StringVar()
        self.dec_key = tk.StringVar()

        # declare widgets
        self.container = tk.Frame(self.root)

        self.help_button = ttk.Button(self.container)
        self.scheme_label = ttk.Label(self.container)
        self.cipher_label1 = ttk.Label(self.container)

        self.enc_instructions = ttk.Label(self.container)
        self.enc_input = tk.Text(self.container)
        self.enc_key_label = ttk.Label(self.container)
        self.enc_key_entry = ttk.Entry(self.container)
        self.enc_clear_button = ttk.Button(self.container)
        self.encrypt_button = ttk.Button(self.container)
        self.enc_result = tk.Text(self.container)

        self.dec_instructions = ttk.Label(self.container)
        self.dec_input = tk.Text(self.container)
        self.dec_key_label = ttk.Label(self.container)
        self.dec_key_entry = ttk.Entry(self.container)
        self.dec_clear_button = ttk.Button(self.container, command=self.dec_clear)
        self.decrypt_button = ttk.Button(self.container)
        self.dec_result = tk.Text(self.container)

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
        self.scheme_label.configure(text="Encryption Scheme:")
        self.cipher_label1.configure(text="Vigenere Cipher")

        self.enc_instructions.configure(text="Enter text for encryption below:")
        self.enc_input.configure(height=5)
        self.enc_key_label.configure(text="Key:")
        self.enc_key_entry.configure(textvariable=self.enc_key)
        self.enc_clear_button.configure(text="Clear", command=self.enc_clear)
        self.encrypt_button.configure(text="Encrypt", command=self.encrypt)
        self.enc_result.configure(height=5, state="disabled")

        self.dec_instructions.configure(text="Enter text for decryption below:")
        self.dec_input.configure(height=5)
        self.dec_key_label.configure(text="Key:")
        self.dec_key_entry.configure(textvariable=self.dec_key)
        self.dec_clear_button.configure(text="Clear")
        self.decrypt_button.configure(text="Decrypt", command=self.decrypt)
        self.dec_result.configure(height=5, state="disabled")
        return

    def configure_frame(self):
        for i in range(8):
            self.container.columnconfigure(i, weight=1)
        for i in range(5):
            self.container.rowconfigure(i, weight=1)
        return

    def pack_widgets(self):
        self.help_button.grid(row=0, column=0, padx=5, pady=5)
        self.scheme_label.grid(row=0, column=2, padx=5, pady=5)
        self.cipher_label1.grid(row=0, column=3, padx=5, pady=5)

        self.enc_instructions.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.enc_input.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
        self.enc_key_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        self.enc_key_entry.grid(row=3, column=0, padx=5, pady=5, sticky="E")
        self.enc_clear_button.grid(row=3, column=2, padx=5, pady=5)
        self.encrypt_button.grid(row=3, column=3, padx=5, pady=5)
        self.enc_result.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

        self.dec_instructions.grid(row=1, column=4, columnspan=2, padx=5, pady=5)
        self.dec_input.grid(row=2, column=4, columnspan=4, padx=5, pady=5)
        self.dec_key_label.grid(row=3, column=4, padx=5, pady=5, sticky="W")
        self.dec_key_entry.grid(row=3, column=4, padx=5, pady=5, sticky="E")
        self.dec_clear_button.grid(row=3, column=6, padx=5, pady=5)
        self.decrypt_button.grid(row=3, column=7, padx=5, pady=5)
        self.dec_result.grid(row=4, column=4, columnspan=4, padx=5, pady=5)

        self.container.pack()
        return

    # callback functions
    def open_help_window(self):
        helpwindow.HelpWindow()
        return

    def enc_clear(self):
        self.enc_input.delete("1.0", "end")
        self.enc_key.set("")
        self.enc_result.configure(state="normal")
        self.enc_result.delete("1.0", "end")
        self.enc_result.configure(state="disabled")
        return

    def dec_clear(self):
        self.dec_input.delete("1.0", "end")
        self.dec_key.set("")
        self.dec_result.configure(state="normal")
        self.dec_result.delete("1.0", "end")
        self.dec_result.configure(state="disabled")
        return

    def encrypt(self):
        plaintext = self.enc_input.get("1.0", "end")
        key = self.enc_key.get()
        ciphertext = crypto.enc_vigenere(plaintext, key)
        self.enc_result.configure(state="normal")
        self.enc_result.delete("1.0", "end")
        self.enc_result.insert("1.0", ciphertext)
        self.enc_result.configure(state="disabled")
        return

    def decrypt(self):
        ciphertext = self.dec_input.get("1.0", "end")
        key = self.dec_key.get()
        plaintext = crypto.dec_vigenere(ciphertext, key)
        self.dec_result.configure(state="normal")
        self.dec_result.delete("1.0", "end")
        self.dec_result.insert("1.0", plaintext)
        self.dec_result.configure(state="disabled")
        return
