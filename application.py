# Michael Hunter
# CryptoApp
# application.py

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel
import helpwindow
import crypto
import zmq


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.configure_root()

        self.configure_socket()

        # declare variables
        self.enc_key = tk.StringVar()
        self.dec_key = tk.StringVar()
        self.dont_show_again = False

        # frame to hold all other widgets
        self.container = tk.Frame(self.root)

        # declare widgets
        self.help_button = ttk.Button(self.container)
        self.scheme_label = ttk.Label(self.container)
        self.cipher_label1 = ttk.Label(self.container)

        self.generate_text_button = ttk.Button(self.container)

        self.enc_input_label = ttk.Label(self.container)
        self.enc_input = tk.Text(self.container)
        self.enc_key_label = ttk.Label(self.container)
        self.enc_key_entry = ttk.Entry(self.container)
        self.enc_clear_button = ttk.Button(self.container)
        self.encrypt_button = ttk.Button(self.container)
        self.enc_result_label = ttk.Label(self.container)
        self.enc_result = tk.Text(self.container)

        self.dec_input_label = ttk.Label(self.container)
        self.dec_input = tk.Text(self.container)
        self.dec_key_label = ttk.Label(self.container)
        self.dec_key_entry = ttk.Entry(self.container)
        self.dec_clear_button = ttk.Button(self.container)
        self.decrypt_button = ttk.Button(self.container)
        self.dec_result_label = ttk.Label(self.container)
        self.dec_result = tk.Text(self.container)

        self.configure_widgets()
        self.configure_frame()
        self.pack_widgets()

        self.root.mainloop()
        return

    def configure_root(self):
        """
        Configures top level window
        """
        self.root.title("CryptoApp")
        self.style.configure("TLabel", font=("Helvetica", 10))
        self.root.protocol("WM_DELETE_WINDOW", func=self.stop_microservice)
        return

    def configure_socket(self):
        """
        Sets up socket for communication with microservice
        """
        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:4000")
        return

    def configure_widgets(self):
        self.configure_top_widgets()
        self.configure_enc_widgets()
        self.configure_dec_widgets()
        return

    def configure_top_widgets(self):
        self.help_button.configure(text="Help", command=self.open_help_window)
        self.scheme_label.configure(text="Encryption Scheme:")
        self.cipher_label1.configure(text="Vigen\xe8re Cipher")
        return

    def configure_enc_widgets(self):
        self.generate_text_button.configure(text="Autofill", command=self.generate_text)

        self.enc_input_label.configure(text="Enter text for encryption below:")
        self.enc_input.configure(height=5, width=50, wrap="word")
        self.enc_key_label.configure(text="Key:")
        self.enc_key_entry.configure(textvariable=self.enc_key)
        self.enc_clear_button.configure(text="Clear", command=self.enc_clear)
        self.encrypt_button.configure(text="Encrypt", command=self.encrypt)
        self.enc_result_label.configure(text="Ciphertext:")
        self.enc_result.configure(height=5, width=50, wrap="word", state="disabled", bg="#f2f2f2")
        return

    def configure_dec_widgets(self):
        self.dec_input_label.configure(text="Enter text for decryption below:")
        self.dec_input.configure(height=5, width=50, wrap="word")
        self.dec_key_label.configure(text="Key:")
        self.dec_key_entry.configure(textvariable=self.dec_key)
        self.dec_clear_button.configure(text="Clear", command=self.dec_clear)
        self.decrypt_button.configure(text="Decrypt", command=self.decrypt)
        self.dec_result_label.configure(text="Decrypted message:")
        self.dec_result.configure(height=5, width=50, wrap="word", state="disabled", bg="#f2f2f2")
        return

    def configure_frame(self):
        for i in range(9):
            self.container.columnconfigure(i, weight=1)
        for i in range(6):
            self.container.rowconfigure(i, weight=1)
        return

    def pack_widgets(self):
        """
        packs widgets into the container frame using the grid() method
        """
        self.pack_top_widgets()
        ttk.Separator(self.container, orient="horizontal").grid(row=1, columnspan=9,
                                                                sticky="EW", pady=(10, 0))
        self.pack_enc_widgets()
        ttk.Separator(self.container, orient="vertical").grid(row=2, column=4, rowspan=5,
                                                              sticky="NS", padx=10)
        self.pack_dec_widgets()
        self.container.pack()
        return

    def pack_top_widgets(self):
        self.help_button.grid(row=0, column=0, padx=10, pady=10)
        self.scheme_label.grid(row=0, column=2, padx=10, pady=10)
        self.cipher_label1.grid(row=0, column=3, padx=10, pady=10)
        return

    def pack_enc_widgets(self):
        self.generate_text_button.grid(row=2, column=3, padx=10, pady=10)

        self.enc_input_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="W")
        self.enc_input.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        self.enc_key_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.enc_key_entry.grid(row=4, column=0, padx=10, pady=10, sticky="E")
        self.enc_clear_button.grid(row=4, column=2, padx=10, pady=10)
        self.encrypt_button.grid(row=4, column=3, padx=10, pady=10)
        self.enc_result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="W")
        self.enc_result.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
        return

    def pack_dec_widgets(self):
        self.dec_input_label.grid(row=2, column=5, columnspan=2, padx=10, pady=10, sticky="W")
        self.dec_input.grid(row=3, column=5, columnspan=4, padx=10, pady=10)
        self.dec_key_label.grid(row=4, column=5, padx=10, pady=10, sticky="W")
        self.dec_key_entry.grid(row=4, column=5, padx=10, pady=10, sticky="E")
        self.dec_clear_button.grid(row=4, column=7, padx=10, pady=10)
        self.decrypt_button.grid(row=4, column=8, padx=10, pady=10)
        self.dec_result_label.grid(row=5, column=5, columnspan=2, padx=10, pady=10, sticky="W")
        self.dec_result.grid(row=6, column=5, columnspan=4, padx=30, pady=10)
        return

    # callback functions
    def open_help_window(self):
        """
        Opens an informational help window
        """
        helpwindow.HelpWindow()
        return

    def generate_text(self):
        """
        Gets a random sentence and random word from a text generating microservice.
        Replaces enc_input text with the sentence and enc_key with the word.
        If microservice isn't running, inserts default text.
        """
        message = ("It is a period of civil war. Rebel spaceships, striking from a hidden base, "
                   "have won their first victory against the evil Galactic Empire.")
        key = "skywalker"

        try:
            self.socket.send_string("sentence")
            event = self.socket.poll(100)
            if event > 0:
                message_bytes = self.socket.recv()
                message = message_bytes.decode()[17:]
                self.socket.send_string("word")
                key_bytes = self.socket.recv()
                key = key_bytes.decode()[13:]
        except zmq.ZMQError:
            message = ("It is a period of civil war. Rebel spaceships, striking from a hidden base, "
                       "have won their first victory against the evil Galactic Empire.")
            key = "skywalker"

        self.enc_input.delete("1.0", "end")
        self.enc_input.insert("1.0", message)

        self.enc_key.set(key)
        return

    def enc_clear(self):
        """
        Sets the values of enc_input text and enc_key to empty strings.
        The first time enc_clear() or dec_clear() is called, a popup window asks for
        confirmation before the text is cleared.
        """

        answer = askokcancel(title="Clear confirmation",
                             message="Clicking continue will clear all entered text, \n"
                                     "including the key and the resulting ciphertext. \n "
                                     "Are you sure you wish to proceed?")

        if answer:
            self.enc_input.delete("1.0", "end")
            self.enc_key.set("")
            self.enc_result.configure(state="normal")
            self.enc_result.delete("1.0", "end")
            self.enc_result.configure(state="disabled")
        return

    def dec_clear(self):
        """
        Sets the values of dec_input text and dec_key to empty strings.
        The first time enc_clear() or dec_clear() is called, a popup window asks for
        confirmation before the text is cleared.
        """

        answer = askokcancel(title="Clear confirmation",
                             message="Clicking continue will clear all entered text, \n"
                                     "including the key and the resulting ciphertext. \n "
                                     "Are you sure you wish to proceed?")

        if answer:
            self.dec_input.delete("1.0", "end")
            self.dec_key.set("")
            self.dec_result.configure(state="normal")
            self.dec_result.delete("1.0", "end")
            self.dec_result.configure(state="disabled")
        return

    def encrypt(self):
        """
        Encrypts enc_input text and puts the result in enc_result
        """
        plaintext = self.enc_input.get("1.0", "end")
        key = self.enc_key.get()
        ciphertext = crypto.enc_vigenere(plaintext, key)
        self.enc_result.configure(state="normal")
        self.enc_result.delete("1.0", "end")
        self.enc_result.insert("1.0", ciphertext)
        self.enc_result.configure(state="disabled")
        return

    def decrypt(self):
        """
        Decrypts dec_input text and puts the result in dec_result
        """
        ciphertext = self.dec_input.get("1.0", "end")
        key = self.dec_key.get()
        plaintext = crypto.dec_vigenere(ciphertext, key)
        self.dec_result.configure(state="normal")
        self.dec_result.delete("1.0", "end")
        self.dec_result.insert("1.0", plaintext)
        self.dec_result.configure(state="disabled")
        return

    def stop_microservice(self):
        """
        Sends a message to the microservice to stop and then destroys the application.
        """
        try:
            self.socket.send_string("stop")
        except zmq.ZMQError:
            pass
        finally:
            self.root.destroy()
        return


if __name__ == '__main__':
    app = Application()
