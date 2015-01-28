__author__ = 'huyheo'


import logging
from gluon import *
from intent_def import *


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

class job_obj(object):
    def __init__(self, name):
        self.name = name
        #get information from somewhere
        if self.name == 'programmer':
            self.initialze_info(19, 10, 'ok')
        elif self.name == 'worker':
            self.initialze_info(7, 10, 'bad')



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
        self.work = job_obj(work)
        self.position = work
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
    def __init__(self):
        pass
    def check_if_good_or_bad(self, activity):
        return 'good'
class fun_obj(object):
    def __init__(self):
        pass
    def check_if_fun(self, activity):
        return 'fun'

class act_base(object):
    def __init__(self, name,
                 why_doing,
                 resouce_consuming,
                 impact_to_other):
        self.name = name
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




class waiting_act(act_base):
    """
    define action
    exp: waiting
    """
    def __init__(self,name):
        super(waiting_act,self).__init__(WAITING_ACT, [health_obj,fun_obj], ['energy', 'time'], '')
        self.target = 'bus'
        self.status = 'boring'
        self.motivation = 'go to to Hoan Kiem lake'
        self.have_time = 'yes'
        #necesssary thing
        self.time_arrive = ''
        self.how_long = ''
        self.seat_number = ''
        pass
    def need_smth(self):
        """
        return necessary thing that is missing
        """
        if self.time_arrive == '':
            return 'ask_time'
        else:
            return 'nothing'
    def get_intent(self):
        return self.name
    def get_target(self):
        return self.target

class running_act(act_base):
    """
    define action
    exp: waiting
    """
    def __init__(self):
        super(running_act,self).__init__('running', [health_obj,fun_obj], ['energy', 'time'], '')
        self.fun = 'fun or boring'
        self.have_time_for_other_thing = 'yes'
        self.distance = '20 km'
        self.timing = 'weekend'
        #necesssary thing
        self.place = ''
        self.time = ''
        self.weather = ''
    def need_smth(self):
        """
        return necessary thing that is missing
        """
        if self.time_arrive == '':
            return 'ask_time'
        else:
            return 'nothing'
    def get_distance(self):
        msg = 'i run ' + self.distance + ' in ' + self.timing
        return msg
    def why(self):
        msg = 'because it fun and good for health'
        return msg

    def duration_info(self):
        return '1 year'

    def reply(self,intent):
        if intent == ASK_DISTANCE:
            return self.get_distance()
        elif intent == ASK_WHY_LIKE:
            return self.why()
        elif intent == ASK_DURATION:
            return self.duration_info()
        return ''

    def suggest_time_to_do(self):
        return 'now'
    def suggest_thing_to_prepare(self):
        return 'decide place, time, check weather'

class hobby(object):
    def __init__(self):
        self.list = [running_act()]
    def get_by_name(self, name):
        for temp in self.list:
            if name in temp.get_name():
                return temp
        return ''
    def get_all(self):
        return self.list

class human_obj(user_obj):
    """
    simulate real people
    - state
    - activity
    """
    def __init__(self, name, activity_info):
        #super class
        super(human_obj, self).__init__(name)
        self.doing_now = waiting_act(activity_info)
        self.doing = [traveling_act(), working_act()]
        self.hobby = hobby()
        pass
    def get_doing_now_info(self):
        return self.doing_now.get_name()
    def get_doing_info(self):
        return self.doing




