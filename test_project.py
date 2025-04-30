import unittest
import os
import string
import project  # import whole module


class TestProjectFunctions(unittest.TestCase):

    def setUp(self):
        self.original_filename = project.FILENAME
        project.FILENAME = "test_students.csv"  # Redirect to test file
        if os.path.exists(project.FILENAME):
            os.remove(project.FILENAME)

    def test_generate_id(self):
        student_id = project.generate_id()
        self.assertEqual(len(student_id), 5)
        self.assertTrue(all(c in string.ascii_uppercase + string.digits for c in student_id))

    def test_is_valid_email(self):
        self.assertTrue(project.is_valid_email("test@example.com"))
        self.assertFalse(project.is_valid_email("invalid-email"))

    def test_initialize_file(self):
        project.initialize_file()
        self.assertTrue(os.path.exists(project.FILENAME))
        with open(project.FILENAME, "r", encoding="utf-8") as f:
            header = f.readline().strip()
            self.assertEqual(header.split(","), project.FIELDS)

    def tearDown(self):
        if os.path.exists(project.FILENAME):
            os.remove(project.FILENAME)
        project.FILENAME = self.original_filename  # Restore original

if __name__ == '__main__':
    unittest.main()
