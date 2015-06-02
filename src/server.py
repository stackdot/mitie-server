#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 * Copyright © 2015 Uncharted Software Inc.
 *
 * Property of Uncharted™, formerly Oculus Info Inc.
 * http://uncharted.software/
 *
 * Released under the MIT License.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
""" 

import sys, os, json, web

parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../MITIE/mitielib')
from mitie import *

urls = { '/ner', 'NerHandler'}

print "\nloading NER model..."
ner = named_entity_extractor('../MITIE/MITIE-models/english/ner_model.dat')
print "\nTags output by this NER model:", ner.get_possible_ner_tags()

class MyApplication(web.application):
    def run(self, argv):
        func = self.wsgifunc()
        return web.httpserver.runsimple(func, (sys.argv[1], int(sys.argv[2])))

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
    app.run(argv=sys.argv)
