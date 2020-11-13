import unittest
from unittest import mock
import simple

def sum(a,b):
    return a + b

class Test1(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def tearDown(self):
        self.a = 0
        self.b = 0  

    def test_func1(self):
        result = sum(self.a, self.b)
        self.assertEqual(result, self.a + self.b)

    @mock.patch('simple.simple_function')
    def test_func2(self, mock_simple_func):
        self.assertIs(mock_simple_func, simple.simple_function)

    @mock.patch('simple.SimpleClass')
    def test_func3(self, mock_class):
        cls1 = mock_class
        cls2 = simple.SimpleClass
        self.assertEqual(cls1.explode, cls2.explode)

    def test_func4(self):
        with mock.patch('simple.os.getcwd', return_value = 'testing'):
            assert simple.work_on() == 'testing'

    def test_func5(self):
        with mock.patch('simple.Helper') as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = simple.Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work_on(), 'testing')

if __name__ == '__main__':
    unittest.main()