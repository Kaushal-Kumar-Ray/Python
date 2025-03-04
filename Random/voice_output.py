import pyttsx3

engine = pyttsx3.init()

text = "Hello! I can talk using Python."

# Speak the text
engine.say(text)
engine.runAndWait()
