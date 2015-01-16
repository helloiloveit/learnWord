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





class user_obj(object):
    def __init__(self, name):
        # load from DB
        if name =='huy':
            self.intialize_info('huy', '33', 'programming', 'ho dac di')

    def intialize_info(self, name, age, work, position):
        self.name = name
        self.age = age
        self.work = work
        self.position = work
        pass
    def get_position(self):
        return self.position
    def get_age(self):
        return self.age

    def get_available_time(self):
        return '1 2 3 4 5 6 7 8 9 10'


