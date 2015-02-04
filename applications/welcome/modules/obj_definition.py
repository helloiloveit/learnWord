__author__ = 'huyheo'


import logging
from gluon import *
from intent_def import *
from utility import *
from base_handler import *
log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

session = current.session
class place_obj(object):
    def __init__(self, place):
        """
        define place, destination
        load from db
        """
        self.intialize_info_from__name(place, '','','')

    def get_position(self):
        return self.position
    def where_is_it(self):
        return self.position

    def intialize_info_from__name(self, name, position, size, access_time):
        """
        should generate this infor from db or internet db
        """
        self.what_for ='work'
        self.position = 'van dien'
        self.size = 'big'
        self.name = name


    def access_method(self):
        return 'bike, car'
    def access_time(self):
        return '8-12AM, 13-17 PM'



class obj_intent_base(object):
    def __init__(self):
        pass

    def handler(self, json_data):
        intent = ai_json(json_data).get_intent(0)
        dic_info = self.answer_topic[intent]
        msg = dic_info['handler'](json_data)
        data = data_format.saying(msg, dic_info['intent'], dic_info['topic'])
        return data





class job_obj(obj_intent_base):
    def __init__(self, name):
        self.name = name
        #get information from somewhere
        if self.name == 'programmer':
            self.initialze_info(19, 10, 'ok')
        elif self.name == 'worker':
            self.initialze_info(7, 10, 'bad')

        self.answer_topic = {
            ASK_JOB:{'handler':self.what_is, 'intent': IT_IS_SMTH, 'topic':JOB_TOPIC}
        }

    def what_is(self, json_data):
        msg =  self.name
        return msg

    def initialze_info(self, salary, working_hour, social_status):
        self.salary =salary
        self.working_hour =working_hour
        self.social_status =social_status
    def get_name(self):
        return self.name



class user_obj(object):
    def __init__(self, name):
        # load from DB
        if name =='huy':
            self.intialize_info(name, '33', 'programmer', 'ho dac di')
        elif name =='ai':
            self.intialize_info(name, '1', 'worker', 'ho dac di')
        else:
            pass


    def intialize_info(self, name, age, work, position):
        self.name = name
        self.age = age
        if work:
            self.work = job_obj(work)
        else:
            self.work = None
        self.position = position
        pass
    def get_position(self):
        return self.position
    def get_age(self):
        return self.age + ' years old'
    def get_name(self):
        return self.name
    def get_job(self):
        return self.work


    def get_available_time(self):
        return '1 2 3 4 5 6 7 8 9 10'

    def give_opinion(self, target):
        """
        this user will use its own criteria to decide
        """
        if  target.__class__.__name__ =='job_obj':
            if target.salary > 20:
                return 'this job is good'
            elif target.salary <=10:
                return 'this job is terrible'
            else:
                return 'this job is ok'

class health_obj(object):
    def __init__(self, name):
        if name == RUNNING_ACT:
            self.status = 'good'
        else:
            self.status = 'unknown'
    def get_status(self ):
        msg = 'it is ' + self.status + ' for health'
        return msg

    def handler(self, json_data):
        data = ''
        intent = ai_json(json_data).get_intent(0)
        if intent == ASK_HEALTH_STS:
            msg = self.get_status()
            data = data_format.saying(msg, ADJECTIVE_INFO, HEALTH_OBJ)
        return data




class distance_obj(object):
    def __init__(self, name):
        """
        init according to name of object
        """
        self.distance = ''
        self.average = ''
        if name == RUNNING_ACT:
            self.average = 5
    def get_value(self):
        return self.distance
    def set_value(self, value):
        self.distance = value

    def handler(self, json_data):
        msg = self.distance
        data = data_format.saying(msg, DISTANCE_INFO, RUNNING_ACT)
        return data

