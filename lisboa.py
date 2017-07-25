from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from adventure_details import a_dict


def create_app():
    this_app = Flask(__name__)
    Bootstrap(this_app)
    return this_app

app = create_app()


@app.route('/')
def adventure_list():
    return render_template('lisboa.html', entries=range(1, 8))


@app.route('/<adventure_num>')
def show_adventure(adventure_num):
    return render_template('adventure.html', entries=a_dict[str(adventure_num)])


@app.route('/<adventure_num>/reveal')
def show_adventure_reveal(adventure_num):
    return render_template('reveal.html', entries=a_dict[str(adventure_num)])
