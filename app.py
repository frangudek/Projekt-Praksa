from scipy.spatial import distance as dist
import numpy as np
import cv2
from imutils import face_utils
from fastai.vision import *
from flask import Flask, render_template, Response, jsonify
from camera import VideoCamera
import imutils
import argparse
import time
import dlib

app = Flask(__name__)


video_stream = VideoCamera()


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False,port="5000")



































































































































































































































