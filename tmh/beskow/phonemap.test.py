import unittest
from tmh.beskow import phonemap

class TestStringMethods(unittest.TestCase):

    def test_phonemap(self):
        pm = phonemap.phonemap('STA','IPA')
        self.assertEqual(pm, pm)

if __name__ == '__main__':
    unittest.main()

