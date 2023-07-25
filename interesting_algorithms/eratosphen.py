# Решето Эратосфена (для поиска простых чисел)


def eratosphened(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


import time
import unittest


class Testing(unittest.TestCase):
    def test(self):
        expected = 0
        start_time = time.perf_counter_ns()
        result = eratosphened(100000)
        end_time = time.perf_counter_ns()
        print("Elapsed time:", (end_time - start_time) / 1_000_000, "ms")
        # self.assertEqual(expected, result)


unittest.main()
