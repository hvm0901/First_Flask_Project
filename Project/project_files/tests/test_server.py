import unittest

from Project.project_files.server import app


class TranslatorAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_english_to_french_translation(self):
        response = self.app.get("/french/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "bonjour")

    def test_french_to_english_translation(self):
        response = self.app.get("/english/bonjour")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "hello")


if __name__ == "__main__":
    unittest.main()
