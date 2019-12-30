from pydub import AudioSegment
import simpleaudio as sa

class Reader:
    def __init__(self):
        self.text = ""
        self.load_sounds("sound/v1/")
        self.file = AudioSegment.from_wav(self.data["_"])

    def load_sounds(self, path="sound/v1/"):
        alfabet = "_abcdefghijklmnoprstwuyz"
        self.data = {}
        for letter in alfabet:
            self.data[letter] = path + letter + ".wav"
            
    def build_to_sound(self, text):
        self.file = AudioSegment.from_wav(self.data["_"])
        self.text = text
        for letter in self.text:
            self.file += AudioSegment.from_wav(self.data[letter])

    def save_in_temp(self):
        self.file.export("temp.wav", format="wav")

    def set_volume(self, dB, basic_value):
        dB -= basic_value
        self.file = self.file[0:-1] + dB
        self.file.export("temp.wav", format="wav")

    def play(self):
        wave_obj = sa.WaveObject.from_wave_file("temp.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()