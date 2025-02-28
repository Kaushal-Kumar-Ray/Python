import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()



# Input text
text = "Hello! I can talk using Python."

# Speak the text
engine.say(text)
engine.runAndWait()
