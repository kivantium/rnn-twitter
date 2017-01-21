#!/usr/bin/python
#-*- coding: utf-8 -*-

from __future__ import print_function
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
from requests_oauthlib import OAuth1Session
import json
import sys
import codecs
import string
import jaconv
import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session

f = open('key.json')
oath_key = json.load(f)
appid = oath_key['appid']
f.close()

def conv_print(text):
    hira = jaconv.kata2hira(text)
    yahoo_url = "http://jlp.yahooapis.jp/JIMService/V1/conversion"
    parameter = {'appid': appid,
                'sentence': hira,
                'results': 1}
    r = requests.get(yahoo_url, params=parameter)
    soup = BeautifulSoup(r.text)
    sentence = ''
    for word in soup.find_all('candidatelist'):
        sentence += word.find('candidate').text
    content = '{}'.format(sentence.encode('utf-8'))
    sys.stderr.write(content)
    sys.stderr.write('\n')

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds+0.0001) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# open file
text = codecs.open('data.txt', 'r', 'utf-8').read()
print('corpus length:', len(text))

chars = sorted(list(set(text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 10
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

# build the model: a single LSTM
print('Load model...')
model = load_model('model-1.h5') # change manually

# train the model, output generated text after each iteration
for iteration in range(1, 500):
    # learning
    # generate tweet
    batch = np.random.randint(1000000, size=1)
    model.fit(X[batch:batch+512], y[batch:batch+512], batch_size=128, nb_epoch=1)
    model.reset_states()
    generated = ''
    start_index = random.randint(0, len(text) - maxlen - 1)
    sentence = text[start_index: start_index + maxlen]
    start = sentence
    generated = ''
    temp = np.random.uniform(0.0, 0.6, size=1)
    try:
        for i in range(200):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, temp)
            next_char = indices_char[next_index]
            generated += next_char
            sentence = sentence[1:] + next_char
        text = '{}{}'.format(start.encode('utf-8'), generated.encode('utf-8'))
        text = text.decode('utf-8')
        texts = text.split(u'\n')
        if len(texts) > 2:
            conv_print(texts[1])
        if len(texts) > 3:
            conv_print(texts[2])
    except Exception, e:
        continue
