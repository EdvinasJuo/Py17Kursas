import unittest

import Task2
from Task2 import BankAccount

class TestTask2(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("123456", "John", 100)
    def test_deposit_is_greater_than_zero(self):
        initial_balance = self.account.balance
        self.account.deposit(50)
        self.assertEqual(self.account.balance, initial_balance + 50)

    def test_deposit_is_less_than_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-5)

    def test_deposit_is_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_25_from_account_balance(self):
        initial_balance = self.account.balance
        self.account.withdraw(25)
        self.assertEqual(self.account.balance, initial_balance - 25)

    def test_withdraw_more_than_account_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(120)

    def test_create_bank_account(self):
        account = BankAccount("123321", "Edvinas Juodeika", 500)

        self.assertEqual(account.account_number, "123321")
        self.assertEqual(account.owner, "Edvinas Juodeika")
        self.assertEqual(account.balance, 500)

    def test_get_balance(self):
        initial_balance = self.account.balance
        self.assertEqual(initial_balance,100)

    def test_make_transaction_deposit(self):
        Task2.make_transaction(self.account, "withdraw", 50)
        self.assertEqual(self.account.balance, 50)

    def test_make_transaction_withdraw(self):
        Task2.make_transaction(self.account, "deposit", 50)
        self.assertEqual(self.account.balance, 150)

    def test_invalid_transaction_type(self):
        with self.assertRaises(ValueError):
            Task2.make_transaction(self.account, "invalid", 50)
