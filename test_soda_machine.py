import unittest
from unittest.case import TestCase
from cans import Cola
from coins import Coin
from customer import Customer
from simulation import Simulation
from wallet import Wallet
from soda_machine import SodaMachine
from coins import Quarter
from coins import Dime
from coins import Nickel
from coins import Penny


class TestSodaMachine(unittest.TestCase):
    """ Tests for Soda Machine Class"""

    def setUp(self):
         self.soda_machine = SodaMachine()
         self.quarter = Quarter()
         self.dime = Dime()
         self.nickel = Nickel()
         self.penny = Penny()

    # def test_fill_register(self):
    #     """Instantiate a SodaMachine object, test that its register list has a len of 88"""
    #     test_register_value = len(self.soda_machine.register)
    #     self.assertEqual(test_register_value,88)



    # def test_fill_inventory(self):
    #     """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
    #     test_inventory_value = len(self.soda_machine.inventory)
    #     self.assertEqual(test_inventory_value,30)

# These five need work____________________________________________
    # def test_get_quarter_from_register(self):
    #     quarter = self.quarter.name
    #     register_change = self.soda_machine.get_coin_from_register("Quarter")
    #     self.assertEqual(quarter, register_change.name)

    # def test_get_dime_from_register(self):
    #     dime = self.dime.name
    #     register_change = self.soda_machine.get_coin_from_register("Dime")
    #     for coin in register_change:
    #         coin_name = coin
    #     self.assertEqual(dime, coin_name)

    # def test_get_nickel_from_register(self):
    #     nickel = self.nickel.name
    #     register_change = self.soda_machine.get_coin_from_register("Nickel")
    #     for coin in register_change:
    #         coin_name = coin
    #     self.assertEqual(nickel, coin_name)

    # def test_get_penny_from_register(self):
    #     penny = self.penny.name
    #     register_change = self.soda_machine.get_coin_from_register("Penny")
    #     for coin in register_change:
    #         coin_name = coin
    #     self.assertEqual(penny, coin_name)

    # def test_get_coin_from_register(self):
    #     register_change = self.soda_machine.get_coin_from_register("Pickle")
    #     for coin in register_change:
    #         coin_name = coin 
    #     self.assertIsNone(coin_name)

#         self.assertEqual(.25, returned_coin.value)



    def test_register_has_quarter(self):
        """ Test that Quarter will return True"""
        quarter="Quarter"
        coin_check=self.soda_machine.register_has_coin(quarter)
        self.assertTrue(coin_check)

    def test_register_has_penny(self):
        """ Test that Penny will return True"""
        penny="Penny"
        coin_check=self.soda_machine.register_has_coin(penny)
        self.assertTrue(coin_check)
    
    def test_register_has_nickel(self):
        """ Test that Nickel will return True"""
        nickel= "Nickel"
        coin_check=self.soda_machine.register_has_coin(nickel)
        self.assertTrue(coin_check)
    
    def test_register_has_Dime(self):
        """ Test that Dime will return True"""
        dime="Dime"
        coin_check=self.soda_machine.register_has_coin(dime)
        self.assertTrue(coin_check)
    
    def test_register_has_quarter(self):
        """ Test that Quarter will return True"""
        quarter="Cow"
        coin_check=self.soda_machine.register_has_coin(quarter)
        self.assertFalse(coin_check)
# # ------------------------------------------------------

#     def test_determine_change_value(self):
#         pass

#     def test_calculate_coin_value(self):
#         pass

#     def test_get_inventory_soda(self):
#         pass
   
#     def test_return_inventory(self):
#         pass

#     def test_deposit_coins_into_register(self):
#         pass





if __name__ == '__main__':
    unittest.main()
