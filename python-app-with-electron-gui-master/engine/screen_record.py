from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('screenRecord.html')


import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}-output.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

@app.route('/record/')
def record():
  while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', img_final)

    captured_video.write(img_final)
    if cv2.waitKey(1) == ord('q'):
        break
        render_template('screenRecord.html')
  return ('screenRecord.html')
if __name__ == '__main__':
  app.run(debug=True)