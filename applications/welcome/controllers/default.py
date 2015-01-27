# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

from topic_handler import *
from intent_def import *

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    redirect(URL('talk'))
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())



def talk():
    print'start'
    #initialize session storage info

    return dict()

def test_STT():
    return dict()






def handle_user_saying_json():
    """

    """
    if not session.topic_list:
        session.topic_list =[]

    import json
    data = request.vars.keys()[0]
    json_data = json.loads(data)
    msg = handle_topic_data(json_data)
    return msg


def handle_topic_data(json_data):
    """
    - check if user start new topic
    - check if user still talk about same topic
    """
    intent = json_data['outcomes'][0]['intent']
    """
    if session.expected_saying == intent:
        #get last topic handler
        #handle old topic
        msg = handle_intent(session.topic_list[-1], json_data)
        pass
    else:
        #new topic
        clear_session_info()
        msg = handle_intent(intent, json_data)
    """
    msg = handle_intent(intent, json_data)

    return msg


def handle_intent(intent, json_data):
    """
    handle ajax call from user
    need a better algorithm for handle too many case
    Exp: When talk about smth...only some intent are epxected . So it will requires less computing power
    """
    if session.scenario_flag == True:
        """
        correct AI information should be initialized here
        """
        human_object = human_obj('ai')
    if intent == TO_GO_SOMEWHERE:
        msg = handler_go_to_some_where(json_data)
    elif intent == ASK_AGE:
        msg = handler_talk_about_user(json_data)
    elif intent == ASK_NAME:
        msg = handler_talk_about_user(json_data)
    elif intent == ASK_JOB:
        msg = handler_talk_about_user(json_data)
    elif intent == ASK_OPINION_ABOUT_SOMETHING:
        #msg = handler_talk_about_user(json_data)
        msg = ask_opinion_about_sth(json_data).return_msg()
    elif intent == GREETING:
        msg = greeting_handler(json_data).return_msg()
    elif intent == OFFER_HELP:
        msg = receive_offer_help_handler(json_data).return_msg()
    elif intent == TIME_INFO:
        msg = time_info_handler(json_data).return_msg()
    elif intent == INTRODUCE_MYSELF:
        msg = introduce_myself_handler(json_data).return_msg()
    elif intent == ASK_DURATION:
        msg = ask_duration_handler(json_data).return_msg()
    elif intent == ASK_CONTACT_INFO:
        msg = ask_contact_info_handler(json_data).return_msg()
    elif intent == ASK_WHAT_ARE_U_DOING:
        msg = ask_what_are_u_doing_handler(json_data).return_msg()
    elif intent == ASK_WHAT_TO_DO:
        msg = 'no idea'
    elif intent == ASK_HOBBY:
        msg = ask_hobby_handler(json_data).return_msg()
    elif intent ==  DONT_NO:
        msg = 'thanks'

    #personal assistant
    elif intent == ASK_WHAT_SHOULD_I_DO:
        msg = ask_advice(json_data).return_msg()
    elif intent == ASK_WHY:
        msg = 'youre productive and creative at the airport'

    else:
        msg = get_answer(json_data['outcomes'][0]['intent'])


    #session.topic_list.append(intent)
    return msg

def handle_user_saying():
    return get_asnwer(request.vars.info)



def get_answer(intention):
    if 'ask_name' in intention:
        return 'im Huy'
    elif 'ask_relationship' in intention:
        return 'im not. But i have a girl friend now'
    elif 'ask_if_someone_have_a_meal' in  intention:
        return 'im looking forward to my delicious dinner'
    elif 'ask_when_have_a_meal' in intention:
        return 'i cant remember'
    elif 'ask_job' in intention:
        return " i'm a software engineer"
    elif 'ask_company' in intention:
        return "im working for vkx company"

    return 'Sorry, currently i could talk about my job, my age only'
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)








def clear_session_info():
    session.time_to_go = None
    session.by_what = None
    session.expected_saying = None

def handler_go_to_some_where(json_data):
    intent = json_data['outcomes'][0]['intent']
    entity = json_data['outcomes'][0]['entities']
    value =''
    if intent != TO_GO_SOMEWHERE:
        # different intent in topic go_to_somewhere
        handler = go_to_place(session.place)
    else:
        # new request about place
        place = entity['target_place'][0]['value']
        handler = go_to_place(place)
    question = handler.handle_user_saying(intent,entity)
    return question

def handler_talk_about_user( json_data):
    intent = json_data['outcomes'][0]['intent']
    handler = talk_about_people('huy')
    msg = handler.handler_user_saying(intent)

    return msg


def ask_and_get_answer(question):
    if question =='ask about time':
        return '3AM'
    elif question =='ask method to go':
        return 'bike'

def handler_user_answer(answer):
    if answer =='3AM':
        intention ='time'
        value ='3AM'
        handler = go_to_place('')
        handler.handle_user_saying(intention,value)
    elif answer =='bike':
        intention = 'vehicle'
        value = 'bike'
        handler = go_to_place('')
        handler.handle_user_saying(intention,value)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
