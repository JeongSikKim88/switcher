# -*- coding: utf8 -*-

import sys, os
from flask import Flask
from flask import request

import subprocess

app = Flask(__name__)
httpHOST='0.0.0.0'
httpPORT=9001

startcmd1 = 'ffmpeg -rtsp_transport tcp -i rtsp://192.168.100.41:1554/video1+audio1  -c:v h264_nvenc -c:a aac -b:a 128k -ar 44100 -f mpegts udp://localhost:50000?fifo_size=10000000'

startcmd2 = 'ffmpeg -rtsp_transport tcp -i rtsp://192.168.100.41:1554/video1+audio1  -vf scale=640:-1 -c:v h264_nvenc -b:v 200k -c:a aac -f mpegts udp://localhost:50000?fifo_size=10000000'

@app.route("/on")
def HQ():
    subprocess.call (startcmd1, shell=True)
    return "<html><body>on</body></html>"

@app.route("/off")
def LQ():
    subprocess.call (startcmd2, shell=True)
    return "<html><body>off</body></html>"

@app.route("/stop")
def stop():
    os.system('pkill -9 -ef ffmpeg')
    return "<html><body>stop</body></html>"

if __name__ == "__main__":
    # app.debug = True
    app.run(httpHOST, httpPORT)
