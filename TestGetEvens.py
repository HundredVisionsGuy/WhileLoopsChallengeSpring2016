# TestGetEvens.py

# Import Statements
import unittest
import getEvens

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    
    def test_getEvensForNegativeToNegative(self):
        # Capture the results of the function
        result = getEvens.getEvens(3, 13)
        # Check for expected output
        self.assertEqual('4, 6, 8, 10, 12', result)

    def test_getEvensForNegativeToPostive(self):
        # Capture the results of the function
        result = getEvens.getEvens(5, 16)
        # Check for expected output
        self.assertEqual('6, 8, 10, 12, 14, 16', result)

    def test_getEvensForPositiveToNegative(self):
        # Capture the results of the function
        result = getEvens.getEvens(-4, 9)
        # Check for expected output
        self.assertEqual('-4, -2, 0, 2, 4, 6, 8', result)

    def test_getEvensForPositiveToPostive(self):
        # Capture the results of the function
        result = getEvens.getEvens(12, 24)
        # Check for expected output
        self.assertEqual('12, 14, 16, 18, 20, 22, 24', result)

    
# Run the tests
if __name__ == '__main__':
    unittest.main()
