# coding: utf-8
import requests
import json
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
import whereis
import json

@respond_to('tenki')
def mention_tenki(message):
    message.react('panda9')
    response_text = requests.get('http://flaskwithslackbot_flaskforslackbot_1:5000/plz/tenki/tenki')
    message.reply(response_text.text)
@respond_to('どこ')
def mention_whereis(message):
    message.react('panda9')
    message.reply(json.dumps(whereis.whereis_dict,ensure_ascii=False,separators=(',',':'), indent=4))
