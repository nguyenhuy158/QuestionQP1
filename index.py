import pyttsx3
engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
vi_voice_id = "vietnam"

# Use female English voice
engine.setProperty('voice', vi_voice_id)
engine.say('Hello with my new voice')

engine.runAndWait()
