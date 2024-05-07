from colorama import Fore, Style, Back

class ExitCommand(Exception):
    """Exception raised to exit the application when the user types 'exit'."""
    pass


class Questions:
    """
    A class to handle user interactions and data input through the console.

    Utilizes a Validator object to ensure that user inputs are valid according to specified rules.

    Methods:
    ask(question_text, text_options=None): Asks a question and optionally validates against provided options.
    select_option(question_text, text_options): Asks the user to select an option from a list.
    select_file(question_text, file_type=None): Requests a file path and validates it.
    select_folder(question_text): Requests a directory path and validates it.
    select_files(question_text, file_type=None): Requests a directory path and validates files of a specified type within it.
    """

    def __init__(self, validator):
        """
        Initialize the Questions object with a Validator.

        Args:
        validator (Validator): The Validator object to use for validating inputs.
        """
        self.validator = validator
        
    def input_with_exit(self, prompt):
        """Custom input function that checks for the 'exit' command."""
        # Imprimir el mensaje de salida en una línea separada y en color rojo
        print(Style.BRIGHT + Back.RED + Fore.WHITE + 'Type "exit" to quit' + Style.RESET_ALL)
        user_input = input(prompt)
        if user_input.strip().lower() == 'exit':
            raise ExitCommand("User exited the application.")
        return user_input

    
    def ask(self, question_text, text_options=None):
        """
        Ask the user a question and return their input, with optional validation against allowed options.

        Args:
        question_text (str): The text of the question to ask.
        text_options (list, optional): A list of valid responses if response validation is required.

        Returns:
        str: The user's response, which is validated if text_options is not None.
        """
        full_prompt = question_text  # Add exit option to prompt
        while True:
            response = self.input_with_exit(full_prompt)
            if text_options and response not in text_options:
                print("Invalid response, valid options are: {}".format(', '.join(text_options)))
                continue
            return response

    def select_option(self, question_text, text_options):
        """
        Ask the user to select an option from a list of text options.

        Args:
        question_text (str): The text of the question to present as the choice prompt.
        text_options (list of str): The options from which the user is to choose.

        Returns:
        str: The option chosen by the user.
        """
        full_prompt = question_text + "\n" + "\n".join(f"{idx+1}. {option}" for idx, option in enumerate(text_options)) 
        while True:
            selection = self.input_with_exit(full_prompt)
            if selection.isdigit() and 1 <= int(selection) <= len(text_options):
                return text_options[int(selection) - 1]
            print("Invalid selection, please try again.")

    def select_file(self, question_text, file_type=None):
        """
        Request and validate a file path from the user.

        Args:
        question_text (str): The prompt to display to the user requesting a file path.
        file_type (str, optional): The required file type extension.

        Returns:
        str: The validated file path.
        """
        full_prompt = question_text   # Add exit option to prompt
        while True:
            file_path = self.input_with_exit(full_prompt)
            if self.validator.validate_file(file_path, file_type):
                return file_path
            print("Invalid file. Please try again.")

    def select_folder(self, question_text):
        """
        Request and validate a directory path from the user.

        Args:
        question_text (str): The prompt to display to the user requesting a directory path.

        Returns:
        str: The validated directory path.
        """
        full_prompt = question_text   # Add exit option to prompt
        while True:
            folder_path = self.input_with_exit(full_prompt)
            if self.validator.validate_folder(folder_path):
                return folder_path
            print("Invalid directory. Please try again.")

    def select_files(self, question_text, file_type=None):
        """
        Request a directory path from the user and validate the existence of files of a specified type within it.

        Args:
        question_text (str): The prompt to display to the user.
        file_type (str, optional): The type of files to validate within the directory.

        Returns:
        list: A list of validated file paths.
        """
        full_prompt = question_text # Add exit option to prompt
        while True:
            folder_path = self.input_with_exit(full_prompt)
            files = self.validator.validate_files_in_folder(folder_path, file_type)
            if files:
                return files
            print("No valid files found. Please try again.")
