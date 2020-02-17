# your app.py
from flask import Flask
import flask_profiler
import time

app = Flask(__name__)
app.config["DEBUG"] = True

# You need to declare necessary configuration to initialize
# flask-profiler as follows:
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
	    "^/static/.*"
	]
}


@app.route('/product/<id>', methods=['GET'])
def getProduct(id):
    return "product id is " + str(id)


@app.route('/product/<id>', methods=['PUT'])
def updateProduct(id):
    time.sleep(1)
    return "product {} is being updated".format(id)


@app.route('/products', methods=['GET'])
def listProducts():
    time.sleep(3)
    return "suppose I send you product list..."

# In order to active flask-profiler, you have to pass flask
# app as an argument to flask-profiler.
# All the endpoints declared so far will be tracked by flask-profiler.
flask_profiler.init_app(app)


# endpoint declarations after flask_profiler.init_app() will be
# hidden to flask_profiler.
@app.route('/doSomething', methods=['GET'])
def doSomething():
    return "flask-profiler will not measure this."


# But in case you want an endpoint to be measured by flask-profiler,
# you can specify this explicitly by using profile() decorator
@app.route('/doSomethingImportant', methods=['GET'])
@flask_profiler.profile()
def doSomethingImportant():
    return "flask-profiler will measure this request."

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
