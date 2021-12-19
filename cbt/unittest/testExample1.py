import math
import unittest

def calcCircumfrence(r):
	return r*2*math.pi

class TestMyCode(unittest.TestCase):
	def testCircumfrence(self):
		self.assertEqual(calcCircumfrence(5), 31.41592653589793)

unittest.main()