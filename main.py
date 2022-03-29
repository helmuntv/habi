import json
from property.property import Property
from wsgiref.simple_server import make_server
from urllib import parse
from urllib.error import HTTPError
from property.filters import Filters


def application(environ, start_response):
    headers = [('Content-Type', 'application/json')]
    
    start_response('200 ok', headers)
    
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    
    if path == '/properties' and method == 'GET':
        year_qs, city_qs, status_qs = Filters.validate_filters(environ['QUERY_STRING'])

        response = Property.get_properties(year_qs, city_qs, status_qs)

        return [bytes(json.dumps(response), 'utf-8')]
        

if __name__ == '__main__':
    try:
        server = make_server('localhost', 8000, application)
        print('Serving api on http://localhost:8000')
        print('Use <Ctrl + c> to stop the server')
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
