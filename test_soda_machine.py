import unittest
from unittest.case import TestCase
from cans import Can, Cola, OrangeSoda, RootBeer
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
         self.cola = Cola()
         self.orange_soda = OrangeSoda()
         self.root_beer = RootBeer() 

    def test_fill_register(self):
        """Instantiate a SodaMachine object, test that its register list has a len of 88"""
        test_register_value = len(self.soda_machine.register)
        self.assertEqual(test_register_value,88)



    def test_fill_inventory(self):
        """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
        test_inventory_value = len(self.soda_machine.inventory)
        self.assertEqual(test_inventory_value,30)


    def test_get_quarter_from_register(self):
        """Test gets quarter from register"""
        quarter = self.quarter.name
        register_change = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(quarter, register_change.name)

    def test_get_dime_from_register(self):
        """Test gets dime from register"""
        dime = self.dime.name
        register_change = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(dime,register_change.name)

    def test_get_nickel_from_register(self):
        """test gets nickel from register"""
        nickel = self.nickel.name
        register_change = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(nickel, register_change.name)

    def test_get_penny_from_register(self):
        """test gets penny from register"""
        penny = self.penny.name
        register_change = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(penny, register_change.name)

    def test_get_coin_from_register(self):
        """test if not listed item throws none"""
        register_change = self.soda_machine.get_coin_from_register("Pickle")
        self.assertIsNone(register_change)



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
    
    def test_register_has_false(self):
        """ Test that Quarter will return True"""
        false_list="Cow"
        coin_check=self.soda_machine.register_has_coin(false_list)
        self.assertFalse(coin_check)

    def test_determine_change_value_with_higher(self):
        """test with total payment higher"""
        higher= self.soda_machine.determine_change_value(1.00,.50)
        self.assertTrue(higher)

    def test_determine_change_soda_price_higher(self):
        """test with select soda price higher"""
        soda_higher= self.soda_machine.determine_change_value(.50,1.00)
        self.assertTrue(soda_higher)
    
    def test_determine_change_soda_price_even(self):
        """test 2 equel values"""
        price_even= self.soda_machine.determine_change_value(1.00,1.00)
        self.assertFalse(price_even)
    

    def test_calculate_coin_value(self):
        """Instantiate each of the 4 coins and append them to a list. 
        Pass the list into this function, ensure the returned value is .41"""
        coin_list = [self.quarter, self.dime, self.nickel, self.penny]
        value = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(0.41, value)
    

    def test_calculate_coin_value_empty_list(self):
        """use a empty list to ensure the returned value is 0"""
        coin_list = []
        value = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(0, value)


    def test_get_inventory_soda_cola(self):
        """making sure cola matches Cola"""
        soda=self.soda_machine.get_inventory_soda("Cola")
        self.assertEqual(soda.name,self.cola.name)
    
    def test_get_inventory_soda_orange(self):
        """making sure orange soda matches orange soda"""
        soda=self.soda_machine.get_inventory_soda("Orange Soda")
        self.assertEqual(soda.name,self.orange_soda.name)

    def test_get_inventory_soda_root_beer(self):
        """making sure Root beer matches Root Beer"""
        soda=self.soda_machine.get_inventory_soda("Root Beer")
        self.assertEqual(soda.name,self.root_beer.name)

    def test_get_inventory_mountain_dew(self):
        """making sure Mountain Dew matches none"""
        soda=self.soda_machine.get_inventory_soda("Mountain Dew")
        self.assertIsNone(soda)
    
    
   
    def test_return_inventory(self):
        """Instantiate a can and pass it into the method. Test that the 
        len of self.inventory is now 31"""
        self.soda_machine.return_inventory(self.cola)
        added_drink = len(self.soda_machine.inventory)
        self.assertEqual(31,added_drink)

    def test_deposit_coins_into_register(self):
        """Instantiate each of the 4 coins and append them to a list.
        pass the list into tewh function, ensure the len is equel to 92"""
        list=[self.quarter,self.dime,self.penny,self.nickel]
        self.soda_machine.deposit_coins_into_register(list)
        added_coin = len(self.soda_machine.register)
        self.assertEqual(92,added_coin)


if __name__ == '__main__':
    unittest.main()
