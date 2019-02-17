#!/usr/bin/env python
"""VERSION 2.0"""

try:
    from Tkinter import *
except ModuleNotFoundError:
    from tkinter import *
root = Tk()
root.geometry('240x240+100+100')
root.title("Cypher")
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)
root.update()


# flip encode and decode
# encode
def flip(encode):
    """
    flips the alphabet backwards
    a=z, b=y, c=x etc.
    does not require separate encode and decode
    because it is the same forwards and backwards
    x=c, y=b, z=a
    """

    def translate(word):
        """checks to see if chr number is in legend and returns its key
        if it isn't, it returns the original number (punctuation
        or a space)"""
        for x in word:
            try:
                new_word.append(chr(legend[x]))
            except KeyError:
                new_word.append(chr(x))

    legend = dict(zip(range(97, 123), range(122, 96, -1)))
    # creates a dictionary of chr values that flips the alphabet
    encode = encode.lower()
    new_word = []
    word_number = [ord(x) for x in list(encode)]
    translate(word_number)
    return "".join(new_word)


"""Basic Shift cyphers. Shift a given plaintext a given distance down the alphabet"""


# encode
def e_shift(word, shift):
    word = word.lower()
    # dealing with shift
    try:
        shift = int(shift)
    except ValueError:
        return 'Invalid Shift Input'
    if shift > 26:
        shift = shift % 26
    # new word list
    new_word = [ord(x) for x in list(word)]
    # shifting each ord number
    for n in range(0, len(new_word)):
        if new_word[n] in range(ord("a"), ord("z") + 1):
            if new_word[n] + shift > ord('z'):
                new_word[n] += shift - 26
            elif new_word[n] + shift < ord('a'):
                new_word[n] += shift + 26
            else:
                new_word[n] += shift
    # creating final word
    new_word = [chr(x) for x in new_word]
    return "".join(new_word)


# decode
def d_shift(word, shift):
    word = word.lower()
    # dealing with shift
    try:
        shift = int(shift)
    except ValueError:
        return 'Invalid Shift Response'
    shift = 0 - shift
    if shift > 26:
        shift = shift % 26
    # new word list
    new_word = [ord(x) for x in list(word)]
    for n in range(0, len(new_word)):
        if new_word[n] in range(ord("a"), ord("z") + 1):
            if new_word[n] + shift > ord('z'):
                new_word[n] += shift - 26
            elif new_word[n] + shift < ord('a'):
                new_word[n] += shift + 26
            else:
                new_word[n] += shift
    new_word = [chr(x) for x in new_word]
    return "".join(new_word)


"""A Keyword Cypher, also called a Vigenere cipher
It is a version of the above shift cipher but shifts
each letter in the plaintext a different distance based
on a keyword provided by the user"""


# encode
def e_keyword(word, keyword):
    legend = []
    new_word = []
    word = word.lower()
    keyword = keyword.lower()
    n = 0  # nth of keyword
    p = 0  # pth of word
    r = 0  # rth of legend
    while len(legend) < len(word):
        """Iterates letters of the keyword converted into numbers
        until the legend equals the length of the phrase to encode"""
        legend_letter = keyword[n]
        legend.append(ord(legend_letter))
        if n < (len(keyword) - 1):
            n = n + 1
        else:
            n = 0
    legend = [x - 97 for x in legend]  # converts each letter to shift distance
    while p < len(word):
        number = ord(word[p])
        if ord(word[p]) not in range(ord('a'), ord('z') + 1):
            number = ord(word[p])
            r -= 1  # this keeps punctuation from using a piece of the legend
        else:
            number = number + legend[r]
            if number > ord('z'):
                number = number - 26
            elif number < ord('a'):
                number = number + 26
        word_letter = chr(number)
        new_word.append(word_letter)
        p += 1
        r += 1
    return "".join(new_word)


