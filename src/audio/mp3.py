import os
import subprocess


class Mp3(object):

	def __init__(self, filepath):
		self._filepath = filepath

	def play(self):
		if not os.path.isfile(self._filepath):
			raise FileNotFoundError(self._filepath)
		else:
			subprocess.call(['afplay', self._filepath])