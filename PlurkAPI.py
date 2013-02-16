from urllib import urlencode, quote_plus
from urllib2 import urlopen
from time import time
from hashlib import sha1
import hmac, binascii, json, random

class PlurkAPI:
	def __init__(self):
		self.CONSUMER_KEY = ''
		self.CONSUMER_SECRET = ''
		self.TOKEN_KEY = ''
		self.TOKEN_SECRET = ''
		self.baseURL = 'http://www.plurk.com/APP'
		self.data = {
			'oauth_consumer_key': self.CONSUMER_KEY,
			'oauth_token': self.TOKEN_KEY,
			'oauth_signature_method': 'HMAC-SHA1',
			'oauth_version': '1.0',
		}
	def getNonce(self):
		r = random.Random()
		return r.randint(10000000, 99999999)
	def getSignature(self, url):
		qstr = urlencode(sorted(self.data.items()))
		plain = "POST&" + quote_plus(url) + "&" + quote_plus(qstr)
		key = self.CONSUMER_SECRET + "&" + self.TOKEN_SECRET
		hashed = hmac.new(key, plain, sha1)
		return binascii.b2a_base64(hashed.digest())[:-1]
		
	def call(self, api, args={}):
		self.data['oauth_timestamp'] = int(time())
		self.data['oauth_nonce'] = self.getNonce()
		for key in args:
			self.data[key] = args[key]
		self.data['oauth_signature'] = self.getSignature(self.baseURL + api)

		f = urlopen(self.baseURL + api, urlencode(self.data))

		return json.loads(f.read())
