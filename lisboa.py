from flask import Flask, render_template
from adventure_details import a_dict
app = Flask(__name__)


@app.route('/')
def adventure_list():
    return render_template('lisboa.html', entries=range(1, 8))


@app.route('/<adventure_num>')
def show_adventure(adventure_num):
    return render_template('adventure.html', entries=a_dict[str(adventure_num)])


@app.route('/<adventure_num>/reveal')
def show_adventure_reveal(adventure_num):
    return render_template('reveal.html', entries=a_dict[str(adventure_num)])
