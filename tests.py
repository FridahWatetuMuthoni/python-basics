from unittest import TestCase
import unittest
from funcs import formated_name,location
from surveys import AnonymousSurvey, Employee
#UNITTESTS ASSERT METHODS
"""
assertEqual(a, b) : Verify that a == b
assertNotEqual(a, b) : Verify that a != b
assertTrue(x) : Verify that x is True
assertFalse(x) : Verify that x is False
assertIn(item, list) : Verify that item is in list
assertNotIn(item, list) : Verify that item is not in list
"""
#TESTING FUNCTIONS
class FullNamesTestCase(TestCase):
    #tests for funcs.py
    def test_two_names(self):
        #does names like 'jabis Joplin work
        name = formated_name('janis','joplin')
        self.assertEqual(name, 'Janis Joplin')
    
    def test_three_names(self):
        name = formated_name('Anna','jane','Manna')
        self.assertEqual(name, 'Anna Manna Jane')

class LocationTestCase(TestCase):
    def test_full_location(self):
        full_location = location('nairobi','kenya')
        self.assertEqual(full_location,'Nairobi, Kenya')


#TESTING CLASSSES
class SurveyTestCase(TestCase):
    
    # Create a survey and a set of responses for use in all test methods.
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
            
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
            #checking that the hard codded responses were stored in the classes responses
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


class EmployeeTestCase(TestCase):
    
    def setUp(self):
        self.employee = Employee('Fridah','watetu','45000')
    
    def test_with_raise(self):
        with_custom_raise = self.employee.give_raise(2000)
        self.assertEqual(with_custom_raise,47000)
    
    def without_custom_raise(self):
        without = self.employee.give_raise()
        self.assertEqual(without,51000)




if __name__ == '__main__':
    unittest.main()