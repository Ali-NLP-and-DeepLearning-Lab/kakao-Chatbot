from flask import Flask, request, jsonify

import time
import re
import requests


app = Flask(__name__)

'''
@app.route('/')
def hello_world():
	return 'Hello World!'
'''

nowdate = time.strftime('%y%m%d', time.localtime(time.time()))

# 입력을 받는 keyboard 부분
@app.route('/keyboard')
def Keyboard():
	
	dataSend = {
		"type" : "buttons",
		"buttons" : ["시작하기"]
	}
	return jsonify(dataSend)

# 출력을 하는 message 부분
@app.route('/message', methods=['Post'])
def Message():

	dataReceive = request.get_json()
	content = dataReceive['content']
	
	# 첫 인삿말 만들기
	today = str(nowdate)
	hello = "20" + today[0:2] + "년 " + today[2:4] + "월 " + today[4:6] + "일" + "\n안녕하세요! 오늘 점심뭐먹을까 입니다.\n점심 음식점, 메뉴 걱정말고 저에게 맡겨주세요!" 
	
	# 날씨 정보 출력하기
	regionCode = "09530540"
	weather, temp = get_weather(regionCode)
	winfo = "오늘의 날씨는 " + str(weather) + "이고,\n온도는 " + str(temp) + "℃ 네요."

	if content == u"시작하기":
		dataSend = {
			"message" : {
				"text" : hello
			}
		}
	elif content == u"날씨" :
		dataSend = {
			"message" : {
				"text" : winfo
			}
		}
	return jsonify(dataSend)

# 지역의 코드를 가져오는 함수
def get_naver_region(cityName):
	baseUrl = 'https://m.weather.naver.com/ac?q_enc=utf-8&r_format=json&r_enc=utf-8&r_lt=1&st=1&q=' + cityName
	response = requests.get(baseUrl)
	if response.json()['items']==[]:
		regionCode = None
		return regionCode
	else:
		regionCode = response.json()['items'][0][0][1]
		return str(regionCode[0)
	

# 지역의 날씨와 온도를 가져오는 함수	
def get_weather(regionCode):
	url = "https://m.weather.naver.com/m/main.nhn?regionCode=" + regionCode
	summary_regex = r"weather_set_summary\">(.+?)<br>"
	nowTemp_regex = r"degree_code full\">(.+?)</em>"
	response = requests.get(url)
	data = response.text
	summary = re.search(summary_regex, data)
	nowTemp = re.search(nowTemp_regex, data)
	
	return summary.group(1), nowTemp.group(1)
	
if __name__ == '__main__':
	app.run(debug=True)