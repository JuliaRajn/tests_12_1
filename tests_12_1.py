import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distance should be 50 after 10 walks")

    def test_run(self):
        runner = Runner("Jane")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Distance should be 100 after 10 runs")

    def test_challenge(self):
        runner1 = Runner("Alice")
        runner2 = Runner("Bob")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Distances should be different")

if __name__ == '__main__':
    unittest.main()
