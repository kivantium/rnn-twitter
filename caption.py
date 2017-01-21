#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import MeCab
 
mt = MeCab.Tagger("-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
mt.parse('')
f = open('yjcaptions26k_clean.json', 'r')
data = json.load(f)
f.close()
for one in data[u'annotations']:
    text = one['caption'].encode('utf-8')
    node = mt.parseToNode(text)
    node = node.next
    data = ''
    while node:
        if node.next:
            data += node.feature.split(',')[-2]
        node = node.next
    print data
