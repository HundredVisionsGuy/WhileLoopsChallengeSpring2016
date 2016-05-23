# TestindexMaker.py

# Import Statements
import unittest
import indexMaker

class KnownValues(unittest.TestCase):
    
    def test_indexMakerForShortEntry(self):
        # Capture the results of the function
        result = indexMaker.indexMaker("Yo", 11)
        # Check for expected output
        self.assertEqual('Yo..........................11',
                         result)

    def test_indexMakerForMediumEntry(self):
        # Capture the results of the function
        result = indexMaker.indexMaker("Google Docs", 100)
        # Check for expected output
        self.assertEqual('Google Docs................100',
                         result)

    def test_indexMakerForFiveLetterEntry(self):
        # Capture the results of the function
        result = indexMaker.indexMaker("Phred", 1)
        # Check for expected output
        self.assertEqual('Phred........................1',
                         result)

    def test_indexMakerForLongEntry(self):
        # Capture the results of the function
        result = indexMaker.indexMaker("Gerrymandering", 199)
        # Check for expected output
        self.assertEqual('Gerrymandering.............199',
                         result)

    def test_indexMakerForLenOfShortEntry(self):
        # Capture the results of the function
        result = len(indexMaker.indexMaker("Yo", 11))
        # Check for expected output
        self.assertEqual(30, result)

    def test_indexMakerForLenOfMediumEntry(self):
        # Capture the results of the function
        result = len(indexMaker.indexMaker("Google Docs", 100))
        # Check for expected output
        self.assertEqual(30, result)

    def test_indexMakerForLenOfFiveLetterEntry(self):
        # Capture the results of the function
        result = len(indexMaker.indexMaker("Phred", 1))
        # Check for expected output
        self.assertEqual(30, result)

    def test_indexMakerForLenOfLongEntry(self):
        # Capture the results of the function
        result = len(indexMaker.indexMaker("Gerrymandering", 199))
        # Check for expected output
        self.assertEqual(30, result)
    
# Run the tests
if __name__ == '__main__':
    unittest.main()
