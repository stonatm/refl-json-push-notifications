# (c) stonatm@gmail.com
# Refl: JSON Push notification

import socket
import json
import time
import os

# debug
DEBUG = False

# edit your server port and host ip
PORT = 8000
HOST = ''

# initialize socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (HOST, PORT) )
s.listen(1)

# main loop
while True:

    try:
        # receive request
        conn, addr = s.accept()
        request = None
        request = conn.recv(1024).decode('iso-8859-1')
        if DEBUG: print('{} connection from {} with request:\n{}\n'.format(time.asctime(), addr[0], request) )
    except Exception as e:
        if DEBUG: print( '{} {}\n'.format( time.asctime(), e) )

    # create response headers
    refl = True
    notification = False
    sound = False
    vibration = False
    stealth = True
    refresh = 288

    # create response message
    title = "MESSAGE TITLE"
    image_url = None
    message = "MESSAGE CONTENT"

    # example: linux system uptime
    #message = str( os.popen("uptime").read() )

    # REFL json response message
    response = { "refl":refl, "title":title, "message":message, "notification":notification, "sound":sound, "vibration":vibration, "refresh":refresh, "stealth":stealth, "image":image_url}

    try:
        # send response header
        conn.send( 'HTTP/1.1 200 OK\n'.encode() )
        conn.send( 'Content-Type: text/html\n'.encode() )
        conn.send( 'Connection: close\n\n'.encode() )
        # send response message
        response = json.dumps(response)
        conn.sendall( response.encode() )
        # close connection
        conn.close()
    except Exception as e:
        if DEBUG: print( '{} {}\n'.format(time.asctime(), e) )
