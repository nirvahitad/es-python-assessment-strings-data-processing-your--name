
import unittest
from solution import reverse_string, count_vowels


class TestReverseString(unittest.TestCase):

    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_spaces_and_punctuation(self):
        self.assertEqual(
            reverse_string("Hi, there!"),
            "!ereht ,iH"
        )

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_string(123)


class TestCountVowels(unittest.TestCase):

    def test_normal_string(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_uppercase_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_repeated_vowels(self):
        self.assertEqual(count_vowels("Education"), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_vowels(None)


if __name__ == "__main__":
    unittest.main()
