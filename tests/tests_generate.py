import unittest
import requests
import re

class TestGeneratePassword(unittest.TestCase):
    def test_password_meets_requirements(self):
        response = requests.get('http://127.0.0.1:3000/generate')
        self.assertEqual(response.status_code, 200)
        
        generated_password = response.json().get('password')
        self.assertIsNotNone(generated_password)
        
        # Check if the password is 10 characters long and contains only letters and digits
        self.assertTrue(re.match(r'^[a-zA-Z0-9]{10}$', generated_password))

        print("Generated password:", generated_password)

if __name__ == '__main__':
    unittest.main()