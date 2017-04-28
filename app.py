import os
from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] =  os.environ['BUBBLETEAM_MONGO_URI']
mongo = PyMongo(app)

@app.route('/')
def homepage():
    foos = mongo.db.foo.find()
    return """
    <h1>Hello bubble team 🛁🍵</h1>
    {foo}
    """.format(foo=foos[0])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
