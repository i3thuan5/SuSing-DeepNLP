
from sys import stdin

from deepnlp import pos_tagger
import deepnlp
from flask import Flask


deepnlp.register_model('pos', 'tw')
tagger = pos_tagger.load_model(name='tw')

app = Flask(__name__)


@app.route("/<bun5ji7>")
def hello(bun5ji7):
    tagging = tagger.predict(bun5ji7.rstrip().split(" "))
    return list(tagging)
