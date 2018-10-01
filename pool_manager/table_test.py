import unittest
import json
import table

example_data = json.loads('{"cost": 180, "occupied": true, "start_time": "09-30-2018 20:40:59", "end_time": "10-01-2018 01:44:40", "number": 1}')

class TestPoolTable(unittest.TestCase):

    '''
    No matter how exactly JSON deserializes and how we construct the object,
    the data must be preserved
    '''

    def test_full_input_init(self):
        dummy = table.PoolTable(example_data)
        self.assertTrue(dummy.occupied)
        self.assertEqual(dummy.number, 1)
        self.assertEqual(dummy.cost, 180)
        self.assertEqual(dummy.start_time, '09-30-2018 20:40:59')
        self.assertEqual(dummy.end_time, '10-01-2018 01:44:40')


    def test_none_input(self):
        dummy = table.PoolTable()
        self.assertFalse(dummy.occupied)
        self.assertEqual(dummy.number, 0)
        self.assertEqual(dummy.cost, 0)
        self.assertEqual(dummy.start_time, 0)
        self.assertEqual(dummy.end_time, 0)


if __name__ == '__main__':
    unittest.main()
