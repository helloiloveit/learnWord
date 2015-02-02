__author__ = 'huyheo'


import logging
from gluon import *
from intent_def import *
from obj_definition import *


act_generator ={
    WORKING_ACT:working_act
}


expected_intent_gen = {
    ASK_HOBBY:LIKE_SMTH,
    ASK_DISTANCE: [
                    DISTANCE_INFO,
                    DOING_SMTH
                   ],
    ASK_TIME: [
        TIME_INFO,
        DOING_SMTH
    ],
    None:None
}

topic_intent_dic = {
    'hobby':{
        'intent':
                [ASK_HOBBY,
                LIKE_SMTH],
        'class'  : hobby
    },
    RUNNING_ACT: {
        'intent':[
                    ASK_DURATION,
                    ASK_DISTANCE,
                    ASK_WHY_LIKE,
                    ASK_HOW_TO_DO

                 ],
        'class' : running_act
    }
}


