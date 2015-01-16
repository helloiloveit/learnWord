__author__ = 'huyheo'


import logging
from gluon import *


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
    def get_opinion(self):
        if self.salary > 20:
            return 'this job is good'
        elif self.salary <=10:
            return 'this job is terrible'
        else:
            return 'this job is ok'



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
        return self.work.get_name()


    def get_available_time(self):
        return '1 2 3 4 5 6 7 8 9 10'


