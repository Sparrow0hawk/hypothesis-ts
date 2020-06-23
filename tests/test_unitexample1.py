import unittest
from hypothesis import given
from hypothesis.strategies import text
from code import example1

class TestEncoding(unittest.TestCase):
    
    @given(text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(example1.decode(example1.encode(s)), s)


if __name__ == "__main__":
    unittest.main()
