__author__ = 'huyheo'

import os
file_path = os.path.join(os.getcwd(),'applications','welcome','unittest','setup_test.py')
execfile(file_path, globals())
from intent_def import *

class TestGoToSomeWhere(unittest.TestCase):
    def setUp(self):
        set_up_basic_environment()
        session.time_to_go = None
        session.by_what = None
        session.place = None
        session.topic_list = []

    def json_data_go_to_place(self,saying, intent, target_place, urgent):
        json_data = {u'outcomes': [{u'entities': {u'level_of_urgent': [{u'value': urgent}],
                                                  u'target_place': [{u'value': target_place}]},
                                    u'confidence': 0.975,
                                    u'intent': intent,
                                    u'_text': saying}],
                     u'msg_id': u'95295c05-ca50-42bc-8c3d-a6a95ae5a4d3', u'_text': u'i want to go to the office'}
        return json_data

    def json_data_time_info(self, saying, intent, time):
        json_data = {u'outcomes': [{u'entities': {u'datetime': [{u'value': time}],
                                                  },
                                    u'confidence': 0.975,
                                    u'intent': intent,
                                    u'_text': saying}],
                     u'msg_id': u'95295c05-ca50-42bc-8c3d-a6a95ae5a4d3', u'_text': u'i want to go to the office'}
        return json_data

    def json_data_method_to_go(self, saying, intent, method):
        json_data = {u'outcomes': [{u'entities': {u'method': [{u'value': method}],
                                                  },
                                    u'confidence': 0.975,
                                    u'intent': intent,
                                    u'_text': saying}],
                     u'msg_id': u'95295c05-ca50-42bc-8c3d-a6a95ae5a4d3', u'_text': u'i want to go to the office'}
        return json_data

    def json_no_entity(self, saying, intent):
        json_data = {u'outcomes': [{u'entities': {
                                                  },
                                    u'confidence': 0.975,
                                    u'intent': intent,
                                    u'_text': saying}],
                     u'msg_id': u'95295c05-ca50-42bc-8c3d-a6a95ae5a4d3', u'_text': u'i want to go to the office'}
        return json_data

    def json_talk_age(self, saying, intent, method):
        json_data = {u'outcomes': [{u'entities': {u'age_of_person': [{u'value': method}],
                                                  },
                                    u'confidence': 0.975,
                                    u'intent': intent,
                                    u'_text': saying}],
                     u'msg_id': u'95295c05-ca50-42bc-8c3d-a6a95ae5a4d3', u'_text': u'i want to go to the office'}
        return json_data



    def check_reply_from_ai(self, intention, place, urgent, value, expected_return):
        question_msg = handler_user_saying(intention, place, urgent,value)
        self.assertEqual(question_msg, expected_return)
    """
    def testAskBasicInfo(self):
        user_ask = 'i want to go to school'
        intention ='go_to_some_where'
        place = 'school'
        urgent = 'want'
        value =''
        expected_return = 'ask about time'
        self.check_reply_from_ai(intention, place, urgent, value, expected_return)

        #user answer
        session.topic_list.append('go_to_place')
        intention = 'time'
        value = '3AM'
        urgent = ''
        expected_return ='ask method to go'
        self.check_reply_from_ai(intention, place, urgent, value, expected_return)


        session.topic_list.append('go_to_place')
        intention = 'vehicle'
        value = 'bike'
        expected_return  = 'you could go there'
        self.check_reply_from_ai(intention, place, urgent, value, expected_return)
        self.assertEqual(value, session.by_what)

    def testAskWithoutSubject(self):
        #ask where is it (place)
        #reset
        self.testAskBasicInfo()
        ask_info ='where is it?'

        intention = 'where_is_it'
        place = 'it'
        urgent = ''
        value = ''
        expected_return ='van dien'
        self.check_reply_from_ai(intention, place, urgent, value, expected_return)

    def testQuestionNeedUserInfo(self):
        #how far is it from here
        #    require location of user
        self.testAskBasicInfo()
        intention = 'how_far_is_it'
        place = 'it'
        urgent = ''
        value = ''
        expected_return ='5km'
        self.check_reply_from_ai(intention, place, urgent, value, expected_return)
        """

    def testTalkToGoSomeWhere(self):
        json_data = self.json_data_go_to_place('',TO_GO_SOMEWHERE, 'office', 'want')

        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'ask about time')

        json_data = self.json_data_time_info('',TIME_INFO,'3am')
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'ask method to go')

        json_data = self.json_data_method_to_go('', METHOD_TO_GO, 'bike')
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'you could go there')

    def testTalkAboutPersonalThing(self):

        json_data = self.json_no_entity('', ASK_AGE)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, '1 years old')

        json_data = self.json_no_entity('', ASK_NAME)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'ai')

        json_data = self.json_no_entity('', ASK_JOB)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'worker')

        json_data = self.json_no_entity('', ASK_JOB_OPINION)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'this job is ok')








        pass












suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestGoToSomeWhere))
unittest.TextTestRunner(verbosity=2).run(suite)


