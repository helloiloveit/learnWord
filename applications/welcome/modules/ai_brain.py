__author__ = 'huyheo'


import logging
from gluon import *
from intent_relation_def import *

from topic_handler import *

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session


handler_dic = {LIKE_SMTH: like_smth_handler,
               OFFER_HELP: receive_offer_help_handler,
               TIME_INFO: time_info_handler,
               ASK_DURATION: ask_duration_handler,
               ASK_CONTACT_INFO: ask_contact_info_handler,
               ASK_WHAT_ARE_U_DOING: ask_what_are_u_doing_handler,
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
                ASK_JOB: talk_about_people,
                INTRODUCE_MYSELF: talk_about_people,
                GREETING: talk_about_people,
                ASK_HOBBY: talk_about_people,
                NICE_TO_MEET_YOU: talk_about_people

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

    def merge_sentence(self, reply, ask, json_data):
        if   ask:
            memory_handler().save_to_short_memory(ASK_FLAG, 'ai', '',ask)
            msg = reply['saying'] + '. ' + ask['saying']
        else:
            msg = reply['saying'] + '.'
            memory_handler().save_to_short_memory(ANSWER_FLAG,'ai',json_data,reply )
        return msg

    def not_ask_intent(self,intent, handler):
        not_ask = [GREETING,  INTRODUCE_MYSELF]
        if intent in not_ask:
            ask_data = None
        else:
            ask_data = handler.ask('huy')
        return ask_data

    def think_with_expected(self, json_data):
        """
        waiting for expected intent to arrive
        """
        topic_handler = memory_handler().get_handler()
        reply_data = topic_handler.handler(json_data)
        memory_handler().save_to_short_memory(ANSWER_FLAG,'ai',json_data,reply_data )
        memory_handler().set_expected_intent(None, None)
        ask_data = topic_handler.ask('huy')
        if not ask_data:
            #ask_data = talk_about_people('').ask('')
            topic_name = memory_handler().get_last_topic()
            class_name = topic_intent_dic[topic_name]['class']
            temp_obj = class_name('huy')
            ask_data = temp_obj.ask('')
            if not ask_data and session.TALK_ACTIVE_FLAG:
                # go back to root subject
                ask_data = talk_about_people('').ask('')
            pass
        msg = self.merge_sentence(reply_data, ask_data, json_data)
        return msg

    def think_with_not_prepare_topic(self, json_data):
        """
        receive intent for the fist time
        """
        intent= ai_json(json_data).get_intent(0)
        handler = handler_dic[intent](json_data)
        reply_data = handler.return_msg()

        ask_data = self.not_ask_intent(intent, handler)
        msg = self.merge_sentence(reply_data, ask_data, json_data)
        return msg

    def think(self, topic_name, json_data):
        """
        each ai character will be shown here
        tend to ask more
        or listen more
        """
        msg = ''
        intent= ai_json(json_data).get_intent(0)
        topic_class = topic_intent_dic[topic_name]['class']
        reply_data = topic_class('ai').handler(json_data)
        ask_data = self.not_ask_intent(intent, topic_class('huy'))
        msg = self.merge_sentence(reply_data, ask_data, json_data)

        return msg






class memory_handler(object):
    def __init__(self):
        pass
    @classmethod
    def intialize_db_for_memory(cls):
        if not session.topic_list:
            session.topic_list =[]
        if not session.intent_list:
            session.intent_list = []

    def set_last_intent(self, intent):
        session.intent_list.append(intent)
        pass
    def get_last_intent(self):
        return session.intent_list[-1]
    def intent_list(self):
        return session.intent_list
    def count(self):
        return len(session.intent_list)
    # expected intent
    def set_expected_intent(self, intent, topic):
        if not intent:
            session.expected_intent = None
            return
        expected_intent = expected_intent_gen[intent]
        data = {
            'class':topic,
            'intent':expected_intent
        }
        session.expected_intent = data
    def get_expected_intent(self):
        try:
            return session.expected_intent['intent']
        except:
            return ''
    def set_next_handler(self,user, intent):
        temp = {'user':'',
                'handler':''}
        if user == 'ai':
            if intent == ASK_HOBBY:
                temp = {'user':'ai',
                        'handler':hobby_obj}
        return temp
    def set_last_topic(self, topic):
        """
        topic obj
        """
        session.topic_list.append(topic)
    def get_topic_list(self):
        return session.topic_list
    def get_last_topic(self):
        return session.topic_list[-1]

    def get_handler(self):
        """
        get info from session
        return obj to handle intent
        """
        topic_name = session.expected_intent['class']
        class_name = topic_intent_dic[topic_name]['class']
        return class_name('huy')

    def save_to_short_memory(self, flag, user, json_data, message):
        if not message['saying']:
            return
        memory_handler().set_next_handler(user,message['intent'])
        memory_handler().set_last_intent(json_data)
        memory_handler().set_last_topic(message['topic'])
        if flag == ASK_FLAG:
            memory_handler().set_expected_intent(message['intent'], message['topic'])



