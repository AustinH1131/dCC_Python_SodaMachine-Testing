import unittest
from coins import Coin
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Test for the get_wallet_coin method in Customer class"""

    def setUp(self):
        self.customer=Customer()

    def test_quarter_string_returns_quarter_instances(self):
        """Test that passing in 'Quarters' returns a quarter object"""    
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(.25, returned_coin.value)

    def test_nickel_string_returns_nickel_instances(self):
        """Test that passing in 'Nickel' returns a Nickel object"""    
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(.05, returned_coin.value)

    def test_dime_string_returns_dime_instances(self):
        """Test that passing in 'Dime' returns a Dime object"""    
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(.10, returned_coin.value)

    def test_penny_string_returns_penny_instances(self):
        """Test that passing in 'Penny' returns a Penny object"""    
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(.01, returned_coin.value)
        
    def test_valid_name(self):

        coin_names = []
        for thing_in_wallet in self.customer.wallet.money:
            if thing_in_wallet.name not in coin_names:
                coin_names.append(thing_in_wallet.name)

        coins_returned_from_method = []

        for name_of_coin in coin_names:
            coin_from_method = self.customer.get_wallet_coin(name_of_coin)
            coins_returned_from_method.append(coin_from_method)

        does_match = True
        for num in range(len(coins_returned_from_method)):
            if coin_names[num] != coins_returned_from_method[num].name:
                does_match = False

        self.assertFalse(does_match)
            
    def test_returns_none(self):
        name_of_coin = 'Cow'
        coin_from_method = self.customer.get_wallet_coin(name_of_coin)
        self.assertIsNone(coin_from_method)

class TestAddCoinsToWallet(unittest.TestCase):
    """Pass in a list of 3 coins, test that the len of the customer’s wallet’s money list went up by
3"""

    def setUp(self):
        self.customer=Customer()

    def test_coins_added_to_wallet(self):
        """Test if coins are added to wallet"""





if __name__ == '__main__':
    unittest.main()