class greeting_obj(object):
    def __init__(self, name):
        self.answer_topic = {
            GREETING:{'handler':self.reply, 'intent': GREETING, 'topic':GREETING_ACT},
            EMOTIONAL_EXPRESSION:{'handler':self.reply_emotional, 'intent': GREETING, 'topic':GREETING_ACT},
        }
        self.load_db()

    def load_db(self):
        self.greeting_flag = session.greeting_flag
        self.ask_topic =[
            {'value':self.greeting_flag, 'handler':self.ask_greeting, 'intent':GREETING, 'topic':GREETING_ACT}
        ]

    def save_db(self, greeting):
        session.greeting_flag = greeting
        self.load_db()
    def reply_emotional(self, json_data):
        info = ai_json(json_data).get_entity(FEELING)
        msg ='great'
        if info == 'happy':
            msg = 'great'
        elif info == 'bad':
            msg = 'sorry to know that'
        self.save_db(True)
        return msg
    def reply(self, json_data):
        msg = 'hello'
        level = ai_json(json_data).get_entity(GREETING_LEVEL)
        activity_info =ai_json(json_data).get_entity(ACTIVITY_INFO)
        if level or activity_info:
            msg = 'im doing very well'
        return msg

    def ask_greeting(self):
        msg ='And you. How are u doing?'
        return msg

    def handler(self, json_data):
        intent = ai_json(json_data).get_intent(0)
        dic_info = self.answer_topic[intent]
        msg = dic_info['handler'](json_data)
        data = data_format.saying(msg, dic_info['intent'], dic_info['topic'])
        return data
        pass
    def ask(self):
        data = ''
        for dic_info in self.ask_topic:
            if not dic_info['value']:
                msg = dic_info['handler']()
                data = data_format.saying(msg, dic_info['intent'], dic_info['topic'])
                return data


        return data

class fun_obj(object):
    def __init__(self):
        pass
    def check_if_fun(self, activity):
        return 'fun'

class act_base(object):
    """
    base info for an activity
    """
    def __init__(self, name,
                 why_doing,
                 resouce_consuming,
                 impact_to_other):
        self.name = name
        self.start_time =''
        self.end_time =''
        self.happening = ''
        self.motivation = why_doing
        self.resource_consuming  = resouce_consuming,
        self.impact_to_other = impact_to_other
    def get_name(self):
        return self.name
    def reply_info(self,intent):
        pass

    def reply(self, intent):
        if intent == ASK_DURATION:
            return self.duration_info()
        return ''

class traveling_act(act_base):
    def __init__(self):
        super(traveling_act,self).__init__('travel', ['grow up','explore'], ['money', 'time'], '')
        #necessary thing
        #load and save to db
        self.start_time = 'last month'
        self.end_time = 'next month'
        self.resource = ['money','time']
    def duration_info(self):
        msg = '9 months'
        return msg

class working_act(act_base):
    """

    """
    def __init__(self):
        super(working_act, self).__init__('working', ['earn a living'], ['time'], '')
        pass
    def duration_info(self):
        msg = '1 year'
        return msg

class reading_act(act_base):
    def __init__(self,name):
        super(reading_act,self).__init__(READING_ACT, [health_obj,fun_obj], ['energy', 'time'], '')


class bus(object):
    """
    simulate a bus
    """
    def __init__(self, name):
        self.name = name
        # load infor from db if existed
        self.arrive_at_destination_time= ''
        self.depart_from_station_time = ''
        self.arrive_at_destination_time =''
    def get_arrive_at_station_time(self, position):
        return ''
    def get_duration_of_arrival_time(self):
        return '10 min'
    def get_depart_from_station_time(self):
        return 'after 10 min'
    def ask_arrive_at_station_time(self):
        return 'Could you tell me when will the bus arrive?'

class waiting_act(act_base):
    """
    define action
    exp: waiting
    """
    def __init__(self,name):
        super(waiting_act,self).__init__(WAITING_ACT, [fun_obj], ['energy', 'time'], '')
        self.waiting_for = bus('bus name')
        self.status = 'boring'
        #necesssary thing
        self.arrive_at_station_time = self.waiting_for.get_arrive_at_station_time('')
        self.depart_from_station_time =self.waiting_for.get_depart_from_station_time()
        self.importance_thing =[self.arrive_at_station_time]
        self.not_importance = [self.depart_from_station_time]
    def need_smth(self):
        """
        return necessary thing that is missing
        """
        return 'ask_time'
    def say_smth(self):
        msg =''
        for temp in self.importance_thing:
            if temp == '':
                msg = self.waiting_for.ask_arrive_at_station_time()
                return msg
        return ''


    def get_intent(self):
        return self.name
    def get_target(self):
        return self.target

