import pyautogui
import speech_recognition as sr
import time
recognizer = sr.Recognizer()
input_lang = "en-IN"
with sr.Microphone() as source:
      print('Speak Now')
      voice = recognizer.record(source, duration=5)
      text = recognizer.recognize_google(voice, language=input_lang)
      print(text)
#time.sleep(2)
#pyautogui.typewrite("hello my name is shlok how are you all its christmas day !!!!!!!!!!!!!!!!!!!!!!!")
