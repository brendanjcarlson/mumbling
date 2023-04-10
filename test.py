import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('abc'), 'A-Bb-Ccc')

    def test_2(self):
        self.assertEqual(solution('whiteboard'), 'W-Hh-Iii-Tttt-Eeeee-Bbbbbb-Ooooooo-Aaaaaaaa-Rrrrrrrrr-Dddddddddd')

    def test_3(self):
        self.assertEqual(solution('hello'), 'H-Ee-Lll-Llll-Ooooo')

    def test_4(self):
        self.assertEqual(solution('reactweek'), 'R-Ee-Aaa-Cccc-Ttttt-Wwwwww-Eeeeeee-Eeeeeeee-Kkkkkkkkk')

if __name__ == '__main__':
    unittest.main()