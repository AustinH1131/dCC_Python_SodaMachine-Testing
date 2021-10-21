import unittest
from unittest.case import TestCase
from cans import Cola
from coins import Coin
from customer import Customer
from simulation import Simulation
from wallet import Wallet
from soda_machine import SodaMachine
from user_interface import validate_main_menu
from user_interface import try_parse_int


class TestUserInterfaceModule(unittest.TestCase):

    # def test_validate_main_menu_1(self):
    #     """Pass in 1 , ensure the tuple returns True, number"""
    #     self.user = validate_main_menu(1)
    #     self.assertEqual(self.user,(True,1))

    # def test_validate_main_menu_2(self):
    #     """Pass in 2 , ensure the tuple returns True, number"""
    #     self.user = validate_main_menu(2)
    #     self.assertEqual(self.user,(True,2))    

    # def test_validate_main_menu_3(self):
    #     """Pass in 3 , ensure the tuple returns True, number"""
    #     self.user = validate_main_menu(3)
    #     self.assertEqual(self.user,(True,3))

    # def test_validate_main_menu_4(self):
    #     """Pass in 4 , ensure the tuple returns True, number"""
    #     self.user = validate_main_menu(4)
    #     self.assertEqual(self.user,(True,4))
    
    # def test_validate_main_menu_5(self):
    #     """Pass in 5 , ensure the tuple returns False, None"""
    #     self.user = validate_main_menu(5)
    #     self.assertEqual(self.user,(False,None))

    # def test_parse_pass_in_10(self):
    #     """Pass in 10 ensure the int value is 10"""  
    #     num10= try_parse_int(10)
    #     self.assertEqual(10,num10)
    
    
    # def test_parse_pass_in_hello(self):
    #     """Pass in hello ensure the int value is 0"""  
    #     num0= try_parse_int("Hello")
    #     self.assertEqual(0,num0)


    def test_get_unique_can_names():
        pass

    # def test_display_payment_value():
    #     pass

    # def test_validate_coin_selection():
    #     pass

if __name__ == '__main__':
    unittest.main()

