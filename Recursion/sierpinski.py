"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program can recursively print the Sierpinski triangle on GWindow,
	and the order of the Sierpinski triangle is defined by the variable ORDER.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the order of the Sierpinski Triangle
	:param length: int, the length of the Sierpinski Triangle
	:param upper_left_x: int, the upper left x coordinate of the Sierpinski Triangle
	:param upper_left_y: int, the upper left y coordinate of the Sierpinski Triangle
	:return: object, the Sierpinski triangle on GWindow
	"""
	if order == 0:
		return
	else:
		first_line = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		second_line = GLine(upper_left_x, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
		third_line = GLine(upper_left_x+length, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
		window.add(first_line)
		window.add(second_line)
		window.add(third_line)
		sierpinski_triangle(order-1, 0.5*length, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1, 0.5*length, upper_left_x+0.5*length, upper_left_y)
		sierpinski_triangle(order-1, 0.5*length, upper_left_x+0.25*length, upper_left_y+0.433*length)


if __name__ == '__main__':
	main()
