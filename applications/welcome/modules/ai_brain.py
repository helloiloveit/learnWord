__author__ = 'huyheo'


import logging
from gluon import *
from base_handler import *
from intent_relation_def import *

from topic_handler import *

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session


handler_dic = {LIKE_SMTH: like_smth_handler,
               GREETING: greeting_handler,
               OFFER_HELP: receive_offer_help_handler,
               TIME_INFO: time_info_handler,
               INTRODUCE_MYSELF:introduce_myself_handler,
               ASK_DURATION: ask_duration_handler,
               ASK_CONTACT_INFO: ask_contact_info_handler,
               ASK_WHAT_ARE_U_DOING: ask_what_are_u_doing_handler,
               ASK_HOBBY: ask_hobby_handler,
               ASK_DISTANCE: ask_distance_handler,
               ASK_WHY_LIKE: ask_why_like_handler,
               ASK_HOW_TO_DO: ask_how_to_do_handler,
               EMOTIONAL_EXPRESSION: emotional_expression,
               ASK_HEALTH_STS: health_sts_handler,
               #assistant
               ASK_WHAT_SHOULD_I_DO: ask_advice,
               ASK_WHAT_MAKE_HAPPY: ask_what_make_happy,
              # ask personal info
                ASK_AGE: talk_about_people,
                ASK_NAME: talk_about_people,
                ASK_JOB: talk_about_people

               }

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

    def merge_sentence(self, reply, ask):
        if   ask:
            memory_handler().save_to_short_memory(ASK_FLAG, 'ai', '',ask)
            msg = reply['saying'] + '. ' + ask['saying']
        else:
            msg = reply['saying'] + '.'
        return msg

    def think_with_expected(self, json_data):
        """
        waiting for expected intent to arrive
        """
        topic_handler = memory_handler().get_handler()
        reply_data = topic_handler.handler(json_data)
        memory_handler().set_expected_intent(None, None)
        ask_data = topic_handler.ask()
        msg = self.merge_sentence(reply_data, ask_data)
        return msg

    def think_with_not_prepare_topic(self, json_data):
        """
        receive intent for the fist time
        """
        intent= ai_json(json_data).get_intent(0)
        handler = handler_dic[intent](json_data)
        reply = handler.return_msg()
        ask_data = handler.ask()
        msg = reply
        try:
            msg = msg['saying']
        except:
            msg = msg
        return msg
    def think(self, topic_name, json_data):
        """
        each ai character will be shown here
        tend to ask more
        or listen more
        """
        msg = ''
        topic_class = topic_intent_dic[topic_name]['class']
        reply_data = topic_class('ai').handler(json_data)
        ask_data = topic_class('huy').ask()
        msg = self.merge_sentence(reply_data, ask_data)

        return msg







