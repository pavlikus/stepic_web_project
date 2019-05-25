#!/usr/bin/env python


def echo(environ, start_response):
    response = environ['QUERY_STRING'].replace('&', '\n')
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [response.encode()]  
