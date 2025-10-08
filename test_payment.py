import unittest
from io import StringIO
import sys

from payment import checkout, PaymentMode, parse_payment_mode

class TestPaymentProcessing(unittest.TestCase):
    def setUp(self):
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.held_stdout

    def get_output(self):
        return sys.stdout.getvalue()

    def test_paypal_payment(self):
        checkout(PaymentMode.PAYPAL, 100.0)
        output = self.get_output()
        self.assertIn("Processing PayPal payment of $100.00", output)

    def test_googlepay_payment(self):
        checkout(PaymentMode.GOOGLEPAY, 49.99)
        output = self.get_output()
        self.assertIn("Processing GooglePay payment of $49.99", output)

    def test_creditcard_payment(self):
        checkout(PaymentMode.CREDITCARD, 150.75)
        output = self.get_output()
        self.assertIn("Processing Credit Card payment of $150.75", output)

    def test_invalid_payment_mode_type(self):
        checkout("INVALID_MODE", 50.0)
        output = self.get_output()
        self.assertIn("Error: Invalid payment mode type!", output)

    def test_parse_payment_mode_valid(self):
        mode = parse_payment_mode("paypal")
        self.assertEqual(mode, PaymentMode.PAYPAL)

    def test_parse_payment_mode_invalid(self):
        mode = parse_payment_mode("invalidmode")
        output = self.get_output()
        self.assertIsNone(mode)
        self.assertIn("Error: Unsupported payment mode 'invalidmode'", output)

if __name__ == "__main__":
    unittest.main()
