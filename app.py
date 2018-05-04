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
	hello = today + "\n안녕하세요! 오늘 점심뭐먹을까 입니다.\n점심 음식점, 메뉴 걱정말고 저에게 맡겨주세요!" 
	
	# 날씨 정보 출력하기
	
	if content == u"시작하기":
		dataSend = {
			"message" : {
				"text" : hello
			}
		}
	elif content == u"날씨":
		dataSend = {
			"message" : {
				"text" : "곧 날씨정보도 알려드릴 예정입니다."
			}
		}
	return jsonify(dataSend)

	
if __name__ == '__main__':
	app.run()