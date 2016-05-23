# TestwordPeat.py

# Import Statements
import unittest
import wordPeat

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    
    def test_wordPeatForShortWord(self):
        # Capture the results of the function
        result = wordPeat.wordPeat("Yo")
        # Check for expected output
        self.assertEqual('YoYo', result)

    def test_wordPeatForMediumWord(self):
        # Capture the results of the function
        result = wordPeat.wordPeat("google")
        # Check for expected output
        self.assertEqual('googlegooglegooglegooglegooglegoogle', result)

    def test_wordPeatForFourLetterWord(self):
        # Capture the results of the function
        result = wordPeat.wordPeat("Fred")
        # Check for expected output
        self.assertEqual('FredFredFredFred', result)

    def test_wordPeatForLongWord(self):
        # Capture the results of the function
        result = wordPeat.wordPeat("Gerrymander")
        # Check for expected output
        self.assertEqual('GerrymanderGerrymanderGerrymanderGerrymanderGerrymanderGerrymanderGerrymanderGerrymanderGerrymanderGerrymanderGerrymander', result)

    
# Run the tests
if __name__ == '__main__':
    unittest.main()
