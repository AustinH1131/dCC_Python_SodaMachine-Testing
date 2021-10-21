import unittest
from unittest.case import TestCase
from cans import Cola
from coins import Coin
from customer import Customer
from simulation import Simulation
from wallet import Wallet
from soda_machine import SodaMachine


class TestSodaMachine(unittest.TestCase):
    """ Tests for Soda Machine Class"""

    def setUp(self):
         self.soda_machine = SodaMachine()

    def test_fill_register(self):
        """Instantiate a SodaMachine object, test that its register list has a len of 88"""
        test_register_value = len(self.soda_machine.register)
        self.assertEqual(test_register_value,88)



    def test_fill_inventory(self):
        """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
        test_inventory_value = len(self.sodamach.inventory)
        self.assertEqual(test_inventory_value,30)


    def test_get_coin_from_register(self):
        pass

    def test_register_has_coin(self):
        pass
# ------------------------------------------------------

    def test_determine_change_value(self):
        pass

    def test_calculate_coin_value(self):
        pass

    def test_get_inventory_soda(self):
        pass
   
    def test_return_inventory(self):
        pass

    def test_deposit_coins_into_register(self):
        pass





if __name__ == '__main__':
    unittest.main()
