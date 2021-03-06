# imports go here.
from flask import Flask, request

app = Flask(__name__)

### Routes ####
## these functions dictate how your server responds to HTTP requests.
## Request object docs: http://flask.pocoo.org/docs/1.0/api/#flask.Request
@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"

@app.route("/hello",methods=["GET"])
def hello():
    return "THIS IS HELLO WORLD!"

@app.route("/", methods=["GET"])
def login():
    username = request.args.get('useername')
    
    
@app.route('/user/<username>')
def profile(username):
    return'{}\'s profile'.format(uusername)
@app.route('/post/<int:post_ids>')
def post(post_ids):
    return "'POST %d' %post_ids

@app.route('/')
    def index():
        return '''
        <html>
        <h1> helo </h1>
        <body>
        <p>
        hi this is done by inline html
        </p>
        </body>
        
        </html>
        
# This block is run if you execute this file locally, i.e. running 
# `python3 app.py` from the command line. You can change the port if you want.
# if you're curious: 
# __name__ is a magic variable set by the python interpreter upon executing this file. 
# more info: https://stackoverflow.com/a/419185
if __name__ == "__main__":
    app.run(port=5050)
