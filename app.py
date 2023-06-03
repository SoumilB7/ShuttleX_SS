import json
import cv2
import dlib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
cors = CORS(app)

a,b=random.randint(10,50)*10 ,random.randint(10,50)*10
MH = ["n-block","q-block","m-block","l-block","k-block","e-block","enzo","l-block","a-block","h-block","main-subway","foodies","smv","library","anna-audi","cdmm","main-gate"]
#MHx = [[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b],[a,b]]
GH = ["mgb","prp","sjt","c-block-girls","balaji","tt","dc","g-block-girls","smv","library","mgr","main-gate"]

Shuttles ={
"Shuttle_1" : ['1',"1B36C-MH",[a,b],"26",],   # ID , Location , Count ,
"Shuttle_2" : ['1',"1B36F-MH",["x1","y1"],"26",],   # ID , Location , Count ,
"Shuttle_3" : ['1',"1B36G-MH",["x1","y1"],"26",],   # ID , Location , Count ,
"Shuttle_4" : ['0',"1B36H-MH",["x1","y1"],"26",],   # ID , Location , Count ,
"Shuttle_5" : ['1',"1B36J-MH",["x1","y1"],"26",],   # ID , Location , Count ,
}

def rangeof(n):
    if n<3:
        return n , n+2
    else:
        return n-2 ,n+2

k=[1]
@app.route('/')
def index():
    return render_template('index.html', items = "Hello from backend")
    # return "<h1>Hello, World</h1>"
    
counter = [0,0,0,0,0]
output_value=[0,0,0,0,0]

@app.route('/process_data', methods=['POST'])
def process_data():
    data = json.loads(request.data)
    input_value = data['input']
    #------------------------------------------------------------
    
    if(input_value=='cam$$'):
    
        cap = cv2.VideoCapture(0)
        address = "https://192.168.43.1:8080/video"
        cap.open(address)
        
        detector = dlib.get_frontal_face_detector()
        queue = [0,0,0,0,0]
        while True:

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            n = 0

            for _ in faces:
                n = n+1  
                
            print(f"Number of faces: {n}")
            
            i = 0
            while i < 4:
                queue[i] = queue[i+1]
                i = i+1
            queue[i] = n
            dict = {}
            for fn in queue:
                if fn in dict:
                    dict[fn]+=1
                else:
                    dict[fn] = 1
            max = 0
            key = 0
            for k in dict.keys():
                if dict[k] > max:
                    max = dict[k]
                    key = k

            if max >= 4 and key != 0:
                counter[0] -= 1 
                output_value[0] = str(counter[0])
                print("Count decrease -------------------------------------------------------------------------------------------")
                queue = [0,0,0,0,0]

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    elif input_value=='personLocation':
        outputt = str([random.randint(10,50)*10 ,random.randint(10,50)*10]) 
        return jsonify({'output': outputt})
    elif input_value =='counter1':
        counter[0]+=1
        output_value[0] = str(counter[0])
    elif input_value =='counter2':
        counter[1]+=1
        output_value[1] = str(counter[1])
    elif input_value =='counter3':
        counter[2]+=1
        #a,b = rangeof(counter[2])
        output_value[2] = str(counter[2])
    elif input_value =='counter4':
        counter[3]+=1
        #a,b = rangeof(counter[3])
        output_value[3] = str(counter[3])
    elif input_value =='counter5':
        counter[4]+=1
        #a,b = rangeof(counter[4])
        output_value[4] = str(counter[4])
    elif input_value == 'reload':
        return jsonify({'output': str(output_value[0])+','+str(output_value[1])+','+str(output_value[2])+','+str(output_value[3])+','+str(output_value[4])})
        
                
    # input_value format : 
    # member counte       
    
    #------------------------------------------------------------
    return jsonify({'output': str(output_value[0])+','+str(output_value[1])+','+str(output_value[2])+','+str(output_value[3])+','+str(output_value[4])})

if __name__ == '__main__':
    app.run(host = '192.168.43.170',port='5000',debug=True)
