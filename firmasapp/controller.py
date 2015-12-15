#!/usr/bin/python2.7 -tt

def application(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    yield "Hola"
