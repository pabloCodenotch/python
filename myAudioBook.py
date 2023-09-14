# For the GUI
import tkinter as tk
import tkinter.filedialog as fd
# To read the epub
import epub2txt as epub
# To voice the epub
import pyttsx3

root = tk.Tk()
root.title('Narrator')
root.geometry('400x300')

file = []
engine = None

def select_file():
    file.clear()
    file_path = fd.askopenfilename()
    file.append(file_path)
    if file_path == '':
        print ('Error: No file selected')

def convert():
    global engine
    text = epub.epub2txt(file[0])
    engine = pyttsx3.init()
    engine.save_to_file(text,'NewAudioBook.mp3')
    engine.runAndWait()

def read():
    global engine
    text = epub.epub2txt(file[0])
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def stop():
    global engine
    if engine:
        engine.stop()
    
# Buttons
tk.Button(text= ('Open'),
          command= select_file).pack(fill= tk.X)

tk.Button(text= ('Convert'),
          command= convert).pack(fill=tk.X)

tk.Button(text= ('Read'),
          command= read).pack(fill=tk.X)

tk.Button(text= ('Stop'),
          command= stop, fg='red').pack(fill=tk.X)

tk.mainloop()