import os
import glob

class Validator:
    """
    A class to validate file and directory paths.

    Methods:
    normalize_path(input_path): Strips quotes and extra whitespace from the path.
    validate_file(file_path, file_type=None): Checks if the file exists and optionally matches the specified type.
    validate_folder(folder_path): Verifies that the directory exists.
    validate_files_in_folder(folder_path, file_type=None): Checks for files of a specific type in a directory.
    """

    def normalize_path(self, input_path):
        """
        Normalize a file or directory path.

        Strips quotes and leading/trailing whitespace from the input path.
        
        Args:
        input_path (str): The path to normalize.

        Returns:
        str: The normalized path.
        """
        if input_path.startswith(("\"", "\'")) and input_path.endswith(("\"", "\'")):
            input_path = input_path[1:-1]  # Remove enclosing single or double quotes
        return input_path.strip()  # Remove leading/trailing whitespace

    def validate_file(self, file_path, file_type=None):
        """
        Validate the existence of a file with an optional type.

        Args:
        file_path (str): The path to the file to validate.
        file_type (str, optional): The required file extension type.

        Returns:
        bool: True if file exists and matches the type if specified, False otherwise.
        """
        file_path = self.normalize_path(file_path)
        if not os.path.isfile(file_path):
            return False
        if file_type and not file_path.endswith('.' + file_type):
            return False
        return True

    def validate_folder(self, folder_path):
        """
        Validate the existence of a directory.

        Args:
        folder_path (str): The path to the directory to validate.

        Returns:
        bool: True if directory exists, False otherwise.
        """
        folder_path = self.normalize_path(folder_path)
        return os.path.isdir(folder_path)

    def validate_files_in_folder(self, folder_path, file_type=None):
        """
        Validate the existence of files of a specific type within a directory.

        Args:
        folder_path (str): The directory to check for files.
        file_type (str, optional): The file type to look for.

        Returns:
        list: A list of matching files if any, False otherwise.
        """
        folder_path = self.normalize_path(folder_path)
        if not os.path.isdir(folder_path):
            return False
        pattern = f"*.{file_type}" if file_type else "*"
        search_path = os.path.join(folder_path, pattern)
        files = glob.glob(search_path)
        return files if files else False
