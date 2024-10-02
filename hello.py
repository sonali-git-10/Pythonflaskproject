from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/get_data")
def getdata():
    data = {
        'name' : 'Sonali',
        'url' : 'https://sonali.com'
    }
    return json.dumps(data)

if __name__ == "__main__":
    app.run()
