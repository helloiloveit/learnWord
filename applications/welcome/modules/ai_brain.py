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


    def think(self, topic_obj, message_data):
        """
        each ai character will be shown here
        tend to ask more
        or listen more
        """
        msg = ''
        reply_msg = message_data['saying']
        """
        ask_msg = topic_obj.ask()
        msg = reply_msg + '. ' + ask_msg
        """
        msg = reply_msg

        return msg







