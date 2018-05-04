import unittest
import random
from draw import Draw


class TestDraw(unittest.TestCase):

    def setUp(self):
        self.width = 20
        self.height = 20

    def test_dimension(self):
        self.width = random.randint(5, 20)
        self.height = random.randint(5, 20)
        self.assertLessEqual(self.width, 20)
        self.assertLessEqual(self.height, 20)
        self.assertGreaterEqual(self.width, 5)
        self.assertGreaterEqual(self.height, 5)

    def test_set_canvas(self):
        canvas = Draw(self.width, self.height)
        self.assertEqual(canvas.width * canvas.height, (self.width + 2) * (self.height + 2))

    def test_draw_line(self):
        canvas = Draw(self.width, self.height)

        x1 = random.randint(1, self.width)
        y1 = random.randint(1, self.height)
        x2 = random.randint(x1, self.width)
        y2 = y1

        canvas.draw_line(x1, y1, x2, y2)
        canvas.draw_canvas()
        self.assertEqual(canvas.canvas[y1][x1], 'x')
        self.assertEqual(canvas.canvas[y2][x2], 'x')

        x1 = random.randint(1, self.width)
        y1 = random.randint(1, self.height)
        x2 = x1
        y2 = random.randint(x1, self.height)

        canvas.draw_line(x1, y1, x2, y2)
        canvas.draw_canvas()
        self.assertEqual(canvas.canvas[y1][x1], 'x')
        self.assertEqual(canvas.canvas[y2][x2], 'x')

    def test_draw_rectangle(self):
        canvas = Draw(self.width, self.height)

        x1 = random.randint(1, (self.width - 1))
        y1 = random.randint(1, (self.height - 1))
        x2 = random.randint((x1 + 1), self.width)
        y2 = random.randint((y1 + 1), self.height)

        canvas.draw_rectangle(x1, y1, x2, y2)
        canvas.draw_canvas()

        self.assertEqual(canvas.canvas[y1][x1], 'x')
        self.assertEqual(canvas.canvas[y2][x2], 'x')
        self.assertEqual(canvas.canvas[y1][x2], 'x')
        self.assertEqual(canvas.canvas[y2][x1], 'x')

    def test_fill_bucket(self):
        canvas = Draw(self.width, self.height)
        letter = 'd'
        x = random.randint(1, self.width)
        y = random.randint(1, self.height)

        canvas.fill_bucket(x, y, letter)
        canvas.draw_canvas()
        self.assertEqual(canvas.canvas[y][x], letter)

    def test_sample_case(self):
        width = 20
        height = 4
        canvas = Draw(width, height)

        canvas.draw_line(1, 2, 6, 2)
        canvas.draw_line(6, 3, 6, 4)
        canvas.draw_rectangle(16, 1, 20, 3)
        canvas.fill_bucket(10, 3, 'd')
        canvas.draw_canvas()

        self.assertEqual(canvas.width * canvas.height, (width+2) * (height+2))

        self.assertEqual(canvas.canvas[3][6], 'x')
        self.assertEqual(canvas.canvas[4][6], 'x')

        self.assertEqual(canvas.canvas[1][16], 'x')
        self.assertEqual(canvas.canvas[3][20], 'x')
        self.assertEqual(canvas.canvas[1][20], 'x')
        self.assertEqual(canvas.canvas[3][16], 'x')

        self.assertEqual(canvas.canvas[10][3], 'd')


if __name__ == '__main__':
    unittest.main()
