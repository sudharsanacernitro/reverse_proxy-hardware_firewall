#!/home/sudharsan/myenv/bin/python3
from flask import Flask, request,render_template, abort, redirect, url_for
import logging
import os
import db

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__, static_url_path='/static')
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

'''@app.before_request
def before_request_func():
    client_mac = request.headers.get('Client-MAC')
    print("Requester MAC:", client_mac)
    condition = db.check(client_mac)
    if not condition:
        abort(403)'''
        

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
    if(db.login(data['name'],data['password'])):
        return redirect(url_for('profile'))
    else:
        return "INVALID CREDENTIALS"
        
@app.route('/endpoint')
def test():
    return 'Hello, World!'

@app.route('/profile')
def profile():
    data=db.profile()
    print(data)
    return render_template('profile.html',data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
