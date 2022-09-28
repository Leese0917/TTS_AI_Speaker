# TTS (Text to Speech)
# STT (Speech to Text)

from gtts import gTTS

text_EN = 'Can I help you?' #set the text 
file_name_EN = 'sample_EN.mp3'

tts_en = gTTS(text=text_EN, lang='en') #set AI to speack text in English
tts_en.save(file_name_EN)

from playsound import playsound
# playsound(file_name_EN)    # play mp3 file without open mp3 file

# set the text in Korean this time
text_KR = '뭘 도와드릴까요?' 
file_name_Kr = 'sample_KO.mp3'

tts_Kr = gTTS(text = text_KR, lang = 'ko')
tts_Kr.save(file_name_Kr)
# playsound(file_name_Kr)

#set long text from file
with open('sample.txt', 'r', encoding='utf8') as f: 
    text_from_TextFile = f.read() #read text from sample.txt file 

tts_en = gTTS(text=text_from_TextFile, lang='en')
tts_en.save(file_name_EN)
playsound(file_name_EN)