# your app.py
from flask import Flask
from flask_profiler import Profiler
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


@app.route('/slowtest', methods=['GET'])
def getslow():
    total = 0
    for i in range(10):
        total += i
        print(total)
        time.sleep(4)
    print('-------------------')
    return "slow done"

@app.route('/mediumtest', methods=['GET'])
def getmedium():
    total = 0
    for i in range(10):
        total += i
        print(total)
        time.sleep(2)
    print('-------------------')
    return "medium done"

@app.route('/fasttest', methods=['GET'])
def getfast():
    total = 0
    for i in range(10000000):
        total += i
    print('-------------------')
    print(type(profiler))
    print('-------------------')
    return 'Fast done'


# In order to active flask-profiler, you have to pass flask
# app as an argument to flask-profiler.
# All the endpoints declared so far will be tracked by flask-profiler.
profiler = Profiler()
profiler.init_app(app)


# endpoint declarations after flask_profiler.init_app() will be
# hidden to flask_profiler.
@app.route('/doSomething', methods=['GET'])
def doSomething():
    return "flask-profiler will not measure this."


# But in case you want an endpoint to be measured by flask-profiler,
# you can specify this explicitly by using profile() decorator

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
