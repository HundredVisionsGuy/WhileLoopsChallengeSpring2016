# Testreductions.py

# Import Statements
import unittest
import reductions

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    
    def test_reductionsForEvenValues(self):
        # Capture the results of the function
        result = reductions.reductions(4)
        # Check for expected output
        self.assertEqual('4, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0',
                         result)

    def test_reductionsForOddFloatValues(self):
        # Capture the results of the function
        result = reductions.reductions(3.3)
        # Check for expected output
        self.assertEqual('3.3, 2.8, 2.3, 1.8, 1.3, 0.8, 0.3',
                         result)

    def test_reductionsForPositiveOddValues(self):
        # Capture the results of the function
        result = reductions.reductions(5)
        # Check for expected output
        self.assertEqual('5, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0',
                         result)

    def test_reductionsForPositiveFloatValues(self):
        # Capture the results of the function
        result = reductions.reductions(4.4)
        # Check for expected output
        self.assertEqual('4.4, 3.9, 3.4, 2.9, 2.4, 1.9, 1.4, 0.9, 0.4',
                         result)

    def test_reductionsForNegativeNumber(self):
        # Capture the results of the function
        result = reductions.reductions(-3)
        # Check for expected output
        self.assertEqual('0', result)

    def test_reductionsForZero(self):
        # Capture the results of the function
        result = reductions.reductions(0)
        # Check for expected output
        self.assertEqual('0', result)
# Run the tests
if __name__ == '__main__':
    unittest.main()
