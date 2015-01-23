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




class user_factory(object):
    def __init__(self):
        pass
    def me(self):
        #return user_obj('ai')
        return human_obj('ai', 'reading_act')
    def user(self):
        return user_obj('huy')

