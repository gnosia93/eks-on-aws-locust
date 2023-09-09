__author__ = "soonbeom kwon"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "gnosia93@naver.com"

import os, sys
from locust.main import main

"""
커맨드 라인 실행할때 념겨줄수 있는 환경변수 모음.
https://docs.locust.io/en/stable/configuration.html#environment-variables
"""

def run_locust(url):
	os.environ['LOCUST_HOST'] = url
	os.environ['LOCUST_USERS'] = "300"
	os.environ['LOCUST_RUN_TIME'] = "10m"
	os.environ['LOCUST_NO_WEB'] = "True"
	os.environ['LOCUST_LOCUSTFILE'] = "scenario.py"
	os.environ['LOCUST_WEB_PORT'] = "8081"
#	os.environ['LOCUST_CLIENTS'] = str(kwargs.get('LOCUST_CLIENTS'))
#	os.environ['LOCUST_HATCH_RATE'] = str(kwargs.get('LOCUST_HATCH_RATE'))
	main()

if len(sys.argv) != 2:
	print("usage: python test.py <URL>")
	exit(-1)

run_locust(sys.argv[1])