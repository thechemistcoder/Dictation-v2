import pyautogui
import speech_recognition as sr
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say Something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognizer could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google")

def type(text):
    pyautogui.write(text)

def change_status():
    b1.configure(text="Listening",bootstyle=WARNING)
    root.after(100, listen_and_type)
    current_state = b1.cget("text")

    if current_state == "Listen":
        b1.configure(text="Listening")
        root.after(100, listen_and_type)
    elif current_state == "Listening":
        b1.configure(text="Listen")
def listen_and_type():
    text = speech_to_text()
    if text:
        type(text)
    root.after(100, listen_and_type)

root = tk.Tk()
root.title('Dictation Application')
root.geometry("400x100")
style = ttk.Style("darkly")
b1 = ttk.Button(root, text="Listen", bootstyle=SUCCESS, command=change_status)
b1.pack(side=TOP, padx=5, pady=10)
b2 = ttk.Button(root, text="Quit", style=DANGER, command=root.destroy)
b2.pack(side=BOTTOM, padx=6, pady=10)
root.mainloop()




