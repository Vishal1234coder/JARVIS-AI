import os
import pygame
import speech_recognition as sr

pygame.init()
pygame.mixer.init()

def speak(text):
    voice = "en-IE-EmilyNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    os.system(command)

    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.wait()

    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)  # Adjust for a shorter duration
        audio = r.listen(source, timeout=5)  # Set a timeout for listening (5 seconds)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')

    except Exception as e:
        print(e)
        return ""

    return query

if __name__ == "__main__":
    speak("Hello, I am Your Virtual Assistant. How Can I Assist You Today?")
    query = take_command()
    print(query)
    speak(query)
