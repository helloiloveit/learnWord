__author__ = 'huyheo'


import logging
from gluon import *


session = current.session



class data_format(object):
    """
    define data format for user internally
    """
    def __init__(self):
        pass
    @classmethod
    def saying(self, msg, intent, topic):
        data = {'saying':msg, 'intent':intent, 'topic':topic}
        return data


class ai_json(object):
    """
    handle json data format
    """
    def __init__(self, base_json):
        self.base_json = base_json
        number = 0
        self.entity = self.base_json['outcomes'][number]['entities']
        pass
    def get_intent(self, number):
        self.intent = self.base_json['outcomes'][number]['intent']
        return self.intent
    def get_entity_list(self, number):
        return self.entity
    def get_entity(self, name):
        try:
            value = self.entity[name][0]['value']
            return value
        except:
            return ''
    def make_json(self, intent, entity):
        data = {"outcomes":[
            {
            "intent" :  intent,
            "entities" : entity
                            }
        ]}
        return data
    def make_entity(self,name, value):
        entity_json = {
            name:[
                {
                    "value":value
                }
            ]
        }
        return entity_json
