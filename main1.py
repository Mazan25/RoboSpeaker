from gtts import gTTS
import os
import playsound

print("Welcome to RoboSpeaker 1.1. Created by Mazan")

while True:
    text = input("Enter what you want me to Speak (or 'q' to quit): ")
    if text.lower() == "q":
        tts = gTTS("Bye bye friend", lang='en')
        tts.save("bye.mp3")
        playsound.playsound("bye.mp3")
        os.remove("bye.mp3")
        break
    tts = gTTS(text, lang='en')
    tts.save("speak.mp3")
    playsound.playsound("speak.mp3")
    os.remove("speak.mp3")
