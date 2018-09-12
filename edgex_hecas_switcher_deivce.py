from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests
import consulate
import json

app = Flask(__name__)
api = Api(app)

CONSUL_NAME = "hecas-switcher-device-sevice"

def initConsulate():
    print("Register iot-example to the localhost Consul")
    consul = consulate.Consul()
    consul.agent.service.register(name=CONSUL_NAME, address="129.254.190.41", port=50020, httpcheck="http://129.254.190.41:50020/health", interval="10s" )

#    print("Deregister iot-example from the localhost Consul")
#    consul.agent.service.deregister("iot-example")

    print("Find iot-example service by service id from the localhost Consul")
    service = consul.catalog.service(CONSUL_NAME)
    print(service)

#    prediction = {"timestamp": _timeStamp, "noise": _noise,"noise_next": noise_next}
#               print("prediction : ", prediction)
               #r = requests.post('http://localhost:5001/user', json=user)
                #r = requests.post('http://localhost:50003/api/v1/data', json=prediction)
#            r = requests.put('http://localhost:50003/api/v1/data', json=prediction)
#             printResponse(r)


def printResponse(r):
    print ("Status code  : ", r.status_code)
    print ("Encoding     : ", r.encoding)
#    print ("JSON         : ", r.json())
#    print ("Content type : ", r.headers["Content-Type"])


class CreateHealth(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']

            print(" received!! \n")
            print(request.values)
            print(request.method)
            print(request.url)
            print(request.json)
            print(request.args.get('key',''))

            return {'Email':args['email'], 'UserName':args['user_name'], 'Password':args['password']}

        except Exception as e:
            return {'error':str(e)}

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']

            print(" received!! \n")
            print(request.values)
            print(request.method)
            print(request.url)
            print(request.json)
            print(request.args.get('key',''))

#            prediction = {"timestamp": _timeStamp, "noise": _noise,"noise_next": noise_next}
#               print("prediction : ", prediction)
               #r = requests.post('http://localhost:5001/user', json=user)
                #r = requests.post('http://localhost:50003/api/v1/data', json=prediction)
#            r = requests.put('http://localhost:50003/api/v1/data', json=prediction)
#             printResponse(r)


            return {'Email':args['email'], 'UserName':args['user_name'], 'Password':args['password']}

        except Exception as e:
            return {'error':str(e)}

class CreateScandepth(Resource):
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('depth', type=str)
            args = parser.parse_args()

            _depth = args['depth']

            print("================================================================ \n")
            print("sendDepth received!! \n")
            print(request.values)
            print(request.method)
            print(request.url)
            print(request.json)
            print(json.loads(request.data))
            print("================================================================ \n")

            return {}

        except Exception as e:
            return {'error':str(e)}

class CreateSnapshotDuration(Resource):
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('depth', type=str)
            parser.add_argument('duration', type=str)
            args = parser.parse_args()

            _duration = args['duration']

            print("================================================================ \n")
            print("snapshot duration received!! \n")
            print(request.method)
            print(request.url)
            print(request.values)
            print(request.json)
            print(_duration)
            print("================================================================ \n")

            return {}

        except Exception as e:
            return {'error':str(e)}

api.add_resource(CreateUser, '/user')
api.add_resource(CreateHealth, '/health')
api.add_resource(CreateScandepth, '/api/v1/devices/5b9223a49f8fc200015fc45f/scandepth')
api.add_resource(CreateSnapshotDuration, '/api/v1/devices/5b9223a49f8fc200015fc45f/SnapshotDuration')

if __name__ == '__main__':
    initConsulate()
    app.run(debug=True, host='0.0.0.0', port=int('50020'))
