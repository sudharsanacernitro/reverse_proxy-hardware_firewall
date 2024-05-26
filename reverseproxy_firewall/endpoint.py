#!/home/sudharsan/myenv/bin/python3
from flask import Flask, request, send_file,send_from_directory
import os
app = Flask(__name__)
os.chdir('/home/sudharsan/projects/esp_python/static')

@app.route('/<path:path>', methods=['GET', 'POST'])
def handle_request(path):
    data = request.data.decode('utf-8')
    return f"POST request received for path: {path}, data: {data}"
      
@app.route('/',methods=['GET'])
@app.route('/generate204',methods=['GET'])
def captiveportal():
    return send_file('index.html')


        
@app.route('/endpoint')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run Flask server on localhost:5000

