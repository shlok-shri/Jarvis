import datetime
import os
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
from datetime import date
from easygui import passwordbox
import pyautogui
import googletrans
import gtts
import playsound


said = pyttsx3.init()
listener = sr.Recognizer()


def talk(text):
    said.say(text)
    said.runAndWait()


def verify_user():
    user_dict = {"Sohm": ["sohms@pappu.py", "6s+@sohm"], "Shlok": ["shlokshri@pappu.py", "creator@pappu"], "Shrikant": ["patanahi@pappu.py", "kuchnahi"], "Sonali": ["aai@pappu.py", "pappu@aai"], "Shobha and Shridhar": ["maidada@pappu.py", "movieserial"]}
    ask = input("Do you remember your password ? (y/n) : ")
    if ask == "y":
        name = input("Please enter your name : ")
        login_id = input("Enter your login-id : ")
        pass_word = passwordbox("Enter your password : ")
        ask2 = input("Do you want to see your password ? (y/n) : ")
        if ask2 == 'y':
            print(pass_word)
        else:
            pass
        if user_dict[name] == [login_id, pass_word]:
            print("Access Granted")

            def wishMe():
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    talk("Good Morning ")

                elif hour >= 12 and hour < 17:
                    talk("Good Afternoon ")

                else:
                    talk("Good Evening!")

                talk(" sir, please tell me how may i help you ")


            def new_year():
                today1 = date.today()
                d11 = today1.strftime("%d/%m/%Y")
                if d11 == "01/01/2021":
                    talk("also, Happy new year sir")
                    print("Happy new year sir")


            def wish_birthday():
                today2 = date.today()
                d2 = today2.strftime("%d/%m/%y")
                if d2 == "22/07/2021":
                    talk("Happy Birthday Sir !!!!!!")
                    print("Happy Birthday Sir !!!!!!")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "01/02/21":
                    talk("Happy Birthday i ")
                    print("Happy Birthday Aai !!!")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "05/11/2021":
                    talk("happy birthday soham")
                    print("Happy Birthday Sohm !!!!!!!!")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "07/09/2021":
                    talk("happy birthday papa")
                    print("Happy Birthday Papa")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "21/03/2021":
                    talk("happy birthday maaai")
                    print("Happy Birthday Mai")
                    pywhatkit.playonyt("Baar Baar din ye aaye")


            def take_command():
                recognizer = sr.Recognizer()
                translator = googletrans.Translator()
                input_lang = 'hi-IN'
                output_lang = 'en'
                try:
                    with sr.Microphone() as source:
                        print('Speak Now')
                        voice = recognizer.record(source, duration=5)
                        text = recognizer.recognize_google(voice, language=input_lang)
                        print(text)
                        translated = translator.translate(text, dest=output_lang)
                except:
                    pass
                    return command


            def run_pappu():
                command = take_command()
                if 'play' in command:
                    song = command.replace('play', ' ')
                    talk('Playing' + song)
                    pywhatkit.playonyt(song)
                elif "play  cant dance saala " in command:
                    talk("Shut up !!!!!!!!!")
                    print("SHUT UP !!!!!!!!!!!!!!!")
                elif "open gmail" in command:
                    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
                elif "open google" in command:
                    chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome"
                    os.startfile(chromepath)
                elif "open youtube" in command:
                    webbrowser.open("https://youtube.com/")
                elif "open microsoft edge" in command:
                    mspath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge"
                    os.startfile(mspath)
                elif "open class" in command:
                    webbrowser.open("https://physicswallah.live/landing-page")
                elif 'weather' in command:
                    url = "https://www.google.com/search?q=weather+in+bhopal&rlz=1C1CHBF_enIN919IN919&oq=weather+in+bhopal&aqs=chrome..69i57j0l6j69i60.6270j1j7&sourceid=chrome&ie=UTF-8"
                    webbrowser.open_new_tab(url)
                elif "into" in command:
                    command = command.replace("into", "*")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "by" in command:
                    command = command.replace("by", "/")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "plus" in command:
                    command = command.replace("plus", "+")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "minus" in command:
                    command = command.replace("minus", "-")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "open school" in command:
                    teamspath = "C:\\Users\\welcome\\Desktop\\Microsoft Teams"
                    os.startfile(teamspath)
                elif 'good ' in command:
                    talk("Same to you sir !!!")
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    talk('current time is ' + time)
                elif "date" in command:
                    today = date.today()
                    d1 = today.strftime("%d/%m/%y")
                    print(d1)
                    talk(d1)
                elif 'who is ' in command:
                    person = command.replace('who is ', ' ')
                    info = wikipedia.summary(person, 2)
                    print(info)
                    talk(info)
                elif 'joke' in command:
                    joke = pyjokes.get_joke()
                    print(joke)
                    talk(joke)
                elif "message" in command:
                    mobNum = {"mam":"+919131160117", "i": "+918827818238", "rahul": "+919822920106", "mami": "+919766153137", "aaji": "+919822594020", "papa": "+919958799407", "appy": "+917869621873"}
                    talk("So to whom would you like to send the message ??")
                    userAsk = take_command()
                    print(userAsk)
                    mob = mobNum[userAsk]
                    talk("listening message !!")
                    m = take_command()
                    print(m)
                    h = int(input("Enter the hour time : "))
                    mun = int(input("Enter the minute time : "))
                    talk("so you are sending message to ")
                    talk(userAsk)
                    talk('saying')
                    talk(m)
                    talk("at")
                    talk(h)
                    talk("hours and")
                    talk(mun)
                    talk("minutes")
                    pywhatkit.sendwhatmsg(mob, m, h, mun)
                elif "open whatsapp" in command:
                    webbrowser.open("web.whatsapp.com")
                elif "switch off " or "shutdown computer" or "shut down computer" or "switch off computer" in command:
                    pyautogui.hotkey('Win', 'D')
                    pyautogui.hotkey('Alt', 'F4')
                    pyautogui.press('Enter')
                elif "restart computer " in command:
                    pyautogui.hotkey('Win', 'D')
                    pyautogui.press('down')

                elif "tell me about shlok shrikhande " in command:
                    print("The great Shlok Shrikhande is my creator, i am his personal assistant")
                    talk("The great Shlok Shrikhande is my creator, i am his personal assistant")
                elif "exit" in command:
                    pyautogui.hotkey("Ctrl", "F2")
                    pyautogui.hotkey('Alt', 'F4')
                    pyautogui.press('down')
                    pyautogui.press('Enter')
                else:
                    talk("pardon")
                print(command)

            wishMe()

            wish_birthday()

            new_year()

            run_pappu()

            with sr.Microphone(device_index=0) as source:
                run_pappu()
                print("listening ...")
                talk("listening")
                voice = listener.record(source, duration=60)
                command = listener.recognize_google(voice, language="en-in")
                talk("recognising")
                print("Recognising....")


        else:
            print("Access Denied")
            pyautogui.move(1343, 715)


    else:
        print("Kindly use our special key to sign in !!")
        special_pass = input("Enter the special key : ")
        if special_pass == datetime.datetime.now().strftime('%I:%M'):
            print("Access Granted")
            name2 = input("Enter your name to check your password and login-id : ")
            print(user_dict[name2])

            def wishMe():
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    talk("Good Morning!")

                elif hour >= 12 and hour < 17:
                    talk("Good Afternoon!")

                else:
                    talk("Good Evening!")

                talk(" sir, please tell me how may i help you ")

            def new_year():
                today1 = date.today()
                d11 = today1.strftime("%d/%m/%Y")
                if d11 == "01/01/2021":
                    talk("also, Happy new year sir")
                    print("Happy new year sir")

            def wish_birthday():
                today2 = date.today()
                d2 = today2.strftime("%d/%m/%y")
                if d2 == "22/07/2021":
                    talk("Happy Birthday Sir !!!!!!")
                    print("Happy Birthday Sir !!!!!!")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "01/02/21":
                    talk("Happy Birthday i ")
                    print("Happy Birthday Aai !!!")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "05/11/2021":
                    talk("happy birthday soham")
                    print("Happy Birthday Sohm !!!!!!!!")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "07/09/2021":
                    talk("happy birthday papa")
                    print("Happy Birthday Papa")
                    pywhatkit.playonyt("Baar Baar din ye aaye")
                elif d2 == "21/03/2021":
                    talk("happy birthday maaai")
                    print("Happy Birthday Mai")
                    pywhatkit.playonyt("Baar Baar din ye aaye")

            def take_command():
                try:
                    with sr.Microphone(device_index=0) as source:
                        print("listening ...")
                        talk("listening")
                        voice = listener.record(source, duration=5)
                        command = listener.recognize_google(voice, language="en-in")
                        talk("recognising")
                        print("Recognising....")
                        command = command.lower()
                        if "pappu" in command:
                            command = command.replace('pappu', '')
                            talk(command)

                except:
                    print("shut up ....")
                    talk("shut up!!!!!!!!!!!!!!! ....")
                return command

            def run_pappu():
                command = take_command()
                if 'play' in command:
                    song = command.replace('play', ' ')
                    talk('Playing' + song)
                    pywhatkit.playonyt(song)
                elif "play  cant dance saala " in command:
                    talk("Shut up !!!!!!!!!")
                    print("SHUT UP !!!!!!!!!!!!!!!")
                elif "open gmail" in command:
                    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
                elif "open google" in command:
                    chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome"
                    os.startfile(chromepath)
                elif "open youtube" in command:
                    webbrowser.open("https://youtube.com/")
                elif "open microsoft edge" in command:
                    mspath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge"
                    os.startfile(mspath)
                elif "open class" in command:
                    webbrowser.open("https://physicswallah.live/landing-page")
                elif 'weather' in command:
                    url = "https://www.google.com/search?q=weather+in+bhopal&rlz=1C1CHBF_enIN919IN919&oq=weather+in+bhopal&aqs=chrome..69i57j0l6j69i60.6270j1j7&sourceid=chrome&ie=UTF-8"
                    webbrowser.open_new_tab(url)
                elif "into" in command:
                    command = command.replace("into", "*")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "by" in command:
                    command = command.replace("by", "/")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "plus" in command:
                    command = command.replace("plus", "+")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "minus" in command:
                    command = command.replace("minus", "-")
                    print(command)
                    res = str(eval(command))
                    print(res)
                    talk(res)
                elif "open school" in command:
                    teamspath = "C:\\Users\\welcome\\Desktop\\Microsoft Teams"
                    os.startfile(teamspath)
                elif 'good ' in command:
                    talk("Same to you sir !!!")
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    talk('current time is ' + time)
                elif "date" in command:
                    today = date.today()
                    d1 = today.strftime("%d/%m/%y")
                    print(d1)
                    talk(d1)
                elif 'who is ' in command:
                    person = command.replace('who is ', ' ')
                    info = wikipedia.summary(person, 2)
                    print(info)
                    talk(info)
                elif 'joke' in command:
                    joke = pyjokes.get_joke()
                    print(joke)
                    talk(joke)
                elif "message" in command:
                    mobNum = {"mam": "+919131160117", "i": "+918827818238", "rahul": "+919822920106",
                              "mami": "+919766153137", "aaji": "+919822594020", "papa": "+919958799407",
                              "appy": "+917869621873"}
                    talk("So to whom would you like to send the message ??")
                    userAsk = take_command()
                    print(userAsk)
                    mob = mobNum[userAsk]
                    talk("listening message !!")
                    m = take_command()
                    print(m)
                    h = int(input("Enter the hour time : "))
                    mun = int(input("Enter the minute time : "))
                    talk("so you are sending message to ")
                    talk(userAsk)
                    talk('saying')
                    talk(m)
                    talk("at")
                    talk(h)
                    talk("hours and")
                    talk(mun)
                    talk("minutes")
                    pywhatkit.sendwhatmsg(mob, m, h, mun)
                elif "open whatsapp" in command:
                    webbrowser.open("web.whatsapp.com")
                elif "switch off " or "shutdown computer" or "shut down computer" or "switch off computer" in command:
                    pyautogui.hotkey('Win', 'D')
                    pyautogui.hotkey('Alt', 'F4')
                    pyautogui.press('Enter')
                elif "restart computer " in command:
                    pyautogui.hotkey('Win', 'D')
                    pyautogui.press('down')

                elif "tell me about shlok shrikhande " in command:
                    print("The great Shlok Shrikhande is my creator, i am his personal assistant")
                    talk("The great Shlok Shrikhande is my creator, i am his personal assistant")
                elif "exit" in command:
                    pyautogui.hotkey("Ctrl", "F2")
                    pyautogui.hotkey('Alt', 'F4')
                    pyautogui.press('down')
                    pyautogui.press('Enter')
                else:
                    talk("pardon")
                print(command)

            wishMe()

            wish_birthday()

            new_year()

            while True:
                run_pappu()
                if "exit" or "shut up" in take_command():
                    break

        else:
            print("Access Denied")


verify_user()