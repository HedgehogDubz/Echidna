
import threading
import speech_recognition as sr
import core 

name = "arena" #word that sounds closest to ERINA from Erinaceidae
bias_words = [name]
input_words = ""
def listen_microphone(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print(recognizer.energy_threshold)
        recognizer.energy_threshold = recognizer.energy_threshold
    while True:
        try:
            with microphone as source:
                
                print("Listening...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print(f"HEARD: {text}")
                core.OnInput(text) 
        except sr.UnknownValueError:
            print("Not understood")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def listen_text_input():
    while True:
        text = input()
        print(f"TYPED: {text}")
        core.OnInput(text) 

def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speech_thread = threading.Thread(target=listen_microphone, args=(recognizer, microphone), daemon=True)
    input_thread = threading.Thread(target=listen_text_input, daemon=True)

    speech_thread.start()
    input_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Program terminated.")
