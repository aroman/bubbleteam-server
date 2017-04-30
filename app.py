import json
import os
import validators
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import flask_pymongo
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] =  os.environ['BUBBLETEAM_MONGO_URI']
mongo = flask_pymongo.PyMongo(app)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username=os.environ['NLU_API_USERNAME'],
    password=os.environ['NLU_API_PASSWORD']
)

@app.route('/')
def homepage():
    return """
    <h1>Hello BubbleTeam™ 🛁🍵</h1>
    <p>Our database has {count} article(s) in it.</p>
    """.format(count=mongo.db.articles.count())

@app.route('/url', methods=['POST'])
def addUrl():

    # Make sure we have a url
    try:
        url = request.get_json()['url']
    except:
        return jsonify(
            success=False,
            reason="missing 'url' field in JSON body",
        )

    # Make sure we have a  username
    try:
        username = request.get_json()['username']
    except:
        return jsonify(
            success=False,
            reason="missing 'username' field in JSON body",
        )

    # Make sure we have a valid URL
    isUrlValid = validators.url(url)
    if not isUrlValid:
        return jsonify(
            success=False,
            reason="url was not valid",
        )

    response = natural_language_understanding.analyze(
        url=url,
        features=[features.Entities(), features.Keywords(), features.Sentiment()])

    # Add username to response from NLU service
    response['username'] = username

    # Add response + username to database
    mongo.db.articles.insert_one(response)

    # Can't serialize an ObjectId, which is added to response after insert_one call
    response['_id'] = str(response['_id'])

    return jsonify(response)

if __name__ == '__main__':
    with app.app_context():
        # Ensure that there are not two URLs associated with the same username
        mongo.db.articles.create_index(
            [("url", flask_pymongo.DESCENDING), ("username", flask_pymongo.ASCENDING)],
            unique=True
        )
    app.run(debug=True, use_reloader=True)
