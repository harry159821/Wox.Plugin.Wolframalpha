# -*- coding: utf-8 -*-
import urllib,urllib2,re,time,json
import mp3play
true = True
null = None
false = False

#----------------Google翻译部分-----------------------
REQUEST_URL = 'http://translate.google.cn/translate_a/t?client=t&text=%s&hl=en&sl=zh-CN&tl=zh-CN&ie=UTF-8&oe=UTF-8&multires=1&otf=1&ssel=0&tsel=0&sc=1'
REQUEST_URL = 'http://translate.google.cn/translate_a/t?client=t&text=%s&sl=zh-CN&tl=en&hl=zh-CN&sc=2&ie=UTF-8&oe=UTF-8&oc=1&otf=2&ssel=3&tsel=3'

UA = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'

def combine_comma(match):
	return ','
comma = re.compile(r',+')

def get_translation(data):
	ret = []
	data = comma.sub(combine_comma, data)
	try:
		data = json.loads(data)
	except Exception, e:
		print e
		return None

	for i in data[0]:
		ret.append(i[0])
	ret = ''.join(ret)
	return ret

def googletranslate(query):
	query = urllib.quote(query)

	url = REQUEST_URL % query
	request = urllib2.Request(url)
	request.add_header('User-Agent', UA)
	try:
		response = urllib2.urlopen(request)
		data = response.read()
	except Exception, e:
		print e
		return None
	
	data = get_translation(data)
	if data:
		return data
	return None


#----------------Google TTS-----------------------
def googletts(text,language=None,NoTranslate = None):
        if language == 'en':
            if NoTranslate:    
                    text = googletranslate(text)
            language = 'en'
        else:
            language = 'zh-CN'
            
        url = 'http://translate.google.cn/translate_tts?'
        Dict = {'ie':'UTF-8',
                'q':text,
                #'tl':'zh-CN',
                #'tl':'en',
                'tl':language,
                'total':'1',
                'idx':'0',
                'textlen':len(text),
                    }
        Data=urllib.urlencode(Dict)
        header = {
                'Referer': 'http://translate.google.cn/',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
                'Accept': '*/*',
                'Host': 'translate.google.cn',
                }
        try:
            req=urllib2.Request(url,data=Data, headers=header)
            resp=urllib2.urlopen(req)
            html = resp.read()
            mp3 = open('test.mp3','wb')
            mp3.write(html)
            mp3.close()
            return True
        except:
            return False

if __name__ == '__main__':
    print googletts("先生，有新动漫，更新",'en')
    try:
        import mp3play
        a = mp3play.load('test.mp3')
        a.play()
        while a.isplaying():
            time.sleep(0.1)
        del a
    except:pass
    