# decode
def d_keyword(word, keyword):
    legend = []
    new_word = []
    word = word.lower()
    keyword = keyword.lower()
    n = 0  # nth of keyword
    p = 0  # pth of word
    r = 0  # rth of legend
    while len(legend) < len(word):
        legend_letter = keyword[n]
        legend.append(ord(legend_letter))
        if n < (len(keyword) - 1):
            n += 1
        else:
            n = 0
    legend = [x - 97 for x in legend]
    while p < len(word):
        number = ord(word[p])
        if ord(word[p]) not in range(ord('a'), ord('z') + 1):
            number = ord(word[p])
            r = r - 1  # this keeps punctuation from using a piece of the legend
        else:
            number -= legend[r]
            if number > ord('z'):
                number = number - 26
            elif number < ord('a'):
                number = number + 26
        word_letter = chr(number)
        new_word.append(word_letter)
        p += 1
        r += 1
    return "".join(new_word)


"""A type of cipher that arranges the plaintext in a square by rows and then returns that square via columns
all punction is filtered out upon encript. '.' are used in encription as placeholders to make an even square
these '.'s are filtered out in decription. spaces remain."""


# encode
def e_transposition(plaintext):
    plaintext = plaintext.lower()
    # removes punc. from plaintext

    word_list = [x for x in plaintext if ord(x) in range(ord('a'), ord('z') + 1) or x == ' ']

    # determines size of square
    n = 1
    while len(word_list) > n ** 2:
        n += 1

    # makes wordList length to even square
    while len(word_list) < n ** 2:
        word_list.append('.')

    word_key = []
    x = 0
    while len(word_key) < len(word_list):
        if x < len(word_list):
            word_key.append(x)
            x += n
        else:
            x -= n ** 2 - 1
    new_word = []
    for x in word_key:
        new_word.append(word_list[x])
    return "".join(new_word)


# decode
def d_transposition(cipher_text):
    cipher_text = cipher_text.lower()
    word_list = list(cipher_text)

    # determines size of square
    n = 1
    while len(word_list) > n ** 2:
        n += 1

    word_key = []
    x = 0
    while len(word_key) < len(word_list):
        if x < len(word_list):
            word_key.append(x)
            x += n
        else:
            x -= n ** 2 - 1
    new_word = []
    for x in word_key:
        new_word.append(word_list[x])
    new_word = [x for x in new_word if ord(x) in range(ord('a'), ord('z') + 1) or x == " "]
    return "".join(new_word)


"""A variant of a shift cipher that places a key word at the beginning of the key
and then writes the alphabet out after it, without duplicating letters"""


# encode
def e_substitution(plaintext, keyword):
    key_list = []
    keyword = keyword.lower()
    plaintext = plaintext.lower()
    for x in range(0, len(keyword)):
        if keyword[x] not in key_list:
            key_list.append(ord(keyword[x]))
    for x in range(ord('a'), ord('z') + 1):
        if x not in key_list:
            key_list.append(x)
    legend = dict(zip(range(ord('a'), ord('z') + 1), key_list))
    plaintext_list = [ord(x) for x in list(plaintext)]
    new_word = []
    for x in plaintext_list:
        try:
            new_word.append(chr(legend[x]))
        except KeyError:
            new_word.append(chr(x))
    return "".join(new_word)


# decode
def d_substitution(plaintext, keyword):
    key_list = []
    keyword = keyword.lower()
    plaintext = plaintext.lower()
    for x in range(0, len(keyword)):
        if keyword[x] not in key_list:
            key_list.append(ord(keyword[x]))
    for x in range(ord('a'), ord('z') + 1):
        if x not in key_list:
            key_list.append(x)
    legend = dict(zip(key_list, range(ord('a'), ord('z') + 1)))
    plaintext_list = [ord(x) for x in list(plaintext)]
    new_word = []
    for x in plaintext_list:
        try:
            new_word.append(chr(legend[x]))
        except KeyError:
            new_word.append(chr(x))
    return "".join(new_word)


