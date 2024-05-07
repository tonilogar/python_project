import unittest
from unittest.mock import patch
from ..src.classes.questions import Questions, ExitCommand  # Ajusta la ruta del importe según tu estructura de proyecto
from ..src.classes.validator import Validator  # Ajusta la ruta del importe según tu estructura de proyecto


class TestQuestions(unittest.TestCase):
    def setUp(self):
        """Configura los objetos necesarios antes de cada prueba."""
        self.validator = Validator()
        self.questions = Questions(self.validator)

    @patch('builtins.input', side_effect=['Alice'])
    def test_ask_correct_input(self, mock_input):
        """Testea que el método 'ask' recoge correctamente una entrada válida."""
        response = self.questions.ask("¿Cuál es tu nombre?")
        self.assertEqual(response, 'Alice')

    @patch('builtins.input', side_effect=['exit'])
    def test_ask_exit_command(self, mock_input):
        """Testea que el método 'ask' maneja correctamente el comando 'exit'."""
        with self.assertRaises(ExitCommand):
            self.questions.ask("Type 'exit' to quit")

    @patch('builtins.input', side_effect=['1'])
    def test_select_option(self, mock_input):
        """Testea la selección de una opción válida."""
        response = self.questions.select_option("Elige un color", ["rojo", "verde", "azul"])
        self.assertEqual(response, "rojo")

    @patch('builtins.input', side_effect=['4', '2'])  # Primero un valor inválido, luego un valor válido
    def test_select_option_with_retry(self, mock_input):
        """Testea que se pida al usuario reintentar después de una selección inválida."""
        response = self.questions.select_option("Elige un número", ["1", "2", "3"])
        self.assertEqual(response, "2")
        self.assertEqual(mock_input.call_count, 2)  # Verifica que input fue llamado dos veces

    # Añade más métodos de prueba según sea necesario para cubrir otros casos

if __name__ == '__main__':
    unittest.main()
