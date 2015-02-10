__author__ = 'huyheo'


import logging
from gluon import *
from intent_relation_def import expected_intent_gen, topic_intent_dic
from utility import *

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session






class user_factory(object):
    def __init__(self):
        pass
    def me(self):
        #return user_obj('ai')
        return human_obj('ai', 'reading_act')
    def user(self):
        return human_obj('huy',READING_ACT)


