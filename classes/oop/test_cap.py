import unittest
import cap

# class for testing, use this as is:


class TestCap(unittest.TestCase):

    # a function for testing the cap_text method from the cap.py file
    def test_one_word(self):
        text = 'python'
        # call the function you want to test
        result = cap.cap_text(text)
        # checks that the output = 'Python'
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()  # this is the same name in the class statement
