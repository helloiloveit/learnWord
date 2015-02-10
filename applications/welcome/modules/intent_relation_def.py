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
    GREETING:[
        GREETING,
        EMOTIONAL_EXPRESSION
    ],
    ASK_AGE:[
        AGE_INFO
    ],
    ASK_JOB:[
        INTRODUCE_MYSELF
    ],
    None:None
}

topic_intent_dic = {
    USER_TOPIC:{
        'intent':[
            INTRODUCE_MYSELF
        ],
        'class': user_obj

    },
    JOB_TOPIC:{
        'intent':
            [
                ASK_JOB,
                ASK_WHY_LIKE,
                ASK_DURATION,
                ASK_TIME,
                ASK_IF_WANT_TO_DO_SMTH,
                ASK_IF_DOING_SMTH,
                INTRODUCE_MYSELF,
                ASK_OPINION_ABOUT_SOMETHING

            ],
        'class': job_obj
    },
    HOBBY_TOPIC:{
        'intent':
                [ASK_HOBBY,
                LIKE_SMTH],
        'class'  : hobby_obj
    },
    RUNNING_ACT: {
        'intent':[
                    ASK_HEALTH_STS,
                    ASK_DURATION,
                    ASK_DISTANCE,
                    ASK_WHY_LIKE,
                    ASK_HOW_TO_DO,
                    ASK_TIME
                 ],
        'class' : running_act
    },
    GREETING_ACT:{
        'intent':[
            GREETING,
            EMOTIONAL_EXPRESSION
        ],
        'class':greeting_obj
    },
    AGE_INFO:{
        'intent':[
            AGE_INFO

        ],
        'class':user_obj
    }
}


