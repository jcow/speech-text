import os
from gtts import gTTS


class VoiceOutput(object):

	def __init__(self, output_filename):
		self._output_filename = output_filename

	def write_speech(self, text):
		tts = gTTS(text=text, lang='en')
		tts.save(self._output_filename)