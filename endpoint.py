#!/home/sudharsan/myenv/bin/python3
from flask import Flask, request,render_template, abort
import os
import db

app = Flask(__name__, static_url_path='/static')
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@app.before_request
def before_request_func():
    client_mac = request.headers.get('Client-MAC')
    print("Requester MAC:", client_mac)
    condition = db.check(client_mac)
    if not condition:
        abort(403)


@app.route('/',methods=['GET'])
@app.route('/generate204',methods=['GET'])
def captiveportal():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    client_mac = request.headers.get('Client-MAC')
    print("Requester MAC:", client_mac)
    data = request.form.to_dict()   
    print("Requested Data: " + str(data)) 
    return f"POST request:{data}"
        
@app.route('/endpoint')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  


'''@app.route('/<path:path>', methods=['GET', 'POST'])
def handle_request(path):
    if request.method == 'POST':
        data = request.data.to_dict()   
        print("Requested Data: " + data) 
        return f"POST request received for path: {path}, data: {data}"
    else:
        return f"GET request received for path: {path}"
     ''' 

