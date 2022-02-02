from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',msg="Hello World")

@app.route('/_ah/warmup')
def warmup():
    # Handle your warmup request logic here, e.g. set up a database connection pool
    return "Success"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80)