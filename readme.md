# CryptoApp

This is a desktop application for encrypting and 
decrypting text.  I made this project for a software 
engineering class.  It is written in Python.  The GUI
uses the python package tkinter which is included in most
installations of Python.

If you want to try it out, get the source code by either
cloning the repository or downloading the latest release, then
start CryptoApp with the command `python main.py`.

## Ciphers

CryptoApp supports encryption and decryption with three different ciphers.

### Vigenère
The Vigenère cipher is a classic cipher, dating back to at least the 
16th century. It is similar to the Caesar Cipher in that each letter of
the plaintext is shifted by a certain amount. The size of that shift
cycles through values based on the letters in the key. Check out the
[Wikipedia article](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
for more information.

### Substitution
A substitution cipher is a general term for ciphers that obscure a message
by substituting each letter of the plaintext for another. Thus, the 
vigenère cipher is actually an example of a substitution cipher.

The substitution cipher implemented in CryptoApp is described 
[here](https://en.wikipedia.org/wiki/Substitution_cipher#Simple). A
ciphertext alphabet is constructed by first listing the letters of
the key without repeats and then listing the remaining letters 
of the alphabet in order. To form the ciphertext, each letter of the 
plaintext is substituted with the corresponding letter of the ciphertext
alphabet. For example, the key "galaxy" would result in the following 
ciphertext alphabet:

Ciphertext Alphabet: GALXYBCDEFHIJKMNOPQRSTUVWZ

Every 'A' in the plaintext would be substituted with 'G', every 'B' would 
be substituted with 'A', and so on.

### Transposition

Again, transposition cipher is a general term for ciphers that obscure
the plaintext by mixing up (or *transposing*) the order of the letters
in the plaintext.

The transposition cipher that is implemented in CryptoApp is columnar
transposition.  In to encrypt a message with this cipher, the letters 
of the plaintext are written into a grid by *row*. Then the columns of 
the grid are rearranged according to the alphabetical order of the letters 
in the key. Lastly, the ciphertext is formed by reading each *column* 
of the grid. You can find a more detailed explanation 
[here](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition).

## Autofill Feature
New in version 1.1 is an autofill feature which provides 
an example plaintext and encryption key.  It is designed 
to be used with a random text generator microservice created by my 
classmate [@shindelr](https://github.com/shindelr) and can be found in 
[this repository](https://github.com/shindelr/Random-Text-Generator).
CryptoApp will still work without the microservice running, but
the autofill text will not be randomly generated.

## Screenshots

![screenshot-vigenere](https://github.com/user-attachments/assets/6059d46c-07b6-49f3-83db-f31d4d377e66)

---

![screenshot-substitution](https://github.com/user-attachments/assets/ee88259c-6097-4eff-9dbb-fcf4a4095de6)

---

![screenshot-transposition](https://github.com/user-attachments/assets/47927475-cdcc-4e5d-bd20-432d8e9dc1d5)






