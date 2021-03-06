#coding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/player')
def player():
    return render_template('player.html')

if __name__ == '__main__':
    app.run()
