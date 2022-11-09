import random
import pyttsx3

engine = pyttsx3.init()

greetings = ["Hi","Hello","Greetings sir","Greetings young Master"]

def greet():
    
    greeting = random.choice(greetings)

    engine.say(greeting)
