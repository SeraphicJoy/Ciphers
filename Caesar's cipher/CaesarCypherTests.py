import unittest
from CaesarCipher import caesar_encrypt, caesar_decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_encrypt("abc", 1), "bcd")
        self.assertEqual(caesar_encrypt("xyz", 3), "abc")
        self.assertEqual(caesar_encrypt("Python 3.8", 5), "Udymts 3.8")

    def test_decryption(self):
        self.assertEqual(caesar_decrypt("Khoor, Zruog!", 3), "Hello, World!")
        self.assertEqual(caesar_decrypt("bcd", 1), "abc")
        self.assertEqual(caesar_decrypt("abc", 3), "xyz")
        self.assertEqual(caesar_decrypt("Udymts 3.8", 5), "Python 3.8")

if __name__ == "__main__":
    unittest.main()