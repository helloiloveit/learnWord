__author__ = 'huyheo'

import os
file_path = os.path.join(os.getcwd(),'applications','welcome','unittest','setup_test.py')
execfile(file_path, globals())
from intent_def import *

class Base_Test(unittest.TestCase):
    def setUp(self):
        set_up_basic_environment()
        session.time_to_go = None
        session.by_what = None
        session.place = None
        session.topic_list = []
        session.intent_list = []
        # set temporary variable for db = none
        session.db_age = None
        session.db_username =None
        session.db_job = None
        session.expected_intent = None
        session.user_act = None
        session.distance_info = None
        session.timing_info = None
        session.greeting_flag = None
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

    def check_message_with_no_entity(self, saying, intent, expected_msg):
        json_data = self.json_no_entity(saying, intent)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, expected_msg)

    def check_message_with_entity(self, saying, intent, entity_name, entity_value, expected_msg):
        json_data = self.json_data_with_entity_info(saying, intent, entity_name, entity_value)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, expected_msg)

    def check_reply_from_ai(self, intention, place, urgent, value, expected_return):
        question_msg = handler_user_saying(intention, place, urgent,value)
        self.assertEqual(question_msg, expected_return)

class TestGoToSomeWhere(Base_Test):
    def setUp(self):
        super(TestGoToSomeWhere, self).setUp()
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


    def testTalkHobby(self):



        expected_msg = 'i like running. what is your hobby?'
        self.check_message_with_no_entity('what is your hobby?', ASK_HOBBY , expected_msg)

        expected_msg = 'nice.'
        self.check_message_with_entity('i like running too', LIKE_SMTH , ACTIVITY_INFO, 'running',  expected_msg)

        expected_msg = 'i run 20 km in weekend. how long do you run'
        self.check_message_with_entity('Nice. How long do you run?', ASK_DISTANCE , ACTIVITY_INFO, 'run',  expected_msg)

        expected_msg = 'nice. when do you run'
        self.check_message_with_entity('10km only', DISTANCE_INFO , DISTANCE, '10km',  expected_msg)

        expected_msg = 'nice. when did you start running'
        self.check_message_with_entity('i run in the weekend', DOING_SMTH , DATETIME, 'weekend',  expected_msg)

        expected_msg = 'nice.'
        self.check_message_with_entity('2 years ago', TIME_INFO, DATETIME,'2 years', expected_msg)

        expected_msg = 'i practice it every week.'
        self.check_message_with_entity('Woa. How could you run 20 km?', ASK_HOW_TO_DO , ACTIVITY_INFO, 'run',  expected_msg)

        expected_msg = 'i run in weekend.'
        self.check_message_with_entity('when do you run?', ASK_TIME , ACTIVITY_INFO, 'run',  expected_msg)


        expected_msg = 'because it fun and good for health.'
        self.check_message_with_entity('why do you like running?', ASK_WHY_LIKE,ACTIVITY_INFO,'running', expected_msg)

        expected_msg = '1 year.'
        self.check_message_with_entity('how long have you been running?', ASK_DURATION, ACTIVITY_INFO, 'running', expected_msg)

        expected_msg = 'it is good for health.'
        self.check_message_with_no_entity('is it good for health', ASK_HEALTH_STS, expected_msg)

        expected_msg = 'i started running 2 years ago.'
        self.check_message_with_entity('when did you start running?', ASK_TIME, START_STOP_INFO,'start', expected_msg)

        """
        expected_msg = 'yeah i love it. Its addictive.'
        self.check_message_with_no_entity('do you enjoy it so far', ASK_OPINION_ABOUT_SOMETHING, expected_msg)
        """

    """
    def testWhatAreUDoing(self):
        expected_msg = 'hello.'
        self.check_message_with_no_entity('hello', GREETING, expected_msg)


        expected_msg = 'im traveling.'
        self.check_message_with_entity('what are u doing', ASK_WHAT_ARE_U_DOING, CONTACT_TYPE, 'you', expected_msg)
    """



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
        expected_msg = 'thank you.Im John.Nice to meet you.'
        self.check_message_with_entity('', TIME_INFO, DATETIME, '9AM', expected_msg)
        # introduce my self
        # ask nationality
        json_data = self.json_data_with_entity_info('im huy', INTRODUCE_MYSELF, NAME_INFO , 'huy')
        self.assertEqual( handle_topic_data(json_data),
                            'Nice to meet you.')

        # Say yes
        # How long have you been here
        expected_msg = '9 months'
        self.check_message_with_entity('how long have u been traveling?', ASK_DURATION,  ACTIVITY_INFO , 'traveling', expected_msg)


    def testBasicConversationInPublicPlace2(self):


        json_data = self.json_no_entity('whatre u doing', ASK_WHAT_ARE_U_DOING)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'im waiting.')

        json_data = self.json_no_entity('hello may i help you?', OFFER_HELP)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'could u help me to know the time the bus arrive?')

    def testBasicConversationInPublicPlace3(self):
        json_data = self.json_no_entity('hello may i help you?', OFFER_HELP)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'could u help me to know the time the bus arrive?')

        json_data = self.json_no_entity('', DONT_NO)
        msg = handle_topic_data(json_data)
        self.assertEqual(msg, 'thanks')

        pass


    #test AI assistant
    def testAssistant(self):
        expected_msg = 'lets do some work sir'
        self.check_message_with_no_entity('ai. What should i do', ASK_WHAT_SHOULD_I_DO, expected_msg)

        expected_msg = 'youre productive and creative at the airport'
        self.check_message_with_no_entity('why', ASK_WHY, expected_msg)

