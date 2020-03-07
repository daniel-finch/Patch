import unittest
import manage



class TestMachineGroup(unittest.TestCase):

    def test_add(self):
        result = manage.add(10,15)
        self.assertEqual(result, 25)