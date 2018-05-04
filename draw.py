class Draw(object):
    char = 'x'
    width = 0
    height = 0
    canvas = []

    def __init__(self, width, height, *args, **kwargs):
        super(Draw, self).__init__(*args, **kwargs)
        self.width = width + 2
        self.height = height + 2
        self.set_canvas()
        self.draw_canvas()

    def _is_validate(self, x1, x2, y1, y2, is_canvas=False):
        if is_canvas:
            if self._is_validate_point(x1, y1, is_canvas) \
               and self._is_validate_point(x2, y2, is_canvas):
                return True
            else:
                return False
        else:
            if self._is_validate_point(x1, y1) \
               and self._is_validate_point(x2, y2):
                return True
            else:
                return False

    def _is_validate_point(self, x, y, is_canvas=False):
        if is_canvas:
            if x >= 0 and x <= self.width \
               and y >= 0 and y <= self.height:
                return True
            else:
                return False
        else:
            if x > 0 and x <= (self.width - 2) \
               and y > 0 and y <= (self.height - 2):
                return True
            else:
                return False

    def _is_vertical_horizontal(self, x1, x2, y1, y2):
        is_vertical = False
        is_horizontal = False
        if x1 == x2:
            is_vertical = True
        elif y1 == y2:
            is_horizontal = True

        return (is_vertical or is_horizontal)

    def draw_canvas(self):
        canvas_string = ''
        for row in self.canvas:
            for element in row:
                canvas_string += '{:2}'.format(element)
            canvas_string += '\n'
        print(canvas_string)

    def set_canvas(self):
        for x in xrange(self.height):
            self.canvas.append([''] * self.width)

        self.draw_line(0, 0, (self.width - 1), 0, '-', True)
        self.draw_line(
                        0,
                        (self.height - 1),
                        (self.width - 1),
                        (self.height - 1),
                        '-',
                        True
                        )

        self.draw_line(0, 1, 0, (self.height - 2), '|', True)
        self.draw_line(
                        (self.width - 1),
                        1,
                        (self.width - 1),
                        (self.height - 2),
                        '|',
                        True
                        )

    def draw_line(self, x1, y1, x2, y2, letter=char, is_canvas=False):
        if not self._is_validate(x1, x2, y1, y2, is_canvas):
            raise ValueError('*** invalid points, they exceed the size of the canvas (%sx%s) or is zero' % ((self.width - 2), (self.height - 2)))
        elif not self._is_vertical_horizontal(x1, x2, y1, y2):
            raise ValueError('*** invalid points, it is not a vertical or horizontal line')
        else:
            try:
                y = y1 if y1 != 0 or is_canvas else (y1 + 1)
                while y <= y2:
                    x = x1 if x1 != 0 or is_canvas else (x1 + 1)
                    while x <= x2:
                        if (x, y) != (0, 0) and (x, y) != ((self.width - 1), 0) \
                           and (x, y) != (0, (self.height - 1)) \
                           and (x, y) != ((self.width - 1), (self.height - 1)):
                            self.canvas[y][x] = letter
                        else:
                            self.canvas[y][x] = '*'
                        x += 1
                    y += 1
            except IndexError as e:
                raise IndexError('*** arguments should be positive numbers')

    def draw_rectangle(self, x1, y1, x2, y2):
        if not self._is_validate(x1, x2, y1, y2):
            raise ValueError('*** invalid points, they exceed the size of the canvas (%sx%s) or is zero' % ((self.width - 2), (self.height - 2)))
        else:
            self.draw_line(x1, y1, x2, y1)
            self.draw_line(x1, y1, x1, y2)
            self.draw_line(x2, y1, x2, y2)
            self.draw_line(x1, y2, x2, y2)

    def fill_bucket(self, x, y, letter):
        try:
            if self.canvas[y][x] != '':
                return

            if self._is_validate_point(x, y):
                if self.canvas[y][x] == '':
                    self.canvas[y][x] = letter
                self.fill_bucket((x + 1), y, letter)
                self.fill_bucket((x - 1), y, letter)
                self.fill_bucket(x, (y - 1), letter)
                self.fill_bucket(x, (y + 1), letter)
            else:
                raise ValueError('*** invalid points, they exceed the size of the canvas (%sx%s) or is zero' % ((self.width - 2), (self.height - 2)))
        except IndexError as e:
            raise IndexError('*** arguments should be positive numbers')
        except Exception as e:
            raise e
