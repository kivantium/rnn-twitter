# -*- coding: utf-8 -*-

import json
import subprocess
from bs4 import BeautifulSoup

def popen(cmd):
    """シェルの実行結果を取得する"""
    outputs = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = outputs.communicate()
    # bytesで受け取った結果をstrに変換する
    return stdout

# get Authorization
f = open('key.json')
oath_key = json.load(f)
appid = oath_key['azureid']
f.close()

SUBSCRIPTION_KEY = appid

f = open('japanese.txt')
lines2 = f.readlines()
f.close()

for text in lines2:
    text = text.rstrip()
    token_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
    translate_url = "https://api.microsofttranslator.com/v2/http.svc/Translate"
    CATEGORY = "generalnn"
    request_token = popen('curl -X POST \"{url}\" -H \"Content-type: application/json\" -H \"Content-length: 0\" -H \"Accept: application/jwt\" -H \"Ocp-Apim-Subscription-Key:{key}\"'.format(url=token_url, key=SUBSCRIPTION_KEY))
    result = popen(
        "curl -X GET --header \'Accept: application/xml\' \'{url}?appid=Bearer%20{token}&text={text}&from=ja&to=en&category={category}\'".format(
            url=translate_url, token=request_token, text=text, category=CATEGORY))
    soup = BeautifulSoup(result)
    print(soup.string)
