from config import ts, apikey, hash
import requests
from flask import Flask, render_template

def get_chr():
    endpoint = ('https://gateway.marvel.com/v1/public/characters?')

    try:
        data_chr = requests.get(f'{endpoint}ts={ts}&apikey={apikey}&hash={hash}&limit=1').json()  # noqa: E501

        name = data_chr["data"]["results"][0]["name"]
        description = data_chr["data"]["results"][0]["description"]
        thumbnail = data_chr["data"]["results"][0]["thumbnail"]["path"]
        extension = data_chr["data"]["results"][0]["thumbnail"]["extension"]
        # Format URL for image from resp.
        thumbnail = f"{thumbnail}/landscape_incredible.{extension}"

        return {"name": name, "description": description, "thumbnail": thumbnail}
    except IndexError:
        return render_template("index.html")


app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
