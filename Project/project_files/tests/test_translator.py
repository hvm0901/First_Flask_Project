import unittest
from Project.project_files.translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test_englishToFrench_assert(self):
        self.assertEqual(
            "Je m'appelle Harsh Vardhan", englishToFrench("My name is Harsh Vardhan")
        )

    def test_englishToFrench_not_assert(self):
        self.assertNotEqual(
            "Je m'appelle Harsh Vardhan", englishToFrench("My name is Harsh")
        )

    def test_frenchToEnglish_assert(self):
        self.assertEqual(
            "My name is Harsh Vardhan", frenchToEnglish("Je m'appelle Harsh Vardhan")
        )

    def test_frenchToEnglish_not_assert(self):
        self.assertNotEqual(
            "My name is Harsh", frenchToEnglish("Je m'appelle Harsh Vardhan")
        )