class TestTalkHobby(Base_Test):
    def setUp(self):
        super(TestTalkHobby, self).setUp()

    def testTalkHobby(self):

        #set flag
        session.TALK_ACTIVE_FLAG = False

        expected_msg = 'i like running. what is your hobby?'
        self.check_message_with_no_entity('what is your hobby?', ASK_HOBBY , expected_msg)

        expected_msg = 'nice. how long do you run'
        self.check_message_with_entity('i like running too', LIKE_SMTH , ACTIVITY_INFO, 'running',  expected_msg)

        expected_msg = 'nice. when do you run'
        self.check_message_with_entity('10km only', DISTANCE_INFO , DISTANCE, '10km',  expected_msg)

        expected_msg = 'nice. when did you start running'
        self.check_message_with_entity('i run in the weekend', DOING_SMTH , DATETIME, 'weekend',  expected_msg)

        expected_msg = 'nice.'
        self.check_message_with_entity('2 years ago', TIME_INFO, DATETIME,'2 years', expected_msg)

        expected_msg = 'i practice it every week.'
        self.check_message_with_entity('Woa. How could you run 20 km?', ASK_HOW_TO_DO , ACTIVITY_INFO, 'run',  expected_msg)

        expected_msg = 'i run in weekend.'
        self.check_message_with_entity('when do you run?', ASK_TIME , ACTIVITY_INFO, 'run',  expected_msg)


        expected_msg = 'because it fun and good for health.'
        self.check_message_with_entity('why do you like running?', ASK_WHY_LIKE,ACTIVITY_INFO,'running', expected_msg)

        expected_msg = '1 year.'
        self.check_message_with_entity('how long have you been running?', ASK_DURATION, ACTIVITY_INFO, 'running', expected_msg)

        expected_msg = 'it is good for health.'
        self.check_message_with_no_entity('is it good for health', ASK_HEALTH_STS, expected_msg)

        expected_msg = 'i started running 2 years ago.'
        self.check_message_with_entity('when did you start running?', ASK_TIME, START_STOP_INFO,'start', expected_msg)

        """
        expected_msg = 'yeah i love it. Its addictive.'
        self.check_message_with_no_entity('do you enjoy it so far', ASK_OPINION_ABOUT_SOMETHING, expected_msg)
        """



class TestGreeting(Base_Test):
    def setUp(self):
        super(TestGreeting, self).setUp()

    def testGreeting(self):
        expected_msg = 'im doing very well. And you. How are u doing?'
        self.check_message_with_entity('hello how are you doing', GREETING, GREETING_LEVEL,'how', expected_msg)

        expected_msg = 'sorry to know that.'
        self.check_message_with_entity('im doing terrible', EMOTIONAL_EXPRESSION,FEELING,'bad', expected_msg)


class TestJob(Base_Test):
    def setUp(self):
        super(TestJob, self).setUp()

    def testTalkAboutJob(self):
        expected_msg = 'ai'
        self.check_message_with_no_entity('what your name', ASK_NAME, expected_msg)

        expected_msg = '1 years old'
        self.check_message_with_no_entity('how old are you', ASK_AGE, expected_msg)

        expected_msg = 'worker'
        self.check_message_with_no_entity('whats your job', ASK_JOB, expected_msg)

        expected_msg = 'this job is ok'
        self.check_message_with_entity('do you like your job?', ASK_OPINION_ABOUT_SOMETHING,TARGET_NAME, 'it', expected_msg)

        expected_msg = 'because its well paid.'
        self.check_message_with_no_entity('why you like your job?', ASK_WHY_LIKE, expected_msg)

        expected_msg = '1 years.'
        self.check_message_with_entity('how long have you been working?', ASK_DURATION, ACTIVITY_INFO, 'working', expected_msg)

        expected_msg = 'i started this job 1 year ago.'
        self.check_message_with_entity('When did you start this job', ASK_TIME, START_STOP_INFO, 'start', expected_msg)

        expected_msg = 'yes.'
        self.check_message_with_entity('Do you want to find a new job?', ASK_IF_WANT_TO_DO_SMTH, ACTIVITY_INFO, 'find a new job', expected_msg)

        expected_msg = 'yes im looking for new job.'
        self.check_message_with_entity('Are u looking for it now?', ASK_IF_DOING_SMTH, TARGET_NAME, 'it', expected_msg)

