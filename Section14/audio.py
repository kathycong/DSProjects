
#tried below but didn't work
#pip3 install pyglet
#import pyglet
#file = pyglet.resource.media('audio/case-closed-531.mp3')
#file.play()
#pyglet.app.run()

import pyaudio
import wave
import speech_recognition as sr
import subprocess

def say(text):
    subprocess.call('say' + text, shell = True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb') #opening the file as read binary
    pa = pyaudio.PyAudio() #instatiate pyaudio

    #used to stream the audio
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

#specch recogniser
r = sr.Recognizer()

def initSpeech():
    print("Listening...")
    play_audio("./audio/good-things-happen-547.wav")

    with sr.Microphone() as source:
        print("say Something")
        audio = r.listen(source)

    play_audio("./audio/case-closed-531.wav")

    command = ""

    #a fail safe if the recognizer can't understand what we are saying
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro")

    print('Your command:')
    print(command)
    say('You said: '+ command)

initSpeech()


