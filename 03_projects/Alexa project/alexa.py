import speech_recognition as sr # It’ll help the assistant listen to our commands
import pyttsx3 # This is the Text-to-Speech (TTS) library
import pywhatkit # help us play the required songs directly on YouTube.
import datetime # This module helps us to manipulate dates and times 
import wikipedia # it easy to access and parse data from Wikipedia. 
import pyjokes # module will help us generate random one-line jokes 

# its Required internet connection please connect internet 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command =command.replace("alexa","")
    except:
        pass     
    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace('play','')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Currenrt Time is :',time)
    elif 'who is' in command:
        person = command.replace("who is",'')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'give me' in command:
        person = command.replace("give me",'')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a hedache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    else:
        talk('Please say the command again...')

while True:
    run_alexa()