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
    ashitano_tenki = json.dumps(tenki['forecasts'][1]['telop'], ensure_ascii=False, indent=4,  separators=(',', ': '))
    return ('今日の天気は({kyouno_tenki}), 明日の天気は({ashitano_tenki})'.format(kyouno_tenki=kyouno_tenki,ashitano_tenki=ashitano_tenki))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