# TK Interface Code
# Commands
def ebutton():
    decision = choice.get()
    if decision == 1:
        outputEntry_text.set(e_transposition(inputEntry_text.get()))
    elif decision == 2:
        outputEntry_text.set(flip(inputEntry_text.get()))
    elif decision == 3:
        outputEntry_text.set(e_keyword(inputEntry_text.get(), optionEntry_text.get()))
    elif decision == 4:
        outputEntry_text.set(e_shift(inputEntry_text.get(), optionEntry_text.get()))
    elif decision == 5:
        outputEntry_text.set(e_substitution(inputEntry_text.get(), optionEntry_text.get()))
    else:
        outputEntry_text.set("Choose an option")


def dbutton():
    decision = choice.get()
    if decision == 1:
        outputEntry_text.set(d_transposition(inputEntry_text.get()))
    elif decision == 2:
        outputEntry_text.set(flip(inputEntry_text.get()))
    elif decision == 3:
        outputEntry_text.set(d_keyword(inputEntry_text.get(), optionEntry_text.get()))
    elif decision == 4:
        outputEntry_text.set(d_shift(inputEntry_text.get(), optionEntry_text.get()))
    elif decision == 5:
        outputEntry_text.set(d_substitution(inputEntry_text.get(), optionEntry_text.get()))
    else:
        outputEntry_text.set("Choose an option")


def radio_update():
    optionEntry_text.set("")
    optionLabel_text.set(radioButtonDict[choice.get()])
    outputEntry_text.set("")


# Row one
frm = Frame(root)
frm.grid(row=0, column=0, columnspan=3, pady=10)
frm2 = Frame(root)
frm2.grid(row=1, column=0, columnspan=3)
choice = IntVar()
choice.set(None)
radioButtonDict = {5: "Key:", 4: "Shift:", 3: "Key:", 2: "N/A:", 1: "N/A:"}  # readouts for optionLabel_text
radioSub = Radiobutton(frm2, text="Substitution", value=5, variable=choice, command=radio_update)
radioShift = Radiobutton(frm, text="Shift", value=4, variable=choice, command=radio_update)
radioKey = Radiobutton(frm, text="Keyword", value=3, variable=choice, command=radio_update)
radioFlip = Radiobutton(frm, text="Flip", value=2, variable=choice, command=radio_update)
radioTransposition = Radiobutton(frm2, text="Square", value=1, variable=choice, command=radio_update)
radioShift.grid(row=0, column=0, sticky=W)
radioKey.grid(row=0, column=1, sticky=W)
radioFlip.grid(row=0, column=2, sticky=W)
radioTransposition.grid(row=0, column=0, sticky=W)
radioSub.grid(row=0, column=1, sticky=W)

# Row two
inputLabel_text = StringVar()
inputLabel_text.set("Input:")
inputLabel = Label(root, textvariable=inputLabel_text)
inputLabel.grid(row=2, column=0, sticky=E, pady=5)

inputEntry_text = StringVar()
inputEntry = Entry(root, textvariable=inputEntry_text)
inputEntry.grid(row=2, column=1, columnspan=2, padx=3, pady=5)

# Row three
optionLabel_text = StringVar()
optionLabel = Label(root, textvariable=optionLabel_text)
optionLabel.grid(row=3, column=0, sticky=E, pady=5)

optionEntry_text = StringVar()
optionEntry = Entry(root, textvariable=optionEntry_text)
optionEntry.grid(row=3, column=1, columnspan=2, padx=3, pady=5)

# Row four
frm3 = Frame(root)
frm3.grid(row=4, columnspan=3)

enButton = Button(frm3, text="Encode", command=ebutton)
enButton.grid(row=0, column=0, padx=5, pady=5)

deButton = Button(frm3, text="Decode", command=dbutton)
deButton.grid(row=0, column=2, padx=5, pady=5)

# Row five
outputLabel = Label(root, text="Output")
outputLabel.grid(row=5, column=1)

# Row six
outputEntry_text = StringVar()
outputEntry = Entry(root, textvariable=outputEntry_text)
outputEntry.grid(row=6, column=0, columnspan=3)
outputEntry.configure(relief=FLAT, state="readonly")

root.mainloop()
