import unittest

from main import categorize_email


class CategorizeEmailTest(unittest.TestCase):
    def test_email_categories(self):
        cases = (
            ("Please reply ASAP", "Urgent"),
            ("Your PAYMENT is due", "Bill/Payment"),
            ("Your Order has shipped", "Order/Shipping"),
            ("Hello there", "other"),
        )
        for email_text, expected in cases:
            with self.subTest(email_text=email_text):
                self.assertEqual(categorize_email(email_text), expected)
