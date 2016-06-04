

import xml.etree.ElementTree as ET
import requests
import urllib


class WolframAlpha(object):

	filepath = "stuff/wolfram_query_output.xml"

	def __init__(self, api_key):
		self.api_key = api_key
		pass

	def get(self, query):
		query = self._encode_query(query)
		url = 'http://api.wolframalpha.com/v2/query?input={}&appid={}'.format(query, self.api_key)

		print(url)

		r = requests.get(url)
		f = open('stuff/wolfram_query_output.xml', 'w+')
		f.write(r.text)
		f.close()

	def parse(self):
		filepath = self.filepath
		tree = ET.parse(filepath)
		root = tree.getroot()

		found = False
		if len(root) > 1:
			if len(root[1]) > 0:
				element = root[1][0].find('plaintext')
				if element is not None:
					return root[1].get('title') + ". " + element.text

		return None

	def _encode_query(self, query):
		return urllib.parse.quote_plus(query)