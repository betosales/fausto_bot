import random
import requests
import json
from conf import *


def call_fausto(name="FAUSTO_BOT", receiver=None, message=None, emoji=":fausto:", web_hook=None):
	if not receiver:
		receiver = random.choice(receivers)
	if not message:
		message = random.choice(phrases)
	if not web_hook:
		web_hook = web_url

	payload={"channel": receiver, 
		   "username": name, 
		   "text": message, 
		   "icon_emoji": ":fausto:"}
	
	r = requests.post(web_hook, data=json.dumps(payload))
	print "OLOCO BIXO, MANDEI '{}' para '{}'".format(message, receiver)


if __name__ == '__main__':
	call_fausto()