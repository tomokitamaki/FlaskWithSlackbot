from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def helo():
    return('helo')

@app.route('/plz/tenki/<tenki>')
def returnTenki(tenki):
    tenki = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=016010').json()
    kyouno_tenki = json.dumps(tenki['forecasts'][0]['telop'], ensure_ascii=False, indent=4,  separators=(',', ': '))

    try:
        kyouno_mintenper = json.dumps(tenki['forecasts'][0]['temperature']['min']['celsius'], ensure_ascii=False, indent=4,  separators=(',', ': '))
    except:
        kyouno_mintenper = 'null'

    try:
        kyouno_maxtenper = json.dumps(tenki['forecasts'][0]['temperature']['max']['celsius'], ensure_ascii=False, indent=4,  separators=(',', ': '))
    except:
        kyouno_maxtenper = 'null'

    ashitano_tenki = json.dumps(tenki['forecasts'][1]['telop'], ensure_ascii=False, indent=4,  separators=(',', ': '))
    ashitano_mintenper = json.dumps(tenki['forecasts'][1]['temperature']['min']['celsius'], ensure_ascii=False, indent=4,  separators=(',', ': '))
    ashitano_maxtenper = json.dumps(tenki['forecasts'][1]['temperature']['max']['celsius'], ensure_ascii=False, indent=4,  separators=(',', ': '))
    
    return ('今日の天気は({kyouno_tenki}), 最高気温は({kyouno_maxtenper}) 最低気温は({kyouno_mintenper})\n明日の天気は({ashitano_tenki}) 最高気温は({ashitano_maxtenper}) 最低気温は({ashitano_mintenper})'.format(kyouno_tenki=kyouno_tenki,ashitano_tenki=ashitano_tenki,kyouno_maxtenper=kyouno_maxtenper,kyouno_mintenper=kyouno_mintenper,ashitano_maxtenper=ashitano_maxtenper,ashitano_mintenper=ashitano_mintenper))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
