import unittest
from unittest.case import TestCase
from cans import Cola
from coins import Coin
from customer import Customer
from simulation import Simulation
from wallet import Wallet
from soda_machine import SodaMachine

class TestAddCanToBackpack(unittest.TestCase):
    """Pass in a Cola object, test that the len of the customer’s backpack’s purhcased_cans list
went up by 1"""

    def setUp(self):
        self.customer=Customer()

    def test_bought_items_added_to_backpack(self):
        """Testing is items purchased are added into the backpack"""
        drink_list=["Cola"]
        self.customer.add_can_to_backpack("Cola")
        self.assertEqual(self.customer.backpack.purchased_cans,drink_list)
    
    def test_add_one_can_to_backpack(self):
        """Testing is items purchased are added into the backpack"""
        (self.customer.add_can_to_backpack("Cola"))
        one_can_add = len(self.customer.backpack.purchased_cans)
        self.assertEqual(one_can_add,1)
    
    def test_add_can(self):
        """Testing boolean to test length of purchase_can list"""
        check_list_twice = "Cola"
        self.customer.add_can_to_backpack(check_list_twice)
        test_variable = 1
        self.assertTrue(test_variable, self.customer.backpack.purchased_cans)


if __name__ == '__main__':
    unittest.main()

