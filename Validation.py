import unittest
from validator import validate_filename

class TestFilename(unittest.TestCase):
    def test_valid_filename(self):
        self.assertTrue(validate_filename("MED_DATA_20240101120000.csv"))

    def test_invalid_filename(self):
        self.assertFalse(validate_filename("datafile.csv"))

if __name__ == "__main__":
    unittest.main()

    