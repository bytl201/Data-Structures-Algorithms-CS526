"""
This lab is primarily concerned with familiarizing you with the development environment and style of the labs.
Complete the twoSum method
When you run this file, all test cases should print true.

2Sum Problem Statement
Given an array of integers nums and an integer target, find the two integers that add up to a target.
The answer should be returned as an array of the two indices into the array  in ascending order.
If there is no solution return None.

You should assume that there is at most 1 solution

EXAMPLE: Nums = [3,4,5,10] Target = 13
3 (index 0) + 10 (index 3) = 13
Return [0, 3]
"""
def two_sum(nums: list, target: int):
    # dict to store {nums[i], index}
    mapp = {}

    # iterate over index in len(nums)
    for i in range(len(nums)):
        # check if the remainder is in the 'mapp'
        if target - nums[i] in mapp.keys():
            # return index in mapp first because we already passed by it, and it would be the first index in the return list
            return [mapp[target-nums[i]], i]
        # add index to dict if subtraction isn't found
        else:
            mapp[nums[i]] = i

    # if no two sum is found
    return None


"""
DO NOT EDIT BELOW THIS
Below is the unit testing suite for this file.
It provides all the tests that your code must pass to get full credit.
"""


class TestingBase:
    def print_test_result(self, test_name, result):
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        print(f"{color}[{result}] {test_name}{reset}")

    def test_answer(self, test_name, expected, result):
        if result == expected:
            self.print_test_result(test_name, True)
        else:
            self.print_test_result(test_name, False)
            print(f"Expected: {expected} \nGot:      {result}")


class TestTwoSum(TestingBase):
    def run_unit_tests(self):
        self.test_example()
        self.test_simple()
        self.test_no_answer()
        self.test_duplicate_values()
        self.test_longer_list()

    def test_example(self):
        nums = [3, 4, 5, 10]
        target = 13
        expected = [0, 3]
        self.test_answer("test_example", expected, two_sum(nums, target))

    def test_simple(self):
        nums = [1, 3, 7]
        target = 8
        expected = [0, 2]
        self.test_answer("test_simple", expected, two_sum(nums, target))

    def test_no_answer(self):
        nums = [1, 4, 6]
        target = 8
        expected = None
        self.test_answer("test_no_answer", expected, two_sum(nums, target))

    def test_duplicate_values(self):
        nums = [1, 4, 4, 6]
        target = 8
        expected = [1, 2]
        self.test_answer("test_duplicate_values", expected, two_sum(nums, target))

    def test_longer_list(self):
        nums = [2, 6, 3, 10, 5, 7, 1, 1, 3]
        target = 15
        expected = [3, 4]
        self.test_answer("test_longer_list", expected, two_sum(nums, target))


if __name__ == '__main__':
    test_runner = TestTwoSum()
    test_runner.run_unit_tests()
