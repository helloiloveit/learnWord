__author__ = 'huyheo'
"""
Syntax:
 python web2py.py -S chuotnhat -M -R applications/chuotnhat/unittest/test_user_tag_handler.py
"""
import unittest
import gluon
from gluon.globals import Request

import os
file_path = os.path.join(os.getcwd(),'applications','welcome')
execfile(os.path.join(file_path,'models','db.py'), globals())
execfile(os.path.join(file_path,'controllers','default.py'), globals())


def set_up_basic_environment():
    #set up request
    env = dict()
    request = Request(env)
    #clear all table
    db.auth_user.truncate()
    db.commit()

