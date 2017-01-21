codes inside [@licarent](https://twitter.com/licarent)

# software requirement
- keras
- Mecab neologd
- jaconv
- BeautifulSoup

 etc.

# How to use
1. Get [YJ Captions 26k Dataset](https://github.com/yahoojapan/YJCaptions) and unzip.
2. Extract caption
```
python caption.py > data.txt
```
3. (optional) Clean dataset manually
4. Train char-rnn
```
python train.py
```
5. Create sentences
```
python create_sentence.py > /dev/null 2> japanese.txt
```
6. (optional) Clean sentence manually
7. Translate to English
```
python translate.py > english.txt
```
8. Generate images. Use https://github.com/reedscot/icml2016
9. Tweet (use cron)
```
python tweet.py
```

# How to get key
Check following web page

- Twitter http://phiary.me/twitter-api-key-get-how-to/
- Yahoo http://developer.yahoo.co.jp/start/
- Microsoft https://www.microsoft.com/ja-jp/translator/getstarted.aspx
