from config import ts, apikey, hash
import requests as req
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    chr_name = 'hulk'
    endpoint = ('https://gateway.marvel.com/v1/public/characters?')
    params = (f'name={chr_name}&ts={ts}&apikey={apikey}&hash={hash}&limit=1')

    r = req.get(f'{endpoint}{params}').json()

    # Variables to treat thumbnails and his extension
    thumbnail = r["data"]["results"][0]["thumbnail"]["path"]
    extension = r["data"]["results"][0]["thumbnail"]["extension"]

    data = {
        "name": r["data"]["results"][0]["name"],
        "description": r["data"]["results"][0]["description"],
        "thumbnail": f"{thumbnail}/landscape_incredible.{extension}"
    }

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
