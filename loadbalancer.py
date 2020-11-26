# loadbalancer.py
from flask import Flask, request
import requests, random

loadbalancer = Flask(__name__)
MANGO_BACKENDS = ["localhost:8081", "localhost:8082"]
APPLE_BACKENDS = ["localhost:9081", "localhost:9082"]

#@loadbalancer.route('/')
#def router():
#    host_header = request.headers["Host"]
#    if host_header == "www.mango.com":
#        response = requests.get("http://{}".format(random.choice(MANGO_BACKENDS)))
#        return response.content, response.status_code
#    elif host_header == "www.apple.com":
#        response = requests.get("http://{}".format(random.choice(APPLE_BACKENDS)))
#        return response.content, response.status_code
#    else:
#        return "Not Found", 404

#호스트가 뭔지 신경안써도 되는데 내가 틀릴수도있어, 2번째거는 호스트를 하지마 나도 잘은 몰라ㅠㅠ
@loadbalancer.route('/mango')
def mango_path():
    response = requests.get("http://{}".format(random.choice(MANGO_BACKENDS)))
    return response.content, response.status_code

@loadbalancer.route('/apple')
def apple_path():
    response = requests.get("http://{}".format(random.choice(APPLE_BACKENDS)))
    return response.content, response.status_code