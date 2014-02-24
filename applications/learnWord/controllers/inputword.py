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

def post_question():
    data_group = [{'type':'now',"data":""},{'type':'future',"data":""}]
    return json.dumps(data_group)




def article():
    """
    Display blog by id
    """
    log.info("request.vars = %s", request.args[0])
    log.info("request.vars = %s",request.vars)



    if request.args[0] == 'post_comment':
        log.info('post a comment')
        post_comment(request.vars.questionId, request.vars.editor1, auth.user.id)
        redirect(URL(r = request, f= 'article', args = request.vars.questionId))

    else:
        log.info('show article with comment')
        log.info('id = %s', request.args[0])

        try:
            question = db(db.question_tbl.id == int(request.args[0])).select()[0]
        except:
            log.error('cant query a blog from db')
            question = None
        comment_list = show_question(request.args[0])

        return dict(item = question, comment_list = comment_list)


def show_question(question_id):

    comment_list = db(db.comment_tbl.question_info == question_id).select()
    return  comment_list


def post_comment(question_id, comment_info, user_id):
    log.info("post_comment")

    log.info("session.user = %s", auth.user)
    log.info("auth.user.id = %s", user_id)



    try:
        comment_id = db.comment_tbl.insert(comment_info = comment_info,
                                question_info = question_id,
                                author_info = user_id
                                )
        log.info('successfully create a comment_tbl')


    except:
        log.error('cant create comment_tbl')


@auth.requires_login()
def edit_article():
    """
    Edit blog
    """
    log.info("edit artchile")
    log.info("request.vars 0= %s", request.args[0])
    log.info("request.vars = %s", request.args)
    id_info = request.args[0]

    article_class_list = db(db.article_tag).select()
    log.info("article_class = %s", article_class_list)

    try:
        blog_item = db(db.blog.id == int(id_info)).select()[0]
    except:
        log.error('cant query a blog from db')
        blog_item = None



    if request.vars.editor1:
        article_id = get_article_id(request.vars.article_class)
        log.info("article-id = %s", article_id)
        id =db(db.blog.id == int(request.args[0])).update(
            article_type = article_id,
            article_header = request.vars.article_header,
            article_introduction = request.vars.article_introduction,
            story = request.vars.editor1
        )
        redirect(URL(r = request, f= 'article', args = [request.args[0]]))

    log.info("blog_item = %s",blog_item)
    return dict(article = blog_item, article_class_list = article_class_list)

        
def delete_article():
    selection = request.vars
    log.info('selection = %s', selection['selection'])
    log.info('id = %s', request.args[0])
    id_info = request.args[0]
    if selection['selection'] == "YES":
        log.info("delete post")
        db(db.question_tbl.id == int(request.args[0])).delete()
        redirect(URL(r = request, f= 'article_list'))
    elif selection['selection'] == "NO":
        redirect(URL(r = request, f= 'article', args = [request.args[0]]))
    return dict()

#@auth.requires_login()
#@auth.requires_login()
def check_example():
    log.info("post_example")
    """
    months = ['There is now a mood of deepening pessimism about/over the economy',
              'An underlying pessimism infuses all her novels',
              'An underlying pessimism infuses all her novels',
              'The tone of the meeting was very pessimistic',
              'The doctors are pessimistic (= not hopeful) about his chances of recovery']
    """
    log.info("request.vars = %s",request.vars)

    try:
        select_option = request.vars["meanning_option"]
    except:
        select_option = 'option3'
        log.error("no select option..user hasnt click on option ")
        #return "var x=$('#word_meanning_explain_1'); x.html('');"

    print session.display_word_id
    example_list = db(db.example_tbl.word_id == session.display_word_id).select()
    print example_list
    example = select_example_to_display(example_list)
    #import pdb;pdb.set_trace()
    print example
    select_option = check_display_position(select_option)
    print select_option
    #return json.dumps(request.vars.tag_info)
    if select_option == "option1":
        id_info = "word_meanning_explain_1"
        return "var x=$('#word_meanning_explain_1'); x.html('%s');" % example.replace("'","\\'")
    elif select_option =="option2":
        id_info = "word_meanning_explain_2"
        return "var x=$('#word_meanning_explain_2'); x.html('%s');" % example.replace("'","\\'")

    #return "var x=$('#word_meanning_explain_1'); x.html('%s');" % example.replace("'","\\'")

def check_display_position(select_option):
    if select_option == "option1" or select_option == "option2":
        return select_option
    else:
        #update for correct position later
        return "option1"

def select_example_to_display(example_list):
    from random import choice
    temp_vaar = choice(example_list)
    return temp_vaar.example

