import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for HBNBCommand class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up after test.
        """
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """
        Test help command.
        """
        with patch('builtins.input', side_effect=['help', 'quit']):
            self.console.cmdloop()
        self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """
        Test quit command.
        """
        with self.assertRaises(SystemExit):
            with patch('builtins.input', return_value='quit'):
                self.console.cmdloop()
        self.assertIn("Exiting...", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_eof_command(self, mock_stdout):
        """
        Test EOF command.
        """
        with self.assertRaises(SystemExit):
            with patch('builtins.input', return_value='EOF'):
                self.console.cmdloop()
        self.assertIn("Exiting...", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        """
        Test empty line behavior.
        """
        with patch('builtins.input', side_effect=['', 'quit']):
            self.console.cmdloop()
        self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
