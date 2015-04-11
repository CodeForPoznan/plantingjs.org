# -*- coding: utf-8 -*-

u"""
module: planting
"""

from flask import Flask
from flask import render_template

from save import save


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return render_template('index.html', name=None)

@app.route('/manifesto.json')
def send_manifesto():
    return app.send_static_file('manifesto.json')

@app.route('/objects/<path:path>')
def send_objects(path):
    return app.send_static_file('objects/%s' % path)

@app.route('/callback')
def callback():
    return render_template('save_callback.html')


save = app.route('/save', methods=['POST'])(save)


if __name__ == '__main__':
    app.run(debug=True)