import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cv2
import numpy as np
import dlib


app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = json.loads(request.data)
    input_value = data['input']
    #------------------------------------------------------------    
        
    count = 2
    
    cap = cv2.VideoCapture(0)
    address = "https://192.168.43.1:8080/video"
    cap.open(address)

    detector = dlib.get_frontal_face_detector()

    queue = [0,0,0,0,0,0,0,0,0,0]
    j = 0
    while j < 50:
    
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        n = 0
        
        for _ in faces:
            n = n+1  
    
        print(f"Number of faces: {n}")
        i = 0
        while i < 9:
            queue[i] = queue[i+1]
            i = i+1
        queue.append(n)
        dict = {}
        for fn in queue:
            if fn in dict:
                dict[fn]+=1
            else:
                dict[fn] = 0
        max = 0
        key = 0
        for k in dict.keys():
            if dict[k] > max:
                max = dict[k]
                key = k

        if max >= 9 and key != 0:
            count -= 1
            print(count)
            queue = [0,0,0,0,0,0,0,0,0,0]
        
        cv2.imshow('frame', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        j += 1
        
    output_value = "DONE"
    
    cap.release()
    cv2.destroyAllWindows()
    #------------------------------------------------------------
    return jsonify({'output': output_value})

if __name__ == '__main__':
    app.run(host = '192.168.43.170',port='5000',debug=True)