import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import Scrollbar
from langchain_ollama import OllamaLLM


engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

model = OllamaLLM(model="llama3")

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak_text("I am listening , Sir")
        print("J.A.R.V.I.S : Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        print("Voice not recognized")
        return None
    except sr.RequestError:
        print("Google Speech recognition service is down")
        return None

# GUI için Tkinter penceresi oluşturuluyor
root = tk.Tk()
root.title("J.A.R.V.I.S - Voice Assistant")
root.geometry("600x400")  # Pencereyi biraz büyütüyoruz

# Konuşmaların görüneceği metin kutusu
conversation_box = tk.Text(root, wrap=tk.WORD, width=70, height=15, font=("Helvetica", 12), state=tk.NORMAL)
conversation_box.pack(pady=20)

# Kaydırma çubuğu ekliyoruz
scrollbar = Scrollbar(root, command=conversation_box.yview)
conversation_box.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


def update_conversation_box(text):
    conversation_box.insert(tk.END, text + '\n')
    conversation_box.yview(tk.END)
    conversation_box.update_idletasks()

def on_start_button_click():
    _input = recognize_speech()
    if _input:
        update_conversation_box(f"You: {_input}")
        result = model.invoke(input=_input)
        update_conversation_box(f"J.A.R.V.I.S: {result}")
        speak_text(result)
    else:
        update_conversation_box("J.A.R.V.I.S: Sorry, I didn't understand.")
        speak_text("Sorry, I didn't understand.")

def on_exit_button_click():
    speak_text("Goodbye, Sir")
    root.quit()


start_button = tk.Button(root, text="Start Listening", command=on_start_button_click, font=("Helvetica", 14), width=20, height=2)
start_button.pack(pady=10)


exit_button = tk.Button(root, text="Exit", command=on_exit_button_click, font=("Helvetica", 14), width=20, height=2)
exit_button.pack(pady=10)


root.mainloop()
