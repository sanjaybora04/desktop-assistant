import speech_recognition as sr
from playsound import playsound


r = sr.Recognizer()

r.energy_threshold = 300
r.pause_threshold = 0.8
r.dynamic_energy_threshold = False

def start():
    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        playsound("listening.mp3")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Processing audio...")

        

        return r.recognize_google(audio)
