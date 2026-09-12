import unittest

from pilot_app.service import total


class ServiceTests(unittest.TestCase):
    def test_total(self) -> None:
        self.assertEqual(6, total([1, 2, 3]))
