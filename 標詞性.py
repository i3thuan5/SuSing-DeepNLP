from deepnlp import pos_tagger
from deepnlp import register_model
from flask import Flask
import json


deepnlp.register_model('pos', 'tw')
tagger = pos_tagger.load_model(name='tw')

app = Flask(__name__)


@app.route("/<bun5ji7>")
def 標記(bun5ji7):
    tagging = tagger.predict(bun5ji7.rstrip().split(" "))
    return json.dumps(
        list(tagging),
        indent=2, ensure_ascii=False, sort_keys=True
    )
