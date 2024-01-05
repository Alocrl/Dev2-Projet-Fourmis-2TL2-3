import sys
sys.path.insert(0, '/Users/maxime/Documents/GitHub/Dev2-Projet-Fourmis-2TL2-3')
from libs.supply_generator import Supply
import unittest
import coverage

class TestSupply(unittest.TestCase):

    def test__init__(self):
        """Test class declaration"""

        #normal value
        test1 = Supply({"banane":{"nbr_life_eat":2}})
        self.assertEqual(test1.all_type_and_life, {"banane":{"nbr_life_eat":2}})

        test2 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4}})
        self.assertEqual(test2.all_type_and_life, {"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4}})

        test3 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})
        self.assertEqual(test3.all_type_and_life, {"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})

        #raises valueError : nbr_life_eat < 1
        with self.assertRaises(ValueError) as value_error:
            Supply({"fraise":{"nbr_life_eat":-4}})
        self.assertEqual(value_error.exception.args[0], 'nbr_life_eat must be greater than or equal to 1 for all food types.')

        with self.assertRaises(ValueError) as value_error:
            Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":0},"graine": {"nbr_life_eat" :1}})
        self.assertEqual(value_error.exception.args[0], 'nbr_life_eat must be greater than or equal to 1 for all food types.')

        with self.assertRaises(ValueError) as value_error:
            Supply({"banane":{"nbr_life_eat":-2},"fraise":{"nbr_life_eat":-1},"graine": {"nbr_life_eat" :-21}})
        self.assertEqual(value_error.exception.args[0], 'nbr_life_eat must be greater than or equal to 1 for all food types.')

        with self.assertRaises(ValueError) as value_error:
            Supply({"banane":{"nbr_life_eat":0},"fraise":{"nbr_life_eat":0},"graine": {"nbr_life_eat" :0}})
        self.assertEqual(value_error.exception.args[0], 'nbr_life_eat must be greater than or equal to 1 for all food types.')

        #raises TypeError : nbr_life_eat = string
        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":"test"}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":"test"},"graine": {"nbr_life_eat" :1}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":14},"graine": {"nbr_life_eat" :""}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":""},"fraise":{"nbr_life_eat":12},"graine": {"nbr_life_eat" :3}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":""},"fraise":{"nbr_life_eat":""},"graine": {"nbr_life_eat" :""}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        #raises TypeError : nbr_life_eat = float
        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":2.44}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":1},"fraise":{"nbr_life_eat":12.3433},"graine": {"nbr_life_eat" :1}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":1.111},"fraise":{"nbr_life_eat":12.3433},"graine": {"nbr_life_eat" :932.433}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":0.333},"fraise":{"nbr_life_eat":32},"graine": {"nbr_life_eat" : 2}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        #raises TypeError : nbr_life_eat = boolean
        with self.assertRaises(TypeError) as type_error:
            Supply({"graine":{"nbr_life_eat":True}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":12},"fraise":{"nbr_life_eat":False}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":12},"fraise":{"nbr_life_eat":21},"graine": {"nbr_life_eat" :True}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":True},"fraise":{"nbr_life_eat":True},"graine": {"nbr_life_eat" :True}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            Supply({"banane":{"nbr_life_eat":False},"fraise":{"nbr_life_eat":False},"graine": {"nbr_life_eat" :False}})
        self.assertEqual(type_error.exception.args[0], 'nbr_life_eat must be an integer.')

    def test_check_supply(self):
        """Test if the check_supply method returns the Supply class check"""

        test1 = Supply({"banane":{"nbr_life_eat":2}})
        self.assertTrue(test1.check_supply())

        test2 = Supply({"graine":{"nbr_life_eat":2},"banane":{"nbr_life_eat":4}})
        self.assertTrue(test2.check_supply())

        test3 = Supply({})
        self.assertFalse(test3.check_supply())

        test4 = Supply({"tomate":{"nbr_life_eat":1},"fraise":{"nbr_life_eat":233},"carotte": {"nbr_life_eat" : 6}})
        self.assertTrue(test4.check_supply())

    def test_del_food(self):
        """Test if the del_food method actually removes food from the Supply class"""

        test1 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})
        self.assertTrue(test1.del_food())

        test2 = Supply({"banane":{"nbr_life_eat":1}})
        self.assertTrue(test2.del_food())

        test3 = Supply({})
        self.assertFalse(test3.del_food())

        test4 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})
        test4.del_food()
        self.assertEqual(test4.all_type_and_life, {'banane': {'nbr_life_eat': 1}, 'fraise': {'nbr_life_eat': 4}, 'graine': {'nbr_life_eat': 1}})

        test5 = Supply({"banane":{"nbr_life_eat":1}})
        test5.del_food()
        self.assertEqual(test5.all_type_and_life, {})

        test6 = Supply({})
        test5.del_food()
        self.assertEqual(test6.all_type_and_life, {})

    def test_add_food(self):
        """Test if the del_food method actually add food from the Supply class"""

        #NotEqual random testing
        test1 = Supply({"banane":{"nbr_life_eat":3}})
        self.assertEqual(test1.all_type_and_life, {"banane":{"nbr_life_eat":3}})
        test1.add_food(1)
        self.assertNotEqual(test1.all_type_and_life, {"banane":{"nbr_life_eat":3}})

        test2 = Supply({})
        self.assertEqual(test2.all_type_and_life, {})
        test2.add_food(1)
        self.assertNotEqual(test2.all_type_and_life, {})

        test3 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})
        self.assertEqual(test3.all_type_and_life, {"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})
        test3.add_food(3)
        self.assertNotEqual(test2.all_type_and_life, {"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":4},"graine": {"nbr_life_eat" :1}})

        #raises TypeError : nbr_collect = string
        with self.assertRaises(TypeError) as type_error:
            test4 = Supply({"fraise":{"nbr_life_eat":12}})
            test4.add_food("test")
        self.assertEqual(type_error.exception.args[0], 'nbr_collect must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            test5 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":244},"graine": {"nbr_life_eat" :1}})
            test5.add_food("12")
        self.assertEqual(type_error.exception.args[0], 'nbr_collect must be an integer.')

        #raises TypeError : nbr_collect = bool
        with self.assertRaises(TypeError) as type_error:
            test6 = Supply({"fraise":{"nbr_life_eat":24}})
            test6.add_food(True)
        self.assertEqual(type_error.exception.args[0], 'nbr_collect must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            test7 = Supply({"banane":{"nbr_life_eat":12},"fraise":{"nbr_life_eat":32},"graine": {"nbr_life_eat" :43}})
            test7.add_food(False)
        self.assertEqual(type_error.exception.args[0], 'nbr_collect must be an integer.')

        #raises TypeError : nbr_collect = float
        with self.assertRaises(TypeError) as type_error:
            test8 = Supply({"fraise":{"nbr_life_eat":24}})
            test8.add_food(2.444)
        self.assertEqual(type_error.exception.args[0], 'nbr_collect must be an integer.')

        with self.assertRaises(TypeError) as type_error:
            test9 = Supply({"banane":{"nbr_life_eat":12},"fraise":{"nbr_life_eat":32},"graine": {"nbr_life_eat" :43}})
            test9.add_food(32.122)
        self.assertEqual(type_error.exception.args[0], 'nbr_collect must be an integer.')

        #raises ValueError : nbr_collect < 1
        with self.assertRaises(ValueError) as value_error:
            test10 = Supply({"fraise":{"nbr_life_eat":124}})
            test10.add_food(0)
        self.assertEqual(value_error.exception.args[0], 'nbr_collect must be greater than or equal to 1 for all food types.')

        with self.assertRaises(ValueError) as value_error:
            test11 = Supply({"fraise":{"nbr_life_eat":64}})
            test11.add_food(-12)
        self.assertEqual(value_error.exception.args[0], 'nbr_collect must be greater than or equal to 1 for all food types.')

    def test_all_supply(self):
        """Test if the all_supply method returns the total number of food items available in the supply"""

        test1 = Supply({"banane":{"nbr_life_eat":3}})
        self.assertEqual(test1.all_supply(), 3)

        test2 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":12},"graine": {"nbr_life_eat" :4}})
        self.assertEqual(test2.all_supply(),18)

        test3 = Supply({})
        self.assertEqual(test3.all_supply(),0)

        test4 = Supply({"banane":{"nbr_life_eat":10},"fraise":{"nbr_life_eat":1}})
        self.assertEqual(test4.all_supply(), 11) 

    def test_all_type_in_supply(self):
        """Test if the all_supply method returns the total number of food types available in the Supply class"""
        
        test1 = Supply({"graine": {"nbr_life_eat" : 1},"salade": {"nbr_life_eat" : 1},"tomate": {"nbr_life_eat" : 4},"carotte": {"nbr_life_eat" : 6}})
        self.assertEqual(test1.all_type_in_supply(),4)

        test2 = Supply({})
        self.assertEqual(test2.all_type_in_supply(),0)

        test3 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":12}})
        self.assertEqual(test3.all_type_in_supply(),2)

        test4 = Supply({"banane":{"nbr_life_eat":2}})
        self.assertEqual(test4.all_type_in_supply(),1)   

    def test__str__(self):
        """Test the textual representation of the Supply class"""

        test1 = Supply({"banane":{"nbr_life_eat":2},"fraise":{"nbr_life_eat":12}})
        self.assertEqual(str(test1), f'here is the object of the class : {test1.all_type_and_life}')

        test2 = Supply({})
        self.assertEqual(str(test2), f'here is the object of the class : {test2.all_type_and_life}')

        test3 = Supply({"graine": {"nbr_life_eat" : 1},"salade": {"nbr_life_eat" : 1},"tomate": {"nbr_life_eat" : 4},"carotte": {"nbr_life_eat" : 6}})
        self.assertEqual(str(test3), f'here is the object of the class : {test3.all_type_and_life}')

        test4 = Supply({"banane":{"nbr_life_eat":2}})
        self.assertEqual(str(test4), f'here is the object of the class : {test4.all_type_and_life}')

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    cov.stop()
    cov.report()