
from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    baseurl = "https://www.omdbapi.com/?"
    movie_name = getMovieName(req)
    if movie_name is None:
        return {}
    en = {'apikey': '...', 't': movie_name}
    yql_url = baseurl + urlencode(en)
    result = urlopen(yql_url).read()
    data = json.loads(result)

    res =[]
    if req.get("result").get("action") == "asked_movie_year":
        res = askedYearWebhookResult(data)
    if req.get("result").get("action") == "asked_movie_rating":
        res = askedRatingWebhookResult(data)

    if req.get("result").get("action") == "asked_movie_genre":
        res = askedGenreWebhookResult(data)

    if req.get("result").get("action") == "asked_movie_actor":
        res = askedActoreWebhookResult(data)


    return res


def getMovieName(req):
    result = req.get("result")
    parameters = result.get("parameters")
    movie_name = parameters.get("movie-name")
    if movie_name is None:
        return None

    return movie_name

def askedActoreWebhookResult(data):
    actor = data.get('Actors')
    title = data.get('Title')
    if (actor is None):
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Actors " + " in movie " + title + " are " + actor

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": []
    }

def askedGenreWebhookResult(data):
    genre = data.get('Genre')
    title = data.get('Title')
    if (genre is None):
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Movie " + title + " is " + genre

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": []
    }

def askedRatingWebhookResult(data):
    imdbRating = data.get('imdbRating')
    metaScore = data.get('Metascore')
    title = data.get('Title')
    if(imdbRating is None and metaScore is None):
        return{}
    if(imdbRating is not None):
        speech = "IMDB rating for "+"movie " + title + "is "+imdbRating
        if(metaScore is not None):
           speech = speech + " and meta score is " +metaScore+" ."
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": []
    }


def askedYearWebhookResult(data):

    year = data.get('Year')
    title = data.get('Title')
    released = data.get('Released')

    if (year is None):
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Movie " + title + " was released on " + released + ", and shown on " + year +  "."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": []
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
