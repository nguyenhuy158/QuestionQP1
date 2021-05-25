from pydub.playback import play
from pydub import AudioSegment
from gtts import gTTS
from playsound import playsound

tts = gTTS('nguyen huy', tld='com.vn', lang='vi')

mp3File = 'hello.mp3'
tts.save(mp3File)
# playsound(mp3File)

play(AudioSegment.from_mp3(mp3File))