class timming_obj(object):
    """
    handle time info for act
    """
    def __init__(self):
        self.start =''
        self.end =''
        self.repeat=''
        self.answer_topic = {

        }
    def handler(self, json_data):
        intent = ai_json(json_data).get_intent(0)
        if intent == ASK_TIME:
            msg = 'i run in' + self.timing
        pass


class running_act(act_base):
    """
    define action
    exp: waiting
    """
    def __init__(self, name):
        super(running_act,self).__init__(RUNNING_ACT, [health_obj,fun_obj], ['energy', 'time'], '')
        self.user_name = name
        self.health_sts = health_obj(RUNNING_ACT)
        self.answer_topic = {
            #maybe same to every action
            ASK_HEALTH_STS:{'handler':self.health_sts},


            #end same
            ASK_DISTANCE:{'handler': self.get_distance, 'intent':DISTANCE_INFO, 'topic':RUNNING_ACT},
            ASK_WHY_LIKE:{'handler': self.why, 'intent':MOTIVATION_INFO, 'topic': RUNNING_ACT},
            ASK_DURATION:{'handler': self.duration_info, 'intent':DURATION_INFO,'topic':RUNNING_ACT},
            ASK_HOW_TO_DO:{'handler':self.how_to_do, 'intent':PRACTISE_INFO, 'topic':RUNNING_ACT},
            DISTANCE_INFO:{'handler':self.receive_distance, 'intent': COMPLIMENT, 'topic':RUNNING_ACT},
            DOING_SMTH:{'handler':self.doing_smth, 'intent': COMPLIMENT, 'topic':RUNNING_ACT},
            ASK_TIME:{'handler':self.get_time, 'intent': TIME_INFO, 'topic':RUNNING_ACT},
            TIME_INFO:{'handler':self.receive_time, 'intent': DATETIME, 'topic':RUNNING_ACT}

        }

        self.load_db(name)
    def load_db(self, user_name):
        if user_name == 'ai':
            self.distance = '20 km'
            self.timing = 'weekend'
            self.start_time = '2 years'
        else:
            self.distance = session.distance_info
            self.timing = session.timing_info
            self.start_time = session.start_time
        self.ask_topic =[
            {'value':self.distance, 'handler':self.ask_distance, 'intent':ASK_DISTANCE, 'topic':RUNNING_ACT},
            {'value':self.timing, 'handler':self.ask_timing, 'intent':ASK_TIME, 'topic':RUNNING_ACT},
            {'value':self.start_time, 'handler':self.ask_start_time, 'intent':ASK_TIME, 'topic':RUNNING_ACT}

        ]
    def save_db(self, distance, time_info , start_time):
        if distance:
            session.distance_info = distance
        if time_info:
            session.timing_info = time_info
        if start_time:
            self.start_time = start_time
        self.load_db(self.user_name)
    def need_smth(self):
        """
        return necessary thing that is missing
        """
        if self.time_arrive == '':
            return 'ask_time'
        else:
            return 'nothing'

    def receive_distance(self, json_data):
        msg = 'nice'
        distance_info = ai_json(json_data).get_entity(DISTANCE)
        self.save_db(distance_info,'','')
        return msg
    def doing_smth(self, json_data):
        msg = 'nice'
        datetime = ai_json(json_data).get_entity(DATETIME)
        self.save_db('', datetime,'')
        return msg

    def how_to_do(self, json_data):
        msg = 'i practice it every week'
        return msg
    def get_distance(self, json_data):
        msg = 'i run ' + self.distance + ' in ' + self.timing
        return msg
    def get_time(self,json_data):
        start_stop_info = ai_json(json_data).get_entity(START_STOP_INFO)
        if start_stop_info:
            msg = 'i started running ' + self.start_time + ' ago'
            return msg
        msg = 'i run in ' + self.timing
        return msg
    def receive_time(self,json_data):
        msg = 'nice'
        start_time = ai_json(json_data).get_entity(DATETIME)
        session.start_time = start_time
        self.save_db('','',start_time)
        return msg

    def why(self, json_data):
        msg = 'because it fun and good for health'
        return msg
    def duration_info(self, json_data):
        msg =  '1 year'
        return msg
    def ask_distance(self):
        return 'how long do you run'
    def ask_timing(self):
        return 'when do you run'
    def ask_start_time(self):
        return 'when did you start running'
    ###############
    def handler(self,json_data):
        intent = ai_json(json_data).get_intent(0)
        dic_info = self.answer_topic[intent]
        if intent == ASK_HEALTH_STS:
            data = dic_info['handler'].handler(json_data)
            return data

        msg = dic_info['handler'](json_data)
        data = data_format.saying(msg, dic_info['intent'], dic_info['topic'])
        return data
    def ask(self):
        data = ''
        for dic_info in self.ask_topic:
            if not dic_info['value']:
                msg = dic_info['handler']()
                data = data_format.saying(msg, dic_info['intent'], dic_info['topic'])
                return data


        return data



