import unittest


class TestSample(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(True, True)

    def test_isupper(self):
        self.assertTrue("FOO".isupper())


if __name__ == "__main__":
    unittest.main()
