import random
import pyttsx3



greetings = ["Hi","Hello","Greetings sir","Greetings young Master"]

def greet():
    
    engine = pyttsx3.init()
    engine.setProperty('volume',1.0)
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[0].id)

    greeting = random.choice(greetings)

    engine.say(greeting)
    engine.runAndWait()
