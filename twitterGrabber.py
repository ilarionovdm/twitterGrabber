from json import dumps
from bottle import request, post, run, route, response
import twitterGrabberBackend


@post('/grab')
def get_tweets():
    response.add_header('content-type', 'application/json')
    return twitterGrabberBackend.get_twits_list(request)


@route('/ping')
def ping():
    result = {"result": "true"}
    response.body = result
    response.add_header('content-type', 'application/json')
    return dumps(result, indent=4)


run(host='localhost', port=8080)


