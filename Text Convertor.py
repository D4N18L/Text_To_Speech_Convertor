#import gtts module 
#An interface to Google Translate's Text-to-Speech API.
from gtts import gTTS

#import os module to help me access features in the operating system
import os

#import the tkinter module 
from tkinter import *

root = Tk()

#Set title of Tkinter window
root.title("Text To Audio Convertor")
canvas = Canvas(root ,width= 400 , height= 400)

canvas.pack()

def text_to_audio():
    
    #Get Text from Entry 
    text = entry.get()
    #Set Lanaguage
    lang = 'en'
    #Initialise the text , type of language and speed of the audio
    text_to_audio = gTTS(text=text , lang= lang , slow=False)
    
    #save as an mp3 
    text_to_audio.save("text_to_audio.mp3")
    
    #play song using os features
    os.system("start text_to_audio.mp3")
    
    
entry = Entry(root)
canvas.create_text(200,90,text= "Text To Speech Convertor", fill="black",font=('Helvetica 15 bold'))
canvas.create_window(200,180,window=entry)

#buttons calls the text to audio function
button = Button(text='Play',command=text_to_audio)

canvas.create_window(200,230, window=button)

root.mainloop()

