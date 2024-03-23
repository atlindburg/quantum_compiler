import unittest
from unittest.mock import patch
import os
import sys

# Adjust the import path to ensure it's correct based on your test file's location
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from python.compile import Compile


class TestMain(unittest.TestCase):

    def setUp(self):
        # Setup before each test
        self.test_file_name = "test_script.qc"
        self.test_file_path = os.path.join("tests", self.test_file_name)
        # Create a test script file
        with open(self.test_file_path, "w") as f:
            f.write("SET q1 TO 1 {0} 0 {1};")

    @patch('python.main.Compile')
    @patch('sys.argv', ['main.py', os.path.join('tests', 'test_script.qc')])
    def test_main_with_valid_file(self, mock_compile):
        # Mock the Compile class to avoid executing its run_lexer method
        mock_compile_instance = mock_compile.return_value
        # Import the main module and run its main function
        with patch('builtins.open', unittest.mock.mock_open(read_data="SET q1 TO 1 {0} 0 {1};")), \
             patch('sys.exit') as mock_sys_exit:
            from python import main
            main.main()
            mock_compile_instance.run_lexer.assert_called_once()
            # Ensure sys.exit was not called, indicating no errors
            mock_sys_exit.assert_not_called()

    # You can add more test cases for other scenarios, such as file not found, etc.

if __name__ == '__main__':
    unittest.main()

