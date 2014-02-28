# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

import json
import logging

log = logging.getLogger("h")
log.setLevel(logging.DEBUG)

from ConstantDefinition import *
try:
    import json
except ImportError:
    from gluon.contrib import simplejson as json
from facebook import GraphAPI, GraphAPIError
from gluon.contrib.login_methods.oauth20_account import OAuthAccount




def convert_record_list_to_list(record_list):
    temp_list = []
    for unit in record_list:
        temp_list.append(unit.word)
    return temp_list

def get_list_of_similar_word():
    word_list = db(db.word_tbl).select()
    word_list = convert_record_list_to_list(word_list)
    print word_list

    month_start = request.vars.word_info
    print 'word = '
    print month_start
    print' month start'
    print month_start
    selected = [m for m in word_list if m.startswith(month_start)]
    print' result'
    print selected
    return selected

def word_validation():
    if not request.vars.word_info: return ''
    selected = get_list_of_similar_word()
    #save word to session
    session.word_store = request.vars.word_info


    return DIV(*[DIV(k,
                     _onclick="jQuery('#word').val('%s')" % k,
                     _onmouseover="this.style.backgroundColor='yellow'",
                     _onmouseout="this.style.backgroundColor='white'"
                     ) for k in selected])



def user():
    return dict(form = auth())

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    #redirect(URL(r = request, f= 'blog', args = 3))
    user = auth.user
    print user
    return dict()



def get_word():

    """
    get word to display to user
    """

    word_list = db(db.word_tbl).select()
    print word_list


    return_word = select_word_to_display(word_list)

    #store word id to session.
    session.display_word_id = return_word.id

    return dict(item = return_word.word)


def select_word_to_display(word_list):
    from random import choice
    temp_vaar = choice(word_list)
    return temp_vaar




@auth.requires_login()
def post():
    log.info("request.vars = %s",request.vars)
    #save example for later store in database
    session.tag_list_store = []
    session.example_list_store = []

    return dict(article_tag_list ="" )


@auth.requires_login()
def add_word():
    log.info("add new word")
    log.info("request.vars = %s",request.vars.sheets)
    result = json.loads(request.vars.sheets)
    print 'result after json'
    print result
    print len(result)

    #import pdb;pdb.set_trace()
    word_id = add_word_to_db()
    add_example_to_db(word_id, result)
    #import pdb;pdb.set_trace()
    #return json.dumps(request.vars.tag_info)
    temp_var = 'lalal'
    return "var x=$('#target'); x.html(x.html()+ '%s');" % temp_var

@auth.requires_login()
def post_example():
    log.info("post_example")
    log.info("request.vars = %s",request.vars.example_sentence)

    session.example_list_store.append(request.vars.example_sentence)
    log.info("session.tag list = %s", session.example_list_store)
    #return json.dumps(request.vars.tag_info)
    return "var x=$('#example_added'); x.html(x.html()+'<br>' + '%s' );" % request.vars.example_sentence.replace("'","\\'")

### add word
def add_example_to_db(word_id, example):
    log.info("add example to db")
    print example
    #import pdb;pdb.set_trace()
    log.info("len of example list = %d", len(example))
    if type(example) is list:
        for unit in example:
            if len(unit) !=0:
                example_id = db.example_tbl.insert(example = unit,
                                       word_id = word_id)
    else:
        if len(example) != 0:
            example_id = db.example_tbl.insert(example = example,
                                       word_id = word_id)
    #import pdb;pdb.set_trace()

def add_word_to_db():
    log.info("add word to db")
    #import pdb;pdb.set_trace()
    #print auth.user.id
    word_id = db.word_tbl.insert(word = session.word_store,
                                 user_info = auth.user)
    return word_id


