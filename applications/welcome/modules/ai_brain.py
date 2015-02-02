__author__ = 'huyheo'


import logging
from gluon import *
from obj_definition import *
from base_handler import *
from intent_relation_def import *


log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session


class brain(object):
    """
    this is ai analog of human brain
    analyze , generate thing to say, make a move
    """
    def __init__(self):
        self.me = user_obj('ai')

    def generate_topic_to_say(self):
        """
        - If some info is missing : ask for it: user information..etc
        - If about a topic: generate idea about it
        - If not about any topic:
              - talk about weather
              - talk about user information
        """
        # talk about current subject
        """
        exp: talke about hobby: make question of hobby to user
        """

    def think_with_expected(self, json_data):
        msg = memory_handler().get_handler().handler(json_data)
        memory_handler().set_expected_intent(None, None)
        return msg['saying']

    def think(self, topic_name, json_data):
        """
        each ai character will be shown here
        tend to ask more
        or listen more
        """
        msg = ''
        topic_class = topic_intent_dic[topic_name]['class']
        reply_data = topic_class('ai').handler(json_data)
        reply_msg = reply_data['saying']
        ask_data = topic_class('huy').ask()
        """
        ask_msg = topic_obj.ask()
        msg = reply_msg + '. ' + ask_msg
        """
        if   ask_data:
            memory_handler().save_to_short_memory(ASK_FLAG, 'ai', '',ask_data)
            msg = reply_msg + '. ' + ask_data['saying']
        else:
            msg = reply_msg

        return msg







