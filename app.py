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

        # Connects to your computer's default camera
    cap = cv2.VideoCapture(0)
    
    
    # Detect the coordinates
    detector = dlib.get_frontal_face_detector()
    
    
    # Capture frames continuously
    lst = []
    j = 0
    while j < 500:
    
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
    
        # RGB to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
    
        # Iterator to count faces
        n = 0
        for face in faces:
    
            # Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
    
            # Increment iterator for each face in faces
            n = n+1
    
            # Display the box and faces
            cv2.putText(frame, 'face num'+str(n), (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(f"Number of faces: {n}")
        lst.append(n)
        # Display the resulting frame
        cv2.imshow('frame', frame)
    
        # This command let's us quit with the "q" button on a keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        j = j+1
        
    output_value = max(lst)
    
    
    # Release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()
    #------------------------------------------------------------
    return jsonify({'output': output_value})

if __name__ == '__main__':
    app.run(debug=True)