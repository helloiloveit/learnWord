__author__ = 'huyheo'


import logging
from gluon import *


from base_handler import *

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session


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

class greeting_handler(base_intent_handler):
    def __init__(self, json_data):
        super(greeting_handler, self).__init__(json_data)
    def return_msg(self):
        reply_msg = 'hello'
        msg = reply_msg+ '. ' + 'how are you'
        return msg



class generate_msg_to_say(object):
    def __init__(self, intent):
        """
        intent data = {'intent':'','entity':'','value':''}
        """
        self.intent_data = intent
        #save to session
    def msg(self):
        total_msg = ''
        for data in self.intent_data:
            intent = data['intent']
            if intent == ASK_TIME:
                msg = 'could u help me to know the time the bus arrive?'
            elif intent == SAY_THANK:
                msg = 'thank you.'
            elif intent == INTRODUCE_MYSELF:
                msg = 'Im John.'
            elif intent == NICE_TO_MEET_YOU:
                msg = 'Nice to meet you.'
            elif intent == TIME_INFO:
                msg = data['value']+'.'
            elif intent == STOP_CONVERSATION:
                msg = 'So i have to go see u soon'
            elif intent == READING_ACT:
                msg = 'im reading a travel guide book'
            elif intent == WAITING_ACT:
                msg = 'im waiting'
            elif intent == WORKING_ACT:
                msg = 'lets do some work sir'
            else:
                msg = 'dont know what to say with this purpose'
            total_msg += msg
        return total_msg

class ask_how_to_do_handler(base_intent_handler):
    def __init__(self, json_data):
        super(ask_how_to_do_handler, self).__init__(json_data)
    def return_msg(self):
        msg = self.__class__
        return msg

class ask_distance_handler(base_intent_handler):
    def __init__(self, json_data):
        super(ask_distance_handler, self).__init__(json_data)
        self.target_name = ai_json(json_data).get_entity(ACTIVITY_INFO)
        temp= self.streamlize_name(self.target_name)
        self.topic_handler = running_act
    def streamlize_name(self, name):
        if name in RUNNING_ACT:
            return RUNNING_ACT
    def generate_intent(self):
        pass
    def return_msg(self):
        msg  = self.topic_handler().handler(self.json_data)
        return msg

class ask_why_like_handler(base_intent_handler):
    def __init__(self, json_data):
        super(ask_why_like_handler, self).__init__(json_data)
        self.activity_info = self.entity[ACTIVITY_INFO][0]['value']
        self.topic_handler = running_act
        # should search for this activity info in db
    def return_msg(self):
        msg  = self.topic_handler().handler(self.json_data)
        return msg




class ask_hobby_handler(base_intent_handler):
    def __init__(self, base_json):
        super(ask_hobby_handler, self).__init__(base_json)
    def return_msg(self):
        contact_info = ai_json(self.json_data).get_entity(CONTACT_TYPE)
        if contact_info in ['my', 'mine']:
            hobby = self.user.hobby
        else:
            hobby = self.me.hobby
        reply = hobby.handler(self.json_data)
        memory_handler().save_to_short_memory(ANSWER_FLAG, 'ai',self.json_data, reply)
        ask = self.user.hobby.ask()
        memory_handler().save_to_short_memory(ASK_FLAG, 'huy',self.json_data, ask)
        saying = reply['saying'] + '. ' + ask['saying']
        #set expected intent
        return saying



class ask_opinion_about_sth(base_intent_handler):
    def __init__(self, json_data):
        super(ask_opinion_about_sth, self).__init__(json_data)
        self.target = self.get_target_info()
        pass

    def get_target_info(self):
        """
        - get target infor from json_data
        - handle it
        """
        target_name = self.entity[TARGET_NAME][0]['value']
        if target_name == IT_SUBJECT:
            # load the last topic to decide the subject
            return user_factory().user().get_job()
        else:
            return user_factory().user().get_job()


    def return_msg(self):
        msg = self.me.give_opinion(self.target)
        return msg

