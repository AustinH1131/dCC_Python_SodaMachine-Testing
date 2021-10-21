import unittest
from unittest.case import TestCase
from cans import Cola
from coins import Coin
from customer import Customer
from simulation import Simulation
from wallet import Wallet
from soda_machine import SodaMachine

class TestAddCoinsToWallet(unittest.TestCase):
    """Pass in a list of 3 coins, test that the len of the customer’s wallet’s money list went up by
3"""

    def setUp(self):
        self.customer=Customer()

    def test_coins_added_to_wallet(self):
        """Test if coins are added to wallet"""
        coin_list = ['Quarter', 'Penny', 'Nickel']
        empty_wallet = self.customer.wallet.money
        empty_empty_wallet = empty_wallet.clear()
        for coin in coin_list:
            empty_wallet.append(coin)
        list_len = len(empty_wallet)
        self.assertEqual(list_len, 3)

    def test_coins_stay_same_after_empty_list(self):
        """Test if coins are added to wallet"""
        coin_list = []
        current_wallet = len(self.customer.wallet.money)
        empty_add_wallet = len(self.customer.wallet.money)
        for coin in coin_list:
            empty_add_wallet.append(coin)
        self.assertEqual(empty_add_wallet, current_wallet)

class TestWalletLength(unittest.TestCase):
    '''Instantiate a wallet object and test money list length of 88'''

    def setUp(self):
        self.wallet = Wallet()

    def test_money_list_length(self):
        test_wallet_length = len(self.wallet.money)
        self.assertEqual(test_wallet_length,88)


if __name__ == '__main__':
    unittest.main()
