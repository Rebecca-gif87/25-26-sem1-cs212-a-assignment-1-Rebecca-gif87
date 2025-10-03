import os
import sys


def display_welcome():
    """Display welcome message to the user."""
    print("=" * 50)
    print("   Welcome to Python CLI File Manager!")
    print("=" * 50)
    print("This is a simple file manager to demonstrate")
    print("Python fundamentals: variables, expressions,")
    print("statements, and functions.")
print()
    # TODO: Add a blank line after the welcome message
    



def calculate_file_size():
    """Calculate and display the size of a specified file."""
    filename = input("Enter the filename (with path if needed): ").strip()
    
    if not filename:
        print("Error: No filename provided.")
        return
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return
        
        # Check if it's a file (not a directory)
        if not os.path.isfile(filename):
            print(f"Error: '{filename}' is not a regular file.")
            return
        
        # Get file size in bytes
        size_bytes = os.path.getsize(filename)
        
        # Calculate size in different units
        # TODO: Fix the code below to perform floating point division
        size_kb = size_bytes / 1024
        size_mb = size_kb / 1024
        
        # Display results
        print(f"\nFile: {filename}")
        print(f"Size: {size_bytes} bytes")
        
        if size_bytes >= 1024:
            print(f"Size: {size_kb:.2f} KB")
            
        if size_bytes >= 1024 * 1024:
            print(f"Size: {size_mb:.2f} MB")
            
    except OSError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def get_user_choice():
    """Get user's menu choice and return it."""
    print("\nAvailable commands:")
    print("1. help - Show this help message")
    print("2. calc - Calculate file size")
    print("3. info - Show program information")
    print("4. quit - Exit the program")
    print()
    
    choice = input("Enter your choice (help/calc/info/quit): ").strip().lower()
    # TODO: Add code to return the choice
    return choice 


def display_help():
    """Display help information about available commands."""
    print("\n" + "=" * 40)
    print("           HELP - Available Commands")
    print("=" * 40)
    print("help  - Display this help message")
    print("calc  - Calculate the size of a file")
    print("        You'll be prompted to enter a filename")
    print("info  - Show information about this program")
    print("quit  - Exit the file manager")
    print()
    print("Tips:")
    print("- File paths can be relative or absolute")
    print("- Use quotes around filenames with spaces")
    print("- The program uses only Python standard library")
    print("=" * 40)


def display_info():
    """Display program information."""
    print("\n" + "=" * 40)
    print("         PROGRAM INFORMATION")
    print("=" * 40)
    print("Program: Python CLI File Manager")
    print("Purpose: Week 1 Python fundamentals practice")
    print("Concepts: Variables, expressions, statements, functions")
    print("Features:")
    print("  - File size calculation")
    print("  - Interactive command system")
    print("  - Help system")
    print("  - Standard library only")
    print()
    print("Author: CS212 Assignment 1")
    print("Python Version:", sys.version.split()[0])
    print("=" * 40)


# TODO - Set the keyword arguments such that;
# 1. show_goodbye defaults to True
# 2. goodbye_message defaults to "Thank you for using Python CLI File Manager!"
# 3. invalid_choice_prefix defaults to "Invalid choice:"
# 4. valid_commands defaults to "help, calc, info, quit"
def process_user_command(choice, running,*, show_goodbye=True, goodbye_message="Thank you for using Python CLI File Manager!", 
                        invalid_choice_prefi="Invalid choice:", valid_commands="help, calc, info, quit"
):
    """
    Process a user command and return the updated running state.
    
    This function demonstrates keyword arguments and is designed to test
    students' understanding of keyword-only arguments and default values.
    
    Args:
        choice (str): The user's command choice
        running (bool): Current state of the program loop
        show_goodbye (bool, keyword-only): Whether to show goodbye message when quitting
        goodbye_message (str, keyword-only): Custom goodbye message
        invalid_choice_prefix (str, keyword-only): Prefix for invalid choice messages
        valid_commands (str, keyword-only): String listing valid commands
    
    Returns:
        bool: Updated running state (False if user chose to quit, True otherwise)
    """
    if choice == "help":
        display_help()
    elif choice == "calc":
        calculate_file_size()
    elif choice == "info":
        display_info()
    elif choice == "quit":
        if show_goodbye:
            print(f"\n{goodbye_message}")
            print("Goodbye!")
        return False
    else:
        print(f"\n{invalid_choice_prefix} '{choice}'")
        print(f"Please enter one of: {valid_commands}")
    
    return running


def main():
    """Main program loop."""
    # Display welcome message
    # TODO: Call the function to display the welcome message
    
    # Main command loop
    # TODO: Initialize a variable to control the loop. Hint set running = True
    running=True
    while running:
        try:
            choice = get_user_choice()
            
            # Use the extracted function to process the command
            # This demonstrates calling a function with keyword arguments
            running = process_user_command(choice, running)
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Thank you for using Python CLI File Manager!")
            break
        except EOFError:
            print("\n\nEnd of input detected.")
            print("Thank you for using Python CLI File Manager!")
            break


if __name__ == "__main__":
    main()