class receive_offer_help_handler(base_intent_handler):
    def __init__(self, base_json):
        super(receive_offer_help_handler, self).__init__(base_json)
        pass
    def generate_intent(self):
        new_intent =  self.me.doing_now.need_smth()
        data = [{'intent':new_intent,'entity':''}]
        return data

    def return_msg(self):
        """
        return mssage by call need_smth() of user activity
        """
        new_intent = self.generate_intent()
        memory_handler().set_last_intent(new_intent)
        msg = generate_msg_to_say(new_intent).msg()
        return msg
class like_smth_handler(base_intent_handler):
    def __init__(self, base_json):
        super(like_smth_handler, self).__init__(base_json)
    def return_msg(self):
        """
        get object of liking
        save info to db
        """
        act_name = ai_json(self.json_data).get_entity(ACTIVITY_INFO)
        response = self.user.hobby.response_to_msg(self.intent)
        new_msg = self.user.hobby.make_new()
        msg = 'really?'

        return msg

class ask_what_are_u_doing_handler(base_intent_handler):
    def __init__(self, base_json):
        super(ask_what_are_u_doing_handler, self).__init__(base_json)
    def generate_intent(self):
        return data
    def return_msg(self):
        reply_msg = self.me.handler(self.json_data)
        msg = reply_msg['saying']
        return msg

class emotional_expression(base_intent_handler):
    def __init__(self, base_json):
        super(emotional_expression, self).__init__(base_json)
    def return_msg(self):
        return 'good to know your emotional state'

class time_info_handler(base_intent_handler):
    def __init__(self, base_json):
        """
        get previous sentence to know why user give time
        """
        self.intent = TIME_INFO
        pass

    def generate_intent(self):
        """
        should have some algorithm here to decide new intent
        """
        data = [
                {'intent':SAY_THANK,'entity':''},
                {'intent':INTRODUCE_MYSELF,'entity':''},
                {'intent':NICE_TO_MEET_YOU,'entity':''}
                ]
        return data

    def return_msg(self):
        new_intent = self.generate_intent()
        memory_handler().set_last_intent(new_intent)
        msg = generate_msg_to_say(new_intent).msg()
        return msg

class introduce_myself_handler(base_intent_handler):
    def __init__(self, base_json):
        self.base_json = base_json
        self.target_name = ai_json(base_json).get_entity( NAME_INFO)

    def generate_intent(self):
        data = [{'intent':NICE_TO_MEET_YOU,'entity':''}]
        return data

    def return_msg(self):
        new_intent = self.generate_intent()
        memory_handler().set_last_intent(new_intent)
        msg = generate_msg_to_say(new_intent).msg()
        return msg

class ask_advice(base_intent_handler):
    def __init__(self, base_json):
        self.base_json= base_json
        pass

    def generate_intent(self):
        """
        call ai_brain to think
        """
        data = [
            {'intent': WORKING_ACT, 'entity':''},
        ]
        return data

    def return_msg(self):
        new_intent = self.generate_intent()
        memory_handler().set_last_intent(new_intent)
        msg = generate_msg_to_say(new_intent).msg()
        return msg

class ask_duration_handler(base_intent_handler):
    def __init__(self, base_json):
        super(ask_duration_handler, self).__init__(base_json)
        self.target_name = ai_json(self.json_data).get_entity(TARGET_NAME)
        self.activity_info = ai_json(self.json_data).get_entity(ACTIVITY_INFO)
    def generate_intent(self):
        if  self.me.get_doing_now_info() in self.activity_info:
            msg = self.me.doing_now.reply(self.intent)
        for act in self.me.get_doing_info():
            if act.get_name() in self.activity_info:
                msg = act.reply(self.intent)
        for act in self.me.hobby.get_all():
            if act.get_name() in self.activity_info:
                msg = act.handler(self.json_data)
        return msg
    def return_msg(self):
        time = '9 months'
        msg = self.generate_intent()
        memory_handler().set_last_intent(self.json_data)
        return msg

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