def word_meanning_for_test():
    word_meanning_info1 = "the amount of space between two places"
    word_meanning_info2 = "a person or organization that supplies goods to shops and companies"
    return [word_meanning_info1, word_meanning_info2]
#@auth.requires_login()
def next_word():
    log.info("post_example")
    months = ['Distance',
              'infuses ',
              ' underlying ',
              ' pessimistic',
              ' doctors ']

    return_word = select_next_word_to_display()
    #return json.dumps(request.vars.tag_info)
    test_list = word_meanning_for_test()
    print test_list
    return "var x=$('#word_info'); x.html('%s'); var x2=$('#word_meanning_explain_1'); x2.html('%s');  var x3=$('#word_meanning_explain_2'); x3.html('%s');" % (return_word.replace("'","\\'") ,  test_list[0].replace("'","\\'"), test_list[1].replace("'","\\'"))


def select_next_word_to_display():
    word_list = db(db.word_tbl).select()
    print word_list
    return_word = select_word_to_display(word_list)
    #store word id to session.
    session.display_word_id = return_word.id

    return return_word.word

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

def check_progress():

    """
    get word to display to user
    """

    word_list = db(db.word_tbl).select()
    print word_list


    return_word = select_word_to_display(word_list)

    #store word id to session.
    session.display_word_id = return_word.id
    word_meanning_info1 = "the amount of space between two places"
    word_meanning_info2 = "a person or organization that supplies goods to shops and companies"
    return dict(item = return_word.word, word_meanning_info1=word_meanning_info1, word_meanning_info2=word_meanning_info2)

def select_word_to_display(word_list):
    from random import choice
    temp_vaar = choice(word_list)
    return temp_vaar

def get_header(text):
    """
        get header of article
    """
    header_position =text.find("<p>&nbsp;</p>")
    log.info("header_position = %d", header_position)
    header_text =  request.vars.editor1[:header_position]
    return header_text


def post_article_class():
    log.info("request.vars = %s",request.vars.article_class)
    article_classes = request.vars.article_class
    article_class_list = db(db.article_class).select()
    log.info("article = %s ",article_class_list )


    result= ""
    if len(article_classes):
        for item in article_classes:
            log.info("item = %s", item)
            try:
                db(db.article_class.id == article_class_list[article_classes.index(item)].id).update(name=item)
            except:
                log.error("database error")
                result = "failure"
    else:
        log.error("no infor about article class")

    result = "update article class successfully"

    return dict(result = result)




def article_class():
    """
        Create, change , update article_class
    """
    article_class_list = db(db.article_class).select()
    log.info("article_class = %s", article_class_list.__doc__ )

    if len(article_class_list) > 0:
            log.info(" article class is existed..display it")
    else:
        log.info("create database:w")
        #create database
        db.article_class.insert(name ="")
        db.article_class.insert(name ="")
        db.article_class.insert(name ="")
        db.article_class.insert(name ="")

    article_class_list = db(db.article_class).select()
    log.info("article_class = %s", article_class_list )
    return dict(article_class_list = article_class_list)

def get_article_id(name):
    """
    return id
    """
    article_class_list = db(db.article_tag).select()
    log.info("article_class = %s", article_class_list)
    for item in article_class_list:
        if item.name == name:
            return item.id
    return False;


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


@auth.requires_login()
def post_article():
    log.info("post")
    log.info("request.vars = %s",request.vars)
    example1 = request.vars.example1


    log.info("session.user = %s", auth.user)
    log.info("header_text = %s", header_text)
    log.info("auth.user.id = %s", auth.user.id)

    add_word_to_db()

    """
    question_id =""

    try:
        question_id = db.question_tbl.insert(word = content_text,
                                example = header_text,
                                writer = auth.user.id)
        log.info('successfully create a question_tbl')


    except:
        log.error('cant create question_tbl')
    try:
        tag_id = db.tag_tbl.insert(tag_info = articleId,
                            question_info = id_temp)
    except:
        log.error('cant create tag for question')
    redirect(URL(r = request, f= 'article', args = question_id))
    """
    redirect(URL(r = request, f= 'post'))
    return dict()




#those code is for manage meta data not using right now
# using flickr for photo uploading
@auth.requires_login()
def show_image():

    image_data = db(db.pic_store).select()
    #image = image_data.pic

    form = SQLFORM(db.pic_store)
    if form.process().accepted:
        response.flash = 'movie info is posted'
    return dict(form = form)
@auth.requires_login()
def manage_image():
    grid = SQLFORM.smartgrid(db.pic_store)
    return dict(grid=grid)

@auth.requires_login()
def manage_article_tag():
    grid = SQLFORM.smartgrid(db.article_tag)
    return dict(grid=grid)