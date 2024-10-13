import unittest
from app.command_divider import returnCommands

class TestReader(unittest.TestCase):

    def test_type(self):
        # checks if its a list
        commands = ['Hello World\n', 'My name is Gabriel']
        result = returnCommands(commands)
        self.assertIsInstance(result, list, 'The result is not a list.')

    def test_results(self):
        # check if the results are correct
        commands = ['Hello World\n', 'My name is Gabriel']
        expected = ['Hello', 'World', 'My', 'name', 'is', 'Gabriel']
        result = returnCommands(commands)
        self.assertEqual(result, expected, f'{result} != {expected}')


if __name__ == '__main__':
    unittest.main()