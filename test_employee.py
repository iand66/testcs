import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    #Class level setup & teardown methods
    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    def tearDownClass(cls):
        print('TearDown Class')

    #Function level setup & teardown methods
    def setUp(self):
        self.e1 = Employee('Corey', 'Schafer', 50000)
        self.e2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.e1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.e2.email, 'Sue.Smith@email.com')

        self.e1.first = 'John'
        self.e2.first = 'Jane'

        self.assertEqual(self.e1.email, 'John.Schafer@email.com')
        self.assertEqual(self.e2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.e1.fullname, 'Corey Schafer')
        self.assertEqual(self.e2.fullname, 'Sue Smith')

        self.e1.first = 'John'
        self.e2.first = 'Jane'

        self.assertEqual(self.e1.fullname, 'John Schafer')
        self.assertEqual(self.e2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.e1.apply_raise()
        self.e2.apply_raise()

        self.assertEqual(self.e1.pay, 52500)
        self.assertEqual(self.e2.pay, 63000)

if __name__ == '__main__':
    unittest.main()