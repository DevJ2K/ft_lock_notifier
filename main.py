#!/bin/python3

import subprocess
import asyncio
from datetime import datetime
import requests
import json

DEV_MODE = False

if DEV_MODE == True:
	with open(".config.json", "r") as f:
		config = json.load(f)
else:
	with open("config.json", "r") as f:
		config = json.load(f)

async def main():
	url = "https://forty-two-helper-6ec37292ad42.herokuapp.com/"
	params = {
		'user_id': config['user_id']
	}
	requests.post(url + 'lock', params=params)

	subprocess.run(config['lock_cmd'],shell=True, capture_output=True, executable="/bin/bash")

	requests.post(url + 'unlock', params=params)




if __name__ == "__main__":
	asyncio.run(main())
