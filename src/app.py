#!/usr/bin/env python
import sys, os, json
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../MITIE/mitielib')
from mitie import *

from flask import Flask, request
app = Flask(__name__)

@app.route("/ner", methods=['POST'])
def ner():
    text = json.loads(request.data)['text']
    print "Data:", text

    tokens = tokenize(text)
    print "Tokenized input:", tokens

    print "loading NER model..."
    ner = named_entity_extractor('../MITIE/MITIE-models/english/ner_model.dat')
    print "\nTags output by this NER model:", ner.get_possible_ner_tags()

    entities = ner.extract_entities(tokens)
    print "\nEntities found:", entities
    print "\nNumber of entities detected:", len(entities)

    results = []
    for e in entities:
        range = e[0]
        tag = e[1]
        score = e[2]
        score_text = "{:0.3f}".format(score)
        entity_text = " ".join(tokens[i] for i in range)
        print "   Score: " + score_text + ": " + tag + ": " + entity_text
        result = {"score":score_text, "tag": tag, "label": entity_text}
        results.append(result)

    return json.dumps(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)