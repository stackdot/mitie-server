#!/usr/bin/env python
import sys, os, json
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../MITIE/mitielib')
from mitie import *

import web
urls = { '/ner', 'NerHandler'}

print "\nloading NER model..."
ner = named_entity_extractor('../MITIE/MITIE-models/english/ner_model.dat')
print "\nTags output by this NER model:", ner.get_possible_ner_tags()

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

app = MyApplication(urls, globals())

def extractEntities(text):
    response = {}
    response['text'] = text
    response['tokens'] = tokenize(text)
    print "\nTokenized input:", response['tokens']

    global ner
    entities = ner.extract_entities(response['tokens'])
    print "\nEntities found:", entities
    print "\nNumber of entities detected:", len(entities)

    response['entities'] = []
    for e in entities:
        range = e[0]
        tag = e[1]
        score = e[2]
        score_text = "{:0.3f}".format(score)
        entity_text = " ".join(response['tokens'][i] for i in range)
        print "   Score: " + score_text + ": " + tag + ": " + entity_text
        result = {"score":score, "tag": tag, "label": entity_text}
        response['entities'].append(result)
    return response

class NerHandler:
    def POST(self):
        data = web.data()
        print "\nData:", data

        text = json.loads(data)['text']
        print "\nText:", text

        result = []
        if isinstance(text, list):
            for item in text:
                result.append(extractEntities(item))
        else:
            result = extractEntities(text)

        return json.dumps(result)


if __name__ == "__main__":
    app.run(port=8888)