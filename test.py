# -*- coding: utf-8 -*-
import wolframalpha,google
client = wolframalpha.Client('7UW6LK-YW9T8YPYAG')
q = google.googletranslate('谁是毛泽东')
print q
res = client.query('30 deg C in deg F')
#res = client.query('who is maozedong')
results = list(res.results)

for pod in res.pods:
    print pod.text
    
for i in results:
    print i.text

print next(que.results).text