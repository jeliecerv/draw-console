import sys
from cmd import Cmd
from draw import Draw


class MyPromptDraw(Cmd):
    intro = 'Welcome to the draw tool in shell. Type help or ? to list commands.\n' + \
            'Instructions:\n' + \
            '* Arguments must be numeric (width, height)\n' + \
            '* Points must be numeric (x1, y1, x2, y2, x, y)\n' + \
            '* Canvas must be created first.\n'
    prompt = '> '
    canvas = None

    def do_C(self, arg):
        """To create canvas: C width height"""
        l = arg.split()
        if len(l) != 2:
            print('*** invalid number of arguments')
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print('*** arguments should be numbers')
            return

        try:
            self.canvas = Draw(l[0], l[1])
        except ValueError as err:
            print(err.args[0])
            return
        except IndexError as err:
            print(err.args[0])
            return
        except Exception as e:
            print('*** unexpected error: %s' % e)
            return

    def do_L(self, arg):
        """To Draw Line: L x1 y1 x2 y2"""
        l = arg.split()
        if len(l) != 4:
            print('*** invalid number of arguments')
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print('*** arguments should be numbers')
            return

        try:
            self.canvas.draw_line(l[0], l[1], l[2], l[3])
            self.canvas.draw_canvas()
        except ValueError as err:
            print(err.args[0])
            return
        except IndexError as err:
            print(err.args[0])
            return
        except Exception as e:
            print('*** unexpected error: %s' % sys.exc_info()[0])
            return

    def do_R(self, arg):
        """To Draw Rectangle: R x1 y1 x2 y2"""
        l = arg.split()
        if len(l) != 4:
            print('*** invalid number of arguments')
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print('*** arguments should be numbers')
            return

        try:
            self.canvas.draw_rectangle(l[0], l[1], l[2], l[3])
            self.canvas.draw_canvas()
        except ValueError as err:
            print(err.args[0])
            return
        except IndexError as err:
            print(err.args[0])
            return
        except Exception as e:
            print('*** unexpected error: %s' % e)
            return

    def do_B(self, arg):
        """To Fill Bucket: B x y c where c is the color and could be any letter"""
        l = arg.split()
        if len(l) != 3:
            print('*** invalid number of arguments')
            return
        try:
            letter = l[2]
            l = [int(i) for i in l[:2]]
        except ValueError:
            print('*** first two arguments should be numbers')
            return

        try:
            self.canvas.fill_bucket(l[0], l[1], letter)
            self.canvas.draw_canvas()
        except ValueError as err:
            print(err.args[0])
            return
        except IndexError as err:
            print(err.args[0])
            return
        except Exception as e:
            print('*** unexpected error: %s' % e)
            return

    def do_Q(self, args):
        """Quits the program. You can also use the Ctrl-D shortcut."""
        print 'Quitting.'
        raise SystemExit

    do_EOF = do_Q


if __name__ == '__main__':
    prompt = MyPromptDraw().cmdloop()
