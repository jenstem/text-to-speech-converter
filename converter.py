from gtts import gTTS
import os
from tkinter import *


root = Tk()


canvas = Canvas(root, width=400, height=300)
canvas.pack()


def convert():
    """
    Converts text input from a user interface into speech and plays it back.

    This function retrieves text from an entry widget, converts it to speech using
    the gTTS library, saves the output as an MP3 file, and plays the audio file
    using the system's audio player.
    """
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    os.system("afplay output.mp3")


entry = Entry(root)
canvas.create_window(200, 180, window=entry)
canvas.create_text(200, 140, text='Enter text to convert to speech')


button = Button(text='Start', command=lambda: convert())
canvas.create_window(200, 230, window=button)


root.mainloop()
