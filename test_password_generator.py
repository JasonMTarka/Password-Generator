import unittest
import password_generator


class TestPasswordGenerator(unittest.TestCase):
    def test_generate(self):

        password = password_generator.Password(lowercase=0)
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertNotIn(char, password)

        password = password_generator.Password(uppercase=0)
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertNotIn(char, password)

        password = password_generator.Password(syms=0)
        for char in "!@#$%^&*":
            self.assertNotIn(char, password)

        password = password_generator.Password(nums=0)
        for char in "0123456789":
            self.assertNotIn(char, password)

        password = password_generator.Password(min_nums=4)
        counter = 0
        for char in password:
            if char in "0123456789":
                counter += 1
        self.assertGreaterEqual(counter, password.min_nums)

        password = password_generator.Password(syms=1, min_syms=4)
        counter = 0
        for char in password:
            if char in "!@#$%^&*":
                counter += 1
        self.assertGreaterEqual(counter, password.min_syms)

    def test_add(self):
        password1 = password_generator.Password(value="5231ja&!")
        password2 = password_generator.Password(value="abCD#*cjzu4")
        self.assertEqual(password1 + password2, "5231ja&!abCD#*cjzu4")
        self.assertEqual(password1 + "abCD#*cjzu4", "5231ja&!abCD#*cjzu4")

    def test_iteration(self):
        password = password_generator.Password(value="abCD#*cjzu4")
        holder = []
        for char in password:
            holder.append(char)
        self.assertEqual(password.value, "".join(holder))

    def test_len(self):
        password = password_generator.Password(pass_len=100)
        self.assertEqual(len(password), password.pass_len)

        password = password_generator.Password(pass_len=0)
        self.assertEqual(len(password), 0)


if __name__ == "__main__":
    unittest.main()