class hobby(object):
    def __init__(self,name):
        self.name = name
        self.load_db(name)
        self.answer_topic = {
            ASK_HOBBY: self.introduce,
            LIKE_SMTH: self.ans_like_smth
        }
        self.load_db(name)

    def save_to_db(self, act):
        session.user_act = [act]
        self.load_db(self.name)
    def load_db(self, name):
        if name == 'ai':
            self.list = [running_act(name)]
        else:
            self.list = session.user_act
    def ans_like_smth(self,json_data):
        """
        save answer of hobby to db
        say smth to answer
        """
        activity_info = ai_json(json_data).get_entity(ACTIVITY_INFO)

        msg = 'nice'
        self.save_to_db(activity_info)
        data = data_format.saying(msg, COMPLIMENT, WORKING_ACT)

        return data
    def get_by_name(self, name):
        for temp in self.list:
            if name in temp.get_name():
                return temp
        return ''
    def get_all(self):
        return self.list
    def introduce(self, json_data):
        if not len(self.list):
            message = 'Sorry i dont know yet'
            topic = 'hobby'
        else:
            if self.name == 'huy':
                message =  'you like' + ' ' + self.list[0].get_name()
            elif self.name == 'ai':
                message =  'i like' + ' ' + self.list[0].get_name()
            topic = self.list[0].get_name()
        data = data_format.saying(message, LIKE_SMTH, topic)
        return data
    def ask_hobby(self):
        return 'what is your hobby?'
    def ask(self):
        data = ''
        if not self.list:
            msg = self.ask_hobby()
            data = data_format.saying(msg, ASK_HOBBY, 'hobby')
        return data
    def handler(self, json_data):
        intent = ai_json(json_data).get_intent(0)
        msg = self.answer_topic[intent](json_data)
        return msg

class human_obj(user_obj):
    """
    simulate real people
    - state
    - activity
    """
    def __init__(self, name ,act_name):
        #super class
        super(human_obj, self).__init__(name)
        self.doing_now = waiting_act(act_name)
        self.doing = [traveling_act(), working_act()]
        self.hobby = hobby(name)
        self.answer_topic = {
            ASK_WHAT_ARE_U_DOING: self.what_are_u_doing
        }
        pass
    def get_doing_now(self):
        return self.doing_now
    def get_doing_now_info(self):
        return self.doing_now.get_name()
    def get_doing_info(self):
        return self.doing
    def what_are_u_doing(self, json_data):
        msg = 'im waiting.'
        data = data_format.saying(msg, DOING_SMTH, 'doing')
        return data
    def handler(self, json_data):
        intent = ai_json(json_data).get_intent(0)
        msg = self.answer_topic[intent](json_data)
        return msg





