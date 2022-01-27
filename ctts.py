from gtts import gTTS
import sys
import playsound
import os
tts = gTTS(sys.argv[1])
tts.save('temp.mp3')
playsound.playsound('temp.mp3', True)
os.remove("temp.mp3")