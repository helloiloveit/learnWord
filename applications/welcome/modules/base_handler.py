__author__ = 'huyheo'


import logging
from gluon import *
from obj_definition import *


log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session


class base_intent_handler(object):
    """
    base for handling intent
    """
    def __init__(self, json_data):
        self.me = user_factory().me()
        self.user = user_factory().user()
        self.entity = json_data['outcomes'][0]['entities']
        self.intent = json_data['outcomes'][0]['intent']
        self.json_data = json_data
    def generate_intent(self):
        pass
    def return_msg(self):
        return 'not implement this intent yet'


class handle_order_of_intent(object):
    def __init__(self):
        pass
    def last_intent(self, intent):
        session.topic_list.append(intent)
        pass
    def get_last_intent(self):
        return session.topic_list[-1]
    def intent_list(self):
        return session.topic_list




class user_factory(object):
    def __init__(self):
        pass
    def me(self):
        #return user_obj('ai')
        return human_obj('ai', 'reading_act')
    def user(self):
        return user_obj('huy')

