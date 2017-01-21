#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import random
import json
from requests_oauthlib import OAuth1Session

f = open('japanese.txt')
lines = f.readlines()
f.close()

f = open('key.json')
oath_key = json.load(f)
CK = oath_key['key']['CK']
CS = oath_key['key']['CS']
AT = oath_key['key']['AT']
AS = oath_key['key']['AS']
f.close()

twitter = OAuth1Session(CK, CS, AT, AS)

tw = random.randint(0, 144)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
files = {"media" : open('result/img_{}.png'.format(tw+1), 'rb')}
req_media = twitter.post(url_media, files = files)
if req_media.status_code != 200:
    exit()

media_id = json.loads(req_media.text)['media_id']

url_text = "https://api.twitter.com/1.1/statuses/update.json"
params = {"status": lines[tw], "media_ids": [media_id]}
req = twitter.post(url_text, params = params)
