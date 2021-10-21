import unittest
from unittest.case import TestCase
from cans import Cola, RootBeer, OrangeSoda
from coins import Coin, Quarter, Dime, Nickel, Penny
from customer import Customer
from simulation import Simulation
from wallet import Wallet
from soda_machine import SodaMachine
from user_interface import try_parse_int , get_unique_can_names , validate_main_menu, display_payment_value, validate_coin_selection


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

 Needs some work_________________
    def test_get_unique_can_names(self):
        self.cola = Cola()
        self.rootbeer = RootBeer()
        self.orange = OrangeSoda()
        name_list = []
        three_name = ["Cola", "Root Beer", "Orange Soda"]
        can_names = [self.cola, self.cola, self.rootbeer, self.rootbeer, self.orange, self.orange]
        unique_names = get_unique_can_names(can_names)
        for name in unique_names:
            name_list.append(str(name)+".name")
        print(name_list)
        self.assertTrue(name_list, three_name)
    

    # def test_empty_list(self):
    #     empty_list = []
    #     unique_names = get_unique_can_names(empty_list)
    #     self.assertEqual(empty_list,unique_names)

    
    # def test_display_payment_value(self):
    #     """ Instantiate each of the 4 coin types and append them to a list. 
    #     Pass the list into theis function, ensure the returned values is .41"""
    #     self.quarter = Quarter()
    #     self.dime = Dime()
    #     self.nickel = Nickel()
    #     self.penny = Penny()
    #     coint_list = [self.quarter, self.dime, self.nickel, self.penny]
    #     payment_value = display_payment_value(coint_list)
    #     self.assertEqual(payment_value, 0.41)
        
    # def test_display_payment_value(self):
    #     """ Instantiate each of the 4 coin types and append them to a list. 
    #     Pass the list into theis function, ensure the returned values is .41"""
    #     coint_list = []
    #     payment_value = display_payment_value(coint_list)
    #     self.assertEqual(payment_value, 0)
        

    # def test_validate_Quarter_selection(self):
    #     """Pass in 1, ensure the appropriate tuple is returned"""
    #     coin_select = validate_coin_selection(1)
    #     self.assertEqual(coin_select, (True, "Quarter"))

    # def test_validate_Dime_selection(self):
    #     """Pass in 2, ensure the appropriate tuple is returned"""
    #     coin_select = validate_coin_selection(2)
    #     self.assertEqual(coin_select, (True, "Dime"))
    
    # def test_validate_Nickel_selection(self):
    #     """Pass in 3, ensure the appropriate tuple is returned"""
    #     coin_select = validate_coin_selection(3)
    #     self.assertEqual(coin_select, (True, "Nickel"))

    # def test_validate_Penny_selection(self):
    #     """Pass in 4, ensure the appropriate tuple is returned"""
    #     coin_select = validate_coin_selection(4)
    #     self.assertEqual(coin_select, (True, "Penny"))

    # def test_validate_Done_selection(self):
    #     """Pass in 5, ensure the appropriate tuple is returned"""
    #     coin_select = validate_coin_selection(5)
    #     self.assertEqual(coin_select, (True, "Done"))

    # def test_validate_None_selection(self):
    #     """Pass in invalid number, ensure None is displayed"""
    #     coin_select = validate_coin_selection(6)
    #     self.assertEqual(coin_select, (False, None))

if __name__ == '__main__':
    unittest.main()

