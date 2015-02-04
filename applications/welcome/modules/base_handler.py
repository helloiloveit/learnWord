__author__ = 'huyheo'


import logging
from gluon import *
from obj_definition import *
from intent_relation_def import  *
from utility import *

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
        self.intent = ai_json(json_data).get_intent(0)
        self.entity = ai_json(json_data).get_entity_list(0)
        self.json_data = json_data
    def generate_intent(self):
        pass
    def ask(self):
        pass
    def return_msg(self):
        return 'not implement this intent yet'


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
                        'handler':hobby}
        return temp
    def set_last_topic(self, topic):
        """
        topic obj
        """
        session.topic_list.append(topic)
    def get_topic_list(self):
        return session.topic_list

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





class user_factory(object):
    def __init__(self):
        pass
    def me(self):
        #return user_obj('ai')
        return human_obj('ai', 'reading_act')
    def user(self):
        return human_obj('huy',READING_ACT)