class TestIntroduction(Base_Test):
    def setUp(self):
        super(TestIntroduction, self).setUp()
    def testMakeFriend(self):
        session.TALK_ACTIVE_FLAG = False
        expected_msg = 'hello.'
        self.check_message_with_no_entity('hello.', GREETING, expected_msg)

        expected_msg = 'im ai. Nice to meet you. huy.'
        self.check_message_with_entity('im huy. Nice to meet you', INTRODUCE_MYSELF, CONTACT_TYPE,'huy', expected_msg)

        expected_msg = 'nice to meet you. How are u doing?'
        self.check_message_with_no_entity('Nice to meet you.', NICE_TO_MEET_YOU, expected_msg)

        expected_msg = 'great.'
        self.check_message_with_entity('im doing well', EMOTIONAL_EXPRESSION,FEELING,'well', expected_msg)

        expected_msg = 'im 1 year old. how old are you?'
        self.check_message_with_no_entity('how old are you', ASK_AGE, expected_msg)

        expected_msg = 'nice.'
        self.check_message_with_entity('im 33 years old', AGE_INFO,AGE_OF_PERSON, '33', expected_msg)

        expected_msg = 'worker. what is your job?'
        self.check_message_with_no_entity('whats your job', ASK_JOB, expected_msg)

        expected_msg = 'engineer nice.'
        self.check_message_with_entity('im an engineer', INTRODUCE_MYSELF, JOB_INFO, 'engineer', expected_msg)

        expected_msg = 'its ok.'
        self.check_message_with_entity('do you like your job?', ASK_OPINION_ABOUT_SOMETHING,TARGET_NAME, 'it', expected_msg)

        expected_msg = 'because its well paid.'
        self.check_message_with_no_entity('why you like your job?', ASK_WHY_LIKE, expected_msg)

        expected_msg = '1 years.'
        self.check_message_with_entity('how long have you been working?', ASK_DURATION, ACTIVITY_INFO, 'working', expected_msg)

        expected_msg = 'i like running. what is your hobby?'
        self.check_message_with_no_entity('what is your hobby?', ASK_HOBBY , expected_msg)

class TestIntroductionAIStartConversation(Base_Test):
    def setUp(self):
        super(TestIntroductionAIStartConversation, self).setUp()
    def testMakeFriend(self):
        session.TALK_ACTIVE_FLAG = False

        expected_msg = 'hello.'
        self.check_message_with_no_entity('hello.', GREETING, expected_msg)

        expected_msg = 'im ai. Nice to meet you. huy.'
        self.check_message_with_entity('im huy. Nice to meet you', INTRODUCE_MYSELF, CONTACT_TYPE,'huy', expected_msg)

        expected_msg = 'nice to meet you. How are u doing?'
        self.check_message_with_no_entity('Nice to meet you.', NICE_TO_MEET_YOU, expected_msg)

        expected_msg = 'sorry to know that.'
        self.check_message_with_entity('im doing terrible', EMOTIONAL_EXPRESSION,FEELING,'bad', expected_msg)



    def testSayHi(self):
        session.TALK_ACTIVE_FLAG =  True

        expected_msg = 'hello. How are u doing?'
        self.check_message_with_no_entity('hello.', GREETING, expected_msg)

        expected_msg = 'great. whats your name?'
        self.check_message_with_entity('im doing well', EMOTIONAL_EXPRESSION,FEELING,'well', expected_msg)

        expected_msg = 'im ai. Nice to meet you. Huy. how old are you?'
        self.check_message_with_entity('im Huy', INTRODUCE_MYSELF,CONTACT_TYPE,'Huy',expected_msg)

        expected_msg = 'nice. where are you from?'
        self.check_message_with_entity('im 33 years old', AGE_INFO,AGE_OF_PERSON, '33', expected_msg)

        expected_msg = 'nice VietNam. what is your job?'
        self.check_message_with_entity('im from VietNam', COME_FROM_INFO, COUNTRY_INFO, 'VietNam', expected_msg)

        expected_msg = 'engineer nice.'
        self.check_message_with_entity('im an engineer', INTRODUCE_MYSELF, JOB_INFO, 'engineer', expected_msg)

        expected_msg = 'im from Vietnam.'
        self.check_message_with_no_entity('where are you from.', ASK_WHERE_ARE_U_FROM, expected_msg)





suite = unittest.TestSuite()
#suite.addTest(unittest.makeSuite(TestGoToSomeWhere))
#suite.addTest(unittest.makeSuite(TestGreeting))
#suite.addTest(unittest.makeSuite(TestJob))
#suite.addTest(unittest.makeSuite(TestIntroduction))
#suite.addTest(unittest.makeSuite(TestTalkHobby))
suite.addTest(unittest.makeSuite(TestIntroductionAIStartConversation))
unittest.TextTestRunner(verbosity=2).run(suite)


