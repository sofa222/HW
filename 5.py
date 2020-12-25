import random
import unittest
from string import ascii_lowercase
from deque import Deque
from collections import deque as CertDeque


class DequeTest(unittest.TestCase):

    def setUp(self):
        self.testing_deque = Deque()
        self.certified_deque = CertDeque()
        self.push_back_action = [
            self.testing_deque.push_back, self.certified_deque.appendleft]
        self.push_front_action = [
            self.testing_deque.push_front, self.certified_deque.append]
        self.pop_back_action = [
            self.testing_deque.pop_back, self.certified_deque.popleft]
        self.pop_front_action = [
            self.testing_deque.pop_front, self.certified_deque.pop]

    def random_put_action(self):
        return random.choice([self.push_back_action, self.push_front_action])

    def random_get_action(self):
        return random.choice([self.pop_back_action, self.pop_front_action])

    def random_value(self):
        return ''.join([random.choice(ascii_lowercase) for _ in range(12)])

    def test_automatic_run(self):
        size = 0
        for i in range(1000):
            if size == 0:
                value = self.random_value()
                testing_action, certified_action = self.random_put_action()
                testing_action(value)
                certified_action(value)
                size += 1

            elif random.randint(0, 1) == 0:
                value = self.random_value()
                testing_action, certified_action = self.random_put_action()
                testing_action(value)
                certified_action(value)
                size += 1
            else:
                testing_action, certified_action = self.random_get_action()
                testing_value = testing_action()
                certified_value = certified_action()
                size -= 1
                self.assertEqual(testing_value, certified_value)
                self.assertEqual(self.testing_deque.size(), size)

    def test_empty_deque_exception(self):
        d = Deque()
        self.assertRaises(Exception, d.pop_front)

    def test_manual(self):
        self.testing_deque.push_back(1)
        self.testing_deque.push_back(2)
        self.testing_deque.push_back(3)

        self.assertEqual(1, self.testing_deque.pop_front())
        self.assertEqual(2, self.testing_deque.pop_front())

        self.testing_deque.push_front(4)

        self.assertEqual(3, self.testing_deque.pop_back())
        self.assertEqual(4, self.testing_deque.pop_back())


if __name__ == "__main__":
    unittest.main()
