from json import dumps
from bottle import request, post, run, route
import twitterGrabberBackend


@post('/results')
def get_tweets():
    return twitterGrabberBackend.get_twits_list(request)


@route('/ping')
def ping():
    result = {"result": "true"}
    return dumps(result, indent=4)


run(host='localhost', port=8080)


