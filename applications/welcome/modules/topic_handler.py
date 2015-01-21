__author__ = 'huyheo'


import logging
from gluon import *


from obj_definition import *
from intent_def import *

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session


class base_intent_handler(object):
    """
    base for handling intent
    """
    def return_msg(self):
        return 'not implement this intent yet'

class talk_about_people(object):
    """
    talk about people
        - introduce it self
        - talk about hobby...etc
    """
    def __init__(self, name):
        self.me = user_obj('ai')
        self.talk_to = user_obj('huy')
    def handle_user_saying(self, intention, entity):
        """
        same topic or new topic
        """
        if 'new topic':
            msg =  'handle new topic'

        elif 'old topic':
            msg = ' old topic'
        return msg

    def handler_user_saying(self, intent):
        if intent == ASK_AGE:
            msg = self.me.get_age()
        elif intent == ASK_NAME:
            msg = self.me.get_name()
        elif intent == ASK_JOB:
            msg = self.me.get_job().get_name()
        return msg

class greeting_handler(object):
    def __init__(self, json_data):
        pass
    def return_msg(self):
        msg = 'hello'
        return msg


class user_factory(object):
    def __init__(self):
        pass
    def me(self):
        #return user_obj('ai')
        return human_obj('ai', 'waiting')
    def user(self):
        return user_obj('huy')

class generate_msg_to_say(object):
    def __init__(self, intent, target):
        self.intent = intent
        #save to session
    def msg(self):
        if self.intent =='ask_time':
            return 'could u help me to know the time the bus arrive?'
        else:
            return 'dont know what to say with this purpose'

class handle_order_of_intent(object):
    def __init__(self):
        pass
    def last_intent(self, intent):
        session.topic_list.append(intent)
        pass
    def get_last_intent(self):
        return session.topic_list[-1]




class ask_opinion_about_sth(object):
    def __init__(self, json_data):
        self.json_data = json_data
        self.target = self.get_target_info()
        self.opinion_of_user = user_factory().me()
        self.user = user_factory().user()
        pass

    def get_target_info(self):
        """
        - get target infor from json_data
        - handle it
        """
        entity = self.json_data['outcomes'][0]['entities']
        target_name = entity[TARGET_NAME][0]['value']
        if target_name == IT_SUBJECT:
            # load the last topic to decide the subject
            return user_factory().user().get_job()
        else:
            return user_factory().user().get_job()


    def return_msg(self):
        msg = self.opinion_of_user.give_opinion(self.target)
        return msg

class receive_offer_help_handler(base_intent_handler):
    def __init__(self, base_json):
        self.receive_offer_user = user_factory().me()
        self.offer_user = user_factory().user()
        self.base_json = base_json
        pass
    def return_msg(self):
        """
        return mssage by call need_smth() of user activity
        """
        new_intent =  self.receive_offer_user.doing.need_smth()
        handle_order_of_intent().last_intent(new_intent)
        if new_intent == "ask_time":
            msg = generate_msg_to_say('ask_time','bus').msg()
            return msg
        else:
            return'no'


class time_info_handler(base_intent_handler):
    def __init__(self, base_json):
        """
        get previous sentence to know why user give time
        """
        pass
    def return_msg(self):
        if handle_order_of_intent().get_last_intent() == 'ask_time':
            return'thank you.Im John. Nice to meet you'
        else:
            print'last intent is', handle_order_of_intent().get_last_intent()
            return 'why you give me time?'

class introduce_myself_handler(base_intent_handler):
    def __init__(self, base_json):
        pass

class ask_duration_handler(base_intent_handler):
    def __init__(self, base_json):
        pass
class ask_contact_info_handler(base_intent_handler):
    def __init__(self, base_json):
        pass

