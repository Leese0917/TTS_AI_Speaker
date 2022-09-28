import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#voice recognize(listen)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = 'en')
        print('[Me] ' + text)

        answer(text)

    except sr.UnknownValueError:
        #failed to recognize voice due to other noize 
        print('failed to recognize voice')
    except sr.RequestError as e:
        #failed to request due to wrong button or network error
        print('request failed: {0}'.format(e)) 

#answer to the input
def answer(input_text):
    answer_text = ''
    if 'Hello' in input_text:
        answer_text = 'hello! nice to meet you'
    elif 'weather' in input_text:
        answer_text = 'todays weather will be hot'
    elif 'thank you' in input_text:
        answer_text = 'you welcome'
    elif 'bye' in input_text:
        answer_text = 'okay see you later'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = 'can you say again?'
    speak(answer_text)

#read the text
def speak(text):
    print('[AI] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound(file_name)

    #delete voice file once it create 
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer() 
m = sr.Microphone() #input from Microphon

speak('what can I help for you today?')
#keep listen background
stop_listening =  r.listen_in_background(m, listen)
#if want to stop, stop_listening(wait_for_stop=False)

while True:
    time.sleep(0.1)