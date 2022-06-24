import unittest
from main import *


class TestProgram(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_domain(self):
        self.assertEqual(domain_name('http://google.com'), 'google')
        self.assertEqual(domain_name('http://google.co.jp'), 'google')
        self.assertEqual(domain_name('www.xakep.ru'), 'xakep')
        self.assertEqual(domain_name('https://youtube.com'), 'youtube')

    def test_int32(self):
        self.assertEqual(int32_to_ip(2154959208), '128.114.17.104')
        self.assertEqual(int32_to_ip(0), '0.0.0.0')
        self.assertEqual(int32_to_ip(2149583361), '128.32.10.1')

    def test_zeros(self):
        self.assertEqual(zeros(0), 0)
        self.assertEqual(zeros(6), 1)
        self.assertEqual(zeros(30), 7)

    def test_bananas(self):
        self.assertEqual(bananas('banann'), set())
        self.assertEqual(bananas('banana'), {'banana'})
        self.assertEqual(bananas('bbananana'), {'b-an--ana', '-banana--', '-b--anana', 'b-a--nana', '-banan--a',
                                                'b-ana--na', 'b---anana', '-bana--na', '-ba--nana', 'b-anan--a',
                                                '-ban--ana', 'b-anana--'})
        self.assertEqual(bananas('bananaaa'), {'banan-a-', 'banana--', 'banan--a'})
        self.assertEqual(bananas('bananana'), {'ban--ana', 'ba--nana', 'bana--na', 'b--anana', 'banana--', 'banan--a'})

    def test_count(self):
        primesL = [2, 3]
        limit = 200
        self.assertEqual(count_find_num(primesL, limit), [13, 192])

        primesL = [2, 5]
        limit = 200
        self.assertEqual(count_find_num(primesL, limit), [8, 200])

        primesL = [2, 3, 5]
        limit = 500
        self.assertEqual(count_find_num(primesL, limit), [12, 480])

        primesL = [2, 3, 5]
        limit = 1000
        self.assertEqual(count_find_num(primesL, limit), [19, 960])

        primesL = [2, 3, 47]
        limit = 200
        self.assertEqual(count_find_num(primesL, limit), [])


if __name__ == '__main__':
    unittest.main()
