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

    def json_data_with_entity_info(self, saying, intent, entity_name, entity_value):
        json_data = {u'outcomes': [{u'entities': {entity_name: [{u'value': entity_value}],
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
    """
    def testTalkToGoSomeWhere(self):
        json_data = self.json_data_go_to_place('',TO_GO_SOMEWHERE, 'office', 'want')

        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'ask about time')

        json_data = self.json_data_time_info('its 3AM',TIME_INFO,'3am')
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'ask method to go')

        json_data = self.json_data_method_to_go('', METHOD_TO_GO, 'bike')
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'you could go there')
    """

    def testTalkAboutPersonalThing(self):

        json_data = self.json_no_entity('', GREETING)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'hello')

        json_data = self.json_no_entity('', ASK_AGE)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, '1 years old')

        json_data = self.json_no_entity('', ASK_NAME)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'ai')

        json_data = self.json_no_entity('', ASK_JOB)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'worker')

    def testAskIfSomeOneLikeTheirJob(self):
        json_data = self.json_no_entity('', ASK_JOB)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'worker')

        json_data = self.json_data_with_entity_info('', ASK_OPINION_ABOUT_SOMETHING, TARGET_NAME, 'it')
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'this job is ok')

    def testBasicConversationInPublicPlace(self):
        """
        meet AI in public place
        AI ask for time
        AI make friend
        basic thing
        - sorry what time is it?
        - Its 7AM
        - Thanks, we re waiting for the bus to come
        - Hey, Im AI . Nice to meet you
        - Yes, Im Huy . Nice to meet you.
        - Are u local people?
        - Yes.
        - Where're u from ?
        - Canadia
        .
        .
        ..Hey i need to go. See u later?


        """
        # say hi . may i help u
        # return yes yes . what time does the bus come
        json_data = self.json_no_entity('hello may i help you?', OFFER_HELP)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'could u help me to know the time the bus arrive?')
        # answer time .
        # start make friend
        json_data = self.json_data_with_entity_info('', TIME_INFO, DATETIME , '9AM')
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'thank you.Im John.Nice to meet you.')
        # introduce my self
        # ask nationality
        json_data = self.json_data_with_entity_info('im huy', INTRODUCE_MYSELF, NAME_INFO , 'huy')
        self.assertEqual( handle_topic_data(json_data),
                            'Nice to meet you.')

        # Say yes
        # How long have you been here
        json_data = self.json_data_with_entity_info('how long have u been traveling?', ASK_DURATION,  ACTIVITY_INFO , 'huy')
        self.assertEqual( handle_topic_data(json_data),
                          '9 months.So i have to go see u soon')
        """
        # say good bye. Ask for contact
        json_data = self.json_data_with_entity_info('could u give my your facebook account so we could stay in touch?', ASK_CONTACT_INFO,  CONTACT_TYPE , 'facebook_account')
        self.assertEqual( handle_topic_data(json_data),
                          'heres mine: hello.i.love.it@gmail.com. Add me. See ya')



        pass
        """

    def testBasicConversationInPublicPlace2(self):

        json_data = self.json_no_entity('', GREETING)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'hello')

        json_data = self.json_no_entity('whatre u doing', ASK_WHAT_ARE_U_DOING)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'im reading a travel guide book')

        json_data = self.json_no_entity('hello may i help you?', OFFER_HELP)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'could u help me to know the time the bus arrive?')

    def testBasicConversationInPublicPlace3(self):
        """
        test more situation of this case
        """

        pass












suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestGoToSomeWhere))
unittest.TextTestRunner(verbosity=2).run(suite)


