import unittest
from main import P

class TestMain(unittest.TestCase):

	def test_one(self):
		self.assertEqual(P(-10), None)

	def test_two(self):
		self.assertEqual(P(0), 0)
		
	def test_three(self):
		self.assertEqual(P(10), 55)


if __name__ == "__main__":
	unittest.main()