#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,urllib2
import wolframalpha,google
client = wolframalpha.Client('7UW6LK-YW9T8YPYAG')
true = True
null = None
false = False

def query(Allkey):
	Allkey = Allkey.encode("utf-8")
	key = ' '.join(Allkey.split(" ")[1:])
	results = []
	if key:
		if Allkey.endswith(' '):
			q = google.googletranslate(key)
			if not q:
				q = key
			que = client.query(q)
			for pod in que.pods:
				if pod.text and pod.text != 'nun':
					res = {} 					
					res["Title"] = pod.text
					res["IcoPath"] = './icon.png'
					results.append(res)
			return json.dumps(results)
		else:
			url = 'http://www.wolframalpha.com/input/autocomplete.jsp?qr=0&i='+key
			html = requests(url)
			html = json.loads(html)
			for i in html["results"]:
				res = {}
				res["Title"] = i["input"]
				try:
					res["SubTitle"] = i["description"]
				except Exception, e:
					print e
				res["IcoPath"] = './icon.png'
				results.append(res)
			return json.dumps(results)
	#else:			
	if Allkey.endswith(' '):
		url = 'http://www.wolframalpha.com/input/random.jsp'
		req = urllib2.urlopen(url)
		dlink = req.geturl()[37:]
		dlink = dlink.replace('+',' ')
		res = {}
		res["Title"] = dlink
		res["SubTitle"] = 'random question'
		res["IcoPath"] = './icon.png'
		results.append(res)
		return json.dumps(results)

def requests(url,timeouts=4):
	header = {
			'Referer': 'http://www.wolframalpha.com/',
			'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
			}	
	request = urllib2.Request(url,headers=header)
	response = urllib2.urlopen(request,timeout=timeouts)
	html = response.read()
	if html:	
		return html
	return False
			
if __name__ == '__main__':
	print query(u"wolframalpha")
	#print query(u"wolframalpha 谁是毛泽东")
	#print query(u"wolframalpha who")
	#print query(u"wolframalpha who is putin ")
