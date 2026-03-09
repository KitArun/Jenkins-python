# # main.py
# def greeting(name):
#     return f"Hello, {name}! Welcome to Jenkins CI/CD."

# if __name__ == "__main__":
#     message = greeting("My Friend")
#     print(message)
#     print("Execution Successful!")
# test_main.py

import unittest
from main import calculate_total, apply_discount, is_valid_username

class TestShoppingSystem(unittest.TestCase):

    # Test ตัวที่ 1: ตรวจสอบการคำนวณราคาปกติ
    def test_calculate_total_success(self):
        self.assertEqual(calculate_total(50, 3), 150)

    # Test ตัวที่ 2: ตรวจสอบ Error เมื่อใส่ค่าติดลบ (ต้องเกิด ValueError)
    def test_calculate_total_negative_value(self):
        with self.assertRaises(ValueError):
            calculate_total(-10, 5)

    # Test ตัวที่ 3: ตรวจสอบการใช้โค้ดส่วนลด 10%
    def test_apply_discount_welcome(self):
        self.assertEqual(apply_discount(1000, "WELCOME10"), 900)

    # Test ตัวที่ 4: ตรวจสอบกรณีใส่โค้ดส่วนลดผิด (ราคาต้องเท่าเดิม)
    def test_apply_discount_invalid_code(self):
        self.assertEqual(apply_discount(1000, "WRONGCODE"), 1000)

    # Test ตัวที่ 5: ตรวจสอบความถูกต้องของ Username
    def test_username_validation(self):
        self.assertTrue(is_valid_username("JenkinsUser"))
        self.assertFalse(is_valid_username("Hi")) # ชื่อสั้นเกินไป ต้องเป็น False

if __name__ == "__main__":
    unittest.main()