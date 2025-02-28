import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to change voice (Male/Female)
def set_voice(gender="male"):
    voices = engine.getProperty("voices")  # Get available voices
    if gender == "female":
        engine.setProperty("voice", voices[1].id)  # Select female voice
    else:
        engine.setProperty("voice", voices[0].id)  # Select male voice

set_voice("female")  # Change to "male" or "female"

def speak(text):
    """Function to make the system speak"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Function to recognize voice command"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for a command...")
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Could not connect to speech recognition service.")
            return None
        except sr.WaitTimeoutError:
            speak("No voice detected, please try again.")
            return None

def confirm_action(action):
    """Function to confirm shutdown/restart/log off"""
    speak(f"Are you sure you want to {action}? Say yes or no.")
    print(f"Are you sure you want to {action}? Say 'yes' or 'no'.")
    
    confirmation = recognize_speech()
    if confirmation and "yes" in confirmation:
        return True
    else:
        speak("Action canceled.")
        return False

def execute_command(command):
    """Function to execute commands based on voice input"""
    
    if "open firefox" in command:
        speak("Opening Firefox")
        webbrowser.open("https://www.google.com")  # Opens a default page in Firefox
        
    elif "open camera" in command:
        speak("Opening Camera")
        subprocess.run("start microsoft.windows.camera:", shell=True)  # Opens Windows Camera App
        
    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.run("calc.exe", shell=True)  # Opens Windows Calculator
        
    elif "open word" in command:
        speak("Opening Microsoft Word")
        subprocess.run("start winword", shell=True)  # Opens Microsoft Word
        
    elif "open excel" in command:
        speak("Opening Microsoft Excel")
        subprocess.run("start excel", shell=True)  # Opens Microsoft Excel
        
    elif "open powerpoint" in command:
        speak("Opening Microsoft PowerPoint")
        subprocess.run("start powerpnt", shell=True)  # Opens Microsoft PowerPoint

    elif "shutdown" in command:
        if confirm_action("shutdown"):
            speak("Shutting down your computer. Goodbye!")
            os.system("shutdown /s /t 5")  # Shutdown in 5 seconds

    elif "restart" in command:
        if confirm_action("restart"):
            speak("Restarting your computer.")
            os.system("shutdown /r /t 5")  # Restart in 5 seconds

    elif "log off" in command or "sign out" in command:
        if confirm_action("log off"):
            speak("Logging out of your system.")
            os.system("shutdown /l")  # Log out    

    elif "exit" in command or "quit" in command:
        speak("Exiting the program. Goodbye!")
        exit()

    else:
        speak("Command not recognized. Please try again.")

# Main program loop
if __name__ == "__main__":
    speak("Voice Command Program Started. Say 'exit' to stop.")
    
    while True:
        command = recognize_speech()
        if command:
            execute_command(command)
        speak("Would you like to give another command?")
