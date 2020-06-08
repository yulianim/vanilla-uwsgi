"""Module to demo HTTP GET Requests to send location, time and username to the server"""

import json

def application(environ, start_response):
    """Main method to manage all HTTP REQUESTS"""
    post_env = environ.copy()
    post_env['QUERY_STRING'] = ''
    print(post_env["REQUEST_METHOD"])
    print(post_env["REQUEST_URI"])
    if post_env["REQUEST_URI"] != "/uwsgi-server/location":
        start_response('404 NOT FOUND')
        return []
    print(post_env["PATH_INFO"])
    print(post_env["CONTENT_TYPE"])
    print('wsgi.input: ')
    print(post_env["wsgi.input"])
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    print(request_body)
    try:
        json_request = json.loads(request_body)
    except:
        start_response('400 BAD REQUEST. Malformed JSON format.')
        return [b'{"message":"malformed JSON format"}']
    print(json_request)
    print(json_request["userId"])
    print(json_request["time"])
    response_data = '{\n"userId": '+json_request["userId"]+\
        ',\n"time":"'+json_request["time"]+'"\n}\n'
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [str.encode(response_data)]
