import unittest
from ImprovedTableCipher import encrypt,decrypt

class TestImprovedTableCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = 3
        cipher = "Hello, world!"
        encrypted_message = encrypt(key, cipher)
        decrypted_message = decrypt(key, encrypted_message)
        self.assertEqual(decrypted_message, cipher)

    def test_encrypt_empty_string(self):
        encrypted_message = encrypt(3, "")
        self.assertEqual(encrypted_message, "")

    def test_decrypt_empty_string(self):
        decrypted_message = decrypt(3, "")
        self.assertEqual(decrypted_message, "")

    def test_encrypt_with_different_column_count(self):
        key2 = 4

        cipher = "Hello, world!"

        encrypted_message_2 = encrypt(key2, cipher)

        decrypted_message_2 = decrypt(key2, encrypted_message_2)

        self.assertEqual(decrypted_message_2, cipher)


if __name__ == "__main__":
    unittest.main()