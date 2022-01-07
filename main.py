from os import name
from flask import Flask, request
from flask_restful import Api, Resource
import gtts
from playsound import playsound
from time import sleep
import random
import os

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def post(self, text):
        name = str(random.randint(0, 1000000)) + ".mp3"
        tts = gtts.gTTS(text)
        tts.save(name)
        sleep(0.5)
        playsound(name)
        os.remove(name)
        return {"data": "done"}

    # def post(self):
    #     print(name)
    #     return {"data": "Posted"}


api.add_resource(HelloWorld, "/helloworld/<string:text>")


if __name__ == "__main__":
    app.run(debug=True)
