
from flask import Flask, jsonify
import json
import datetime

app = Flask(__name__)

@app.route('/news.all.get')
def get_news_all_articles():
    with open('news_data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S'
    )

    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }

    return jsonify(data)

@app.route('/')
def index():
    return 'Welcome Manar from Flask!'

if __name__ == "__main__":
    app.run(port=8080)

