codes inside [@licarent](https://twitter.com/licarent)

# required library
- [Keras](https://keras.io/#installation)
- [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)
- [jaconv](https://github.com/ikegami-yukino/jaconv)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# How to use
- Get [YJ Captions 26k Dataset](https://github.com/yahoojapan/YJCaptions) and unzip.
- Extract caption
```
python caption.py > data.txt
```
- (optional) Clean dataset manually
- Train char-rnn
```
python train.py
```
- Create sentences
```
python create_sentence.py > /dev/null 2> japanese.txt
```
- (optional) Clean sentence manually
- Translate to English
```
python translate.py > english.txt
```
- Generate images. Use https://github.com/reedscot/icml2016
- Tweet (use cron)
```
python tweet.py
```

# How to get key
Check following web page

- Twitter http://phiary.me/twitter-api-key-get-how-to/
- Yahoo http://developer.yahoo.co.jp/start/
- Microsoft https://www.microsoft.com/ja-jp/translator/getstarted.aspx
