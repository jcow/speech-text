import os
import speech_recognition as sr


class VoiceInput(object):

	def __init__(self, output_filename):
		self._output_filename = output_filename

	def get_speech(self):

		# obtain audio from the microphone
		r = sr.Recognizer()
		with sr.Microphone() as source:
		    print("Say something!")
		    audio = r.listen(source)

		text = None

		# recognize speech using Google Speech Recognition
		try:
		    # for testing purposes, we're just using the default API key
		    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		    # instead of `r.recognize_google(audio)`
		    text = r.recognize_google(audio)
		    f = open(self._output_filename, 'w+')
		    f.write(text)
		    f.close()
		except sr.UnknownValueError:
		    print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))

		return text

