import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

k=[1]
@app.route('/')
def index():
    return render_template('index.html')
    # return "<h1>Hello, World</h1>"
counter = [0]
@app.route('/process_data', methods=['POST'])


def process_data():
    data = json.loads(request.data)
    input_value = data['input']
    #------------------------------------------------------------
    
    if(input_value=='cam$$'):
        #do cam 
        l=0
    else:
        counter[0]+=1
    # input_value format : 
    # member counter
    work = 'done : '        
    
    
    output_value = work + str(counter[0])
    #------------------------------------------------------------
    return jsonify({'output': output_value})

if __name__ == '__main__':
    app.run(host = '192.168.43.54',port='5000',debug=True)
