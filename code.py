from gtts import gTTS

import os

f = open('textfile.txt')

x = f.read()

lang = 'en'

audio=gTTS(text = x, lang = lang, slow= False)

audio.save("speech.wav")

os.system("speech.wav") 

//creating branch