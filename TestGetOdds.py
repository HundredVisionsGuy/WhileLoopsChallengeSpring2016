# TestGetOdds.py

# Import Statements
import unittest
import getOdds

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    
    def test_getOddsForNegativeToNegative(self):
        # Capture the results of the function
        result = getOdds.getOdds(3, 13)
        # Check for expected output
        self.assertEqual('3, 5, 7, 9, 11, 13', result)

    def test_getOddsForNegativeToPostive(self):
        # Capture the results of the function
        result = getOdds.getOdds(5, 16)
        # Check for expected output
        self.assertEqual('5, 7, 9, 11, 13, 15', result)

    def test_getOddsForPositiveToNegative(self):
        # Capture the results of the function
        result = getOdds.getOdds(-4, 9)
        # Check for expected output
        self.assertEqual('-3, -1, 1, 3, 5, 7, 9', result)

    def test_getOddsForPositiveToPostive(self):
        # Capture the results of the function
        result = getOdds.getOdds(12, 24)
        # Check for expected output
        self.assertEqual('13, 15, 17, 19, 21, 23', result)

     
# Run the tests
if __name__ == '__main__':
    unittest.main()
