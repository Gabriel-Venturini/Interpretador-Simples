import unittest
from app.document_reader import archiveReader

class TestReader(unittest.TestCase):

    def test_type(self):
        path_test = 'test/files/helloworld.txt'
        read_result = archiveReader(path_test) # call the function
        self.assertIsInstance(read_result, list, 'Not a list!\n') # checks if its returning a list

if __name__ == '__main__':
    unittest.main()