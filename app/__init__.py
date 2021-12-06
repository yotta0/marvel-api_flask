# imports
from config import ts, apikey, hash

# Third party imports
import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    chr_name = 'thor'
    endpoint = ('https://gateway.marvel.com/v1/public/characters?')
    params = (f'name={chr_name}&ts={ts}&apikey={apikey}&hash={hash}&limit=1')

    r = requests.get(f'{endpoint}{params}').json()

    # Variables to treat thumbnails and his extension
    thumbnail = r["data"]["results"][0]["thumbnail"]["path"]
    extension = r["data"]["results"][0]["thumbnail"]["extension"]

    data = {
        "name": r["data"]["results"][0]["name"],
        "description": r["data"]["results"][0]["description"],
        "thumbnail": f"{thumbnail}/landscape_incredible.{extension}"
    }

    return render_template('index.html', data=data, chr_name=chr_name)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404