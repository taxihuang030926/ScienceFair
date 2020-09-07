'''
import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 4000
with sr.WavFile("test.wav") as source :
    audio = r.record(source)

try:
    print("Transcription: " + r.recognize(audio))
except LookupError:
    print("Could not understand audio")
'''

print('hello world')
