__author__ = 'huyheo'


import logging
from gluon import *


from obj_definition import *
from intent_def import *

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session

class go_to_place(object):
    """
    handle talk about place
    """
    def __init__(self, place):
        self.to_do_list = {TIME_INFO:'',
                           METHOD_TO_GO:''}
        self.expected_saying =None
        #intialize place object
        self.initialize_place_info(place)
        self.user = user_obj('huy')

    def initialize_user_info(self, user):
        """
        create user info
        """
        self.user = user_obj()

        pass

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
        self.expected_saying = session.expected_saying

    def create_response(self):
        """
        create question for AI
        """
        if self.to_do_list[TIME_INFO] == None:
            message = 'ask about time'
            session.time_to_go = message
            self.expected_saying = TIME_INFO
            session.expected_saying = self.expected_saying
            return message
        elif self.to_do_list[METHOD_TO_GO] ==None:
            message = 'ask method to go'
            session.by_what = message
            self.expected_saying =METHOD_TO_GO
            session.expected_saying = self.expected_saying
            return message
        else:
            return self._thinking_()

    def _handler_new_saying(self):
        question_msg = self.create_response()
        return question_msg

    def _handler_expected_saying(self, intention, value):
        self.to_do_list[self.expected_saying] = value
        #clear expected saying
        self.expected_saying = None
        session.expected_saying = None

        response_msg =  self.create_response()
        session.time_to_go = self.to_do_list[TIME_INFO]
        session.by_what = self.to_do_list[METHOD_TO_GO]
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
        if self.expected_saying == intention:
            if intention == TIME_INFO:
                value = entity['datetime'][0]['value']
            elif intention == METHOD_TO_GO:
                value = entity['method'][0]['value']

            msg = self._handler_expected_saying(intention, value)
        else:
            msg = self._handler_intention_of_question(intention)
        return msg

    def _handler_intention_of_question(self, intention):

        if intention == 'where_is_it':
            return self.place.where_is_it()
        elif intention == 'how_far_is_it':
            return self._calculate_distance_from_user()
        elif intention =='go_to_some_where':
            return self._handler_new_saying()
        else:
            return 'its not yet programed'

