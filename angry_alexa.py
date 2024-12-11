import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")        
engine.setProperty("voice",voices[1].id)
# engine.say("Iam your alexa")
# engine.say("what can i do for you")

def talk(text):
    engine.say(text)
engine.runAndWait()

def alexa_command():

    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace("alexa","")
                print(command)
    except:
        pass 
    return command

def run_alexa():
    command=alexa_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now("%H:%M")
        print(time)
        talk("current time is",+time)

    
    
        # print(song)


        # talk("playing")
        # print("playing")

run_alexa()





