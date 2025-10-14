#!/usr/bin/env python3
"""
Unit tests for Python CLI File Manager TODO Tasks
Testing completion of TODO tasks in file_manager.py
Uses only unittest from standard library.
"""
# Rebecca

import unittest
import sys
import os
import io
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch

# Import the file_manager module
import file_manager


class TestFileManagerTODOTasks(unittest.TestCase):
    """Test cases specifically for TODO tasks in file_manager."""
    
    def test_display_welcome_blank_line_todo(self):
        """Test TODO: Add a blank line after the welcome message."""
        captured_output = io.StringIO()
        
        with redirect_stdout(captured_output):
            file_manager.display_welcome()
        
        output = captured_output.getvalue()
        
        # Check if welcome message ends with a blank line
        # The output should end with two newlines (one from last print, one blank line)
        self.assertTrue(output.endswith('\n\n') or output.count('\n') >= 6,
                       "TODO: Welcome message should end with a blank line")
    
    def test_floating_point_division_todo(self):
        """Test TODO: Fix floating point division in calculate_file_size."""
        # Create a test file with specific size for division testing
        test_file = "division_test.txt"
        # Create a file that's 1536 bytes (1.5 KB) to test division
        content = "A" * 1536
        
        try:
            with open(test_file, 'w') as f:
                f.write(content)
            
            with patch('builtins.input', return_value=test_file):
                captured_output = io.StringIO()
                
                with redirect_stdout(captured_output):
                    file_manager.calculate_file_size()
                
                output = captured_output.getvalue()
                
                # Check if floating point division is used correctly
                # For 1536 bytes, should show 1.50 KB, not 1.00 KB (which would be integer division)
                if "1.50 KB" in output:
                    self.assertTrue(True, "Floating point division is working correctly")
                elif "1.00 KB" in output:
                    self.fail("TODO: Fix floating point division - still using integer division (//)") 
                else:
                    # Could be that the TODO is not yet implemented
                    self.assertIn("KB", output, "File size calculation should show KB units")
                    
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_get_user_choice_return_todo(self):
        """Test TODO: Add code to return the choice."""
        with patch('builtins.input', return_value='help'):
            captured_output = io.StringIO()
            
            with redirect_stdout(captured_output):
                choice = file_manager.get_user_choice()
            
            # Check that function actually returns the choice (not None)
            self.assertIsNotNone(choice, "TODO: get_user_choice should return the choice")
            self.assertEqual(choice, 'help', "TODO: get_user_choice should return the correct choice")
    
    def test_process_user_command_keyword_arguments_todo(self):
        """Test TODO: Set keyword arguments with default values."""
        # Test if function can be called with default arguments
        try:
            # This should work if default arguments are properly set
            result = file_manager.process_user_command("help", True)
            self.assertIsNotNone(result, "process_user_command should return a value")
        except TypeError as e:
            if "missing" in str(e) and "required positional argument" in str(e):
                self.fail("TODO: Set default values for keyword arguments in process_user_command")
            else:
                raise e
    
    def test_process_user_command_custom_keyword_args(self):
        """Test process_user_command with custom keyword arguments."""
        captured_output = io.StringIO()
        
        with redirect_stdout(captured_output):
            # Test with custom goodbye message
            result = file_manager.process_user_command(
                "quit", True, 
                show_goodbye=True, 
                goodbye_message="Custom goodbye!",
                invalid_choice_prefix="Oops:",
                valid_commands="test commands"
            )
        
        output = captured_output.getvalue()
        self.assertIn("Custom goodbye!", output)
        self.assertFalse(result, "Should return False when quit is chosen")
    
    def test_process_user_command_invalid_choice_custom_message(self):
        """Test process_user_command with custom invalid choice message."""
        captured_output = io.StringIO()
        
        with redirect_stdout(captured_output):
            result = file_manager.process_user_command(
                "invalid", True,
                show_goodbye=True,
                goodbye_message="Bye!",
                invalid_choice_prefix="Custom error:",
                valid_commands="custom, commands"
            )
        
        output = captured_output.getvalue()
        self.assertIn("Custom error:", output)
        self.assertIn("custom, commands", output)
        self.assertTrue(result, "Should return True for non-quit commands")
    
    @patch.object(file_manager, 'display_welcome')
    def test_main_display_welcome_todo(self, mock_display_welcome):
        """Test TODO: Call the function to display the welcome message."""
        # Mock get_user_choice to return 'quit' immediately
        with patch.object(file_manager, 'get_user_choice', return_value='quit'):
            with patch.object(file_manager, 'process_user_command', return_value=False):
                try:
                    file_manager.main()
                except NameError:
                    # Expected if running variable is not initialized
                    pass
        
        # Check if display_welcome was called
        mock_display_welcome.assert_called_once()
    
    def test_main_running_variable_todo(self):
        """Test TODO: Initialize a variable to control the loop."""
        # This test checks if the main function can run without NameError
        with patch.object(file_manager, 'get_user_choice', return_value='quit'):
            with patch.object(file_manager, 'process_user_command', return_value=False):
                with patch.object(file_manager, 'display_welcome'):
                    try:
                        file_manager.main()
                        # If we get here, the running variable was properly initialized
                        self.assertTrue(True, "Running variable is properly initialized")
                    except NameError as e:
                        if "running" in str(e):
                            self.fail("TODO: Initialize running variable in main function")
                        else:
                            raise e

    def test_todo_completion_summary(self):
        """Summary test showing which TODO tasks are completed vs pending."""
        todo_status = {
            "display_welcome_blank_line": False,
            "floating_point_division": False,
            "get_user_choice_return": False,
            "process_user_command_defaults": False,
            "main_display_welcome_call": False,
            "main_running_variable": False
        }
        
        # Test 1: Welcome blank line
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            file_manager.display_welcome()
        if captured_output.getvalue().endswith('\n\n'):
            todo_status["display_welcome_blank_line"] = True
        
        # Test 2: Return statement in get_user_choice
        with patch('builtins.input', return_value='test'):
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                result = file_manager.get_user_choice()
            if result is not None:
                todo_status["get_user_choice_return"] = True
        
        # Test 3: Floating point division
        test_file = "float_test.txt"
        try:
            with open(test_file, 'w') as f:
                f.write("A" * 1536)  # 1.5 KB
            
            with patch('builtins.input', return_value=test_file):
                captured_output = io.StringIO()
                with redirect_stdout(captured_output):
                    file_manager.calculate_file_size()
                
                if "1.50 KB" in captured_output.getvalue():
                    todo_status["floating_point_division"] = True
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)
        
        # Test 4: Default arguments in process_user_command
        try:
            file_manager.process_user_command("help", True)
            todo_status["process_user_command_defaults"] = True
        except TypeError:
            pass
        
        # Test 5: Display welcome call in main
        with patch.object(file_manager, 'display_welcome') as mock_welcome:
            with patch.object(file_manager, 'get_user_choice', return_value='quit'):
                with patch.object(file_manager, 'process_user_command', return_value=False):
                    try:
                        file_manager.main()
                        if mock_welcome.called:
                            todo_status["main_display_welcome_call"] = True
                    except (NameError, UnboundLocalError):
                        pass
        
        # Test 6: Running variable initialization
        with patch.object(file_manager, 'get_user_choice', return_value='quit'):
            with patch.object(file_manager, 'process_user_command', return_value=False):
                with patch.object(file_manager, 'display_welcome'):
                    try:
                        file_manager.main()
                        todo_status["main_running_variable"] = True
                    except (NameError, UnboundLocalError):
                        pass
        
        # Print summary for students
        completed = sum(todo_status.values())
        total = len(todo_status)
        
        print(f"\n=== TODO TASK COMPLETION SUMMARY ===")
        print(f"Completed: {completed}/{total} tasks")
        print("\nTask Status:")
        for task, completed in todo_status.items():
            status = "✓ DONE" if completed else "✗ TODO"
            print(f"  {task}: {status}")
        
        if completed == total:
            print("\n🎉 All TODO tasks completed! Great work!")
        else:
            print(f"\n📝 {total - completed} TODO tasks remaining.")
        
        # This test always passes - it's just for information
        self.assertTrue(True)

    def test_todo_hints_and_solutions(self):
        """Provides hints for completing each TODO task."""
        hints = {
            "Line 20 - display_welcome() blank line": 
                "Add: print() at the end of the function",
            
            "Line 47 - floating point division": 
                "Change // to / for floating point division",
            
            "Line 76 - get_user_choice() return": 
                "Add: return choice",
            
            "Lines 105-108 - process_user_command() defaults": 
                "Add default values like: show_goodbye=True, goodbye_message='Thank you...'",
            
            "Line 152 - main() display_welcome call": 
                "Add: display_welcome()",
            
            "Line 155 - main() running variable": 
                "Add: running = True"
        }
        
        print("\n=== TODO TASK HINTS ===")
        for location, hint in hints.items():
            print(f"\n{location}:")
            print(f"  Hint: {hint}")
        
        # This test always passes - it's just for information
        self.assertTrue(True)


if __name__ == '__main__':
    # Create a test suite and run all TODO tests
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)