class go_to_place(object):
    """
    handle talk about place
    """
    def __init__(self, place):
        self.to_do_list = {TIME_INFO:'',
                           METHOD_TO_GO:''}
        self.expected_intention =None
        #intialize place object
        self.initialize_place_info(place)
        self.user = user_obj('huy')

    def initialize_user_info(self, user):
        """
        create user info
        """
        self.user = user_obj()

        pass

    def _save_info_to_session(self):
        """
        session act as a brain to remember info
        """
        session.time_to_go = self.to_do_list[TIME_INFO]
        session.by_what = self.to_do_list[METHOD_TO_GO]

    def _thinking_about_time_at_destination(self, time):
        """
        - check if timing is good to enter the place
        - check if timing is good to go to their place
        - check the impact of time with user check user time_constraint
        """
        if time in self.place.access_time():
            print 'time is ok to enter'
        if time  in self.user.get_available_time():
            print 'you have time to go'
        return True
    def _thinking_about_method(self, vehicle):
        """
        - check if vehicle is available
        """
        #assume that vehicle is ready
        return 'vehicle is ready'

    def _thinking_(self):
        time_result =  self._thinking_about_time_at_destination(self.to_do_list[TIME_INFO])
        vehicle_result = self._thinking_about_method(self.to_do_list[METHOD_TO_GO])
        if time_result and vehicle_result:
            time_travel = self._calculate_how_long_does_it_take(self.to_do_list[METHOD_TO_GO])
            if self._thinking_about_time_at_destination(self.to_do_list[TIME_INFO] + time_travel):
                return 'you could go there'
            else:
                return 'there s not enough time to get there'




    def initialize_place_info(self, place):
        """
        get information about this talk from db or session
        """
        related_name = ['there', 'that place','it']
        if session.place == place or place in related_name:
            #same place
            self.place = place_obj(session.place)
        elif session.place == None:
            self.place = place_obj(place)

        #load information from session .
        self.to_do_list[TIME_INFO] = session.time_to_go
        self.to_do_list[METHOD_TO_GO] = session.by_what
        self.expected_intention = session.expected_saying

    def create_response(self):
        """
        create question for AI
        if necessary infor is not existed , AI will ask question to get it
        """
        if self.to_do_list[TIME_INFO] == None:
            message = 'ask about time'
            session.time_to_go = message
            self.expected_intention = TIME_INFO
            session.expected_saying = self.expected_intention
            return message
        elif self.to_do_list[METHOD_TO_GO] ==None:
            message = 'ask method to go'
            session.by_what = message
            self.expected_intention =METHOD_TO_GO
            session.expected_saying = self.expected_intention
            return message
        else:
            return self._thinking_()

    def _handler_new_saying(self):
        """
        verify information in this saying
        if enought info.. go to analyze it
        if not ..ask question
        """
        if self.to_do_list[TIME_INFO] and self.to_do_list[METHOD_TO_GO]:
            msg = self._thinking_()
        else:
            msg = self.create_response()
        return msg

    def _handler_user_reply(self, intention, value):
        self.to_do_list[self.expected_intention] = value
        #clear expected saying
        self.expected_intention = None
        session.expected_saying = None

        response_msg =  self.create_response()
        self._save_info_to_session()
        return response_msg

    def _calculate_distance_from_user(self):
        #self.place.where_is_it() - self.user.get_position()
        return '5km'
    def _calculate_how_long_does_it_take(self, vehicle):
        return '1h'

    def handle_user_saying(self, intention, entity):
        """
        1.asnwer appropriate info
        """
        if self.expected_intention == intention:
            #handle reply from user for AI question
            if intention == TIME_INFO:
                value = entity['datetime'][0]['value']
            elif intention == METHOD_TO_GO:
                value = entity['method'][0]['value']

            msg = self._handler_user_reply(intention, value)
        else:
            # handle sub intention of this
            msg = self._handler_intention_of_question(intention)
        return msg

    def _handler_intention_of_question(self, intention):

        if intention == 'where_is_it':
            return self.place.where_is_it()
        elif intention == 'how_far_is_it':
            return self._calculate_distance_from_user()
        elif intention == TO_GO_SOMEWHERE:
            return self._handler_new_saying()
        else:
            return 'its not yet programed'

