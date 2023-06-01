import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


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

    input_value

    work = 'hskdjlfnksnc'
    
    
    
    
    
    
    output_value = work + input_value[0]
    #------------------------------------------------------------
    return jsonify({'output': output_value})

if __name__ == '__main__':
    app.run(debug=True)
