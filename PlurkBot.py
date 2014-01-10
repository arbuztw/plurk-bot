from PlurkAPI import PlurkAPI
import urllib2
import re
import json
import random

def loadResp():
	print ">>> update responses"
	f = open("resp.json", "r")
	r = json.load(f)
	f.close()
	return r

def getResp(cont):
	flag = 0
	for resp in resps:
		if type(resp) != list:
			if re.compile(resp).search(cont) != None:
				flag = 1
		elif flag == 1:
			return random.choice(resp).encode('utf-8')
	return None 


p = PlurkAPI()

comet = p.call("/Realtime/getUserChannel")
comet_channel = comet.get("comet_server") + "&new_offset=%d"

jsonp_re = re.compile('CometChannel.scriptCallback\((.+)\);\s*')
new_offset = -1

count = 0

while True:
	try:
		p.call("/Alerts/addAllAsFriends")
		if count == 0:
			resps = loadResp()
		count = (count + 1) % 30
		print comet_channel % new_offset
		req = urllib2.urlopen(comet_channel % new_offset, timeout=80)
		rawdata = req.read()
		match = jsonp_re.match(rawdata)
		if match:
			rawdata = match.group(1)

		data = json.loads(rawdata)
		new_offset = data.get('new_offset')
		msgs = data.get('data')
		if not msgs:
			continue
		for msg in msgs:
			if msg.get('type') == 'new_plurk':
				pid = msg.get('plurk_id')
				content = msg.get('content_raw')
				print content
				r = getResp(content)
				print r
				if r:
					p.call('/Responses/responseAdd',
						{"plurk_id": pid,
						 "content": r,
						 "qualifier": ":"})
	except Exception as e:
		print e.message
