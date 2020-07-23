import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb 
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Hi! Sir")
    time()
    date()
    #hour = datetime.datetime.now().hour
    #if hour >=6 and hour<12:
        #speak("good morning!")
    #elif hour>=12 and hour<18:
        #speak("good afternoon!")
    #elif hour>=18 and hour<24:
        #speak("good evening!")
    #else:
        #speak("Good night")
    speak("current time?")
    speak("today's date?")
    speak("search Ai bot in wekipedia")
    speak("Take Note")
    speak("Read Notes")
    speak("Take ScreenShot")
    speak("Play songs")
    speak("Tell me a joke")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=None)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Sorry I am New Please Repeat")
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2505shivang@gmail.com','Shivang@123')
    server.sendmail('2505shivang@gmail.com', to,content)
    server.close()


def screenshot(name):
    img = pyautogui.screenshot()
    img.save('./ScreenShot/'+name+'.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('Cp is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def input():
     r = sr.Recognizer()
     with sr.Microphone() as source:
      flag = True 
      while flag :
        print("Listening.......")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=None)
        query = "None"    
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(query)
            return query
    
        except Exception as e:
            print(e)
            speak("")
        
     return query

if __name__ == "__main__":
    #wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        #elif 'send email' in query:
            #try:
                #speak("what should I say?")
                #content = takeCommand()
                #to = 'somyaagrawal.ime19@gmail.com'
                #sendemail(to,content)
                #speak("EMail send!")
            #except Exception as e:
                #print(e)
                #speak("Unable to send mail")

        elif 'chrome' in query:
            speak("what to search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = input().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'open youtube' in query:
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = input().lower()
            wb.get(chromepath).open_new_tab('https://youtube.com')

        elif 'play songs' in query:
            songs_dir = './Songs'
            speak("which song ?")
            song = input().lower()
            songs = os.listdir(songs_dir)
            try:
                for  i in songs:
                    if song in i.lower():
                        os.startfile(os.path.join(songs_dir,i))
            except Exception as e:
                speak('No Song named'+song+'in Playlist Please add the song in songs folder then try again')

        elif 'take note' in query:
            speak("New Note Sir ?")
            new = input().lower()
            filename = 'default'
            if(new == 'yes'):
                speak('Heading of Note Sir ?')
                filename  = input().lower()

            speak("what should i ?")
            data = input().lower()
            speak(data + "Noted this")
            remember = open('./Notes/'+filename+'.txt' , 'w')
            remember.write(data)
            remember.close()

        elif 'read notes' in query:
            speak("Which Note sir?")
            filename = input()
            try:
                remember = open('./Notes/'+filename+'.txt','r')
                speak(filename+'Note says :-') 
                speak(remember.read())
            except Exception as e:
                speak('No Notes exist with heading'+filename)

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'screenshot' in query:
            speak("Name of the Screenshot ?")
            namefile = input().lower()
            screenshot(namefile)
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Going Offline")
            quit()
