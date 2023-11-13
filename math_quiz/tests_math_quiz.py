import unittest
from math_quiz import generate_rand_int, generate_rand_choice, perform_output


class TestMathGame(unittest.TestCase):

    def test_generate_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val) # asserts true if the conditions inside brackets is true

        min_val = 20
        max_val = 30
        for _ in range(2000):  # Test a large number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

        min_val = 400
        max_val = 800
        for _ in range(50):  # Test small number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

        min_val = 1000
        max_val = 10000
        for _ in range(800):  # Test a large number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_rand_choice(self):
        for _ in range(2000):  # Test a large number of random values
            choice = generate_rand_choice() # The random choice is saved in choice variable
            self.assertTrue(choice == "+" or choice == "-" or choice == "*")

    def test_perform_output(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 2, '-', '3 - 2', 1),
                (4, 1, '*', '4 * 1', 4),
                (3, 5, '+', '3 + 5', 8),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                output = perform_output(num1, num2, operator) 
                self.assertTrue(output[0] == expected_problem)
                self.assertTrue(output[-1] == expected_answer)

if __name__ == "__main__":
    unittest.main()
