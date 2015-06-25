#coding=utf8

import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()
#result = nlp.parse(u"Hello world!  It is so beautiful.")
result = nlp.parse(u"今天天气真不错啊！")
pprint(result)

from nltk.tree import Tree
tree = Tree.fromstring(result['sentences'][0]['parsetree'])
#pprint(tree)
tree.pretty_print()
