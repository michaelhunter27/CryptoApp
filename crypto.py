

def shift_forward(char, k, mode="DEFAULT"):
    if mode == "DEFAULT":
        if not str.isalpha(char):
            return char
        n = (((ord(str.upper(char)) - 65) + (ord(str.upper(k)) - 65)) % 26) + 65
        if str.isupper(char):
            return chr(n)
        else:
            return str.lower(chr(n))

    if mode == "UPPER_ALPHA_ONLY":
        if 65 <= ord(char) <= 90:
            n = (((ord(char) - 65) + (ord(k) - 65)) % 26) + 65
            return chr(n)
        else:
            return char


def shift_backward(char, k, mode="DEFAULT"):
    if mode == "DEFAULT":
        if not str.isalpha(char):
            return char
        n = (((ord(str.upper(char)) - 65) - (ord(str.upper(k)) - 65)) % 26) + 65
        if str.isupper(char):
            return chr(n)
        else:
            return str.lower(chr(n))

    if mode == "UPPER_ALPHA_ONLY":
        if 65 <= ord(char) <= 90:
            n = (((ord(char) - 65) - (ord(k) - 65)) % 26) + 65
            return chr(n)
        else:
            return char


def enc_vigenere(plain_text, key, mode="DEFAULT"):
    if len(key) < 1:
        return plain_text

    cipher_text = ""
    j = 0
    for i in range(len(plain_text)):
        cipher_text += shift_forward(plain_text[i], key[j % len(key)], mode)
        if str.isalpha(cipher_text[i]):
            j += 1

    return cipher_text


def dec_vigenere(cipher_text, key, mode="DEFAULT"):
    if len(key) < 1:
        return cipher_text

    plain_text = ""
    j = 0
    for i in range(len(cipher_text)):
        plain_text += shift_backward(cipher_text[i], key[j % len(key)], mode)
        if str.isalpha(plain_text[i]):
            j += 1

    return plain_text
