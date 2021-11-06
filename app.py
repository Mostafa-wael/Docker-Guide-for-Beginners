# flask_web/app.py
# to build --> docker build -t <image-name:TAG> .
# to run --> docker run -p 5000:5000 <image-name:TAG>

From flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
