import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    # listen speech from microphon and save it to audio
    print("I'm listening!")
    audio = r.listen(source) 

#listen speech from file (wav, aiff, flac, (mp3 not support))
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#     audio = r.recode(source)

try:
    #recognize voice in English 
    #since using from Google, limited 50 times per day
    text = r.recognize_google(audio, language='en-US')
    print(text)

except sr.UnknownValueError:
    #failed to recognize voice due to other noize 
    print('failed to recognize voice')
except sr.RequestError as e:
    #failed to request due to wrong button or network error
    print('request failed: {0}'.format(e)) 